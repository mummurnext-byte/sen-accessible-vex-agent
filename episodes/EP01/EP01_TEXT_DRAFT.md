# EP01 - Meet Your VEX IQ Brain

## Status

- State: `TEXT_REVIEW_REQUIRED`
- Owner approval: pending
- Physical test: not started
- Planned public video duration: 85 seconds
- Spoken language: English
- Caption languages: English and Thai

## Learning Design

### Objective

Learners identify **input**, **Brain**, and **output** in a VEX IQ program and connect each idea to a visible part of one Blocks stack.

### Success Criteria

By the end of the lesson, a learner can:

1. point to the Brain Check button and label it as an input;
2. point to the VEXcode stack and explain that the Brain follows the blocks in order; and
3. identify the screen message and drivetrain movement as outputs.

### Prerequisites

- No robotics or coding experience required.
- Learners should be able to match three icons in a left-to-right sequence.

### Hardware and Setup

- VEX IQ Brain (2nd generation)
- charged VEX IQ battery
- configured two-motor drivetrain or BaseBot
- computer or tablet with VEXcode IQ Blocks
- USB-C or supported wireless connection
- a clear 500 mm driving lane
- start line and 300 mm target line made with high-contrast tape
- three large cards: `INPUT`, `BRAIN`, `OUTPUT`

### Verified Sources

- Brain button sensing and events: https://api.vex.com/iq2/home/blocks/Sensors/brain_sensing.html
- Brain screen printing and font color: https://api.vex.com/iq2/home/blocks/screen.html
- Drivetrain movement: https://api.vex.com/iq2/home/blocks/drivetrain.html
- VEX IQ 2nd Gen Blocks reference: https://api.vex.com/iq2/home/blocks/index.html

## Public Video Text

### English Narration

Every robot program begins with one pattern: **input, Brain, output**.

The Check button is our input. It tells the robot that something has happened.

The VEX IQ Brain reads that input and follows these blocks from top to bottom. First, the screen says **PRESS CHECK**. This gives us a visual instruction before the robot moves.

When I press the Check button, the waiting block becomes true. The Brain changes the screen to **GO**, then tells the drivetrain to move forward for 300 millimeters.

When the movement finishes, the final output appears: **DONE**.

Input is what the robot detects. The Brain is where the program makes the decision. Output is what the robot shows or does.

Now predict: if we change 300 to 500 millimeters, which part stays the same, and which output changes?

Download the English and Thai lesson materials from our open repository.

Input your logic, spark their world. See you in the next log.

### Timestamped Visual Plan

| Time | Visual | Narration purpose | Accessibility cue |
| --- | --- | --- | --- |
| 00:00-00:05 | No speech for the first two seconds. Close-up of the Check button, then the screen changes from `PRESS CHECK` to `GO`; robot begins moving. Title: `INPUT -> BRAIN -> OUTPUT`. | Silent hook and result preview | Three labeled boxes and arrows; no meaning depends on sound |
| 00:05-00:13 | Sen digital host beside three large cards: finger icon `INPUT`, Brain icon `BRAIN`, wheel/screen icon `OUTPUT`. | Introduce the model | Stable cards remain visible while each term is spoken |
| 00:13-00:25 | Full-screen VEXcode Blocks stack. Highlight `wait until <Brain Check button pressed?>`. | Connect button to input | Yellow outline and number `1`; caption placed above lower safe zone |
| 00:25-00:39 | Highlight the blocks from top to bottom: `PRESS CHECK`, wait, `GO`, drive 300 mm, `DONE`. | Explain Brain execution order | Moving highlight advances one block at a time; arrows stay fixed |
| 00:39-00:55 | Split view: left shows finger pressing Check; center shows highlighted block; right shows robot driving to the 300 mm tape line. | Prove input-to-output behavior | Labels `INPUT`, `BRAIN`, `OUTPUT` stay over the three views |
| 00:55-01:05 | Brain screen close-up changes to `DONE`; then freeze frame of target line. | Confirm final output | Word plus check icon, not color alone |
| 01:05-01:15 | Two parameter cards, `300 mm` and `500 mm`; learner sees a large question mark over the output card. | Visual prediction check | Five-second pause gives reading and response time |
| 01:15-01:25 | Sen digital host; GitHub repository card with `EP01`, teacher deck, worksheet, and Blocks project icons. | Open-source call to action | Download items are shown as labeled icons; complete sign-off remains on screen |

