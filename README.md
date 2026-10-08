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

ปัจจุบันมีรายการวัสดุครอบคลุม **63 แพ็กเกจมาตรฐาน** ใน 12 หมวดงาน:

### Division 03 — คอนกรีต (Concrete)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `concrete-cast-in-place-asa` | งานคอนกรีตเทในที่ (Cast-in-Place Concrete - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 03 30 00, มอก. 15 เล่ม 1-2547 (ปูนซีเมนต์ปอร์ตแลนด์), มอก. 213-2520 (คอนกรีตผสมเสร็จ), มอก. 409-2525 (การทดสอบความต้านแรงอัด), มอก. 566-2528 (มวลผสมคอนกรีต), มาตรฐาน วสท. 1014-46, ASTM C143 (Slump Test), ASTM C42 (Drilled Cores) | `03 30 00` |
| `concrete-curing-asa` | การบ่มคอนกรีต (Concrete Curing - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 03 39 00, มอก. 15 เล่ม 1-2547 (ปูนซีเมนต์ปอร์ตแลนด์), มาตรฐาน วสท. 1014-46, ACI 308R | `03 39 00` |
| `concrete-forming-asa` | งานไม้แบบและแบบหล่อคอนกรีต (Concrete Forming - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 03 11 00, มอก. 178-2549 (ไม้อัดสำหรับงานทั่วไปและงานแบบหล่อ), มาตรฐานสำหรับอาคารคอนกรีตเสริมเหล็ก วสท. 1014-46 | `03 11 00` |
| `concrete-lean-140ksc` | คอนกรีตหยาบรองก้นหลุม 140 ksc (Lean Concrete Sub-base 140 ksc Cylinder) | มอก. 213-2552 (คอนกรีตผสมเสร็จ), มยผ. 1101-52 | `03 30 00` |
| `concrete-readymix-240ksc` | คอนกรีตผสมเสร็จกำลังอัด 240 ksc (Ready-Mixed Concrete 240 ksc Cylinder) | มอก. 213-2552 (คอนกรีตผสมเสร็จ), มยผ. 1101 ถึง 1103-52 (มาตรฐานงานคอนกรีตและคอนกรีตเสริมเหล็ก), ASTM C39 / ASTM C94 | `03 30 00` |
| `concrete-readymix-280ksc` | คอนกรีตผสมเสร็จกำลังอัดสูง 280 ksc (High Strength Concrete 280 ksc Cylinder) | มอก. 213-2552 (คอนกรีตผสมเสร็จ), ASTM C39 / ASTM C94 | `03 30 00` |
| `concrete-reinforcing-asa` | งานเหล็กเสริมคอนกรีต (Concrete Reinforcing - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 03 20 00, มอก. 20-2543 (เหล็กเส้นกลม), มอก. 24-2548 (เหล็กข้ออ้อย), มอก. 138-2535 (ลวดผูกเหล็ก), มาตรฐานอาคารคอนกรีตเสริมเหล็กโดยวิธีหน่วยแรงใช้งาน วสท. 1014-46, AWS D1.4 | `03 20 00` |
| `cpac-super-plus-waterproof` | คอนกรีตกันซึมผสมเสร็จ ซีแพค (CPAC Waterproof Ready-Mixed Concrete) | มอก. 213-2552 (คอนกรีตผสมเสร็จ) | `03 30 00` |
| `post-tension-unbonded` | ระบบพื้นคอนกรีตอัดแรงชนิดดึงทีหลังแบบไร้แรงยึดเหนี่ยว (Unbonded Post-Tensioned Flat Plate System) | มอก. 420-2540 (ลวดเหล็กกล้าตีเกลียวสำหรับคอนกรีตอัดแรง), ASTM A416 (Grade 270 Low Relaxation 7-wire Strand) | `03 38 16` |
| `precast-hollow-core-plank-asa` | งานพื้นคอนกรีตสำเร็จรูป (Precast Concrete Hollow Core Planks - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 03 41 13, มอก. 576-2546 (แผ่นคอนกรีตเสริมเหล็กอัดแรงหล่อสำเร็จสำหรับระบบพื้น), มอก. 828-2531 (ชิ้นส่วนคอนกรีตเสริมเหล็กอัดแรงหล่อสำเร็จสำหรับระบบพื้นประกอบ), มาตรฐาน วสท. 1014-46 | `03 41 13` |

### Division 04 — งานก่ออิฐและบล็อก (Masonry)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `autoclaved-aerated-concrete-masonry-asa` | งานผนังก่อคอนกรีตมวลเบา (Autoclaved Aerated Concrete Masonry - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 04 22 19, มอก. 1505-2541 (ชิ้นส่วนคอนกรีตมวลเบาแบบมีฟองอากาศ-อบไอน้ำ), มอก. 1776-2542 (ปูนก่อสำเร็จรูป), มาตรฐาน มยผ. 1106-52 | `04 22 19` |
| `clay-brick-masonry-asa` | งานผนังก่ออิฐมอญและอิฐก่อสร้าง (Brick Masonry - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 04 21 13, มอก. 77-2545 (อิฐก่อสร้างสามัญ), มอก. 1776-2542 (ปูนก่อสำเร็จรูป), มาตรฐาน มยผ. 1106-52 | `04 21 13` |
| `clay-brick-traditional` | อิฐมอญก่อสร้างตัน (Traditional Solid Red Clay Brick) | มอก. 77-2545 (อิฐก่อสร้างสามัญ), มยผ. 1106-52 (มาตรฐานงานก่ออิฐและฉาบปูน) | `04 21 00` |
| `concrete-block-hollow` | คอนกรีตบล็อกกลวงไม่รับน้ำหนัก (Non-Load-Bearing Hollow Concrete Masonry Block) | มอก. 57-2560 (บล็อกคอนกรีตไม่รับน้ำหนัก), ASTM C129 | `04 22 00` |
| `q-con-aac-block-g4` | อิฐมวลเบาอบไอน้ำ คิวคอน เกรด G4 (Q-CON Autoclaved Aerated Concrete Block Class G4) | มอก. 1505-2541 (คอนกรีตมวลเบาแบบมีฟองอากาศอบไอน้ำความดันสูง), ASTM C1693 | `04 22 26` |

### Division 05 — งานโลหะและเหล็กโครงสร้าง (Metals)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `light-gauge-steel-roof-truss` | โครงหลังคาเหล็กกล้ากำลังสูงเคลือบกันสนิมกัลวาไนซ์ (Smart Truss Light Gauge High-Tensile Steel) | มอก. 2228-2548 (เหล็กกล้าแผ่นรีดเย็นเคลือบสังกะสี), ASTM A792 (Grade G550) | `05 40 00` |
| `rebar-deformed-sd40` | เหล็กเส้นเสริมคอนกรีตข้ออ้อย SD40 (Deformed Steel Bar Grade SD40) | มอก. 24-2559 (เหล็กเส้นเสริมคอนกรีต: เหล็กข้ออ้อย), ASTM A615 (Grade 60 Equivalent) | `03 21 00` |
| `rebar-round-rb9` | เหล็กเส้นกลมผิวเรียบ RB9 ชั้นคุณภาพ SR24 (Round Steel Bar Grade SR24 RB9) | มอก. 20-2559 (เหล็กเส้นเสริมคอนกรีต: เหล็กเส้นกลม) | `03 21 00` |
| `structural-steel-framing-asa` | งานโครงสร้างเหล็กและงานโลหะ (Structural Steel Framing and Metal Fabrications - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 05 12 00 และ 05 50 00, มอก. 107-2533 (ท่อเหล็กกลม/เหลี่ยมกลวง), มอก. 1227-2539 (เหล็กโครงสร้างรูปพรรณรีดร้อน), มอก. 1288-2538 (เหล็กรูปตัวซีขึ้นรูปเย็น), มาตรฐาน AISC (American Institute of Steel Construction), AWS D1.1 (Structural Welding Code - Steel), JIS G3101 SS400, JIS G3459 | `05 12 00` |
| `structural-steel-sys-sm400` | เหล็กโครงสร้างรูปพรรณรีดร้อน เอสวายเอส เกรด SM400 (SYS Hot-Rolled Structural Steel SM400/SS400) | มอก. 1227-2558 (เหล็กโครงสร้างรูปพรรณรีดร้อน), ASTM A36 / A992 | `05 12 00` |

### Division 06 — งานไม้และพลาสติก (Wood and Plastics)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `architectural-woodwork-asa` | งานไม้สำหรับงานสถาปัตยกรรม (Architectural Woodwork - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 06 40 00, มอก. 178-2549 (แผ่นไม้อัด), มอก. 192-2549 (ไม้แปรรูป), มาตรฐานกรมป่าไม้ กระทรวงทรัพยากรธรรมชาติและสิ่งแวดล้อม | `06 40 00` |

### Division 07 — การป้องกันความร้อนและความชื้น (Thermal & Moisture Protection)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `bluescope-colorbond-metal-sheet` | แผ่นหลังคาเหล็กรีดลอน บลูสโคป คัลเลอร์บอนด์ (BlueScope Colorbond Clean Colorbond Steel Sheet 0.48mm TCT) | มอก. 2753-2559 (เหล็กกล้าแผ่นรีดเย็นเคลือบโลหะผสมสังกะสี-อะลูมิเนียมเคลือบสี) | `07 41 13` |
| `dampproofing-waterproofing-asa` | งานป้องกันความชื้นและการกันซึม (Dampproofing and Waterproofing - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 07 10 00, มอก. 15 เล่ม 1-2547 (ปูนซีเมนต์ปอร์ตแลนด์), มาตรฐาน ASTM D412 (Tensile Properties), ASTM C836 (Cold Liquid-Applied Waterproofing Membrane) | `07 10 00` |
| `polyurethane-waterproofing-liquid` | ระบบกันซึมโพลียูรีเทนไร้รอยต่อชนิดทา (Liquid Applied Polyurethane Waterproofing Membrane) | ASTM C836 (High Solids Cold Liquid-Applied Elastomeric Waterproofing) | `07 14 16` |
| `roof-tiles-asa` | งานหลังคากระเบื้อง (Roof Tiles - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 07 32 00, มอก. 535-2556 (กระเบื้องคอนกรีตมุงหลังคา), มอก. 2619-2556 (แปหลังคาเหล็ก), มาตรฐาน มยผ. 1106-52 | `07 32 00` |
| `scg-stay-cool-75mm` | ฉนวนกันความร้อนใยแก้ว เอสซีจี สเตย์คูล หนา 75 มม. (SCG Stay Cool Thermal Insulation 75mm Premium) | มอก. 486-2527 (ฉนวนใยแก้ว), ASTM C518 / ASTM E84 (Class A Non-Combustible) | `07 21 00` |
| `sika-bituseal-membrane` | แผ่นกันซึมดัดแปลงบิทูเมนแบบเป่าไฟ ซิก้า บิทูซีล หนา 3 มม. (Sika BituSeal T-130 SG Torch-on Waterproofing Membrane) | ASTM D6164 | `07 52 16` |
| `thermal-protection-asa` | งานป้องกันความร้อนและฉนวนกันความร้อน (Thermal Protection - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 07 20 00, มอก. 486-2527 (ฉนวนใยแก้ว), มอก. 487-2526 (การทดสอบฉนวนกันความร้อน), มาตรฐาน ASTM C665 (Mineral-Fiber Blanket Thermal Insulation) | `07 20 00` |

### Division 08 — บานประตู หน้าต่าง และกระจก (Openings)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `aluminium-doors-windows-asa` | งานประตูและหน้าต่างอลูมิเนียม (Aluminium Doors and Windows - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 08 11 16 และ 08 51 13, มอก. 284-2530 (โครงอลูมิเนียมสำหรับงานอาคาร), มอก. 829-2531 (ประตูหน้าต่างอลูมิเนียม), มาตรฐาน ASTM B221 (Aluminum Alloy 6063 T5), AAMA Standards | `08 11 16` |
| `aluminum-powder-coat-framing` | กรอบบานประตูหน้าต่างอะลูมิเนียมอบสีพาวเดอร์โค้ท (Powder Coated Architectural Aluminum Framing System) | มอก. 284-2560 (อะลูมิเนียมอัลลอยอัดขึ้นรูปสำหรับงานสถาปัตยกรรม) | `08 41 13` |
| `door-window-hardware-asa` | อุปกรณ์ประกอบประตูและหน้าต่าง (Door and Window Hardware - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 08 71 00 และ 08 75 00, มอก. 756-2531 (กุญแจลูกบิดติดประตู), มาตรฐาน ANSI/BHMA A156 Series, UL Listed | `08 71 00` |
| `glass-laminated-acoustic-safety` | กระจกนิรภัยลามิเนตกันเสียงและความปลอดภัย (Acoustic Safety Laminated Glass 6+0.76PVB+6mm) | มอก. 1222-2560 (กระจกลามิเนต), ASTM C1172 | `08 80 00` |
| `glass-tempered-clear-10mm` | กระจกนิรภัยเทมเปอร์ใส หนา 10 มม. (10mm Clear Fully Tempered Safety Glass) | มอก. 965-2560 (กระจกเทมเปอร์), ASTM C1048 (Kind FT Fully Tempered Flat Glass) | `08 80 00` |
| `glazing-asa` | งานกระจกและวัสดุติดตั้งกระจก (Glazing - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 08 80 00, มอก. 1222-2560 (กระจกโฟลต), มอก. 965-2537 (กระจกนิรภัยเทมเปอร์), มอก. 1223-2537 (กระจกนิรภัยลามิเนต), มาตรฐาน ASTM C1036 (Flat Glass), ASTM C1048 (Heat-Treated Flat Glass) | `08 80 00` |
| `louvers-asa` | งานบานเกล็ดระบายอากาศ (Louvers - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 08 91 00, มอก. 284-2530 (อลูมิเนียมโครงสร้าง), มอก. 1222-2560 (กระจกแผ่น), มาตรฐาน AMCA 500-L (Laboratory Methods of Testing Louvers for Rating) | `08 91 00` |
| `metal-doors-frames-asa` | งานประตูและวงกบเหล็ก (Metal Doors and Frames - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 08 11 00, มอก. 244-2551 (ประตูเหล็ก), มาตรฐาน NFPA 80 (Standard for Fire Doors), UL 10C (Fire Tests of Door Assemblies) | `08 11 00` |
| `solid-teak-door` | บานประตูไม้สักทองจริงคัดพิเศษ (Solid Natural Golden Teak Architectural Door) | มอก. 267-2521 (ไม้สักแปรรูป) | `08 14 00` |
| `wood-doors-windows-asa` | งานประตูและหน้าต่างไม้ (Wood Doors and Windows - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 08 14 00 และ 08 52 00, มอก. 178-2549 (แผ่นไม้อัด), มอก. 192-2549 (ไม้แปรรูป), มาตรฐานกรมป่าไม้ กระทรวงทรัพยากรธรรมชาติและสิ่งแวดล้อม | `08 14 00` |

### Division 09 — งานตกแต่งผิวและฝ้าเพดาน (Finishes)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `carpeting-asa` | งานพรม (Carpeting - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 09 68 00, มอก. 2486-2553 (พรมปูพื้นทอเครื่อง), มาตรฐาน CRI Green Label Plus, ASTM D5252 | `09 68 00` |
| `cotto-porcelain-tile-60x60` | กระเบื้องพอร์ซเลนเคลือบผิวด้าน คอตโต้ 60x60 ซม. (COTTO Glazed Porcelain Tile 60x60 cm Matte) | มอก. 2508-2555 (กระเบื้องเซรามิก) | `09 30 13` |
| `gyproc-gypsum-board-9mm` | แผ่นยิปซัมบอร์ด ยิปรอค หนา 9 มม. ขอบลาด (Gyproc Standard Gypsum Plasterboard 9mm Tapered Edge) | มอก. 188-2547 (แผ่นยิปซัม), ASTM C1396 | `09 29 00` |
| `gypsum-board-system-asa` | งานฝ้าเพดานและผนังยิบซั่มบอร์ด (Gypsum Board - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 09 29 00, มอก. 219-2552 (แผ่นยิปซัม), มอก. 863-2532 (โครงคร่าวโลหะสำหรับแผ่นยิปซัม), มาตรฐาน ASTM C1396, ASTM C645 | `09 29 00` |
| `linear-wood-ceiling-asa` | งานฝ้าระแนงไม้ (Linear Wood Ceiling - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 09 54 26, มอก. 192-2549 (ไม้แปรรูป), มาตรฐานกรมป่าไม้ กระทรวงทรัพยากรธรรมชาติและสิ่งแวดล้อม | `09 54 26` |
| `painting-asa` | งานทาสี (Painting - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 09 91 00, มอก. 272-2549 (สีอิมัลชัน), มอก. 2625-2557 (สีน้ำมันอัลคีด), มอก. 285-2554 (สีรองพื้นกันสนิม), มาตรฐาน มยผ. 1106-52 | `09 91 00` |
| `portland-cement-plastering-asa` | งานฉาบปูนซีเมนต์ (Portland Cement Plastering - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 09 24 00, มอก. 80-2550 (ปูนซีเมนต์ผสม), มอก. 1776-2542 (ปูนฉาบสำเร็จรูป), มอก. 2595-2556 (ปูนฉาบมวลเบา), มาตรฐาน มยผ. 1106-52, ASTM C926 | `09 24 00` |
| `scg-smartboard-ceiling-4mm` | แผ่นไฟเบอร์ซีเมนต์ฝ้าเพดาน เอสซีจี สมาร์ทบอร์ด หนา 4 มม. (SCG Smartboard Fiber Cement Ceiling Board 4mm) | มอก. 1427-2561 (แผ่นไฟเบอร์ซีเมนต์), ASTM C1186 (Grade I) | `09 51 00` |
| `stone-flooring-facing-asa` | งานพื้นปูหินและผนังบุหิน (Stone Flooring and Facing - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 09 63 40 และ 09 75 00, มอก. 2703-2559 (กาวซีเมนต์ปูหินธรรมชาติ), มอก. 2704-2559 (กาวยาแนว), มาตรฐาน ASTM C615 (Granite), ASTM C503 (Marble) | `09 63 40` |
| `tiling-asa` | งานปูกระเบื้องเซรามิคและกระเบื้องดินเผา (Tiling - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 09 30 00, มอก. 2508-2555 (กระเบื้องเซรามิก), มอก. 2703-2559 (กาวซีเมนต์ปูกระเบื้อง), มอก. 2704-2559 (กาวยาแนวกระเบื้อง), มาตรฐาน ANSI A118 Series, ISO 13007 | `09 30 00` |
| `toa-4-seasons-interior` | สีน้ำอะคริลิกสำหรับทาภายในอาคาร ทีโอเอ โฟร์ซีซั่นส์ (TOA 4Seasons Acrylic Emulsion Interior) | มอก. 272-2549 (สีอิมัลชันใช้งานทั่วไป) | `09 91 23` |
| `toa-supershield-exterior` | สีน้ำอะคริลิกแท้ 100% สำหรับทาภายนอกอาคาร (TOA SuperShield Titanium Exterior Paint) | มอก. 2321-2564 (สีอิมัลชันทนสภาวะอากาศ), ASTM D4587 / ASTM D3359 | `09 91 13` |
| `washed-aggregate-flooring-asa` | งานพื้นและผนังหินล้าง/กรวดล้าง (Washed Aggregate Flooring and Facing - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 09 66 43 และ 09 77 43, มอก. 133-2556 (ปูนซีเมนต์ขาว), มอก. 15 เล่ม 1-2547 (ปูนซีเมนต์ปอร์ตแลนด์), มาตรฐาน มยผ. 1106-52 | `09 66 43` |
| `wood-flooring-asa` | งานพื้นไม้ (Wood Flooring - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 09 64 00, มอก. 192-2549 (ไม้แปรรูป), มอก. 178-2549 (แผ่นไม้อัด), มาตรฐาน NWFA (National Wood Flooring Association) | `09 64 00` |

### Division 10 — งานเบ็ดเตล็ดสถาปัตยกรรมและภูมิทัศน์ (Specialties)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `softscape-asa` | งานต้นไม้และภูมิทัศน์ (Softscape - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 10 99 11, มาตรฐานกรมวิชาการเกษตร กระทรวงเกษตรและสหกรณ์, มาตรฐานสมาคมภูมิสถาปนิกประเทศไทย (TALA) | `10 99 11` |

### Division 12 — งานเฟอร์นิเจอร์ (Furnishings)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `built-in-furniture-asa` | งานเฟอร์นิเจอร์และตกแต่งภายใน (Furnitures - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 12 50 00, มอก. 178-2549 (แผ่นไม้อัด), มอก. 192-2549 (ไม้แปรรูป), มาตรฐานสมาคมมัณฑนากรแห่งประเทศไทย (TIDA) | `12 50 00` |

### Division 22 — งานระบบสุขาภิบาล (Plumbing)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `cotto-water-closet-dual-flush` | โถสุขภัณฑ์นั่งราบประหยัดน้ำ คอตโต้ ระบบดูอัลฟลัช (COTTO Dual Flush Water Closet 3/4.5 Liters) | มอก. 792-2554 (เครื่องสุขภัณฑ์เซรามิก: โถส้วม) | `22 40 00` |
| `plumbing-fixtures-accessories-asa` | งานสุขภัณฑ์และอุปกรณ์ประกอบห้องน้ำ (Plumbing Fixtures and Bath Accessories - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 22 40 00, 10 28 13 และ 10 28 16, มอก. 792-2554 (เครื่องสุขภัณฑ์เซรามิก), มอก. 2066-2552 (ก๊อกน้ำสำหรับเครื่องสุขภัณฑ์), มาตรฐาน วสท. 3001-44, ASME A112.19.2 | `22 40 00` |
| `plumbing-system-asa` | งานระบบท่อสุขาภิบาล (Plumbing System - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 22 00 00, มอก. 17-2532 (ท่อพีวีซีแข็ง), มอก. 277-2532 (ท่อเหล็กอาบสังกะสี), มอก. 249-2540 (ข้อต่อเหล็กหล่อเหนียว), มอก. 343-2523 (ก๊อกน้ำ), มาตรฐาน วสท. 3001-44 | `22 00 00` |
| `scg-pvc-pipe-class-13-5` | ท่อพีวีซีแข็งสำหรับงานส่งน้ำประปารับแรงดัน เอสซีจี ชั้น 13.5 (SCG Rigid PVC Pipe Class 13.5 Potable Water Supply) | มอก. 17-2532 (ท่อพอลิไวนิลคลอไรด์แข็งสำหรับน้ำดื่ม) | `22 11 16` |
| `scg-pvc-pipe-class-8-5` | ท่อพีวีซีแข็งสำหรับงานระบายน้ำเสียและระบายอากาศ เอสซีจี ชั้น 8.5 (SCG Rigid PVC Pipe Class 8.5 Drainage & Vent) | มอก. 17-2532 (ท่อพอลิไวนิลคลอไรด์แข็งสำหรับใช้เป็นท่อน้ำดื่มและระบายน้ำ) | `22 13 16` |

### Division 26 — งานระบบไฟฟ้า (Electrical)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `bangkok-cable-thw` | สายไฟฟ้าตัวนำทองแดงหุ้มฉนวน พีวีซี 60227 IEC 01 THW (Bangkok Cable Copper Wire 60227 IEC 01 THW 450/750V) | มอก. 11-2553 เล่ม 3 (สายไฟฟ้าหุ้มฉนวนพอลิไวนิลคลอไรด์ แรงดันใช้งานไม่เกิน 450/750 โวลต์) | `26 05 19` |
| `electrical-system-asa` | งานระบบไฟฟ้าและสื่อสาร (Electrical System - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 26 00 00, มอก. 11-2531 (สายไฟฟ้าทองแดงหุ้มฉนวน PVC), มอก. 770-2533 (ท่อร้อยสายไฟเหล็ก), มอก. 824-2551 (สวิตช์ไฟฟ้า), มอก. 166-2549 (เต้ารับ), มาตรฐานการติดตั้งทางไฟฟ้าสำหรับประเทศไทย (วสท. 2001-56), มาตรฐานการไฟฟ้านครหลวง/ส่วนภูมิภาค (MEA/PEA), NEC (National Electrical Code) | `26 00 00` |
| `panasonic-wide-series` | ชุดสวิตช์และเต้ารับไฟฟ้ามีกราวด์ พานาโซนิค ไวด์ซีรีส์ (Panasonic Wide Series Switches and Receptacles) | มอก. 824-2551 (สวิตช์ไฟฟ้า) / มอก. 166-2549 (เต้ารับและเต้าเสียบ) | `26 27 26` |

### Division 31 — งานดินและฐานราก (Earthwork)
| Package Slug | Material Spec Name | มาตรฐานอ้างอิง | รหัส MasterFormat |
|---|---|---|---|
| `termite-control-asa` | งานระบบป้องกันและกำจัดปลวก (Termite Control - ASA Standard) | มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยามฯ 2552 หมวด 31 31 16, มาตรฐานสำนักงานคณะกรรมการอาหารและยา (อย.) กระทรวงสาธารณสุข, มาตรฐานกรมวิทยาศาสตร์การแพทย์ กระทรวงสาธารณสุข | `31 31 16` |

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

## 📚 มาตรฐานและเอกสารที่ใช้อ้างอิง (Reference Standards & Documents)

คลังรายการประกอบแบบ `debim-specs-th` รวบรวมและเทียบเคียงข้อกำหนดจากมาตรฐานวิชาชีพและหน่วยงานหลัก ดังนี้:

1. **สมาคมสถาปนิกสยาม ในพระบรมราชูปถัมภ์ (ASA):**
   - *มาตรฐานรายการประกอบแบบก่อสร้าง สมาคมสถาปนิกสยาม ในพระบรมราชูปถัมภ์ ฉบับปี พ.ศ. 2552 (ASA Standard Architectural Specifications 2009)* — เอกสารอ้างอิงหลักสำหรับข้อกำหนดทางสถาปัตยกรรม ครอบคลุม 42 หมวดงานก่อสร้างตาม MasterFormat
2. **สำนักงานมาตรฐานผลิตภัณฑ์อุตสาหกรรม (สมอ. / TISI):**
   - มาตรฐานผลิตภัณฑ์อุตสาหกรรม (มอก.) สำหรับวัสดุก่อสร้างและสุขภัณฑ์
3. **กรมโยธาธิการและผังเมือง (มยผ. / DPT):**
   - มาตรฐานการออกแบบและการก่อสร้างทางวิศวกรรมและสถาปัตยกรรม
4. **วิศวกรรมสถานแห่งประเทศไทย ในพระบรมราชูปถัมภ์ (วสท. / EIT):**
   - มาตรฐานการติดตั้งทางไฟฟ้าและงานโครงสร้างคอนกรีตเสริมเหล็ก
5. **มาตรฐานสากล:**
   - **CSI MasterFormat (50 Divisions):** โครงสร้างการจัดหมวดหมู่สเปคตามมาตรฐานสากล
   - **ASTM International / ISO / JIS / DIN / IEC:** ข้อกำหนดการทดสอบและเกณฑ์คุณภาพสากล

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
