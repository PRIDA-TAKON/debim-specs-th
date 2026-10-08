"""
Update README.md specification catalog tables from registry.json
"""

import json
from pathlib import Path

DIVISION_TITLES = {
    "03-concrete": "Division 03 — คอนกรีต (Concrete)",
    "04-masonry": "Division 04 — งานก่ออิฐและบล็อก (Masonry)",
    "05-metals": "Division 05 — งานโลหะและเหล็กโครงสร้าง (Metals)",
    "06-wood-plastics": "Division 06 — งานไม้และพลาสติก (Wood and Plastics)",
    "07-thermal-moisture": "Division 07 — การป้องกันความร้อนและความชื้น (Thermal & Moisture Protection)",
    "08-openings": "Division 08 — บานประตู หน้าต่าง และกระจก (Openings)",
    "09-finishes": "Division 09 — งานตกแต่งผิวและฝ้าเพดาน (Finishes)",
    "10-specialties": "Division 10 — งานเบ็ดเตล็ดสถาปัตยกรรมและภูมิทัศน์ (Specialties)",
    "12-furnishings": "Division 12 — งานเฟอร์นิเจอร์ (Furnishings)",
    "22-plumbing": "Division 22 — งานระบบสุขาภิบาล (Plumbing)",
    "26-electrical": "Division 26 — งานระบบไฟฟ้า (Electrical)",
    "31-earthwork": "Division 31 — งานดินและฐานราก (Earthwork)",
}

def format_standards(std_dict):
    parts = []
    for k in ["asa", "tis", "dpt", "astm"]:
        if k in std_dict and std_dict[k]:
            v = str(std_dict[k]).strip()
            # truncate long string if needed
            parts.append(v)
    if not parts:
        for v in std_dict.values():
            if v:
                parts.append(str(v).strip())
    full = ", ".join(parts)
    return full if full else "มาตรฐานวิชาชีพสถาปัตยกรรม"


def main():
    root = Path(__file__).resolve().parent.parent
    reg_file = root / "registry.json"
    readme_file = root / "README.md"

    with open(reg_file, "r", encoding="utf-8") as f:
        reg = json.load(f)

    packages = reg.get("packages", [])
    total = len(packages)

    # Group by division
    groups = {}
    for pkg in packages:
        div = pkg.get("division", "other")
        groups.setdefault(div, []).append(pkg)

    catalog_md = []
    catalog_md.append(f"ปัจจุบันมีรายการวัสดุครอบคลุม **{total} แพ็กเกจมาตรฐาน** ใน {len(groups)} หมวดงาน:\n")

    for div, pkgs in sorted(groups.items()):
        div_title = DIVISION_TITLES.get(div, f"Division {div}")
        catalog_md.append(f"### {div_title}")
        catalog_md.append("| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |")
        catalog_md.append("|---|---|---|---|")
        for p in pkgs:
            slug = f"`{p.get('slug')}`"
            name = p.get("name", "")
            stds = format_standards(p.get("standards", {}))
            mf = p.get("masterformat", "").split("-")[0].strip()
            catalog_md.append(f"| {slug} | {name} | {stds} | `{mf}` |")
        catalog_md.append("")

    catalog_section_text = "\n".join(catalog_md)

    with open(readme_file, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Replace section between '## 📚 สารบัญรายการวัสดุมาตรฐาน (Specification Catalog)' and '## 🛠️ โครงสร้างของไฟล์'
    header = "## 📚 สารบัญรายการวัสดุมาตรฐาน (Specification Catalog)\n\n"
    footer = "\n---\n\n## 🛠️ โครงสร้างของไฟล์ `spec.yaml` (Specification Schema)"

    start_idx = readme_content.find(header)
    end_idx = readme_content.find(footer)

    if start_idx != -1 and end_idx != -1:
        new_readme = (
            readme_content[:start_idx + len(header)]
            + catalog_section_text
            + readme_content[end_idx:]
        )
        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(new_readme)
        print("Updated README.md catalog table successfully!")
    else:
        print("Could not find section markers in README.md")

if __name__ == "__main__":
    main()