### On-Screen Title and Cover

- Cover title: `HOW A ROBOT THINKS`
- Supporting line: `INPUT -> BRAIN -> OUTPUT`
- Accessibility label: `VEX IQ BLOCKS · LOG 01`
- Visual style: white background, near-black text, emerald status accent, yellow execution highlight
- Do not use Matrix-style falling code behind the VEXcode stack because it reduces block readability.

## VEXcode IQ Blocks

### Device Configuration

- Platform: VEX IQ (2nd generation)
- Project type: Blocks
- Device: two-motor Drivetrain
- Suggested build: BaseBot
- Verify left and right motor direction in the Devices menu before running.

### Exact Block Stack

```text
when started
  clear screen
  set font to [monospaced] [large] on screen
  set pen / font color to [blue] on screen
  print [PRESS CHECK] on screen
  wait until <Brain [Check] button pressed?>
  clear screen
  set pen / font color to [green] on screen
  print [GO] on screen
  drive [forward] for [300] [mm] and wait
  clear screen
  set pen / font color to [yellow] on screen
  print [DONE] on screen
```

### Visual Block Labels

| Number | Block section | Learning label |
| ---: | --- | --- |
| 1 | `wait until <Brain Check button pressed?>` | INPUT |
| 2 | ordered stack running on the Brain | BRAIN FOLLOWS THE PLAN |
| 3 | screen messages and `drive forward for 300 mm` | OUTPUT |

### Expected Result

1. Brain screen displays `PRESS CHECK`.
2. Robot remains stationary until the Check button is pressed.
3. Brain screen displays `GO`.
4. Robot drives forward approximately 300 mm.
5. Brain screen displays `DONE`.

### Physical Test Record

`NOT YET TESTED`

Before text approval becomes video production approval, test:

- drivetrain direction;
- stopping distance on the selected surface;
- screen text size and contrast on camera;
- whether the Brain button remains accessible on the chosen build; and
- whether the full sequence repeats reliably for three runs.

## Teacher Deck - English

### Slide 1 - Today’s Visual Goal

Show the three-card sequence:

`INPUT -> BRAIN -> OUTPUT`

Goal: “I can show what the robot detects, decides, and does.”

### Slide 2 - Meet the Three Parts

- Input: information entering the robot
- Brain: the device running the Blocks project
- Output: a visible action from the screen or motors

Use icons with each definition.

### Slide 3 - Hardware Map

Show the Brain Check button, Brain screen, and drivetrain motors. Draw a line from each item to its matching card.

### Slide 4 - Predict

Show only the completed block stack. Ask learners to arrange three image cards:

1. press Check;
2. robot drives;
3. screen says DONE.

Do not run the robot yet.

### Slide 5 - Build the Blocks

Build the stack in three numbered sections. Keep the exact English block names visible.

### Slide 6 - Run and Observe

One learner presses Check. One learner points to the active section on a printed block stack. One learner places the output card beside the moving robot.

### Slide 7 - Change One Parameter

Change `300 mm` to `500 mm`. Ask which parts remain the same and which output changes.

### Slide 8 - Check Understanding

Learners match:

- Check button -> INPUT
- VEXcode stack running on Brain -> BRAIN
- screen message and movement -> OUTPUT

### Slide 9 - Extension and License

Extension: replace the Check button with the Left or Right Brain button.

Include official source links and CC BY-NC-SA 4.0 notice.

## Teacher Deck - Thai

### สไลด์ 1 - เป้าหมายที่มองเห็นได้วันนี้

แสดงลำดับการ์ด 3 ใบ:

