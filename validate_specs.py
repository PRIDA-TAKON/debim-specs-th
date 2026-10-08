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


def validate_single_spec(file_path: Path) -> list[str]:
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return [f"YAML parsing error: {e}"]

    if not isinstance(data, dict):
        return ["Root element must be a dictionary/mapping"]

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
    if spec_id and not spec_id.replace("_", "").isalnum():
        errors.append(f"Spec ID '{spec_id}' should use alphanumeric characters and underscores")

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
    for sf in sorted(spec_files):
        rel_path = sf.relative_to(root)
        errs = validate_single_spec(sf)
        if errs:
            print(f"❌ [FAIL] {rel_path}:")
            for e in errs:
                print(f"    - {e}")
            total_errors += len(errs)
        else:
            print(f"✅ [PASS] {rel_path}")

    if total_errors > 0:
        print(f"\nAudit failed with {total_errors} errors.")
        sys.exit(1)

    print(f"\n🎉 All {len(spec_files)} specification packages are 100% compliant with debim schema!")


if __name__ == "__main__":
    main()
