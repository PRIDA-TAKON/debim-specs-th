# 🏛️ debim-specs-th

> **คลังรายการประกอบแบบวัสดุก่อสร้างภาษาไทยแบบเปิด (Open Thai Declarative Architectural Specifications for [debim](https://github.com/PRIDA-TAKON/43-debim))**

[![Validate Specifications](https://github.com/PRIDA-TAKON/debim-specs-th/actions/workflows/validate.yml/badge.svg)](https://github.com/PRIDA-TAKON/debim-specs-th/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Standards: MasterFormat](https://img.shields.io/badge/Standards-MasterFormat%20%7C%20TIS-orange.svg)](#-มาตรฐานและข้อกำหนดที่อ้างอิง)

`debim-specs-th` คือฐานข้อมูลรายการประกอบแบบและสเปควัสดุก่อสร้างภาษาไทยฉบับ Git-native ออกแบบมาเพื่อเป็น Open Registry มาตรฐานสำหรับสถาปนิก, วิศวกร, ผู้รับเหมา และ AI Coding Agents โดยแปลงข้อกำหนดทางสถาปัตยกรรมที่เคยกระจัดกระจายอยู่ในเอกสาร PDF หรือเล่มกระดาษ ให้กลายเป็น **Declarative YAML** ที่ตรวจสอบได้ (Deterministic), ทำ Version Control ได้, และประหยัดบริบทของ AI (Context-efficient)

---

## 🌟 จุดเด่นสำคัญ (Key Features)

1. **สอดคล้องกับมาตรฐานไทยและสากล:** อ้างอิงมาตรฐาน มอก. (TISI), มยผ. (DPT), วสท. (EIT), ASTM, JIS, และ ISO
2. **จัดหมวดหมู่ตาม MasterFormat:** จัดโครงสร้างตาม MasterFormat 50 Divisions สากล เชื่อมโยงกับระบบ IFC4 และ BIM ได้อย่างไร้รอยต่อ
3. **โครงสร้าง 3-Part Section ภาษาไทย:** ครอบคลุมคุณสมบัติทั่วไป (`general_properties`), การเตรียมพื้นผิว (`surface_preparation`), และขั้นตอนการติดตั้ง/ทา (`application_system`)
4. **Zero-Bloat Integration:** เมื่อใช้งานร่วมกับ `debim` ระบบจะดึงเฉพาะสเปคที่อาคารใช้งานจริง (`Active Materials`) เข้าเล่มรายการประกอบแบบอัตโนมัติ

---

## 🚀 วิธีนำไปใช้กับ debim (Usage with debim)

### 1. ติดตั้งสเปคผ่าน CLI
ท่านสามารถดึงสเปคจากรีโพนี้เข้าโฟลเดอร์ `specs/` ของโครงการ `debim` ได้ทันที:

```bash
# ติดตั้งสเปคคอนกรีตผสมเสร็จ 240 ksc
debim spec add PRIDA-TAKON/debim-specs-th/packages/03-concrete/concrete-readymix-240ksc

# ติดตั้งสีทาภายนอก TOA SuperShield
debim spec add PRIDA-TAKON/debim-specs-th/packages/09-finishes/toa-supershield-exterior

# ติดตั้งอิฐมวลเบา Q-CON G4
debim spec add PRIDA-TAKON/debim-specs-th/packages/04-masonry/q-con-aac-block-g4
```

### 2. อ้างอิงในแบบจำลองอาคาร (`project.yaml`)
ระบุ `material` หรือ `spec_id` ในองค์ประกอบ BIM:

```yaml
walls:
  W1:
    start_grid: [A, 1]
    end_grid: [B, 1]
    height: 3.0
    thickness: 0.10
    material: QCON_AAC_BLOCK_G4
```

### 3. ตรวจสอบและรวมเล่มรายการประกอบแบบอัตโนมัติ
```bash
# ตรวจสอบว่าโมเดลขาดสเปครายการใดหรือไม่
debim spec audit -m project.yaml

# รวมเล่มรายการประกอบแบบ MasterFormat เป็น Markdown / PDF
debim spec build -m project.yaml -o dist/specifications.pdf
```

---

## 📚 สารบัญรายการวัสดุมาตรฐาน (Specification Catalog)

ปัจจุบันมีรายการวัสดุครอบคลุม 30 แพ็กเกจหลักใน 8 หมวดงาน:

### Division 03 — คอนกรีต (Concrete)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `concrete-readymix-240ksc` | คอนกรีตผสมเสร็จ 240 ksc (Cylinder) | มอก. 213-2552, ASTM C39, มยผ. 1101 | `03 30 00` |
| `concrete-readymix-280ksc` | คอนกรีตผสมเสร็จกำลังอัดสูง 280 ksc | มอก. 213-2552, ASTM C39 | `03 30 00` |
| `concrete-lean-140ksc` | คอนกรีตหยาบรองก้นหลุม 140 ksc | มอก. 213-2552, มยผ. 1101 | `03 30 00` |
| `cpac-super-plus-waterproof` | คอนกรีตกันซึมผสมเสร็จ ซีแพค | มอก. 213-2552, DIN 1048 | `03 30 00` |
| `post-tension-unbonded` | ระบบพื้นคอนกรีตอัดแรงชนิดดึงทีหลัง Unbonded | มอก. 420-2540, ASTM A416, PTI | `03 38 16` |

### Division 04 — งานก่ออิฐและบล็อก (Masonry)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `clay-brick-traditional` | อิฐมอญก่อสร้างตัน ขนาด 3x6.5x14 ซม. | มอก. 77-2545, มยผ. 1106 | `04 21 00` |
| `q-con-aac-block-g4` | อิฐมวลเบาอบไอน้ำ คิวคอน เกรด G4 | มอก. 1505-2541, ASTM C1693 | `04 22 26` |
| `concrete-block-hollow` | คอนกรีตบล็อกกลวงไม่รับน้ำหนัก 7/9 ซม. | มอก. 57-2560, ASTM C129 | `04 22 00` |

### Division 05 — งานโลหะและเหล็กโครงสร้าง (Metals)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `rebar-deformed-sd40` | เหล็กเส้นเสริมคอนกรีตข้ออ้อย SD40 | มอก. 24-2559, ASTM A615 | `03 21 00` |
| `rebar-round-rb9` | เหล็กเส้นกลมผิวเรียบ RB9 ชั้นคุณภาพ SR24 | มอก. 20-2559 | `03 21 00` |
| `structural-steel-sys-sm400` | เหล็กโครงสร้างรูปพรรณรีดร้อน SYS SM400/SS400 | มอก. 1227-2558, JIS G 3106, ASTM A36 | `05 12 00` |
| `light-gauge-steel-roof-truss` | โครงหลังคาเหล็กกล้ากำลังสูงกัลวาไนซ์ G550 | มอก. 2228-2548, ASTM A792, AS 1397 | `05 40 00` |

### Division 07 — การป้องกันความร้อนและความชื้น (Thermal & Moisture Protection)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `scg-stay-cool-75mm` | ฉนวนใยแก้วกันความร้อน SCG Stay Cool หนา 75 มม. | มอก. 486-2527, ASTM C518, ASTM E84 | `07 21 00` |
| `sika-bituseal-membrane` | แผ่นกันซึมดัดแปลงบิทูเมนเป่าไฟ Sika BituSeal 3 มม. | DIN EN 13707, ASTM D6164 | `07 52 16` |
| `polyurethane-waterproofing-liquid` | ระบบกันซึมโพลียูรีเทนไร้รอยต่อชนิดทา | ASTM C836, BS EN 14891 | `07 14 16` |
| `bluescope-colorbond-metal-sheet` | แผ่นหลังคาเหล็กรีดลอน BlueScope Colorbond 0.48 มม. | มอก. 2753-2559, AS 1397, AS 2728 | `07 41 13` |

### Division 08 — บานประตู หน้าต่าง และกระจก (Openings)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `aluminum-powder-coat-framing` | กรอบบานอะลูมิเนียมอบสีพาวเดอร์โค้ท 6063-T5 | มอก. 284-2560, AAMA 2604 | `08 41 13` |
| `glass-tempered-clear-10mm` | กระจกนิรภัยเทมเปอร์ใส หนา 10 มม. | มอก. 965-2560, ASTM C1048 | `08 80 00` |
| `glass-laminated-acoustic-safety` | กระจกนิรภัยลามิเนตกันเสียง 6+0.76PVB+6 มม. | มอก. 1222-2560, ASTM C1172 | `08 80 00` |
| `solid-teak-door` | บานประตูไม้สักทองจริงคัดพิเศษ อบแห้ง 10-12% | มอก. 267-2521, FSC Certified | `08 14 00` |

### Division 09 — งานตกแต่งและวัสดุผิวสัมผัส (Finishes)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `toa-supershield-exterior` | สีน้ำอะคริลิกทาภายนอก TOA SuperShield | มอก. 2321-2564, ASTM D4587 | `09 91 13` |
| `toa-4-seasons-interior` | สีน้ำอะคริลิกทาภายใน TOA 4Seasons | มอก. 272-2549 | `09 91 23` |
| `cotto-porcelain-tile-60x60` | กระเบื้องเกลซพอร์ซเลน COTTO 60x60 ซม. R10 | มอก. 2508-2555, ISO 13006, DIN 51130 | `09 30 13` |
| `scg-smartboard-ceiling-4mm` | แผ่นไฟเบอร์ซีเมนต์ฝ้าเพดาน SCG สมาร์ทบอร์ด 4 มม. | มอก. 1427-2561, ASTM C1186 | `09 51 00` |
| `gyproc-gypsum-board-9mm` | แผ่นยิปซัมบอร์ด ยิปรอค ขอบลาด หนา 9 มม. | มอก. 188-2547, ASTM C1396, BS EN 520 | `09 29 00` |

### Division 22 — งานระบบสุขาภิบาล (Plumbing)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `scg-pvc-pipe-class-8-5` | ท่อพีวีซีแข็งงานระบายน้ำทิ้ง SCG ชั้น 8.5 | มอก. 17-2532 | `22 13 16` |
| `scg-pvc-pipe-class-13-5` | ท่อพีวีซีแข็งงานส่งน้ำประปารับแรงดัน SCG ชั้น 13.5 | มอก. 17-2532 | `22 11 16` |
| `cotto-water-closet-dual-flush` | โถสุขภัณฑ์ประหยัดน้ำ COTTO Dual Flush 3/4.5L | มอก. 792-2554, ฉลากเขียวเบอร์ 5 | `22 40 00` |

### Division 26 — งานระบบไฟฟ้า (Electrical)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `bangkok-cable-thw` | สายไฟฟ้าทองแดง 60227 IEC 01 THW 450/750V | มอก. 11-2553, IEC 60227, วสท. | `26 05 19` |
| `panasonic-wide-series` | สวิตช์และเต้ารับไฟฟ้ามีกราวด์ Panasonic Wide Series | มอก. 824-2551, มอก. 166-2549, IEC | `26 27 26` |

---

## 🛠️ โครงสร้างของไฟล์ `spec.yaml` (Specification Schema)

แต่ละแพ็กเกจจะประกอบด้วยไฟล์ `spec.yaml` ตามโครงสร้างมาตรฐานของ debim:

```yaml
id: TOA_SUPERSHIELD_EXT
name: "สีน้ำอะคริลิกแท้ 100% สำหรับทาภายนอกอาคาร (TOA SuperShield Titanium Exterior)"
manufacturer: "TOA Paint (Thailand) Public Company Limited"
category: "finishes_paint"
masterformat: "09 91 13 - Exterior Painting"
warranty_years: 15
standards:
  tis: "มอก. 2321-2564 (สีอิมัลชันทนสภาวะอากาศ)"
  astm: "ASTM D4587 / ASTM D3359"
general_properties:
  - "ฟิล์มสีชนิดกึ่งเงา เทคโนโลยี Ti-Pure Titanium ป้องกันรังสี UV สูง"
  - "สะท้อนความร้อนจากแสงแดดได้มากกว่า 96% ช่วยลดอุณหภูมิพื้นผิว"
surface_preparation:
  - "พื้นผิวปูนใหม่: บ่มคอนกรีตไม่น้อยกว่า 28 วัน ความชื้นไม่เกิน 14% ค่า pH 7-9"
  - "ทำความสะอาดคราบฝุ่น ไขมัน และสิ่งสกปรกอุดตันให้แห้งสนิทก่อนทาสี"
application_system:
  - "ชั้นที่ 1: สีรองพื้นปูนใหม่กันด่าง Extra Primer หนา 35 ไมครอน (1 เที่ยว)"
  - "ชั้นที่ 2-3: สีทับหน้า Titanium Exterior หนา 30-35 ไมครอนต่อเที่ยว (2 เที่ยว)"
```

---

## 🤝 การมีส่วนร่วมพัฒนา (Contributing)

เรายินดีต้อนรับการส่งสเปควัสดุใหม่ๆ จากทั้งสถาปนิก วิศวกร และผู้ผลิตวัสดุก่อสร้าง!

1. Fork รีโพนี้
2. สร้างโฟลเดอร์แพ็กเกจใหม่ภายใต้ `packages/<division>/<slug>/spec.yaml`
3. เขียนสเปคตาม schema โดยระบุมาตรฐาน มอก./ASTM และขั้นตอนช่างให้ชัดเจน
4. ตรวจสอบความถูกต้องด้วยคำสั่ง:
   ```bash
   python validate_specs.py
   ```
5. อัปเดต `registry.json` ด้วย:
   ```bash
   python scripts/build_repo.py
   ```
6. ส่ง Pull Request (PR) เข้ามายัง branch `main`

---

## 📄 ใบอนุญาต (License)

เผยแพร่ภายใต้สัญญาอนุญาตแบบ [MIT License](LICENSE) เพื่อประโยชน์สาธารณะของวงการก่อสร้างและสถาปัตยกรรมไทย
