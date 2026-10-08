"""
Generator script to scaffold debim-specs-th packages, registry index, and documentation.
"""

import json
from pathlib import Path
import yaml

PACKAGES = [
    # -------------------------------------------------------------
    # Division 03: คอนกรีต (Concrete)
    # -------------------------------------------------------------
    {
        "division": "03-concrete",
        "slug": "concrete-readymix-240ksc",
        "spec": {
            "id": "CONCRETE_240KSC",
            "name": "คอนกรีตผสมเสร็จกำลังอัด 240 ksc (Ready-Mixed Concrete 240 ksc Cylinder)",
            "manufacturer": "General Ready-Mix Batching Plants / มาตรฐาน มยผ. และ วสท.",
            "category": "concrete_structural",
            "masterformat": "03 30 00 - Cast-in-Place Concrete",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 213-2552 (คอนกรีตผสมเสร็จ)",
                "astm": "ASTM C39 / ASTM C94",
                "dpt": "มยผ. 1101 ถึง 1103-52 (มาตรฐานงานคอนกรีตและคอนกรีตเสริมเหล็ก)",
            },
            "general_properties": [
                "กำลังอัดประลัยของคอนกรีตที่อายุ 28 วัน ไม่น้อยกว่า 240 กก./ตร.ซม. (ทรงกระบอกมาตรฐาน 15x30 ซม.) หรือ 280 กก./ตร.ซม. (ลูกบาศก์ 15x15x15 ซม.)",
                "ใช้ปูนซีเมนต์ปอร์ตแลนด์ประเภท 1 ตาม มอก. 15 หรือปูนซีเมนต์ไฮดรอลิกตาม มอก. 2594",
                "ค่ายุบตัวของคอนกรีต (Slump) ขณะเทหน้างานอยู่ระหว่าง 10 ± 2.5 ซม. (ห้ามเติมน้ำเพิ่มที่หน้างานโดยเด็ดขาด)",
                "อัตราส่วนน้ำต่อวัสดุประสานประสิทธิผล (w/c ratio) ไม่เกิน 0.50",
            ],
            "surface_preparation": [
                "ตรวจสอบแบบหล่อให้แข็งแรง มีค้ำยันเพียงพอ ไม่โก่งงอ และอุดรอยรั่วเพื่อป้องกันน้ำปูนไหลออก",
                "ทำความสะอาดเศษขยะ ฝุ่น และสิ่งแปลกปลอมในแบบหล่อ พร้อมทาน้ำยาทาแบบบางๆ สม่ำเสมอ",
                "จัดระยะห่างของลูกปูนหนุนเหล็กเสริม (Concrete Spacers) ให้ได้ระยะคอนกรีตหุ้ม (Covering) ตามแบบโครงสร้างกำหนด",
            ],
            "application_system": [
                "ลำเลียงและเทคอนกรีตลงแบบหล่ออย่างต่อเนื่อง โดยระยะตกอิสระ (Free Fall) ต้องไม่เกิน 1.50 เมตร เพื่อป้องกันการแยกตัว (Segregation)",
                "ใช้เครื่องสั่นคอนกรีต (Vibrator) จุ่มในแนวดิ่งอย่างทั่วถึง ความถี่และระยะจุ่มห่างกัน 30-50 ซม. โดยไม่จี้โดนเหล็กเสริมหรือแบบหล่อนานเกินไป",
                "เริ่มกระบวนการบ่มคอนกรีตทันทีที่คอนกรีตเริ่มแข็งตัว (Initial Set) ต่อเนื่องอย่างน้อย 7 วัน โดยการขังน้ำ ฉีดน้ำ หรือใช้กระสอบชุ่มน้ำคลุม",
            ],
        },
    },
    {
        "division": "03-concrete",
        "slug": "concrete-readymix-280ksc",
        "spec": {
            "id": "CONCRETE_280KSC",
            "name": "คอนกรีตผสมเสร็จกำลังอัดสูง 280 ksc (High Strength Concrete 280 ksc Cylinder)",
            "manufacturer": "General Ready-Mix Batching Plants / CPAC / Boral / Insee",
            "category": "concrete_structural",
            "masterformat": "03 30 00 - Cast-in-Place Concrete",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 213-2552 (คอนกรีตผสมเสร็จ)",
                "astm": "ASTM C39 / ASTM C94",
            },
            "general_properties": [
                "กำลังอัดประลัยของคอนกรีตที่อายุ 28 วัน ไม่ต่ำกว่า 280 กก./ตร.ซม. (ทรงกระบอก 15x30 ซม.) หรือ 325 กก./ตร.ซม. (ลูกบาศก์)",
                "ออกแบบสำหรับโครงสร้างเสารับน้ำหนักสูง คานช่วงยาว หรือโครงสร้างคอนกรีตอัดแรง",
                "ค่า Slump อยู่ระหว่าง 10 ± 2.5 ซม. หรือ 15 ± 2.5 ซม. เมื่อใช้สารลดน้ำพิเศษ (Superplasticizer Type F/G ตาม ASTM C494)",
            ],
            "surface_preparation": [
                "ตรวจสอบการผูกเหล็กเสริมและการยึดโยงค้ำยันให้ทนทานต่อแรงดันคอนกรีตสดอย่างมั่นคง",
                "พรมน้ำรดแบบหล่อที่แห้งให้ชื้นพองตัว (กรณีไม้แบบ) ก่อนเทคอนกรีต",
            ],
            "application_system": [
                "เทคอนกรีตเป็นชั้นๆ สม่ำเสมอหนาไม่เกิน 40-50 ซม. ต่อชั้น และจี้เขย่าประสานเนื้อคอนกรีตให้แนบแน่น",
                "บ่มชื้นต่อเนื่องทันทีไม่น้อยกว่า 7 วัน หรือพ่นน้ำยาบ่มคอนกรีต (Curing Compound) ชนิดสลายตัวได้ตามมาตรฐาน ASTM C309",
            ],
        },
    },
    {
        "division": "03-concrete",
        "slug": "concrete-lean-140ksc",
        "spec": {
            "id": "CONCRETE_LEAN_140KSC",
            "name": "คอนกรีตหยาบรองก้นหลุม 140 ksc (Lean Concrete Sub-base 140 ksc Cylinder)",
            "manufacturer": "General Ready-Mix Batching Plants",
            "category": "concrete_subbase",
            "masterformat": "03 30 00 - Cast-in-Place Concrete",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 213-2552 (คอนกรีตผสมเสร็จ)",
                "dpt": "มยผ. 1101-52",
            },
            "general_properties": [
                "คอนกรีตหยาบผสมเสร็จกำลังอัดที่อายุ 28 วัน ไม่น้อยกว่า 140 กก./ตร.ซม. (Cube) หรือ 115 กก./ตร.ซม. (Cylinder)",
                "ใช้เทรองก้นหลุมฐานราก คานคอดิน หรือพื้นวางบนดิน เพื่อปรับระดับและป้องกันการปนเปื้อนของดินกับเหล็กเสริมโครงสร้าง",
                "ความหนาเฉลี่ย 5 ถึง 10 ซม. ตามที่ระบุในแบบวิศวกรรม",
            ],
            "surface_preparation": [
                "บดอัดดินก้นหลุมหรือชั้นทรายรองพื้นให้แน่นตามข้อกำหนด ไม่มีการยุบยวบหรือมีน้ำขัง",
                "ปูพลาสติกกันความชื้น (PE Sheet) ความหนาไม่น้อยกว่า 0.15 มม. ก่อนเทหากแบบระบุ",
            ],
            "application_system": [
                "เทคอนกรีตหยาบให้เต็มพื้นที่ ปาดระดับหลังคอนกรีตให้ราบเรียบสม่ำเสมอได้ระดับความสูงอ้างอิง",
                "ทิ้งให้คอนกรีตแข็งตัวอย่างน้อย 24 ชั่วโมง ก่อนเริ่มตีเต๊าไลน์วางแบบหล่อและผูกเหล็กเสริมฐานราก",
            ],
        },
    },
    {
        "division": "03-concrete",
        "slug": "cpac-super-plus-waterproof",
        "spec": {
            "id": "CONCRETE_CPAC_WATERPROOF",
            "name": "คอนกรีตกันซึมผสมเสร็จ ซีแพค (CPAC Waterproof Ready-Mixed Concrete)",
            "manufacturer": "The Concrete Products and Aggregate Co., Ltd. (CPAC / SCG)",
            "category": "concrete_waterproof",
            "masterformat": "03 30 00 - Cast-in-Place Concrete",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 213-2552 (คอนกรีตผสมเสร็จ)",
                "din": "DIN 1048 (Water Permeability Test under 5 bar pressure)",
            },
            "general_properties": [
                "คอนกรีตผสมน้ำยากันซึมและสารลดฟองอากาศ มีค่าความพรุนต่ำ มีความทึบน้ำสูง (Waterproofing Density)",
                "กำลังอัดไม่น้อยกว่า 240 ถึง 300 ksc (Cylinder) เหมาะสำหรับสระว่ายน้ำ ถังเก็บน้ำใต้ดิน และชั้นใต้ดิน (Basement)",
                "ค่ายุบตัว 12.5 ± 2.5 ซม. ไหลลื่นเข้าแบบได้ง่าย ลดโอกาสเกิดโพรงรังผึ้ง (Honeycomb)",
            ],
            "surface_preparation": [
                "ตรวจสอบการติดตั้งแถบกันน้ำขยายตัว (Swellable Waterstop) หรือแผ่นยาง Rubber/PVC Waterstop บริเวณรอยต่อการเทคอนกรีต (Construction Joint)",
                "ยึด Waterstop ให้แน่นหนาตรงกึ่งกลางรอยต่อ ไม่ล้มหรือเอียงขณะเทคอนกรีต",
            ],
            "application_system": [
                "วางแผนการเทคอนกรีตให้ต่อเนื่อง รอยต่อระหว่างรถต้องไม่เกิน 45 นาที เพื่อป้องกันการเกิด Cold Joint",
                "จี้เขย่าด้วยเครื่องสั่นอย่างประณีตบริเวณขอบแบบหล่อและรอบ Waterstop",
                "บ่มน้ำชื้นต่อเนื่องยาวนานเป็นพิเศษไม่น้อยกว่า 14 วันเพื่อลดรอยแตกร้าวจากการหดตัวแบบแห้ง (Drying Shrinkage Cracks)",
            ],
        },
    },
    {
        "division": "03-concrete",
        "slug": "post-tension-unbonded",
        "spec": {
            "id": "POST_TENSION_UNBONDED",
            "name": "ระบบพื้นคอนกรีตอัดแรงชนิดดึงทีหลังแบบไร้แรงยึดเหนี่ยว (Unbonded Post-Tensioned Flat Plate System)",
            "manufacturer": "Thai Post-Tension Contractors Association / VSL / Freyssinet Standard",
            "category": "concrete_prestressed",
            "masterformat": "03 38 16 - Unbonded Post-Tensioned Concrete",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 420-2540 (ลวดเหล็กกล้าตีเกลียวสำหรับคอนกรีตอัดแรง)",
                "astm": "ASTM A416 (Grade 270 Low Relaxation 7-wire Strand)",
                "pti": "PTI Post-Tensioning Manual 6th Edition",
            },
            "general_properties": [
                "ลวดเหล็กตีเกลียว 7 เส้น ชนิดคลายความเค้นต่ำ (Unbonded 7-wire Low Relaxation Strand) ขนาดเส้นผ่านศูนย์กลาง 0.5 นิ้ว (12.7 มม.) เกรด 270",
                "เคลือบจาระบีป้องกันสนิมชนิดพิเศษและหุ้มด้วยปลอกพลาสติกพอลิเอทิลีน (PE Sheath) ความหนาไม่น้อยกว่า 1.0 มม. ตลอดความยาวลวด",
                "หัวยึดสมอยึดปลาย (Anchorages) และลิ่มยึด (Wedges) ได้มาตรฐานความปลอดภัย PTI สำหรับรับแรงดึงสูง",
            ],
            "surface_preparation": [
                "ติดตั้งไม้แบบท้องพื้นให้ได้ระดับและทำความสะอาด ปราศจากตะปูและของมีคมที่อาจทำให้ปลอกพลาสติกฉีกขาด",
                "วางเก้าอี้รองลวด (Chair Supports) เพื่อจัดทรงและระดับโปรไฟล์พาราโบลาของแนวลวดตามแบบคำนวณของวิศวกรอย่างแม่นยำ",
            ],
            "application_system": [
                "ร้อยและขึงลวด Tendons ตามระยะและแนวระบุ ตรวจสอบความสมบูรณ์ของปลอกหุ้ม หากฉีกขาดต้องพันเทปกันน้ำให้แน่น",
                "เมื่อเทคอนกรีตและกำลังอัดลูกปูนหน้างานถึงเกณฑ์ (ไม่น้อยกว่า 175 ksc ที่ 3-4 วัน) ให้ทำการดึงลวดขั้นแรก (Stressing Stage 1)",
                "ทำการดึงลวดเต็มพิกัด (Final Stressing) พร้อมจดบันทึกค่ายืดตัว (Elongation) เทียบกับการคำนวณ (คลาดเคลื่อนไม่เกิน ±7%)",
                "ตัดปลายลวดและอุดหัวสมอด้วยปูนเกราท์ไม่หดตัว (Non-Shrink Grout) เกรดกำลังสูงเพื่อกันน้ำและความชื้นเข้าทำลาย",
            ],
        },
    },

    # -------------------------------------------------------------
    # Division 04: งานก่ออิฐและบล็อก (Masonry)
    # -------------------------------------------------------------
    {
        "division": "04-masonry",
        "slug": "clay-brick-traditional",
        "spec": {
            "id": "CLAY_BRICK_TRADITIONAL",
            "name": "อิฐมอญก่อสร้างตัน (Traditional Solid Red Clay Brick)",
            "manufacturer": "มาตรฐาน มยผ. และโรงงานผู้ผลิตอิฐมอญเผาแกร่งในประเทศ",
            "category": "masonry_brick",
            "masterformat": "04 21 00 - Clay Unit Masonry",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 77-2545 (อิฐก่อสร้างสามัญ)",
                "dpt": "มยผ. 1106-52 (มาตรฐานงานก่ออิฐและฉาบปูน)",
            },
            "general_properties": [
                "อิฐดินเผาตันชนิดเผาสุกสม่ำเสมอ แกร่ง มีเสียงกังวานเมื่อเคาะ ไม่มีรอยแตกร้าวลึก ขนาดมาตรฐานประมาณ 3x6.5x14 ซม.",
                "กำลังรับแรงอัดเฉลี่ยไม่น้อยกว่า 30 กก./ตร.ซม. ตาม มอก. 77",
                "การดูดกลืนน้ำไม่เกินร้อยละ 25 โดยน้ำหนัก",
            ],
            "surface_preparation": [
                "นำอิฐมอญไปแช่น้ำหรือรดน้ำให้ชุ่มทั่วทั้งก้อนก่อนนำมาก่ออย่างน้อย 1-2 ชั่วโมง เพื่อป้องกันอิฐดูดน้ำจากปูนก่อ",
                "ทำความสะอาดพื้นผิวโครงสร้าง ค.ส.ล. บริเวณที่จะก่อผนัง และสกัดผิวให้หยาบ",
            ],
            "application_system": [
                "ก่ออิฐสลับแนวรอยต่อ (Stretcher Bond) ด้วยปูนก่อสำเร็จรูปตาม มอก. 1776 หนา 10-15 มม.",
                "เจาะเสียบเหล็กหนวดกุ้ง (Dowel Bar) ขนาด RB6 ทุกระยะความสูง 40-50 ซม. ยึดเข้ากับเสา ค.ส.ล.",
                "เทเสาเอ็นและคานทับหลัง ค.ส.ล. (Lintels & Stiffeners) ในผนังที่กว้างเกิน 3.00 ม. หรือสูงเกิน 3.00 ม. และรอบช่องเปิดประตูหน้าต่างทุกบาน",
                "ก่อผนังสูงไม่เกิน 1.50 ม. ต่อวัน เพื่อป้องกันผนังทรุดตัวและเอียงล้ม",
            ],
        },
    },
    {
        "division": "04-masonry",
        "slug": "q-con-aac-block-g4",
        "spec": {
            "id": "QCON_AAC_BLOCK_G4",
            "name": "อิฐมวลเบาอบไอน้ำ คิวคอน เกรด G4 (Q-CON Autoclaved Aerated Concrete Block Class G4)",
            "manufacturer": "Quality Construction Products Public Co., Ltd. (Q-CON / SCG)",
            "category": "masonry_aac",
            "masterformat": "04 22 26 - Autoclaved Aerated Concrete Unit Masonry",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 1505-2541 (คอนกรีตมวลเบาแบบมีฟองอากาศอบไอน้ำความดันสูง)",
                "astm": "ASTM C1693",
                "bs": "BS EN 771-4",
            },
            "general_properties": [
                "บล็อกคอนกรีตมวลเบาอบไอน้ำแรงดันสูง (AAC) ชนิดรับแรง ชั้นคุณภาพ G4 ขนาด 20x60 ซม. ความหนา 7.5 หรือ 10 ซม.",
                "ความหนาแน่นแห้ง 400-500 กก./ลบ.ม. น้ำหนักเบากว่าอิฐมอญ 2-3 เท่า",
                "กำลังรับแรงอัดเฉลี่ยไม่น้อยกว่า 40 กก./ตร.ซม. (Class G4)",
                "มีคุณสมบัติเป็นฉนวนกันความร้อนสูง ค่าการนำความร้อน (k-value) 0.09-0.11 W/m.K และทนไฟได้นาน 4 ชั่วโมง",
            ],
            "surface_preparation": [
                "ตีเส้นแนวผนังให้ได้ฉากและดิ่ง ก่อแถวแรกด้วยปูนทรายธรรมดาปรับระดับให้เรียบสนิท",
                "ปัดฝุ่นผงบนผิวก้อนอิฐมวลเบาออกให้หมดก่อนป้ายปูนก่อ ห้ามแช่น้ำเด็ดขาด",
            ],
            "application_system": [
                "ใช้ปูนก่อกาวมวลเบาสำเร็จรูป (Thin-bed Mortar) ปาดด้วยเกรียงหวีหนาเพียง 2-3 มม. ทั้งรอยต่อแนวนอนและแนวตั้ง",
                "ยึดผนังเข้ากับเสา ค.ส.ล. ด้วยแผ่นเหล็กยึด Metal Strap ทุกๆ 2 ชั้นก่อ",
                "ทำเสาเอ็นและทับหลังสำเร็จรูปหรือเท ค.ส.ล. ตามคู่มือช่าง Q-CON เมื่อผนังกว้างเกิน 3 ม. หรือรอบวงกบ",
                "ฉาบด้วยปูนฉาบสำหรับอิฐมวลเบาโดยเฉพาะ หนา 10-15 มม. พร้อมติดตาข่ายไฟเบอร์กันแตกร้าวบริเวณรอยต่อเสา ค.ส.ล.",
            ],
        },
    },
    {
        "division": "04-masonry",
        "slug": "concrete-block-hollow",
        "spec": {
            "id": "CONCRETE_BLOCK_HOLLOW",
            "name": "คอนกรีตบล็อกกลวงไม่รับน้ำหนัก (Non-Load-Bearing Hollow Concrete Masonry Block)",
            "manufacturer": "โรงงานผลิตคอนกรีตบล็อกมาตรฐาน มอก.",
            "category": "masonry_block",
            "masterformat": "04 22 00 - Concrete Unit Masonry",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 57-2560 (บล็อกคอนกรีตไม่รับน้ำหนัก)",
                "astm": "ASTM C129",
            },
            "general_properties": [
                "บล็อกคอนกรีตชนิดกลวง ขนาดมาตรฐาน 19x39 ซม. หนา 7 ซม. หรือ 9 ซม.",
                "เนื้อคอนกรีตแน่น แข็งแรง ไม่ร่วน ขอบและมุมไม่บิ่น แตกหัก",
                "กำลังรับแรงอัดเฉลี่ยตามพื้นที่หน้าตัดรวมไม่น้อยกว่า 2.5 MPa (25 กก./ตร.ซม.)",
            ],
            "surface_preparation": [
                "ทำความสะอาดพื้นผิวที่จะก่อ ปราศจากคราบน้ำมันและสิ่งสกปรก",
                "ตรวจเช็คแนวฉาก แนวดิ่ง และระดับพื้นอ้างอิง",
            ],
            "application_system": [
                "ก่อด้วยปูนก่อสำเร็จรูปตาม มอก. 1776 หนา 10-12 มม.",
                "เสียบเหล็กหนวดกุ้ง RB6 ยึดเสาโครงสร้างทุกๆ 40 ซม.",
                "หล่อคอนกรีตในรูกลวงพร้อมใส่เหล็กเสริมยืน หรือติดตั้งทับหลัง ค.ส.ล. ทุกระยะความสูง 1.50-2.00 ม.",
            ],
        },
    },

    # -------------------------------------------------------------
    # Division 05: งานโลหะและเหล็กโครงสร้าง (Metals)
    # -------------------------------------------------------------
    {
        "division": "05-metals",
        "slug": "rebar-deformed-sd40",
        "spec": {
            "id": "REBAR_DEFORMED_SD40",
            "name": "เหล็กเส้นเสริมคอนกรีตข้ออ้อย SD40 (Deformed Steel Bar Grade SD40)",
            "manufacturer": "โรงงานผลิตเหล็กชั้นนำ มอก. เช่น บลจ.สยามยามาโตะ (SYS) / โรงงานทาทาสตีล (TATA) / มิลล์คอน (MILL)",
            "category": "metals_rebar",
            "masterformat": "03 21 00 - Reinforcing Steel",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 24-2559 (เหล็กเส้นเสริมคอนกรีต: เหล็กข้ออ้อย)",
                "astm": "ASTM A615 (Grade 60 Equivalent)",
            },
            "general_properties": [
                "เหล็กเส้นข้ออ้อยรีดร้อน ชั้นคุณภาพ SD40 (Yield Strength ไม่ต่ำกว่า 4,000 กก./ตร.ซม. หรือ 390 MPa)",
                "กำลังต้านแรงดึงสูงสุด (Tensile Strength) ไม่ต่ำกว่า 5,700 กก./ตร.ซม. (560 MPa)",
                "บั้งและครีบมีความคมชัด ลึกสม่ำเสมอ ผิวเหล็กเรียบ ไม่มีสะเก็ดสนิมล่อน รอยปริ หรือรอยแตกลึก",
                "มีตราประทับนูนแสดงชื่อผู้ผลิต ชนิดเหล็ก ขนาด และชั้นคุณภาพ บนตัวเหล็กเส้นทุกระยะ",
            ],
            "surface_preparation": [
                "จัดเก็บเหล็กเส้นบนหมอนรองเหนือพื้นดิน ไม่ให้สัมผัสความชื้นหรือโคลนดินโดยตรง และมีหลังคาคลุม",
                "ก่อนผูกเหล็ก ต้องทำความสะอาดขจัดคราบดิน น้ำมัน จาระบี และสะเก็ดสนิมขุมออกให้หมด",
            ],
            "application_system": [
                "ดัด งอ โค้งเหล็กด้วยเครื่องดัดเชิงกลตามรัศมีโค้งมาตรฐาน มยผ. และ วสท. โดยไม่ใช้ความร้อนดัดแปลงเหล็ก",
                "ผูกยึดเหล็กเส้นให้แน่นหนาด้วยลวดผูกเหล็กเบอร์ 18 มัดแน่นไม่ขยับหลุดขณะเทคอนกรีต",
                "การต่อทาบเหล็ก (Lap Splice) ต้องมีความยาวไม่น้อยกว่า 40 เท่าของเส้นผ่านศูนย์กลางเหล็ก (40d) หรือตามแบบระบุ",
                "หนุนลูกปูนหรือตัวเว้นระยะที่แข็งแรงทนทาน เพื่อรักษาแนวหุ้มคอนกรีต (Concrete Cover) ตามข้อกำหนด",
            ],
        },
    },
    {
        "division": "05-metals",
        "slug": "rebar-round-rb9",
        "spec": {
            "id": "REBAR_ROUND_RB9",
            "name": "เหล็กเส้นกลมผิวเรียบ RB9 ชั้นคุณภาพ SR24 (Round Steel Bar Grade SR24 RB9)",
            "manufacturer": "โรงงานผลิตเหล็กมาตรฐาน มอก. ในประเทศ",
            "category": "metals_rebar",
            "masterformat": "03 21 00 - Reinforcing Steel",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 20-2559 (เหล็กเส้นเสริมคอนกรีต: เหล็กเส้นกลม)",
            },
            "general_properties": [
                "เหล็กเส้นกลมผิวเรียบ ขนาดเส้นผ่านศูนย์กลาง 9 มม. (RB9) ชั้นคุณภาพ SR24",
                "กำลังคราก (Yield Strength) ไม่น้อยกว่า 2,400 กก./ตร.ซม. (235 MPa)",
                "ผิวเรียบเกลี้ยง ปราศจากสนิมขุม รอยแยก ครีบ หรือรอยแตกร้าว",
                "เหมาะสำหรับใช้ทำเหล็กปลอกเสา เหล็กปลอกคาน (Stirrups/Ties) และเหล็กเสริมกันร้าว",
            ],
            "surface_preparation": [
                "ตรวจเช็คความสะอาด ปราศจากคราบดิน น้ำมัน จาระบี",
                "เก็บไว้บนแท่นวางแห้งเหนือพื้นดิน ป้องกันสนิมน้ำ",
            ],
            "application_system": [
                "ดัดงอทำขอเกี่ยว (Standard Hook 135 องศา สำหรับเหล็กปลอกรับแรงแผ่นดินไหว) ตามมาตรฐาน วสท.",
                "ผูกรัดเหล็กแกนด้วยลวดผูกเหล็กทุกจุดตามระยะห่าง (Spacing) ที่ระบุในแบบแปลนอย่างเคร่งครัด",
            ],
        },
    },
    {
        "division": "05-metals",
        "slug": "structural-steel-sys-sm400",
        "spec": {
            "id": "STRUCTURAL_STEEL_SYS_SM400",
            "name": "เหล็กโครงสร้างรูปพรรณรีดร้อน เอสวายเอส เกรด SM400 (SYS Hot-Rolled Structural Steel SM400/SS400)",
            "manufacturer": "Siam Yamato Steel Co., Ltd. (SYS Thailand)",
            "category": "metals_structural",
            "masterformat": "05 12 00 - Structural Steel Framing",
            "warranty_years": 20,
            "standards": {
                "tis": "มอก. 1227-2558 (เหล็กโครงสร้างรูปพรรณรีดร้อน)",
                "jis": "JIS G 3106 (SM400) / JIS G 3101 (SS400)",
                "astm": "ASTM A36 / A992",
            },
            "general_properties": [
                "เหล็กรูปพรรณรีดร้อนหน้าตัด H-Beam, I-Beam, Channel และ Angle มาตรฐาน มอก. 1227 เกรด SM400 (เหมาะสำหรับงานเชื่อม)",
                "กำลังจุดคราก (Yield Strength) ไม่น้อยกว่า 245 N/mm2 (หนาไม่เกิน 16 มม.) และกำลังต้านแรงดึงสูงสุด 400-510 N/mm2",
                "ผ่านการตรวจสอบองค์ประกอบทางเคมี คาร์บอนสมมูล (Carbon Equivalent CE) ต่ำ ไม่เปราะง่าย เมื่องานเชื่อมประสาน",
            ],
            "surface_preparation": [
                "ทำความสะอาดพื้นผิวเหล็ก ขจัดคราบไขมัน คราบน้ำมัน และสิ่งสกปรก",
                "พ่นขัดทรายทำความสะอาดผิวเหล็กระดับ Sa 2.5 (Near-White Metal Blast Cleaning) ตามมาตรฐาน ISO 8501-1 ก่อนทาสีกันสนิม",
            ],
            "application_system": [
                "การประกอบและเชื่อมโครงสร้างเหล็ก ดำเนินการโดยช่างเชื่อมที่ผ่านการรับรองตามมาตรฐาน AWS D1.1",
                "ทาสีรองพื้นกันสนิม Inorganic Zinc Rich Primer หนา 75 ไมครอน ทันทีหลังขัดพ่นทราย",
                "ทาสีชั้นกลาง Epoxy Intermediate Coat หนา 100 ไมครอน และสีทับหน้า Polyurethane Topcoat หนา 50 ไมครอน รวมความหนาฟิล์มแห้งไม่ต่ำกว่า 225 ไมครอน",
            ],
        },
    },
    {
        "division": "05-metals",
        "slug": "light-gauge-steel-roof-truss",
        "spec": {
            "id": "LIGHT_GAUGE_STEEL_TRUSS",
            "name": "โครงหลังคาเหล็กกล้ากำลังสูงเคลือบกันสนิมกัลวาไนซ์ (Smart Truss Light Gauge High-Tensile Steel)",
            "manufacturer": "SCG Roofing / Lysaght / BlueScope",
            "category": "metals_roof_truss",
            "masterformat": "05 40 00 - Cold-Formed Metal Framing",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 2228-2548 (เหล็กกล้าแผ่นรีดเย็นเคลือบสังกะสี)",
                "astm": "ASTM A792 (Grade G550)",
                "as": "AS 1397",
            },
            "general_properties": [
                "เหล็กกล้าขึ้นรูปเย็นกำลังดึงสูง เกรด G550 (Yield Strength ไม่ต่ำกว่า 550 MPa)",
                "เคลือบสารป้องกันสนิมโลหะผสมสังกะสี-อะลูมิเนียม (Zacs / Zincalume Coating Class AZ100 หรือ AZ150)",
                "ออกแบบโครงสร้างด้วยระบบคอมพิวเตอร์ตามแรงลมและน้ำหนักมุงจริง ชิ้นส่วนผลิตตัดเจาะจากโรงงาน",
            ],
            "surface_preparation": [
                "ตรวจเช็คระดับหลังคาน ค.ส.ล. และติดตั้งแผ่นเพลทพุกเหล็กกลเชิงกลหรือพุกเคมีตามตำแหน่งวิศวกรกำหนด",
            ],
            "application_system": [
                "ยึดประกอบโครงสร้างถัก (Truss) ด้วยสกรูเกลียวปล่อยเคลือบกันสนิม Class 3 ตาม AS 3566 โดยไม่ใช้การเชื่อมประกบด้วยความร้อน",
                "ติดตั้งค้ำยันตามแนวขวางและแนวดิ่ง (Bracing System) ครบถ้วนตามแบบเพื่อป้องกันการบิดตัว",
            ],
        },
    },

    # -------------------------------------------------------------
    # Division 07: การป้องกันความร้อนและความชื้น (Thermal & Moisture Protection)
    # -------------------------------------------------------------
    {
        "division": "07-thermal-moisture",
        "slug": "scg-stay-cool-75mm",
        "spec": {
            "id": "SCG_STAY_COOL_75MM",
            "name": "ฉนวนกันความร้อนใยแก้ว เอสซีจี สเตย์คูล หนา 75 มม. (SCG Stay Cool Thermal Insulation 75mm Premium)",
            "manufacturer": "Siam Fiberglass Co., Ltd. (SCG)",
            "category": "thermal_insulation",
            "masterformat": "07 21 00 - Thermal Insulation",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 486-2527 (ฉนวนใยแก้ว)",
                "astm": "ASTM C518 / ASTM E84 (Class A Non-Combustible)",
            },
            "general_properties": [
                "ฉนวนใยแก้วสำหรับปูเหนือฝ้าเพดาน ความหนา 75 มม. หุ้มรอบด้านด้วยแผ่นอะลูมิเนียมฟอยล์เสริมแรงกันความชื้น",
                "ค่าการต้านทานความร้อนรวมของระบบ (R-Value) ไม่น้อยกว่า 20-27 hr.ft2.F/Btu",
                "เนื้อฉนวนไม่ติดไฟ ไม่ลามไฟ ปราศจากสารพิษและกลิ่นฉุน ได้รับฉลากเขียวด้านสิ่งแวดล้อม",
            ],
            "surface_preparation": [
                "ตรวจเช็คโครงฝ้าเพดานยิปซัมให้แข็งแรง ทนทานต่อน้ำหนักฉนวน",
                "เก็บกวาดฝุ่นผงและสิ่งแปลกปลอมเหนือฝ้าเพดานให้เรียบร้อย",
            ],
            "application_system": [
                "ปูแผ่นฉนวนบนโครงฝ้าเพดานให้ชิดชนกันสนิท ปราศจากช่องว่าง",
                "ปิดรอยต่อระหว่างม้วนด้วยเทปอะลูมิเนียมฟอยล์แท้ (Aluminium Foil Tape) กว้างไม่น้อยกว่า 2.5 นิ้ว",
                "เว้นระยะห่างจากดวงโคมดาวน์ไลท์และอุปกรณ์ไฟฟ้าที่มีความร้อนอย่างน้อย 10-15 ซม.",
            ],
        },
    },
    {
        "division": "07-thermal-moisture",
        "slug": "sika-bituseal-membrane",
        "spec": {
            "id": "SIKA_BITUSEAL_MEMBRANE",
            "name": "แผ่นกันซึมดัดแปลงบิทูเมนแบบเป่าไฟ ซิก้า บิทูซีล หนา 3 มม. (Sika BituSeal T-130 SG Torch-on Waterproofing Membrane)",
            "manufacturer": "Sika (Thailand) Limited",
            "category": "moisture_waterproofing",
            "masterformat": "07 52 16 - Styrene-Butadiene-Styrene (SBS) Modified Bituminous Membrane Roofing",
            "warranty_years": 10,
            "standards": {
                "din": "DIN EN 13707 / DIN EN 13969",
                "astm": "ASTM D6164",
            },
            "general_properties": [
                "แผ่นเมมเบรนกันซึมชนิดดัดแปลงบิทูเมน (APP / SBS) เสริมแรงด้วยเส้นใยโพลีเอสเตอร์ถักเหนียวสูง ความหนา 3.0 มม.",
                "ผิวหน้าเคลือบด้วยแร่เกล็ดหินธรรมชาติป้องกันรังสี UV และการขีดข่วน",
                "มีความยืดหยุ่นตัวสูง (High Elongation) ทนทานต่อการขยายตัวและหดตัวจากความร้อนของคอนกรีตได้ดีเยี่ยม",
            ],
            "surface_preparation": [
                "พื้นผิวคอนกรีตดาดฟ้าต้องเทปรับสโลประบายน้ำ 1:100 ปราศจากน้ำขัง ผิวขัดเรียบ แห้งสนิท (ความชื้นไม่เกิน 5%)",
                "ลบมุมขอบผนัง (Cant Strip/Chamfer) 45 องศา ขนาด 5x5 ซม. ตลอดแนวรอยต่อพื้นชนผนัง",
                "ทาสีรองพื้นบิทูเมนไพรเมอร์ (Sika Bitumen Primer) ทั่วบริเวณ ทิ้งไว้ให้แห้ง 4-6 ชั่วโมง",
            ],
            "application_system": [
                "ติดตั้งแผ่นกันซึมโดยใช้หัวพ่นแก๊สเป่าไฟ (Torch-on) ให้เนื้อบิทูเมนด้านล่างละลายยึดเกาะแน่นกับพื้นผิว",
                "ซ้อนทับรอยต่อด้านข้างไม่น้อยกว่า 10 ซม. และรอยต่อหัวม้วนไม่น้อยกว่า 15 ซม. พร้อมใช้เกรียงรีดกดรอยต่อให้เนื้อเชื่อมผสานเป็นเนื้อเดียวกัน",
                "พับขอบแผ่นขึ้นผนังสูงไม่น้อยกว่า 30 ซม. แล้วเก็บปลายขอบด้วยรางเหล็กและซิลิโคนกันซึม",
                "ทดสอบขังน้ำ (Flood Test) ความลึก 5-10 ซม. เป็นเวลาไม่น้อยกว่า 48 ชั่วโมง ตรวจสอบการรั่วซึมก่อนทำชั้นป้องกัน (Protection Screed)",
            ],
        },
    },
    {
        "division": "07-thermal-moisture",
        "slug": "polyurethane-waterproofing-liquid",
        "spec": {
            "id": "PU_WATERPROOFING_LIQUID",
            "name": "ระบบกันซึมโพลียูรีเทนไร้รอยต่อชนิดทา (Liquid Applied Polyurethane Waterproofing Membrane)",
            "manufacturer": "Sika / Lanko / Bostik / Crocodile",
            "category": "moisture_waterproofing",
            "masterformat": "07 14 16 - Cold Fluid-Applied Waterproofing",
            "warranty_years": 5,
            "standards": {
                "astm": "ASTM C836 (High Solids Cold Liquid-Applied Elastomeric Waterproofing)",
                "bs": "BS EN 14891",
            },
            "general_properties": [
                "โพลียูรีเทนกันซึมชนิดยืดหยุ่นสูงพิเศษ มีค่าความยืดหยุ่น (Elongation at Break) สูงกว่า 400%",
                "ฟิล์มแห้งไร้รอยต่อ ทนแดด ทนรังสี UV และทนต่อสารเคมีในน้ำขัง",
                "ประสานรอยแตกร้าวคอนกรีต (Crack Bridging Capability) ได้ดีเยี่ยมถึง 2 มม.",
            ],
            "surface_preparation": [
                "พื้นผิวต้องแข็งแรง สะอาด ปราศจากคราบฝุ่น น้ำมัน น้ำยาบ่มคอนกรีต และแห้งสนิท",
                "ซ่อมแซมรอยแตกร้าวและขัดลบเสี้ยนคอนกรีตก่อนลงมือ",
                "ทารองพื้น PU Primer ชนิดแทรกซึมลึก จำนวน 1 เที่ยว",
            ],
            "application_system": [
                "ทาชั้นแรกพร้อมปูเสริมแรงด้วยแผ่นตาข่ายไฟเบอร์กลาส (Fiberglass Mesh) ตามรอยต่อและมุม",
                "ทาทับชั้นที่สองและสามในทิศทางตั้งฉากกับเที่ยวแรก รวมความหนาฟิล์มแห้งไม่น้อยกว่า 1.5 มม.",
                "ทิ้งให้แห้งตัวสมบูรณ์ 72 ชั่วโมงก่อนทำการทดสอบขังน้ำหรือปูกระเบื้องทับ",
            ],
        },
    },
    {
        "division": "07-thermal-moisture",
        "slug": "bluescope-colorbond-metal-sheet",
        "spec": {
            "id": "BLUESCOPE_COLORBOND_SHEET",
            "name": "แผ่นหลังคาเหล็กรีดลอน บลูสโคป คัลเลอร์บอนด์ (BlueScope Colorbond Clean Colorbond Steel Sheet 0.48mm TCT)",
            "manufacturer": "NS BlueScope (Thailand) Limited",
            "category": "thermal_roofing",
            "masterformat": "07 41 13 - Metal Roof Panels",
            "warranty_years": 25,
            "standards": {
                "tis": "มอก. 2753-2559 (เหล็กกล้าแผ่นรีดเย็นเคลือบโลหะผสมสังกะสี-อะลูมิเนียมเคลือบสี)",
                "as": "AS 1397 / AS 2728",
            },
            "general_properties": [
                "เหล็กกล้ากำลังสูง G550 เคลือบโลหะผสมซิงค์-อะลูมิเนียม Zincalume (Zincalume AZ150 ไม่น้อยกว่า 150 กรัม/ตร.ม.)",
                "เคลือบสีอบล่วงหน้าระบบ Clean Colorbond ป้องกันคราบฝุ่นเกาะและสะท้อนรังสีความร้อนด้วยเทคโนโลยี Thermatech",
                "ความหนารวมก่อนเคลือบสี (BMT) ไม่น้อยกว่า 0.42 มม. และความหนารวมเคลือบสี (TCT) ไม่น้อยกว่า 0.48 มม.",
            ],
            "surface_preparation": [
                "ตรวจสอบแนวแปหลังคาให้ได้ระดับ แนวระนาบตรง และมีระยะห่างแป (Purlin Spacing) ตามพิกัดรับน้ำหนัก",
            ],
            "application_system": [
                "มุงแผ่นหลังคาตามทิศทางสวนลม รอยทับซ้อนด้านข้างสนิทแนบแน่น",
                "ยึดแผ่นหลังคาด้วยสกรูเกลียวปล่อยเคลือบกันสนิม Class 3 ตาม AS 3566 พร้อมแหวนยาง EPDM คุณภาพสูง",
                "กวาดเศษขี้ตะไบเหล็ก (Swawf) ออกจากหลังคาทุกวันหลังเสร็จงานเพื่อป้องกันการเกิดสนิมจุดแดง",
            ],
        },
    },

    # -------------------------------------------------------------
    # Division 08: บานประตู หน้าต่าง และกระจก (Openings)
    # -------------------------------------------------------------
    {
        "division": "08-openings",
        "slug": "aluminum-powder-coat-framing",
        "spec": {
            "id": "ALUMINUM_POWDER_COAT",
            "name": "กรอบบานประตูหน้าต่างอะลูมิเนียมอบสีพาวเดอร์โค้ท (Powder Coated Architectural Aluminum Framing System)",
            "manufacturer": "มาตรฐาน มอก. เช่น ธาราทอง / เมืองทอง / Schüco / TOSTEM",
            "category": "openings_aluminum",
            "masterformat": "08 41 13 - Aluminum-Framed Entrances and Storefronts",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 284-2560 (อะลูมิเนียมอัลลอยอัดขึ้นรูปสำหรับงานสถาปัตยกรรม)",
                "aama": "AAMA 2604 (High Performance Organic Coatings on Aluminum Extrusions)",
            },
            "general_properties": [
                "อะลูมิเนียมอัลลอยเกรด 6063-T5 ความหนาไม่น้อยกว่า 1.5 มม. สำหรับหน้าต่าง และ 2.0 มม. สำหรับประตูและโครงสร้างรับแรงลม",
                "พ่นเคลือบสีฝุ่นอบความร้อน (Polyester Powder Coating) ความหนาฟิล์มสีไม่น้อยกว่า 60-80 ไมครอน ทนกรด-ด่างและรังสี UV",
                "ใช้ปะเก็นยาง EPDM คุณภาพสูงรอบขอบกระจกและกรอบบาน ป้องกันน้ำรั่วซึมและเสียงรบกวน",
            ],
            "surface_preparation": [
                "ตรวจเช็คช่องเปิดผนัง (Rough Opening) ให้ได้ฉาก แนวดิ่ง และระดับ คลาดเคลื่อนไม่เกิน ±3 มม.",
                "ผนังรอบช่องเปิดต้องฉาบปูนเรียบและจับเซี้ยมอย่างประณีต",
            ],
            "application_system": [
                "ติดตั้งวงกบด้วยพุกเหล็กและสกรูสแตนเลส SUS304 ระยะห่างไม่เกิน 50 ซม. ตลอดแนว",
                "ฉีดอุดช่องว่างระหว่างวงกบกับผนังด้วยโฟมโพลียูรีเทน (PU Foam) และปิดทับด้วยซิลิโคนกันสภาพอากาศ (Weatherproof Neutral Silicone)",
                "ติดตั้งฮาร์ดแวร์ บานพับ ล็อค และลูกล้อสแตนเลสเกรดพรีเมียม ปรับตั้งบานให้เปิดปิดนุ่มนวลแนบสนิท",
            ],
        },
    },
    {
        "division": "08-openings",
        "slug": "glass-tempered-clear-10mm",
        "spec": {
            "id": "GLASS_TEMPERED_CLEAR_10MM",
            "name": "กระจกนิรภัยเทมเปอร์ใส หนา 10 มม. (10mm Clear Fully Tempered Safety Glass)",
            "manufacturer": "AGC Glass Thailand / Guardian Glass / Thai-German Specialty Glass (TGSG)",
            "category": "openings_glass",
            "masterformat": "08 80 00 - Glazing",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 965-2560 (กระจกเทมเปอร์)",
                "astm": "ASTM C1048 (Kind FT Fully Tempered Flat Glass)",
                "ansi": "ANSI Z97.1 (Safety Glazing Materials)",
            },
            "general_properties": [
                "กระจกโฟลตใสผ่านกระบวนการอบความร้อนและทำให้เย็นลงอย่างรวดเร็ว (Thermal Tempering) แข็งแรงกว่ากระจกธรรมดา 4-5 เท่า",
                "เมื่อแตกจะแตกเป็นเม็ดข้าวโพดขนาดเล็ก ไม่มีคมแหลม ลดอันตรายต่อบุคคล",
                "ตัด เจียรขอบมน (Flat Polished Edge) และเจาะรูติดตั้งอุปกรณ์จากโรงงานก่อนเข้าเตาอบเทมเปอร์ (ห้ามตัดเจาะหลังเทมเปอร์)",
            ],
            "surface_preparation": [
                "ทำความสะอาดกรอบบาน ปราศจากเศษทรายหรือโลหะที่อาจสัมผัสผิวกระจก",
                "วางแผ่นรองรับน้ำหนัก (Setting Blocks) ชนิดยาง Neoprene ความแข็ง 80-90 Shore A ใต้ขอบล่างกระจก",
            ],
            "application_system": [
                "ยกติดตั้งกระจกด้วยเครื่องดูดสุญญากาศ ไม่ให้ขอบกระจกกระแทกของแข็งเด็ดขาด",
                "ยึดรอยต่อด้วยซิลิโคนโครงสร้างและซีลกันน้ำภายนอกด้วย Neutral Silicone คุณภาพสูง",
            ],
        },
    },
    {
        "division": "08-openings",
        "slug": "glass-laminated-acoustic-safety",
        "spec": {
            "id": "GLASS_LAMINATED_ACOUSTIC",
            "name": "กระจกนิรภัยลามิเนตกันเสียงและความปลอดภัย (Acoustic Safety Laminated Glass 6+0.76PVB+6mm)",
            "manufacturer": "AGC Glass Thailand / Saint-Gobain Glass / TGSG",
            "category": "openings_glass",
            "masterformat": "08 80 00 - Glazing",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 1222-2560 (กระจกลามิเนต)",
                "astm": "ASTM C1172",
            },
            "general_properties": [
                "กระจกใส 2 แผ่นประกบกันด้วยแผ่นฟิล์มโพลีไวนิลบิวทิรอลชนิดกันเสียง (Acoustic PVB Interlayer) ความหนาฟิล์มไม่น้อยกว่า 0.76 มม.",
                "ช่วยลดเสียงรบกวนจากภายนอก (Sound Transmission Class STC) สูงกว่ากระจกธรรมดาอย่างมีนัยสำคัญ",
                "เมื่อกระจกแตก แผ่นฟิล์มจะยึดเศษกระจกไว้ไม่ให้ร่วงหล่นลงมาทำอันตราย และป้องกันการบุกรุก",
            ],
            "surface_preparation": [
                "ตรวจเช็คร่องรับกระจกให้มีช่องว่างระบายน้ำและความชื้น ไม่ให้ฟิล์ม PVB สัมผัสความชื้นขังต่อเนื่อง",
            ],
            "application_system": [
                "ใช้ซิลิโคนชนิดไม่ทำปฏิกิริยากับฟิล์ม PVB (PVB Compatible Non-Acetic Silicone) เท่านั้น",
                "เว้นระยะขอบรอบกระจกอย่างน้อย 5 มม. เพื่อรองรับการขยายตัวทางความร้อน",
            ],
        },
    },
    {
        "division": "08-openings",
        "slug": "solid-teak-door",
        "spec": {
            "id": "SOLID_TEAK_DOOR",
            "name": "บานประตูไม้สักทองจริงคัดพิเศษ (Solid Natural Golden Teak Architectural Door)",
            "manufacturer": "Siam Timber Fabricators / ช่างไม้มาตรฐาน มอก.",
            "category": "openings_wood",
            "masterformat": "08 14 00 - Wood Doors",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 267-2521 (ไม้สักแปรรูป)",
                "fsc": "Forest Stewardship Council (FSC Certified)",
            },
            "general_properties": [
                "ไม้สักทองธรรมชาติคัดลายสวยงาม ผ่านกระบวนการอบแห้ง (Kiln Dried) ควบคุมความชื้นไม่เกิน 10-12%",
                "บานลูกฟักหรือบานเรียบสถาปัตยกรรม หนาไม่น้อยกว่า 38-45 มม.",
                "ผ่านการอัดน้ำยาป้องกันมอดและปลวก มีความคงทนและไม่บิดงอตามสภาพอากาศ",
            ],
            "surface_preparation": [
                "ติดตั้งวงกบไม้เนื้อแข็งให้ได้ดิ่งและฉากเรียบร้อยก่อนไสปรับบานประตู",
            ],
            "application_system": [
                "ไสปรับขอบบานประตูให้มีช่องว่างรอบวงกบ 2-3 มม. และขอบล่าง 5-8 มม.",
                "ติดตั้งบานพับสแตนเลส SUS304 ขนาด 4x3 นิ้ว หนา 2.5-3.0 มม. จำนวนไม่น้อยกว่า 4 ตัวต่อบาน",
                "เคลือบผิวด้วยสีย้อมไม้โพลียูรีเทน (Polyurethane Wood Coating) ทนรอยขีดข่วน จำนวน 3 เที่ยว",
            ],
        },
    },

    # -------------------------------------------------------------
    # Division 09: งานตกแต่งและวัสดุผิวสัมผัส (Finishes)
    # -------------------------------------------------------------
    {
        "division": "09-finishes",
        "slug": "toa-supershield-exterior",
        "spec": {
            "id": "TOA_SUPERSHIELD_EXT",
            "name": "สีน้ำอะคริลิกแท้ 100% สำหรับทาภายนอกอาคาร (TOA SuperShield Titanium Exterior Paint)",
            "manufacturer": "TOA Paint (Thailand) Public Company Limited",
            "category": "finishes_paint",
            "masterformat": "09 91 13 - Exterior Painting",
            "warranty_years": 15,
            "standards": {
                "tis": "มอก. 2321-2564 (สีอิมัลชันทนสภาวะอากาศ)",
                "astm": "ASTM D4587 / ASTM D3359",
            },
            "general_properties": [
                "สีน้ำอะคริลิกแท้ 100% เกรดอัลตร้าพรีเมียม เทคโนโลยี ไททาเนียม ไตรฟูล (Ti-Pure Titanium) ทนแดด ทนรังสี UV สูง",
                "มีค่าการสะท้อนความร้อนจากแสงแดดสูงถึง 96.7% ช่วยลดอุณหภูมิพื้นผิวและประหยัดพลังงาน",
                "ฟิล์มสีทำความสะอาดตัวเองได้ (Self-Cleaning Technology) ป้องกันคราบฝุ่น คราบน้ำ ด่างและเกลือในปูน",
                "ปลอดภัย ปราศจากสารระเหยที่เป็นพิษ (Ultra Low VOCs) และไร้สารปรอทและตะกั่ว",
            ],
            "surface_preparation": [
                "พื้นผิวปูนใหม่: ต้องบ่มคอนกรีตไม่น้อยกว่า 28 วัน ความชื้นไม่เกิน 14% (วัดด้วยเครื่อง Protimeter) ค่าความเป็นด่าง pH 7-9",
                "ทำความสะอาดคราบฝุ่นผง สิ่งสกปรก คราบไขมัน และเศษปูนที่เกาะติดออกให้หมด แล้วทิ้งให้แห้งสนิท",
                "หากมีรอยแตกร้าวลายงา ให้อุดโป๊วด้วยอะคริลิกฟิลเลอร์คุณภาพสูงก่อนทาสี",
            ],
            "application_system": [
                "ชั้นที่ 1 (สีรองพื้น): ทาสีรองพื้นปูนใหม่กันด่าง TOA SuperShield Extra Primer จำนวน 1 เที่ยว ความหนาฟิล์มแห้ง 35 ไมครอน",
                "ชั้นที่ 2-3 (สีทับหน้า): ทาสีน้ำทับหน้า TOA SuperShield Titanium Exterior จำนวน 2 เที่ยว ความหนาฟิล์มแห้ง 30-35 ไมครอนต่อเที่ยว",
                "ระยะเวลาแห้งทาทับระหว่างเที่ยวไม่น้อยกว่า 2 ชั่วโมง",
            ],
        },
    },
    {
        "division": "09-finishes",
        "slug": "toa-4-seasons-interior",
        "spec": {
            "id": "TOA_4SEASONS_INT",
            "name": "สีน้ำอะคริลิกสำหรับทาภายในอาคาร ทีโอเอ โฟร์ซีซั่นส์ (TOA 4Seasons Acrylic Emulsion Interior)",
            "manufacturer": "TOA Paint (Thailand) Public Company Limited",
            "category": "finishes_paint",
            "masterformat": "09 91 23 - Interior Painting",
            "warranty_years": 8,
            "standards": {
                "tis": "มอก. 272-2549 (สีอิมัลชันใช้งานทั่วไป)",
            },
            "general_properties": [
                "สีน้ำอะคริลิกแท้ชนิดด้าน สำหรับทาผนังและฝ้าเพดานภายในอาคาร",
                "เช็ดล้างทำความสะอาดได้ง่าย ผสมสารป้องกันเชื้อราและแบคทีเรีย กลิ่นอ่อนเข้าอยู่ได้เร็ว",
                "การปกปิดพื้นผิวดีเยี่ยม ให้ฟิล์มสีเรียบเนียนสม่ำเสมอ",
            ],
            "surface_preparation": [
                "ผนังต้องแห้งสนิท สะอาด ปราศจากฝุ่นผงและคราบมัน ความชื้นไม่เกิน 14%",
            ],
            "application_system": [
                "ทาสีรองพื้นปูนใหม่กันด่าง TOA 4Seasons Alkali Resisting Primer จำนวน 1 เที่ยว",
                "ทาสีทับหน้า TOA 4Seasons Interior จำนวน 2 เที่ยว เว้นระยะแห้งทาทับ 2 ชั่วโมง",
            ],
        },
    },
    {
        "division": "09-finishes",
        "slug": "cotto-porcelain-tile-60x60",
        "spec": {
            "id": "COTTO_PORCELAIN_60X60",
            "name": "กระเบื้องพอร์ซเลนเคลือบผิวด้าน คอตโต้ 60x60 ซม. (COTTO Glazed Porcelain Tile 60x60 cm Matte)",
            "manufacturer": "SCG Ceramics Public Co., Ltd. (COTTO)",
            "category": "finishes_tiles",
            "masterformat": "09 30 13 - Ceramic Tiling",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 2508-2555 (กระเบื้องเซรามิก)",
                "iso": "ISO 13006 (Group BIa Water Absorption <= 0.5%)",
                "din": "DIN 51130 (Slip Resistance Class R10)",
            },
            "general_properties": [
                "กระเบื้องเนื้อเกลซพอร์ซเลนตัดขอบ (Rectified) ขนาด 60x60 ซม. ความหนา 9.5-10 มม.",
                "อัตราการดูดซึมน้ำต่ำมาก ไม่เกิน 0.5% (Group BIa) แข็งแกร่ง ทนต่อการขัดสีและสารเคมีทำความสะอาด",
                "ผิวสัมผัสด้าน ค่ากันลื่นระดับ R10 ปลอดภัยต่อการใช้งานทั้งห้องน้ำส่วนแห้ง ห้องนั่งเล่น และทางเดิน",
            ],
            "surface_preparation": [
                "พื้นคอนกรีตต้องบ่มแห้งสนิท ปรับระดับเรียบสม่ำเสมอ คลาดเคลื่อนไม่เกิน 2 มม. ต่อระยะ 2 เมตร",
                "ทำความสะอาดพื้นผิวให้ปราศจากฝุ่นและคราบน้ำมัน",
            ],
            "application_system": [
                "ปูด้วยกาวซีเมนต์เกรดสูง (Tile Adhesive Class C2TE) ปาดด้วยเกรียงหวีขนาด 8-10 มม. เต็มหลังแผ่น (Back Buttering)",
                "เว้นร่องยาแนว 2 มม. โดยใช้อุปกรณ์ปรับระดับกระเบื้อง (Tile Leveling Spacers)",
                "ยาแนวด้วยกาวยาแนวป้องกันเชื้อราและต้านคราบสกปรก (Anti-Fungus Epoxy/Cementitious Grout Class CG2WA)",
            ],
        },
    },
    {
        "division": "09-finishes",
        "slug": "scg-smartboard-ceiling-4mm",
        "spec": {
            "id": "SCG_SMARTBOARD_4MM",
            "name": "แผ่นไฟเบอร์ซีเมนต์ฝ้าเพดาน เอสซีจี สมาร์ทบอร์ด หนา 4 มม. (SCG Smartboard Fiber Cement Ceiling Board 4mm)",
            "manufacturer": "The Siam Fibre-Cement Co., Ltd. (SCG)",
            "category": "finishes_ceiling",
            "masterformat": "09 51 00 - Acoustical Ceilings / Fiber Cement Ceilings",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 1427-2561 (แผ่นไฟเบอร์ซีเมนต์)",
                "astm": "ASTM C1186 (Grade I)",
            },
            "general_properties": [
                "แผ่นไฟเบอร์ซีเมนต์เทคโนโลยี FIRM & FLEX ผสมผสานปูนซีเมนต์ปอร์ตแลนด์ ซิลิก้าบริสุทธิ์ และเส้นใยเซลลูโลส ปราศจากใยหิน 100%",
                "ความหนา 4.0 มม. ขนาด 60x240 ซม. หรือ 120x240 ซม. ขอบเรียบหรือเซาะร่อง",
                "ทนน้ำ ทนชื้น ไม่เปื่อยยุ่ย ปลวกไม่กิน และไม่ลามไฟ เหมาะสำหรับฝ้าเพดานภายนอกและชายคา",
            ],
            "surface_preparation": [
                "ติดตั้งโครงคร่าวเหล็กชุบสังกะสี C-Line เบอร์ 24 ระยะห่างโครงไม่เกิน 40x120 ซม. หรือ 60x60 ซม. ยึดโยงด้วยลวดสปริงปรับระดับได้ระนาบ",
            ],
            "application_system": [
                "ยึดแผ่นเข้ากับโครงคร่าวด้วยสกรูปลายแหลมมีปีก SCG ความยาวไม่น้อยกว่า 18 มม. ระยะห่างสกรูไม่เกิน 20 ซม. ตามขอบแผ่น",
                "เว้นร่องรอยต่อแผ่น 3-5 มม. สำหรับฝ้าตีเว้นร่อง หรือยาแนวด้วยโพลียูรีเทนซีลแลนท์สำหรับงานภายนอก",
            ],
        },
    },
    {
        "division": "09-finishes",
        "slug": "gyproc-gypsum-board-9mm",
        "spec": {
            "id": "GYPROC_GYPSUM_9MM",
            "name": "แผ่นยิปซัมบอร์ด ยิปรอค หนา 9 มม. ขอบลาด (Gyproc Standard Gypsum Plasterboard 9mm Tapered Edge)",
            "manufacturer": "Thai Gypsum Products Public Co., Ltd. (Saint-Gobain Gyproc)",
            "category": "finishes_drywall",
            "masterformat": "09 29 00 - Gypsum Board",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 188-2547 (แผ่นยิปซัม)",
                "astm": "ASTM C1396",
                "bs": "BS EN 520",
            },
            "general_properties": [
                "แผ่นยิปซัมบอร์ดมาตรฐาน ความหนา 9.0 มม. ขนาด 120x240 ซม. ขอบลาด (Tapered Edge)",
                "เนื้อยิปซัมบริสุทธิ์หุ้มด้วยกระดาษเหนียวพิเศษ ผิวหน้าเรียบเนียน ไม่ติดไฟและช่วยหน่วงไฟ",
                "น้ำหนักเบา ติดตั้งง่าย เหมาะสำหรับฝ้าเพดานฉาบเรียบภายในอาคารและผนังกั้นห้อง",
            ],
            "surface_preparation": [
                "ติดตั้งโครงคร่าวโลหะชุบสังกะสี C-Line ตาม มอก. 863 ระยะโครงห่าง 40x120 ซม. ปรับระดับระนาบได้แนวตรง",
            ],
            "application_system": [
                "ยึดแผ่นยิปซัมด้วยสกรูดำปลายแหลมสำหรับยิปซัม ห่างกันไม่เกิน 20 ซม. หัวสกรูจมลงใต้ผิวกระดาษเล็กน้อยโดยไม่ฉีกขาด",
                "ฉาบรอยต่อด้วยปูนฉาบยิปซัม Gyproc Jointing Compound ฝังแถบผ้าเทปกระดาษหรือเทปผ้ายิปซัม ฉาบแต่ง 3 ชั้นให้เรียบเนียน",
                "ขัดแต่งด้วยกระดาษทรายเบอร์ละเอียดและทำความสะอาดฝุ่นก่อนทาสีรองพื้น",
            ],
        },
    },

    # -------------------------------------------------------------
    # Division 22: งานระบบสุขาภิบาล (Plumbing)
    # -------------------------------------------------------------
    {
        "division": "22-plumbing",
        "slug": "scg-pvc-pipe-class-8-5",
        "spec": {
            "id": "SCG_PVC_CLASS_8_5",
            "name": "ท่อพีวีซีแข็งสำหรับงานระบายน้ำเสียและระบายอากาศ เอสซีจี ชั้น 8.5 (SCG Rigid PVC Pipe Class 8.5 Drainage & Vent)",
            "manufacturer": "Thai Pipe Industry / Nawaplastic Industries (SCG)",
            "category": "plumbing_drainage",
            "masterformat": "22 13 16 - Sanitary Waste and Vent Piping",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 17-2532 (ท่อพอลิไวนิลคลอไรด์แข็งสำหรับใช้เป็นท่อน้ำดื่มและระบายน้ำ)",
            },
            "general_properties": [
                "ท่อพีวีซีแข็งสีฟ้า ชั้นคุณภาพ 8.5 (ทนความดันใช้งานได้ 8.5 กก./ตร.ซม. หรือ 0.85 MPa)",
                "เนื้อท่อเหนียว ทนทาน ไม่เป็นสนิม ผิวภายในเรียบลื่น น้ำเสียไหลผ่านได้สะดวก ไม่อุดตันง่าย",
                "เหมาะสำหรับท่อน้ำทิ้ง ท่อของเสีย (Soil Pipe) ท่อน้ำทิ้งสุขภัณฑ์ (Waste Pipe) และท่อระบายอากาศ (Vent Pipe)",
            ],
            "surface_preparation": [
                "ตัดท่อให้ได้ฉาก ลบเศษครีบและลบมุมปลายท่อ 15 องศา",
                "เช็ดทำความสะอาดปลายท่อและข้อต่อด้วยน้ำยาทำความสะอาดท่อพีวีซี (PVC Primer/Cleaner) ให้แห้งสะอาด",
            ],
            "application_system": [
                "ทาน้ำยาประสานท่อพีวีซี (PVC Solvent Cement) สม่ำเสมอทั้งภายนอกปลายท่อและภายในข้อต่อ",
                "สวมท่อเข้าข้อต่อทันที ดันให้สุดแล้วบิดเล็กน้อย ถือค้างไว้ 15-30 วินาทีเพื่อป้องกันท่อดีดตัว",
                "วางสโลประบายน้ำไม่น้อยกว่า 1:50 สำหรับท่อขนาดเล็กกว่า 3 นิ้ว และ 1:100 สำหรับท่อ 4 นิ้วขึ้นไป",
                "ยึดท่อด้วยแคล้มป์รัดท่อ (Pipe Hangers) ทุกระยะ 1.00-1.50 ม. อย่างมั่นคง",
            ],
        },
    },
    {
        "division": "22-plumbing",
        "slug": "scg-pvc-pipe-class-13-5",
        "spec": {
            "id": "SCG_PVC_CLASS_13_5",
            "name": "ท่อพีวีซีแข็งสำหรับงานส่งน้ำประปารับแรงดัน เอสซีจี ชั้น 13.5 (SCG Rigid PVC Pipe Class 13.5 Potable Water Supply)",
            "manufacturer": "Thai Pipe Industry / Nawaplastic Industries (SCG)",
            "category": "plumbing_water_supply",
            "masterformat": "22 11 16 - Domestic Water Piping",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 17-2532 (ท่อพอลิไวนิลคลอไรด์แข็งสำหรับน้ำดื่ม)",
            },
            "general_properties": [
                "ท่อพีวีซีแข็งสีฟ้า ชั้นคุณภาพ 13.5 (ทนแรงดันใช้งานได้ 13.5 กก./ตร.ซม. หรือ 1.35 MPa)",
                "ผลิตจากเม็ดพลาสติก PVC บริสุทธิ์ ปลอดภัยสำหรับน้ำดื่ม ไม่มีสารตะกั่วและโลหะหนักตกค้าง",
                "เหมาะสำหรับระบบท่อน้ำดี ท่อส่งน้ำประปา และท่อหลังปั๊มน้ำแรงดันสูง",
            ],
            "surface_preparation": [
                "ตัดปลายท่อให้ตรง ลบคมมุมปลายท่อ ทำความสะอาดคราบไขมันและสิ่งสกปรก",
            ],
            "application_system": [
                "ต่อท่อด้วยน้ำยาประสานท่อคุณภาพสูงตาม มอก. 1032 หรือข้อต่อเกลียวทองเหลืองสำหรับจุดต่อก๊อกน้ำ",
                "ทดสอบแรงดันน้ำ (Hydrostatic Pressure Test) ที่แรงดัน 1.5 เท่าของแรงดันใช้งานจริง (ไม่น้อยกว่า 10 บาร์) นานอย่างน้อย 2 ชั่วโมงโดยแรงดันไม่ตก",
            ],
        },
    },
    {
        "division": "22-plumbing",
        "slug": "cotto-water-closet-dual-flush",
        "spec": {
            "id": "COTTO_WC_DUAL_FLUSH",
            "name": "โถสุขภัณฑ์นั่งราบประหยัดน้ำ คอตโต้ ระบบดูอัลฟลัช (COTTO Dual Flush Water Closet 3/4.5 Liters)",
            "manufacturer": "SCG Ceramics Public Co., Ltd. (COTTO)",
            "category": "plumbing_fixtures",
            "masterformat": "22 40 00 - Plumbing Fixtures",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 792-2554 (เครื่องสุขภัณฑ์เซรามิก: โถส้วม)",
                "water_sense": "ฉลากเขียวประหยัดน้ำเบอร์ 5",
            },
            "general_properties": [
                "โถสุขภัณฑ์แบบชิ้นเดียวหรือสองชิ้น ผลิตจากเซรามิกวิเทรียสไชน่า (Vitreous China) เคลือบสารยับยั้งแบคทีเรีย Ultra Clean+",
                "ระบบชำระล้าง Dual Flush ใช้น้ำเพียง 3 ลิตร (สำหรับเบา) และ 4.5 ลิตร (สำหรับหนัก)",
                "ระยะท่อน้ำทิ้งลงพื้น (Rough-in) มาตรฐาน 305 มม. จากผนังสำเร็จ",
                "ฝารองนั่งผลิตจากพลาสติก UF หรือ PP ทนรอยขีดข่วน พร้อมระบบปิดแบบนุ่มนวล (Soft Close)",
            ],
            "surface_preparation": [
                "ท่อน้ำทิ้งขนาดเส้นผ่านศูนย์กลาง 4 นิ้ว โผล่เหนือพื้นกระเบื้อง 1-2 ซม.",
                "พื้นห้องน้ำต้องปูกระเบื้องและยาแนวเสร็จสมบูรณ์ได้ระดับ",
            ],
            "application_system": [
                "ติดตั้งหน้าแปลนกันกลิ่นและน้ำรั่ว (Wax Ring / Flange Gasket) รัดเข้ากับปลายท่อน้ำทิ้งอย่างแนบสนิท",
                "ยึดขาโถเข้ากับพื้นด้วยพุกสแตนเลสและยาแนวรอบฐานด้วยซิลิโคนป้องกันเชื้อราสีขาว",
                "ต่อสายน้ำดีสแตนเลสถักเข้ากับวาล์วเปิด-ปิดน้ำ (Stop Valve) ตรวจสอบการไหลและทดสอบการชำระล้าง",
            ],
        },
    },

    # -------------------------------------------------------------
    # Division 26: งานระบบไฟฟ้า (Electrical)
    # -------------------------------------------------------------
    {
        "division": "26-electrical",
        "slug": "bangkok-cable-thw",
        "spec": {
            "id": "BCC_CABLE_THW",
            "name": "สายไฟฟ้าตัวนำทองแดงหุ้มฉนวน พีวีซี 60227 IEC 01 THW (Bangkok Cable Copper Wire 60227 IEC 01 THW 450/750V)",
            "manufacturer": "Bangkok Cable Co., Ltd. (BCC) / Phelps Dodge Thailand",
            "category": "electrical_wiring",
            "masterformat": "26 05 19 - Low-Voltage Electrical Power Conductors and Cables",
            "warranty_years": 10,
            "standards": {
                "tis": "มอก. 11-2553 เล่ม 3 (สายไฟฟ้าหุ้มฉนวนพอลิไวนิลคลอไรด์ แรงดันใช้งานไม่เกิน 450/750 โวลต์)",
                "iec": "IEC 60227-3",
                "eit": "มาตรฐานการติดตั้งทางไฟฟ้าสำหรับประเทศไทย (วสท.)",
            },
            "general_properties": [
                "สายไฟตัวนำทองแดงแท้บริสุทธิ์ 99.9% ชนิดแกนเดี่ยว หุ้มฉนวน PVC ทนอุณหภูมิใช้งาน 70 องศาเซลเซียส แรงดัน 450/750V",
                "สีของฉนวนตามมาตรฐาน วสท. ล่าสุด: เฟส A (น้ำตาล), เฟส B (ดำ), เฟส C (เทา), นิวทรัล (ฟ้า), กราวด์ (เขียวแถบเหลือง)",
                "เหมาะสำหรับเดินร้อยท่อฝังผนัง ร้อยท่อเกาะผนัง หรือร้อยท่อบนฝ้าเพดาน (ห้ามฝังดินโดยตรง)",
            ],
            "surface_preparation": [
                "ท่อร้อยสายไฟ (EMT หรือ UPVC) ต้องติดตั้งเสร็จสมบูรณ์ ปัดฝุ่นและทำความสะอาดภายในท่อ",
            ],
            "application_system": [
                "ร้อยสายไฟด้วยลวดดึงสาย (Fish Tape) โดยไม่ใช้แรงดึงจนฉนวนยืดหรือฉีกขาด และใช้แป้งร้อยสายไฟเพื่อลดแรงเสียดทาน",
                "จำนวนสายในท่อต้องมีพื้นที่หน้าตัดรวมไม่เกิน 40% ของพื้นที่หน้าตัดภายในท่อตามมาตรฐาน วสท.",
                "ต่อสายไฟในกล่องต่อสาย (Junction Box) ด้วยวายนัท (Wire Nut) หรือขั้วต่อสายมาตรฐาน ห้ามพันเทปต่อสายกลางท่อโดยเด็ดขาด",
            ],
        },
    },
    {
        "division": "26-electrical",
        "slug": "panasonic-wide-series",
        "spec": {
            "id": "PANASONIC_WIDE_SERIES",
            "name": "ชุดสวิตช์และเต้ารับไฟฟ้ามีกราวด์ พานาโซนิค ไวด์ซีรีส์ (Panasonic Wide Series Switches and Receptacles)",
            "manufacturer": "Panasonic Life Solutions (Thailand) Co., Ltd.",
            "category": "electrical_devices",
            "masterformat": "26 27 26 - Wiring Devices",
            "warranty_years": 5,
            "standards": {
                "tis": "มอก. 824-2551 (สวิตช์ไฟฟ้า) / มอก. 166-2549 (เต้ารับและเต้าเสียบ)",
                "iec": "IEC 60669-1 / IEC 60884-1",
            },
            "general_properties": [
                "อุปกรณ์สวิตช์และเต้ารับหน้าสัมผัสกว้าง ดีไซน์เรียบหรู ผลิตจากพลาสติกโพลีคาร์บอเนต (PC) ไม่ลามไฟ ทนทานสูง",
                "เต้ารับคู่มีกราวด์ (Duplex Universal Receptacle with Ground) รองรับกระแสไฟฟ้า 16A 250V พร้อมม่านนิรภัย (Safety Shutter)",
                "สวิตช์ไฟรองรับกระแส 16A 250V หน้าสัมผัสเงินบริสุทธิ์ ทนทานต่อการเปิดปิดมากกว่า 40,000 ครั้ง",
            ],
            "surface_preparation": [
                "กล่องฝังผนัง (Handy Box) ติดตั้งได้ระดับ แนวดิ่ง และระดับความสูงตามแบบสถาปัตยกรรม (สวิตช์สูง 1.10-1.20 ม., เต้ารับสูง 0.30-0.40 ม.)",
            ],
            "application_system": [
                "ต่อสายไฟเข้ารูเสียบล็อคอัตโนมัติ (Quick Connect Terminal) ปอกฉนวนตามระยะที่ระบุหลังอุปกรณ์ แน่นหนา ไม่หลวมคลอน",
                "ขันยึดหน้ากากและโครงเข้ากับกล่องฝังให้แนบสนิทกับผิวผนัง",
                "ทดสอบขั้วไฟฟ้า (Polarity Test) ตรวจสอบ L, N, G ถูกต้อง และทดสอบการทำงานของกราวด์อย่างสมบูรณ์",
            ],
        },
    },
]


