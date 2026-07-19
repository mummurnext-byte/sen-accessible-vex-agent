from __future__ import annotations

from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
config.background_color = "#1E1E1E"

BG = "#1E1E1E"
WHITE = "#FFFFFF"
GRAY = "#A0A0A0"
GRID = "#343434"
INPUT = "#00D2FF"
BRAIN = "#FFD700"
OUTPUT = "#BD00FF"
GREEN = "#31E981"
RED = "#FF4D67"


class SilentSparksEP01(Scene):
    def construct(self) -> None:
        self.hud = self.make_hud()
        self.add(self.hud)
        self.block_1_silent_hook()
        self.block_2_input()
        self.block_3_brain()
        self.block_4_simulation()
        self.block_5_prediction()
        self.block_6_repository()

    def make_hud(self) -> VGroup:
        grid = VGroup()
        for x in np.arange(-4.5, 4.6, 0.75):
            grid.add(Line([x, -8, 0], [x, 8, 0], color=GRID, stroke_width=1, stroke_opacity=0.22))
        for y in np.arange(-8, 8.1, 0.75):
            grid.add(Line([-4.5, y, 0], [4.5, y, 0], color=GRID, stroke_width=1, stroke_opacity=0.22))
        label = Text("SILENT SPARKS / LOG 01", font="Arial", font_size=21, weight=BOLD, color=INPUT)
        label.to_corner(UL, buff=0.32)
        version = Text("VEX IQ BLOCKS", font="Arial", font_size=18, color=GRAY)
        version.to_corner(UR, buff=0.32)
        top_rule = Line([-4.15, 7.38, 0], [4.15, 7.38, 0], color=GRID, stroke_width=2)
        return VGroup(grid, label, version, top_rule)

    def caption(self, english: str, thai: str) -> VGroup:
        panel = RoundedRectangle(width=8.25, height=2.15, corner_radius=0.16)
        panel.set_fill("#111111", opacity=0.96).set_stroke("#505050", width=2)
        panel.move_to([0, -6.2, 0])
        en = Text(english, font="Arial", font_size=27, color=GRAY, weight=BOLD)
        en.scale_to_fit_width(7.6).move_to([0, -5.78, 0])
        th = Text(thai, font="Leelawadee UI", font_size=42, color=WHITE, weight=BOLD)
        th.scale_to_fit_width(7.65).move_to([0, -6.48, 0])
        accent = Rectangle(width=0.08, height=1.72, fill_color=INPUT, fill_opacity=1, stroke_width=0)
        accent.move_to([-3.91, -6.2, 0])
        return VGroup(panel, accent, en, th)

    def stick_figure(self, scale: float = 1.0, color: str = WHITE) -> VGroup:
        head = Circle(radius=0.31, color=color, stroke_width=6)
        head.move_to([0, 1.15, 0])
        body = Line([0, 0.84, 0], [0, -0.35, 0], color=color, stroke_width=7)
        left_arm = Line([0, 0.48, 0], [-0.55, -0.02, 0], color=color, stroke_width=7)
        right_arm = Line([0, 0.48, 0], [0.72, 0.18, 0], color=color, stroke_width=7)
        left_leg = Line([0, -0.35, 0], [-0.48, -1.25, 0], color=color, stroke_width=7)
        right_leg = Line([0, -0.35, 0], [0.52, -1.25, 0], color=color, stroke_width=7)
        eye_l = Dot([-0.11, 1.2, 0], radius=0.025, color=color)
        eye_r = Dot([0.11, 1.2, 0], radius=0.025, color=color)
        smile = Arc(radius=0.13, start_angle=PI * 1.12, angle=PI * 0.76, color=color, stroke_width=3)
        smile.move_to([0, 1.08, 0])
        return VGroup(head, body, left_arm, right_arm, left_leg, right_leg, eye_l, eye_r, smile).scale(scale)

    def logic_box(self, label: str, color: str) -> VGroup:
        box = RoundedRectangle(width=2.25, height=1.35, corner_radius=0.15, color=color, stroke_width=6)
        box.set_fill("#272727", opacity=1)
        text = Text(label, font="Arial", font_size=31, weight=BOLD, color=WHITE)
        return VGroup(box, text)

    def code_block(self, text: str, color: str, width: float = 5.9) -> VGroup:
        block = RoundedRectangle(width=width, height=0.74, corner_radius=0.12)
        block.set_fill(color, opacity=0.92).set_stroke(WHITE, width=1.4, opacity=0.42)
        label = Text(text, font="Arial", font_size=23, weight=BOLD, color=WHITE)
        if label.width > width - 0.42:
            label.scale_to_fit_width(width - 0.42)
        return VGroup(block, label)

    def vex_brain(self) -> VGroup:
        body = RoundedRectangle(width=3.0, height=2.8, corner_radius=0.24, color=WHITE, stroke_width=5)
        body.set_fill("#292929", opacity=1)
        screen = RoundedRectangle(width=1.9, height=0.95, corner_radius=0.12)
        screen.set_fill("#0B1720", opacity=1).set_stroke(INPUT, width=4).shift(UP * 0.48)
        title = Text("VEX IQ BRAIN", font="Arial", font_size=20, weight=BOLD, color=GRAY).shift(UP * 1.02)
        check = RoundedRectangle(width=0.72, height=0.58, corner_radius=0.1)
        check.set_fill(INPUT, opacity=1).set_stroke(WHITE, width=2).shift(DOWN * 0.78)
        check_text = Text("CHECK", font="Arial", font_size=13, weight=BOLD, color=BG).move_to(check)
        return VGroup(body, screen, title, check, check_text)

    def robot(self) -> VGroup:
        body = RoundedRectangle(width=1.75, height=0.95, corner_radius=0.18, color=WHITE, stroke_width=4)
        body.set_fill("#333333", opacity=1)
        brain = RoundedRectangle(width=0.95, height=0.65, corner_radius=0.1)
        brain.set_fill("#111111", opacity=1).set_stroke(INPUT, width=3).shift(UP * 0.55)
        screen = Text("GO", font="Arial", font_size=20, weight=BOLD, color=GREEN).move_to(brain)
        wheel_l = Circle(radius=0.31, color=WHITE, stroke_width=4).shift(LEFT * 0.58 + DOWN * 0.62)
        wheel_r = Circle(radius=0.31, color=WHITE, stroke_width=4).shift(RIGHT * 0.58 + DOWN * 0.62)
        spoke_l = VGroup(Line(LEFT * 0.22, RIGHT * 0.22), Line(DOWN * 0.22, UP * 0.22)).move_to(wheel_l)
        spoke_r = VGroup(Line(LEFT * 0.22, RIGHT * 0.22), Line(DOWN * 0.22, UP * 0.22)).move_to(wheel_r)
        return VGroup(body, brain, screen, wheel_l, wheel_r, spoke_l, spoke_r)

    def block_1_silent_hook(self) -> None:
        teacher = self.stick_figure(1.05).move_to([-3.35, 1.0, 0])
        pointer = Line([-2.83, 1.25, 0], [-1.96, 0.63, 0], color="#C99A61", stroke_width=6)
        boxes = VGroup(
            self.logic_box("INPUT", INPUT),
            self.logic_box("BRAIN", BRAIN),
            self.logic_box("OUTPUT", OUTPUT),
        ).arrange(RIGHT, buff=0.48).scale(0.94).move_to([0.25, 1.0, 0])
        arrows = VGroup(
            Arrow(boxes[0].get_right(), boxes[1].get_left(), buff=0.12, color=WHITE, stroke_width=6),
            Arrow(boxes[1].get_right(), boxes[2].get_left(), buff=0.12, color=WHITE, stroke_width=6),
        )
        title = Text("HOW A ROBOT THINKS", font="Arial", font_size=51, weight=BOLD, color=WHITE)
        title.move_to([0, 4.9, 0])
        subtitle = Text("INPUT → BRAIN → OUTPUT", font="Arial", font_size=29, weight=BOLD, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.26)
        cap = self.caption(
            "Every robot program follows one pattern: Input, Brain, Output.",
            "ทุก ๆ โปรแกรมหุ่นยนต์เริ่มด้วยรูปแบบเดียวกัน: อินพุต สมอง เอาต์พุต",
        )
        content = VGroup(teacher, pointer, boxes, arrows, title, subtitle, cap)
        self.add(content)
        self.wait(2)
        self.play(LaggedStart(*[Indicate(a, color=INPUT, scale_factor=1.15) for a in arrows], lag_ratio=0.38), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(content), run_time=0.5)

    def block_2_input(self) -> None:
        title = Text("1 / INPUT", font="Arial", font_size=34, weight=BOLD, color=INPUT).move_to([0, 5.35, 0])
        teacher = self.stick_figure(0.85).move_to([-3.35, 0.1, 0])
        brain = self.vex_brain().move_to([-0.85, 0.5, 0])
        input_tag = self.logic_box("INPUT", INPUT).scale(0.67).move_to([-0.85, 3.15, 0])
        cap = self.caption(
            "The Check button is our input. It tells the robot something happened.",
            "ปุ่ม Check คืออินพุตของเรา มันบอกหุ่นยนต์ว่ามีบางอย่างเกิดขึ้นแล้ว",
        )
        self.play(FadeIn(title), FadeIn(teacher, shift=RIGHT * 0.6), FadeIn(cap), run_time=1.3)
        self.play(teacher.animate.shift(RIGHT * 0.55), run_time=1.0)
        self.play(FadeIn(brain, scale=0.72), FadeIn(input_tag, shift=DOWN * 0.4), run_time=1.0)
        check = brain[3]
        self.play(Indicate(check, color=INPUT, scale_factor=1.35), run_time=1.0)
        block = self.code_block("< pressing Check >", INPUT, 3.35).move_to([2.55, 0.5, 0])
        link = Arrow(brain.get_right(), block.get_left(), buff=0.16, color=INPUT, stroke_width=7)
        packet = Dot(brain.get_right() + RIGHT * 0.08, radius=0.11, color=WHITE)
        self.play(GrowArrow(link), FadeIn(block, shift=LEFT * 0.4), run_time=1.2)
        self.add(packet)
        self.play(MoveAlongPath(packet, link), Flash(block, color=INPUT, flash_radius=1.8), run_time=1.2)
        self.remove(packet)
        self.wait(2.8)
        self.play(FadeOut(VGroup(title, teacher, brain, input_tag, block, link, cap)), run_time=0.5)

    def block_3_brain(self) -> None:
        title = Text("2 / BRAIN LOGIC STACK", font="Arial", font_size=34, weight=BOLD, color=BRAIN)
        title.move_to([0, 5.55, 0])
        blocks = VGroup(
            self.code_block("When Started", "#6B7280"),
            self.code_block('Print "PRESS CHECK"', OUTPUT),
            self.code_block("Wait until <Pressing Check>", INPUT),
            self.code_block('Print "GO"', OUTPUT),
            self.code_block("Drive Forward 300 mm", "#00A86B"),
        ).arrange(DOWN, buff=0.17).move_to([0.75, 0.75, 0])
        teacher = self.stick_figure(0.73).move_to([-3.45, 0.3, 0])
        lens = Circle(radius=0.68, color=BRAIN, stroke_width=7).move_to([-2.62, 1.45, 0])
        handle = Line([-3.0, 0.97, 0], [-3.56, 0.2, 0], color=BRAIN, stroke_width=9)
        laser = Arrow([3.75, 3.03, 0], [3.75, 2.35, 0], color=BRAIN, stroke_width=8, max_tip_length_to_length_ratio=0.35)
        cap = self.caption(
            "The Brain follows these blocks from top to bottom. First, it displays instructions.",
            "สมองอ่านบล็อกจากบนลงล่าง และเริ่มด้วยการแสดงคำสั่งบนหน้าจอ",
        )
        self.play(FadeIn(title), FadeIn(teacher, shift=UP * 0.4), FadeIn(lens), GrowFromPoint(handle, handle.get_start()), FadeIn(cap), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(block, shift=RIGHT * 0.7) for block in blocks], lag_ratio=0.18), run_time=2.5)
        self.add(laser)
        for index, block in enumerate(blocks):
            target_y = block.get_y()
            self.play(laser.animate.move_to([3.75, target_y, 0]), Indicate(block, color=BRAIN, scale_factor=1.05), run_time=1.2)
        self.play(lens.animate.move_to(blocks[1]).scale(1.08), Indicate(blocks[1], color=WHITE), run_time=1.5)
        self.wait(3.5)
        self.play(FadeOut(VGroup(title, teacher, lens, handle, laser, blocks, cap)), run_time=0.5)

    def block_4_simulation(self) -> None:
        title = Text("3 / SIMULATION LOOP", font="Arial", font_size=34, weight=BOLD, color=OUTPUT).move_to([0, 5.55, 0])
        divider = Line([0, -3.5, 0], [0, 4.55, 0], color=GRID, stroke_width=4)
        left_label = Text("INPUT BECOMES TRUE", font="Arial", font_size=22, weight=BOLD, color=INPUT).move_to([-2.25, 4.35, 0])
        right_label = Text("OUTPUT MOVES", font="Arial", font_size=22, weight=BOLD, color=OUTPUT).move_to([2.25, 4.35, 0])
        brain = self.vex_brain().scale(0.78).move_to([-2.2, 1.35, 0])
        wait_block = self.code_block("Wait until <Check>", INPUT, 3.35).move_to([-2.2, -1.05, 0])
        true_tag = Text("TRUE", font="Arial", font_size=31, weight=BOLD, color=GREEN).move_to([-2.2, -2.0, 0])
        lane = Line([0.55, -0.55, 0], [4.0, -0.55, 0], color=GRAY, stroke_width=6)
        target = Line([3.5, -1.08, 0], [3.5, 0.15, 0], color=BRAIN, stroke_width=9)
        target_text = Text("300 mm", font="Arial", font_size=23, weight=BOLD, color=BRAIN).next_to(target, UP, buff=0.18)
        robot = self.robot().scale(0.72).move_to([1.25, 0.18, 0])
        goggles_teacher = self.stick_figure(0.38).move_to([3.78, 2.95, 0])
        goggles = VGroup(Circle(0.12, color=INPUT), Circle(0.12, color=INPUT)).arrange(RIGHT, buff=0.04).move_to(goggles_teacher[0].get_center() + UP * 0.02)
        cap = self.caption(
            "Pressing Check makes the block true. The drivetrain moves. Final output: DONE.",
            "เมื่อกด Check บล็อกจะเป็นจริง ระบบขับเคลื่อนจะเคลื่อนที่ และจบด้วย DONE",
        )
        self.play(FadeIn(title), Create(divider), FadeIn(left_label), FadeIn(right_label), FadeIn(cap), run_time=1.5)
        self.play(FadeIn(brain), FadeIn(wait_block), Create(lane), Create(target), FadeIn(target_text), FadeIn(goggles_teacher), FadeIn(goggles), run_time=1.0)
        self.play(Indicate(brain[3], color=INPUT, scale_factor=1.35), run_time=1.0)
        self.play(Flash(wait_block, color=GREEN, flash_radius=1.7), FadeIn(true_tag, scale=0.6), run_time=1.0)
        self.play(FadeIn(robot, shift=LEFT * 0.5), run_time=1.0)
        self.play(robot.animate.move_to([3.0, 0.18, 0]), Rotate(robot[3], angle=4 * PI), Rotate(robot[4], angle=4 * PI), run_time=5.0, rate_func=smooth)
        done = Text("DONE", font="Arial", font_size=46, weight=BOLD, color=OUTPUT).move_to([2.95, 1.55, 0])
        self.play(Transform(robot[2], done), Flash(target, color=OUTPUT, flash_radius=1.2), run_time=1.0)
        self.wait(3.0)
        self.play(FadeOut(VGroup(title, divider, left_label, right_label, brain, wait_block, true_tag, lane, target, target_text, robot, goggles_teacher, goggles, cap)), run_time=0.5)

    def block_5_prediction(self) -> None:
        title = Text("4 / PREDICT THE OUTPUT", font="Arial", font_size=34, weight=BOLD, color=BRAIN).move_to([0, 5.45, 0])
        teacher = self.stick_figure(0.8).move_to([-3.25, 1.75, 0])
        question = Text("?", font="Arial", font_size=105, weight=BOLD, color=BRAIN).next_to(teacher, UP, buff=0.12)
        old = self.code_block("Drive Forward 300 mm", "#00A86B", 5.35).move_to([1.25, 2.1, 0])
        new = self.code_block("Drive Forward 500 mm", "#00A86B", 5.35).move_to(old)
        option_a = Text("A  Brain order changes", font="Arial", font_size=26, weight=BOLD, color=WHITE).move_to([0.8, 0.35, 0])
        option_b = Text("B  Driving distance changes", font="Arial", font_size=26, weight=BOLD, color=WHITE).move_to([0.8, -0.75, 0])
        cross = Text("NO", font="Arial", font_size=32, weight=BOLD, color=RED).next_to(option_a, RIGHT, buff=0.3)
        check = Text("YES", font="Arial", font_size=32, weight=BOLD, color=GREEN).next_to(option_b, RIGHT, buff=0.3)
        cap = self.caption(
            "Predict: If 300 becomes 500 millimeters, which output changes?",
            "ลองทายดู: ถ้าเปลี่ยน 300 เป็น 500 มิลลิเมตร เอาต์พุตใดจะเปลี่ยน?",
        )
        self.play(FadeIn(title), FadeIn(teacher), FadeIn(question, shift=DOWN * 0.3), FadeIn(old, shift=UP * 0.4), FadeIn(cap), run_time=1.5)
        self.play(Transform(old, new), Flash(old, color=BRAIN, flash_radius=2.4), run_time=2.0)
        self.play(FadeIn(option_a, shift=LEFT * 0.35), FadeIn(option_b, shift=LEFT * 0.35), run_time=1.0)
        self.play(FadeIn(cross, scale=0.3), FadeIn(check, scale=0.3), run_time=1.0)
        self.play(Wiggle(question), Wiggle(teacher), run_time=1.0)
        self.wait(3.0)
        self.play(FadeOut(VGroup(title, teacher, question, old, option_a, option_b, cross, check, cap)), run_time=0.5)

    def block_6_repository(self) -> None:
        teacher = self.stick_figure(0.76).move_to([-3.25, 2.65, 0])
        title = Text("OPEN-SOURCE LESSON PACKAGE", font="Arial", font_size=35, weight=BOLD, color=INPUT).move_to([0, 5.25, 0])
        title.scale_to_fit_width(7.75)
        repo = RoundedRectangle(width=7.5, height=2.2, corner_radius=0.22, color=INPUT, stroke_width=5)
        repo.set_fill("#282828", opacity=1).move_to([0.25, 2.3, 0])
        repo_title = Text("Silent Sparks / EP01", font="Arial", font_size=36, weight=BOLD, color=WHITE).move_to([0.25, 2.75, 0])
        repo_sub = Text("github.com/mummurnext-byte/sen-accessible-vex-agent", font="Arial", font_size=23, color=GRAY)
        repo_sub.scale_to_fit_width(6.65).move_to([0.25, 1.95, 0])
        cards = VGroup()
        for label, color in (("PDF", INPUT), ("BLOCKS", BRAIN), ("TEACHER", OUTPUT)):
            box = RoundedRectangle(width=2.22, height=1.28, corner_radius=0.15, color=color, stroke_width=4)
            box.set_fill("#252525", opacity=1)
            text = Text(label, font="Arial", font_size=24, weight=BOLD, color=WHITE)
            cards.add(VGroup(box, text))
        cards.arrange(RIGHT, buff=0.28).move_to([0.25, 0.2, 0])
        credit = Text("Created by Sen with Codex", font="Arial", font_size=27, weight=BOLD, color=BRAIN).move_to([0, -1.35, 0])
        mission = Text(
            "This channel is an AI-assisted open research log\nfor accessible STEM education.",
            font="Arial",
            font_size=25,
            color=WHITE,
            line_spacing=0.9,
        ).move_to([0, -2.35, 0])
        down = Arrow([0, -3.05, 0], [0, -3.8, 0], color=INPUT, stroke_width=8)
        cap = self.caption(
            "Download open-source materials below. Input your logic, spark their world.",
            "ดาวน์โหลดสื่อโอเพนซอร์สด้านล่าง ใส่ลอจิกของคุณ แล้วจุดประกายโลกของพวกเขา",
        )
        self.play(FadeIn(teacher, shift=UP * 0.35), FadeIn(title), FadeIn(cap), run_time=1.5)
        self.play(teacher.animate.rotate(-0.18, about_point=teacher.get_bottom()), run_time=1.0)
        self.play(teacher.animate.rotate(0.18, about_point=teacher.get_bottom()).shift(DOWN * 0.15), GrowArrow(down), run_time=1.0)
        self.play(FadeIn(repo, shift=UP * 0.6), FadeIn(repo_title, shift=UP * 0.6), FadeIn(repo_sub, shift=UP * 0.6), run_time=1.5)
        self.play(LaggedStart(*[FadeIn(card, shift=UP * 0.4) for card in cards], lag_ratio=0.22), run_time=1.5)
        self.play(FadeIn(credit), FadeIn(mission), run_time=1.5)
        self.play(Indicate(down, color=BRAIN, scale_factor=1.2), run_time=1.0)
        self.wait(6.0)