`INPUT -> BRAIN -> OUTPUT`

เป้าหมาย: “ฉันสามารถชี้ให้เห็นได้ว่าหุ่นยนต์รับข้อมูล ประมวลผล และแสดงผลอย่างไร”

### สไลด์ 2 - รู้จัก 3 ส่วนสำคัญ

- Input (ข้อมูลเข้า): ข้อมูลที่เข้าสู่หุ่นยนต์
- Brain (สมองกล): อุปกรณ์ที่ทำงานตามโปรเจกต์ Blocks
- Output (ผลลัพธ์): สิ่งที่หน้าจอหรือมอเตอร์แสดงออกมาให้เห็น

ใช้ไอคอนคู่กับทุกคำอธิบาย

### สไลด์ 3 - แผนผังอุปกรณ์

แสดงปุ่ม Check หน้าจอ Brain และมอเตอร์ขับเคลื่อน ลากเส้นเชื่อมอุปกรณ์แต่ละชิ้นกับการ์ดที่ตรงกัน

### สไลด์ 4 - คาดเดาก่อนทดลอง

แสดงชุดบล็อกที่เสร็จแล้ว ให้ผู้เรียนเรียงการ์ดภาพ 3 ใบ:

1. กดปุ่ม Check
2. หุ่นยนต์เคลื่อนที่
3. หน้าจอแสดง DONE

ยังไม่เปิดโปรแกรมในขั้นตอนนี้

### สไลด์ 5 - ต่อบล็อก

สร้างชุดบล็อกเป็น 3 ส่วนพร้อมหมายเลข และคงชื่อบล็อกภาษาอังกฤษตามที่ปรากฏใน VEXcode

### สไลด์ 6 - ทดลองและสังเกต

ผู้เรียนคนหนึ่งกด Check คนหนึ่งชี้ส่วนของบล็อกที่กำลังทำงาน และอีกคนวางการ์ด Output ข้างหุ่นยนต์ที่กำลังเคลื่อนที่

### สไลด์ 7 - เปลี่ยนค่าเพียงหนึ่งค่า

เปลี่ยน `300 mm` เป็น `500 mm` แล้วถามว่าส่วนใดเหมือนเดิม และผลลัพธ์ใดเปลี่ยนไป

### สไลด์ 8 - ตรวจสอบความเข้าใจ

ให้ผู้เรียนจับคู่:

- ปุ่ม Check -> INPUT
- ชุดคำสั่ง VEXcode ที่ทำงานใน Brain -> BRAIN
- ข้อความบนหน้าจอและการเคลื่อนที่ -> OUTPUT

### สไลด์ 9 - กิจกรรมต่อยอดและสัญญาอนุญาต

กิจกรรมต่อยอด: เปลี่ยนจากปุ่ม Check เป็นปุ่ม Left หรือ Right บน Brain

ใส่ลิงก์แหล่งข้อมูลทางการและข้อความ CC BY-NC-SA 4.0

## Student Worksheet - English

### Page 1 - Match the Robot System

Draw a line between each item and its job:

| Item | Job choices |
| --- | --- |
| Check button | INPUT / BRAIN / OUTPUT |
| VEX IQ Brain running the Blocks | INPUT / BRAIN / OUTPUT |
| Robot drives forward | INPUT / BRAIN / OUTPUT |
| Screen says DONE | INPUT / BRAIN / OUTPUT |

Number these events from 1 to 4:

- [ ] Robot drives 300 mm.
- [ ] Screen says DONE.
- [ ] Learner presses Check.
- [ ] Screen says GO.

### Page 2 - Predict, Run, Change

Before running:

`I predict the robot will stop at: 100 mm / 300 mm / 500 mm`

After running:

`The robot stopped near: ______ mm`

Change `300 mm` to `500 mm`.

- Input changed: YES / NO
- Brain follows a changed parameter: YES / NO
- Output distance changed: YES / NO

Exit check: circle the correct sequence.

- A. OUTPUT -> INPUT -> BRAIN
- B. INPUT -> BRAIN -> OUTPUT
- C. BRAIN -> OUTPUT -> INPUT

