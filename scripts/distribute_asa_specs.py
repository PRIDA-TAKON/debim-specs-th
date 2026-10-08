"""
Script to unpack packages/spec.yaml into individual debim specification packages
under packages/<division>/<slug>/spec.yaml and update registry.json.
"""

import json
from pathlib import Path
import yaml

DIV_MAPPING = {
    "CONCRETE_FORMING_ASA": ("03-concrete", "concrete-forming-asa"),
    "CONCRETE_REINFORCING_ASA": ("03-concrete", "concrete-reinforcing-asa"),
    "CAST_IN_PLACE_CONCRETE_ASA": ("03-concrete", "concrete-cast-in-place-asa"),
    "CONCRETE_CURING_ASA": ("03-concrete", "concrete-curing-asa"),
    "PRECAST_HOLLOW_CORE_PLANK_ASA": ("03-concrete", "precast-hollow-core-plank-asa"),
    "CLAY_BRICK_MASONRY_ASA": ("04-masonry", "clay-brick-masonry-asa"),
    "AUTOCLAVED_AERATED_CONCRETE_MASONRY_ASA": ("04-masonry", "autoclaved-aerated-concrete-masonry-asa"),
    "STRUCTURAL_STEEL_FRAMING_ASA": ("05-metals", "structural-steel-framing-asa"),
    "ARCHITECTURAL_WOODWORK_ASA": ("06-wood-plastics", "architectural-woodwork-asa"),
    "DAMPPROOFING_AND_WATERPROOFING_ASA": ("07-thermal-moisture", "dampproofing-waterproofing-asa"),
    "THERMAL_PROTECTION_ASA": ("07-thermal-moisture", "thermal-protection-asa"),
    "ROOF_TILES_ASA": ("07-thermal-moisture", "roof-tiles-asa"),
    "METAL_DOORS_AND_FRAMES_ASA": ("08-openings", "metal-doors-frames-asa"),
    "ALUMINIUM_DOORS_AND_WINDOWS_ASA": ("08-openings", "aluminium-doors-windows-asa"),
    "WOOD_DOORS_AND_WINDOWS_ASA": ("08-openings", "wood-doors-windows-asa"),
    "DOOR_AND_WINDOW_HARDWARE_ASA": ("08-openings", "door-window-hardware-asa"),
    "GLAZING_ASA": ("08-openings", "glazing-asa"),
    "LOUVERS_ASA": ("08-openings", "louvers-asa"),
    "PORTLAND_CEMENT_PLASTERING_ASA": ("09-finishes", "portland-cement-plastering-asa"),
    "GYPSUM_BOARD_SYSTEM_ASA": ("09-finishes", "gypsum-board-system-asa"),
    "TILING_ASA": ("09-finishes", "tiling-asa"),
    "LINEAR_WOOD_CEILING_ASA": ("09-finishes", "linear-wood-ceiling-asa"),
    "STONE_FLOORING_AND_FACING_ASA": ("09-finishes", "stone-flooring-facing-asa"),
    "WOOD_FLOORING_ASA": ("09-finishes", "wood-flooring-asa"),
    "WASHED_AGGREGATE_FLOORING_AND_FACING_ASA": ("09-finishes", "washed-aggregate-flooring-asa"),
    "CARPETING_ASA": ("09-finishes", "carpeting-asa"),
    "PAINTING_ASA": ("09-finishes", "painting-asa"),
    "SOFTSCAPE_ASA": ("10-specialties", "softscape-asa"),
    "BUILT_IN_FURNITURE_ASA": ("12-furnishings", "built-in-furniture-asa"),
    "PLUMBING_SYSTEM_ASA": ("22-plumbing", "plumbing-system-asa"),
    "PLUMBING_FIXTURES_AND_ACCESSORIES_ASA": ("22-plumbing", "plumbing-fixtures-accessories-asa"),
    "ELECTRICAL_SYSTEM_ASA": ("26-electrical", "electrical-system-asa"),
    "TERMITE_CONTROL_ASA": ("31-earthwork", "termite-control-asa"),
}


class ThaiDumper(yaml.SafeDumper):
    pass

def represent_str(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)

ThaiDumper.add_representer(str, represent_str)


def main():
    root = Path(__file__).resolve().parent.parent
    spec_multi = root / "packages" / "spec.yaml"
    if not spec_multi.exists():
        print("packages/spec.yaml not found.")
        return

    with open(spec_multi, "r", encoding="utf-8") as f:
        docs = [d for d in yaml.safe_load_all(f) if d]

    print(f"Loaded {len(docs)} specification packages from {spec_multi.name}")

    # Read existing registry.json
    reg_path = root / "registry.json"
    with open(reg_path, "r", encoding="utf-8") as f:
        registry = json.load(f)

    reg_packages = registry.get("packages", [])
    existing_ids = {p["id"]: p for p in reg_packages}

    new_count = 0
    for doc in docs:
        spec_id = doc.get("id")
        if not spec_id:
            continue

        if spec_id in DIV_MAPPING:
            division, slug = DIV_MAPPING[spec_id]
        else:
            # Fallback deduction
            mf = str(doc.get("masterformat", ""))
            div_prefix = mf[:2] if len(mf) >= 2 else "01"
            division = f"{div_prefix}-division"
            slug = spec_id.lower().replace("_", "-")

        pkg_dir = root / "packages" / division / slug
        pkg_dir.mkdir(parents=True, exist_ok=True)
        target_file = pkg_dir / "spec.yaml"

        with open(target_file, "w", encoding="utf-8") as out_f:
            yaml.dump(doc, out_f, Dumper=ThaiDumper, allow_unicode=True, sort_keys=False)

        print(f"Created package: {division}/{slug}/spec.yaml")

        # Update registry entry
        entry = {
            "id": spec_id,
            "name": doc.get("name", ""),
            "slug": slug,
            "division": division,
            "category": doc.get("category", ""),
            "manufacturer": doc.get("manufacturer", ""),
            "masterformat": doc.get("masterformat", ""),
            "warranty_years": doc.get("warranty_years", 1),
            "standards": doc.get("standards", {}),
            "package_path": f"packages/{division}/{slug}",
            "spec_url": f"https://raw.githubusercontent.com/PRIDA-TAKON/debim-specs-th/main/packages/{division}/{slug}/spec.yaml",
        }

        if spec_id in existing_ids:
            # Update existing
            idx = reg_packages.index(existing_ids[spec_id])
            reg_packages[idx] = entry
        else:
            reg_packages.append(entry)
            new_count += 1

    # Sort packages in registry by division and slug
    reg_packages.sort(key=lambda x: (x.get("division", ""), x.get("slug", "")))
    registry["packages"] = reg_packages
    registry["total_packages"] = len(reg_packages)

    with open(reg_path, "w", encoding="utf-8") as rf:
        json.dump(registry, rf, ensure_ascii=False, indent=2)

    print(f"\nRegistry updated: total {len(reg_packages)} packages (+{new_count} new).")

    # Move/remove packages/spec.yaml to avoid collision
    spec_multi.unlink()
    print("Cleaned up packages/spec.yaml after successful distribution.")


if __name__ == "__main__":
    main()