def main():
    root = Path(__file__).resolve().parent.parent
    packages_dir = root / "packages"
    packages_dir.mkdir(parents=True, exist_ok=True)

    registry_entries = []

    print(f"Scaffolding {len(PACKAGES)} material specifications into {packages_dir}...")

    for item in PACKAGES:
        div = item["division"]
        slug = item["slug"]
        spec_data = item["spec"]

        pkg_path = packages_dir / div / slug
        pkg_path.mkdir(parents=True, exist_ok=True)

        spec_file = pkg_path / "spec.yaml"
        with open(spec_file, "w", encoding="utf-8") as f:
            yaml.safe_dump(spec_data, f, sort_keys=False, allow_unicode=True, width=120)

        # Registry index entry
        registry_entries.append({
            "id": spec_data["id"],
            "name": spec_data["name"],
            "slug": slug,
            "division": div,
            "category": spec_data["category"],
            "manufacturer": spec_data["manufacturer"],
            "masterformat": spec_data["masterformat"],
            "warranty_years": spec_data.get("warranty_years"),
            "standards": spec_data.get("standards", {}),
            "package_path": f"packages/{div}/{slug}",
            "spec_url": f"https://raw.githubusercontent.com/PRIDA-TAKON/debim-specs-th/main/packages/{div}/{slug}/spec.yaml",
        })

    # Write registry.json
    registry_file = root / "registry.json"
    with open(registry_file, "w", encoding="utf-8") as f:
        json.dump(
            {
                "schema_version": "1.0.0",
                "repository": "PRIDA-TAKON/debim-specs-th",
                "description": "คลังรายการประกอบแบบวัสดุก่อสร้างภาษาไทยแบบเปิด (Open Thai Declarative Architectural Specifications)",
                "total_packages": len(registry_entries),
                "packages": registry_entries,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )
    print(f"Wrote {registry_file} ({len(registry_entries)} packages indexed)")


if __name__ == "__main__":
    main()