## Student Worksheet - Thai

### หน้า 1 - จับคู่ระบบของหุ่นยนต์

ลากเส้นเชื่อมอุปกรณ์แต่ละอย่างกับหน้าที่:

| อุปกรณ์หรือเหตุการณ์ | ตัวเลือกหน้าที่ |
| --- | --- |
| ปุ่ม Check | INPUT / BRAIN / OUTPUT |
| VEX IQ Brain ที่กำลังทำงานตาม Blocks | INPUT / BRAIN / OUTPUT |
| หุ่นยนต์เคลื่อนที่ไปข้างหน้า | INPUT / BRAIN / OUTPUT |
| หน้าจอแสดง DONE | INPUT / BRAIN / OUTPUT |

ใส่หมายเลข 1 ถึง 4 ตามลำดับเหตุการณ์:

- [ ] หุ่นยนต์เคลื่อนที่ 300 mm
- [ ] หน้าจอแสดง DONE
- [ ] ผู้เรียนกด Check
- [ ] หน้าจอแสดง GO

### หน้า 2 - คาดเดา ทดลอง และเปลี่ยนค่า

ก่อนทดลอง:

`ฉันคาดว่าหุ่นยนต์จะหยุดที่: 100 mm / 300 mm / 500 mm`

หลังทดลอง:

`หุ่นยนต์หยุดใกล้ตำแหน่ง: ______ mm`

เปลี่ยน `300 mm` เป็น `500 mm`

- Input เปลี่ยนหรือไม่: เปลี่ยน / ไม่เปลี่ยน
- Brain ทำงานตามค่าที่เปลี่ยนหรือไม่: ใช่ / ไม่ใช่
- ระยะทาง Output เปลี่ยนหรือไม่: เปลี่ยน / ไม่เปลี่ยน

ตรวจสอบก่อนจบบทเรียน: วงกลมลำดับที่ถูกต้อง

- A. OUTPUT -> INPUT -> BRAIN
- B. INPUT -> BRAIN -> OUTPUT
- C. BRAIN -> OUTPUT -> INPUT

## Facebook Copy

### Title

How Does a VEX IQ Robot Think? | Accessible Robotics Log 01

### Description

Every robot program follows the same visible pattern: INPUT -> BRAIN -> OUTPUT.

In Log 01, Sen uses one VEX IQ Brain button, one Blocks stack, and two screen messages to help first-time learners see exactly how a robot receives information and responds.

English narration. English and Thai captions. Free classroom materials for deaf and hard-of-hearing learners.

Comment **LOG01** to receive the open lesson package when it is published.

This is an AI-assisted open research log for accessible STEM education.

### Hashtags

`#AccessibleSTEM #VEXIQ #VEXcode #DeafEducation #RoboticsEducation #OpenEducation #MummurNext`

### Comment Keyword

`LOG01`

Automation must not be enabled until the downloadable repository link exists and the Facebook account owner has approved the response text.

## Accessibility Audit

- [x] The learning objective works without audio.
- [x] All narration meaning is represented in captions or visuals.
- [x] Input, Brain, and Output each use text plus an icon.
- [x] Color is not the only indicator.
- [x] Block order is numbered.
- [x] English block names remain visible in Thai materials.
- [x] The prediction pause gives learners time to respond.
- [x] Essential captions are planned above the bottom platform overlay zone.
- [ ] Screen text legibility has been confirmed on a real vertical-video recording.
- [ ] A deaf or hard-of-hearing learner or educator has reviewed the classroom package.

## Safety Notes

- Use a clear driving lane at least 500 mm long.
- Keep hands, cables, and loose objects away from the drivetrain.
- Place the robot on a stand while checking motor direction during setup.
- Do not run the drivetrain on a table edge.
- Stop the program before lifting or repositioning the robot.

## Revision Notes

- v0.1: Initial text package prepared for owner review.
- Video production is blocked until explicit `TEXT_APPROVED` is recorded.
