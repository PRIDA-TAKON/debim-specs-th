"""
Specification package validator for debim-specs-th.
Validates all spec.yaml files against schema rules and MasterFormat division conventions.
"""

import sys
from pathlib import Path
import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


REQUIRED_FIELDS = ["id", "name", "category", "masterformat"]
REQUIRED_SECTIONS = ["general_properties", "surface_preparation", "application_system"]


def check_corrupted_characters(data, path_str="") -> list[str]:
    """Check for corrupted characters or Thai PUA codes (U+F700 - U+F71A, U+FFFD)."""
    issues = []
    if isinstance(data, str):
        for ch in data:
            code = ord(ch)
            if 0xF700 <= code <= 0xF71A:
                issues.append(f"Found unnormalized Thai PUA character (U+{code:04X}) in '{path_str}'")
                break
            if code == 0xFFFD:
                issues.append(f"Found replacement character (U+FFFD) in '{path_str}'")
                break
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            issues.extend(check_corrupted_characters(item, f"{path_str}[{idx}]"))
    elif isinstance(data, dict):
        for k, v in data.items():
            issues.extend(check_corrupted_characters(v, f"{path_str}.{k}"))
    return issues


def validate_single_spec(file_path: Path) -> tuple[list[str], dict | None]:
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return [f"YAML parsing error: {e}"], None

    if not isinstance(data, dict):
        return ["Root element must be a dictionary/mapping"], None

    for field in REQUIRED_FIELDS:
        if field not in data or not str(data[field]).strip():
            errors.append(f"Missing required field: '{field}'")

    for section in REQUIRED_SECTIONS:
        if section not in data:
            errors.append(f"Missing recommended section: '{section}'")
        else:
            val = data[section]
            if not val or (isinstance(val, list) and len(val) == 0):
                errors.append(f"Empty section content: '{section}'")

    # Validate MasterFormat format
    mf = str(data.get("masterformat", "")).strip()
    if mf:
        parts = mf.split("-", 1)
        code_part = parts[0].strip()
        digits = [c for c in code_part if c.isdigit()]
        if len(digits) < 2:
            errors.append(f"MasterFormat code '{mf}' must start with at least a 2-digit division")

    # Validate ID convention (uppercase alphanumeric and underscores)
    spec_id = data.get("id", "")
    if spec_id:
        if not spec_id.replace("_", "").isalnum():
            errors.append(f"Spec ID '{spec_id}' should use alphanumeric characters and underscores")
        if spec_id != spec_id.upper():
            errors.append(f"Spec ID '{spec_id}' must be in UPPERCASE")

    # Check for corrupted Thai characters or PUA encoding
    char_issues = check_corrupted_characters(data, "root")
    errors.extend(char_issues)

    return errors, data


def validate_registry_sync(root: Path, disk_spec_ids: dict[str, Path]) -> list[str]:
    """Validate that registry.json is synced with actual spec files on disk."""
    errors = []
    reg_file = root / "registry.json"
    if not reg_file.exists():
        return errors

    try:
        import json
        with open(reg_file, "r", encoding="utf-8") as f:
            reg_data = json.load(f)
    except Exception as e:
        return [f"registry.json parsing error: {e}"]

    packages = reg_data.get("packages", [])
    reg_ids = {pkg.get("id"): pkg for pkg in packages if "id" in pkg}

    # Check for IDs on disk missing from registry
    for sid, spath in disk_spec_ids.items():
        if sid not in reg_ids:
            rel = spath.relative_to(root)
            errors.append(f"Spec '{sid}' ({rel}) is missing from registry.json (run scripts/build_repo.py to sync)")

    # Check for IDs in registry missing from disk
    for rid, rpkg in reg_ids.items():
        if rid not in disk_spec_ids:
            errors.append(f"Registry lists '{rid}' but no corresponding spec.yaml found on disk")

    return errors


def main():
    root = Path(__file__).resolve().parent
    packages_dir = root / "packages"
    if not packages_dir.exists():
        print(f"Error: packages directory '{packages_dir}' not found.")
        sys.exit(1)

    spec_files = list(packages_dir.rglob("spec.yaml"))
    if not spec_files:
        print("No spec.yaml files found.")
        sys.exit(1)

    print(f"Auditing {len(spec_files)} specification packages in debim-specs-th...")

    total_errors = 0
    seen_ids: dict[str, Path] = {}

    for sf in sorted(spec_files):
        rel_path = sf.relative_to(root)
        errs, spec_data = validate_single_spec(sf)

        if spec_data and "id" in spec_data:
            spec_id = spec_data["id"]
            if spec_id in seen_ids:
                prev_path = seen_ids[spec_id].relative_to(root)
                errs.append(f"Duplicate Spec ID '{spec_id}' already defined in '{prev_path}'")
            else:
                seen_ids[spec_id] = sf

        if errs:
            print(f"❌ [FAIL] {rel_path}:")
            for e in errs:
                print(f"    - {e}")
            total_errors += len(errs)
        else:
            print(f"✅ [PASS] {rel_path}")

    # Check registry synchronization
    print("\nAuditing registry.json synchronization...")
    reg_errors = validate_registry_sync(root, seen_ids)
    if reg_errors:
        print("❌ [FAIL] registry.json is out of sync:")
        for re in reg_errors:
            print(f"    - {re}")
        total_errors += len(reg_errors)
    else:
        print("✅ [PASS] registry.json is fully synchronized!")

    if total_errors > 0:
        print(f"\nAudit failed with {total_errors} errors.")
        sys.exit(1)

    print(f"\n🎉 All {len(spec_files)} specification packages are 100% compliant with debim schema!")


if __name__ == "__main__":
    main()
