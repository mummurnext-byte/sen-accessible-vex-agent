from __future__ import annotations

from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
config.background_color = "#ECECEA"

BLACK = "#101010"
WHITE = "#FFFFFF"
GRAY = "#727272"
LIGHT_GRAY = "#D8D8D5"
INPUT = "#00BDEB"
BRAIN = "#FFD000"
OUTPUT = "#B100F2"
GREEN = "#28C76F"
RED = "#EF476F"


class SilentSparksReferenceStyle(Scene):
    def construct(self) -> None:
        self.add(self.soft_background())
        first = self.silent_hook()
        second = self.input_scene(first)
        third = self.brain_scene(second)
        fourth = self.simulation_scene(third)
        fifth = self.prediction_scene(fourth)
        self.repository_scene(fifth)

    def soft_background(self) -> VGroup:
        base = Rectangle(width=9, height=16, stroke_width=0, fill_color="#E9E9E7", fill_opacity=1)
        glow = VGroup()
        for index in range(14):
            radius = 6.6 - index * 0.28
            circle = Circle(radius=radius, stroke_width=0, fill_color=WHITE, fill_opacity=0.045)
            circle.move_to([0.3, 0.4, 0])
            glow.add(circle)
        watermark = Text("✦", font="Arial Unicode MS", font_size=28, color=WHITE)
        watermark.set_opacity(0.82).move_to([3.95, -7.15, 0])
        return VGroup(base, glow, watermark)

    def caption(self, english: str, thai: str, accent: str = INPUT) -> VGroup:
        shadow = RoundedRectangle(width=8.15, height=2.12, corner_radius=0.2, stroke_width=0)
        shadow.set_fill(BLACK, opacity=0.09).move_to([0.08, -6.27, 0])
        panel = RoundedRectangle(width=8.15, height=2.12, corner_radius=0.2, color="#C7C7C4", stroke_width=2)
        panel.set_fill(WHITE, opacity=0.96).move_to([0, -6.19, 0])
        bar = Rectangle(width=0.08, height=1.68, stroke_width=0, fill_color=accent, fill_opacity=1)
        bar.move_to([-3.87, -6.19, 0])
        en = Text(english, font="Arial", font_size=26, weight=BOLD, color=GRAY)
        if en.width > 7.45:
            en.scale_to_fit_width(7.45)
        en.move_to([0.12, -5.77, 0])
        th = Text(thai, font="Leelawadee UI", font_size=41, weight=BOLD, color=BLACK)
        if th.width > 7.48:
            th.scale_to_fit_width(7.48)
        th.move_to([0.12, -6.48, 0])
        return VGroup(shadow, panel, bar, en, th)

    def floor_shadow(self, width: float = 1.6) -> Ellipse:
        shadow = Ellipse(width=width, height=0.25, stroke_width=0, fill_color=BLACK, fill_opacity=0.09)
        return shadow

    def figure(self, pose: str = "point", scale: float = 1.0) -> VGroup:
        head = Circle(radius=0.34, color=BLACK, stroke_width=7).move_to([0, 1.18, 0])
        eye_l = Line([-0.12, 1.25, 0], [-0.12, 1.14, 0], color=BLACK, stroke_width=5)
        eye_r = Line([0.12, 1.25, 0], [0.12, 1.14, 0], color=BLACK, stroke_width=5)
        smile = Arc(radius=0.16, start_angle=PI * 1.14, angle=PI * 0.72, color=BLACK, stroke_width=4)
        smile.move_to([0, 1.07, 0])
        body = Line([0, 0.84, 0], [0, -0.42, 0], color=BLACK, stroke_width=8)
        if pose == "walk":
            limbs = VGroup(
                Line([0, 0.48, 0], [-0.48, 0.0, 0], color=BLACK, stroke_width=8),
                Line([0, 0.48, 0], [0.5, 0.1, 0], color=BLACK, stroke_width=8),
                Line([0, -0.42, 0], [-0.15, -1.05, 0], color=BLACK, stroke_width=8),
                Line([-0.15, -1.05, 0], [0.25, -1.5, 0], color=BLACK, stroke_width=8),
                Line([0, -0.42, 0], [0.45, -0.8, 0], color=BLACK, stroke_width=8),
                Line([0.45, -0.8, 0], [0.2, -1.42, 0], color=BLACK, stroke_width=8),
            )
        elif pose == "think":
            limbs = VGroup(
                Line([0, 0.48, 0], [-0.55, -0.02, 0], color=BLACK, stroke_width=8),
                Line([0, 0.48, 0], [0.42, 0.82, 0], color=BLACK, stroke_width=8),
                Line([0.42, 0.82, 0], [0.25, 1.18, 0], color=BLACK, stroke_width=8),
                Line([0, -0.42, 0], [-0.42, -1.46, 0], color=BLACK, stroke_width=8),
                Line([0, -0.42, 0], [0.48, -1.46, 0], color=BLACK, stroke_width=8),
            )
        elif pose == "bow":
            limbs = VGroup(
                Line([0, 0.48, 0], [-0.38, -0.1, 0], color=BLACK, stroke_width=8),
                Line([0, 0.48, 0], [0.38, -0.1, 0], color=BLACK, stroke_width=8),
                Line([0, -0.42, 0], [-0.4, -1.46, 0], color=BLACK, stroke_width=8),
                Line([0, -0.42, 0], [0.45, -1.46, 0], color=BLACK, stroke_width=8),
            )
        else:
            limbs = VGroup(
                Line([0, 0.48, 0], [-0.52, -0.08, 0], color=BLACK, stroke_width=8),
                Line([0, 0.48, 0], [0.72, 0.18, 0], color=BLACK, stroke_width=8),
                Line([0.72, 0.18, 0], [1.08, 0.34, 0], color=BLACK, stroke_width=8),
                Line([0, -0.42, 0], [-0.4, -1.46, 0], color=BLACK, stroke_width=8),
                Line([0, -0.42, 0], [0.45, -1.46, 0], color=BLACK, stroke_width=8),
            )
        return VGroup(head, eye_l, eye_r, smile, body, limbs).scale(scale)

    def logic_box(self, label: str, color: str) -> VGroup:
        box = Square(side_length=1.72, color=BLACK, stroke_width=4)
        box.set_fill(WHITE, opacity=0.58)
        text = Text(label, font="Arial", font_size=26, color=BLACK).next_to(box, UP, buff=0.18)
        glows = VGroup()
        for buff, opacity in ((0.06, 0.24), (0.14, 0.15), (0.22, 0.08)):
            glow = SurroundingRectangle(box, buff=buff, color=color, stroke_width=8)
            glow.set_opacity(opacity)
            glows.add(glow)
        return VGroup(glows, box, text)

    def particles(self, center: np.ndarray, color: str, count: int = 17) -> VGroup:
        dots = VGroup()
        for index in range(count):
            angle = index * TAU / count * 2.3
            radius = 0.18 + (index % 5) * 0.12
            dot = Circle(radius=0.025 + (index % 3) * 0.013, color=color, stroke_width=2)
            dot.move_to(center + [np.cos(angle) * radius, np.sin(angle) * radius, 0])
            dots.add(dot)
        return dots

    def code_block(self, text: str, color: str, width: float = 5.8) -> VGroup:
        rect = RoundedRectangle(width=width, height=0.72, corner_radius=0.12, color=BLACK, stroke_width=2)
        rect.set_fill(color, opacity=0.83)
        label = Text(text, font="Arial", font_size=22, weight=BOLD, color=BLACK)
        if label.width > width - 0.35:
            label.scale_to_fit_width(width - 0.35)
        return VGroup(rect, label)

    def robot(self) -> VGroup:
        body = RoundedRectangle(width=1.72, height=0.9, corner_radius=0.18, color=BLACK, stroke_width=5)
        body.set_fill("#F7F7F5", opacity=1)
        brain = RoundedRectangle(width=0.9, height=0.62, corner_radius=0.1, color=BLACK, stroke_width=4)
        brain.set_fill(WHITE, opacity=1).shift(UP * 0.5)
        screen = Text("GO", font="Arial", font_size=18, weight=BOLD, color=GREEN).move_to(brain)
        wheels = VGroup(Circle(0.28, color=BLACK, stroke_width=5), Circle(0.28, color=BLACK, stroke_width=5))
        wheels.arrange(RIGHT, buff=0.55).shift(DOWN * 0.6)
        return VGroup(body, brain, screen, wheels)

    def silent_hook(self) -> VGroup:
        teacher = self.figure("point", 0.86).move_to([-3.45, 0.6, 0])
        shadow = self.floor_shadow(1.35).move_to([-3.45, -0.8, 0])
        boxes = VGroup(
            self.logic_box("Input", INPUT),
            self.logic_box("Brain", BRAIN),
            self.logic_box("Output", OUTPUT),
        ).arrange(RIGHT, buff=0.48).scale(0.94).move_to([0.45, 0.8, 0])
        arrows = VGroup(
            Arrow(boxes[0].get_right(), boxes[1].get_left(), buff=0.1, color=BLACK, stroke_width=5),
            Arrow(boxes[1].get_right(), boxes[2].get_left(), buff=0.1, color=BLACK, stroke_width=5),
        )
        title = Text("HOW A ROBOT THINKS", font="Arial", font_size=48, weight=BOLD, color=BLACK).move_to([0, 4.7, 0])
        caption = self.caption(
            "Every robot program follows one pattern: Input, Brain, Output.",
            "ทุกโปรแกรมหุ่นยนต์เริ่มด้วยรูปแบบเดียวกัน: อินพุต สมอง เอาต์พุต",
        )
        group = VGroup(teacher, shadow, boxes, arrows, title, caption)
        self.add(group)
        self.wait(2)
        for index, color in enumerate((INPUT, BRAIN, OUTPUT)):
            dots = self.particles(boxes[index][1].get_center(), color)
            self.play(
                Indicate(boxes[index][1], color=color, scale_factor=1.04),
                LaggedStart(*[GrowFromCenter(dot) for dot in dots], lag_ratio=0.03),
                run_time=0.65,
            )
            self.play(FadeOut(dots), run_time=0.15)
        self.wait(0.6)
        return group

    def input_scene(self, previous: VGroup) -> VGroup:
        self.play(FadeOut(previous), run_time=0.6)
        title = Text("INPUT: PRESS CHECK", font="Arial", font_size=40, weight=BOLD, color=INPUT).move_to([0, 5.15, 0])
        teacher = self.figure("walk", 0.9).move_to([-3.1, 0.2, 0])
        shadow = self.floor_shadow(1.4).move_to([-3.1, -1.25, 0])
        brain_body = RoundedRectangle(width=3.1, height=3.25, corner_radius=0.28, color=BLACK, stroke_width=5)
        brain_body.set_fill("#F7F7F5", opacity=1).move_to([0.6, 0.55, 0])
        brain_screen = RoundedRectangle(width=2.0, height=0.92, corner_radius=0.14, color=INPUT, stroke_width=4)
        brain_screen.set_fill(WHITE, opacity=1).move_to([0.6, 1.2, 0])
        check = Circle(radius=0.49, color=BLACK, stroke_width=4, fill_color=INPUT, fill_opacity=1).move_to([0.6, -0.45, 0])
        check_label = Text("CHECK", font="Arial", font_size=16, weight=BOLD, color=WHITE).move_to(check)
        rings = VGroup(*[Circle(radius=0.62 + i * 0.18, color=INPUT, stroke_width=5).set_opacity(0.5 - i * 0.09) for i in range(4)])
        rings.move_to(check)
        block = self.code_block("< Pressing Check >", INPUT, 3.25).move_to([2.8, -2.0, 0])
        wire = CubicBezier(check.get_right(), [1.55, -0.5, 0], [1.9, -1.8, 0], block.get_left())
        wire.set_color(INPUT).set_stroke(width=5)
        caption = self.caption(
            "The Check button is our input. It tells the robot something happened.",
            "ปุ่ม Check คืออินพุตของเรา มันบอกหุ่นยนต์ว่ามีบางอย่างเกิดขึ้นแล้ว",
            INPUT,
        )
        group = VGroup(title, teacher, shadow, brain_body, brain_screen, check, check_label, rings, block, wire, caption)
        self.play(FadeIn(title), FadeIn(teacher, shift=RIGHT * 0.5), FadeIn(shadow), FadeIn(brain_body), FadeIn(brain_screen), FadeIn(caption), run_time=1.4)
        point_pose = self.figure("point", 0.9).move_to([-2.1, 0.0, 0])
        self.play(Transform(teacher, point_pose), shadow.animate.move_to([-2.1, -1.35, 0]), run_time=1.2)
        self.play(FadeIn(check, scale=0.4), FadeIn(check_label, scale=0.4), LaggedStart(*[Create(ring) for ring in rings], lag_ratio=0.12), run_time=1.4)
        self.play(Indicate(check, color=INPUT, scale_factor=1.18), *[ring.animate.scale(1.22).set_opacity(0.12) for ring in rings], run_time=1.4)
        self.play(Create(wire), FadeIn(block, shift=LEFT * 0.4), run_time=1.1)
        packet = Dot(check.get_right(), radius=0.11, color=INPUT)
        self.add(packet)
        self.play(MoveAlongPath(packet, wire), Flash(block, color=INPUT, flash_radius=1.5), run_time=1.4)
        self.remove(packet)
        self.wait(1.5)
        return group

    def brain_scene(self, previous: VGroup) -> VGroup:
        self.play(FadeOut(previous), run_time=0.8)
        title = Text("BRAIN: FOLLOW THE BLOCKS", font="Arial", font_size=39, weight=BOLD, color=BLACK).move_to([0, 5.35, 0])
        teacher = self.figure("point", 0.7).move_to([-3.4, 0.45, 0])
        shadow = self.floor_shadow(1.1).move_to([-3.4, -0.75, 0])
        blocks = VGroup(
            self.code_block("When Started", LIGHT_GRAY),
            self.code_block('Print "PRESS CHECK"', OUTPUT),
            self.code_block("Wait until <Pressing Check>", INPUT),
            self.code_block('Print "GO"', OUTPUT),
            self.code_block("Drive Forward 300 mm", GREEN),
        ).arrange(DOWN, buff=0.18).move_to([0.85, 0.65, 0])
        lens = Circle(radius=0.66, color=BRAIN, stroke_width=8).move_to([-2.45, 1.0, 0])
        handle = Line([-2.83, 0.52, 0], [-3.36, -0.22, 0], color=BRAIN, stroke_width=10)
        scanner = Arrow([3.8, 3.1, 0], [3.8, 2.45, 0], color=BRAIN, stroke_width=7)
        caption = self.caption(
            "The Brain follows these blocks from top to bottom. First, it displays instructions.",
            "สมองอ่านบล็อกจากบนลงล่าง และเริ่มด้วยการแสดงคำสั่งบนหน้าจอ",
            BRAIN,
        )
        group = VGroup(title, teacher, shadow, blocks, lens, handle, scanner, caption)
        self.play(FadeIn(title), FadeIn(teacher), FadeIn(shadow), FadeIn(caption), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(block, shift=RIGHT * 0.55) for block in blocks], lag_ratio=0.16), run_time=2.0)
        self.play(FadeIn(lens, scale=0.55), GrowFromPoint(handle, handle.get_start()), run_time=1.2)
        self.add(scanner)
        for block in blocks:
            particles = self.particles(block.get_center(), BRAIN, 9)
            self.play(scanner.animate.move_to([3.8, block.get_y(), 0]), Indicate(block, color=BRAIN, scale_factor=1.035), FadeIn(particles), run_time=1.0)
            self.play(FadeOut(particles), run_time=0.2)
        signal = Dot(blocks[-1].get_right(), radius=0.12, color=OUTPUT)
        signal_path = ArcBetweenPoints(blocks[-1].get_right(), [3.5, -2.35, 0], angle=-PI / 2)
        self.add(signal)
        self.play(MoveAlongPath(signal, signal_path), run_time=1.0)
        self.remove(signal)
        self.wait(3.2)
        return group

    def simulation_scene(self, previous: VGroup) -> VGroup:
        self.play(FadeOut(previous), run_time=0.8)
        title = Text("INPUT BECOMES TRUE → OUTPUT MOVES", font="Arial", font_size=34, weight=BOLD, color=BLACK)
        title.scale_to_fit_width(7.5).move_to([0, 5.25, 0])
        divider = Line([0, -3.5, 0], [0, 4.45, 0], color=LIGHT_GRAY, stroke_width=4)
        button = Circle(0.72, color=BLACK, stroke_width=4, fill_color=INPUT, fill_opacity=1).move_to([-2.35, 1.55, 0])
        check = Text("CHECK", font="Arial", font_size=20, weight=BOLD, color=WHITE).move_to(button)
        finger = self.figure("point", 0.43).move_to([-3.35, 1.2, 0])
        wait_block = self.code_block("Wait until <Check>", INPUT, 3.25).move_to([-2.2, -0.6, 0])
        true_text = Text("TRUE", font="Arial", font_size=35, weight=BOLD, color=GREEN).move_to([-2.2, -1.65, 0])
        lane = Line([0.6, -0.15, 0], [4.05, -0.15, 0], color=GRAY, stroke_width=5)
        target = Line([3.48, -0.75, 0], [3.48, 0.55, 0], color=BRAIN, stroke_width=8)
        target_label = Text("300 mm", font="Arial", font_size=23, weight=BOLD, color=BLACK).next_to(target, UP, buff=0.14)
        robot = self.robot().scale(0.82).move_to([1.25, 0.65, 0])
        observer = self.figure("walk", 0.35).move_to([3.72, 3.25, 0])
        goggles = VGroup(Circle(0.12, color=INPUT, stroke_width=4), Circle(0.12, color=INPUT, stroke_width=4)).arrange(RIGHT, buff=0.02)
        goggles.move_to(observer[0].get_center())
        caption = self.caption(
            "Pressing Check makes the block true. The drivetrain moves. Final output: DONE.",
            "เมื่อกด Check บล็อกจะเป็นจริง ระบบขับเคลื่อนจะเคลื่อนที่ และจบด้วย DONE",
            OUTPUT,
        )
        group = VGroup(title, divider, button, check, finger, wait_block, true_text, lane, target, target_label, robot, observer, goggles, caption)
        self.play(FadeIn(title), Create(divider), FadeIn(caption), run_time=0.8)
        self.play(FadeIn(button, scale=0.55), FadeIn(check), FadeIn(finger, shift=RIGHT * 0.3), FadeIn(wait_block), Create(lane), Create(target), FadeIn(target_label), FadeIn(observer), FadeIn(goggles), run_time=1.7)
        ripples = VGroup(*[Circle(0.83 + i * 0.22, color=INPUT, stroke_width=5).set_opacity(0.45 - i * 0.08) for i in range(4)]).move_to(button)
        self.play(Indicate(button, color=INPUT, scale_factor=1.15), LaggedStart(*[Create(r) for r in ripples], lag_ratio=0.12), run_time=1.0)
        self.play(Flash(wait_block, color=GREEN, flash_radius=1.6), FadeIn(true_text, scale=0.4), FadeOut(ripples), run_time=1.0)
        self.play(FadeIn(robot, shift=LEFT * 0.5), run_time=1.0)
        self.play(robot.animate.move_to([3.0, 0.65, 0]), Rotate(robot[3], angle=4 * PI), run_time=5.0, rate_func=smooth)
        done = Text("DONE", font="Arial", font_size=47, weight=BOLD, color=OUTPUT).move_to([2.95, 1.85, 0])
        waves = VGroup(*[Circle(0.52 + i * 0.25, color=OUTPUT, stroke_width=6).set_opacity(0.48 - i * 0.08) for i in range(4)]).move_to(done)
        self.play(FadeIn(done, scale=0.4), LaggedStart(*[Create(w) for w in waves], lag_ratio=0.12), Flash(target, color=OUTPUT), run_time=1.5)
        self.wait(2.2)
        return VGroup(group, ripples, done, waves)

    def prediction_scene(self, previous: VGroup) -> VGroup:
        self.play(FadeOut(previous), run_time=0.8)
        title = Text("PREDICT THE OUTPUT", font="Arial", font_size=41, weight=BOLD, color=BLACK).move_to([0, 5.25, 0])
        teacher = self.figure("think", 0.82).move_to([-3.15, 1.2, 0])
        shadow = self.floor_shadow(1.3).move_to([-3.15, -0.15, 0])
        question = Text("?", font="Arial", font_size=90, weight=BOLD, color=BRAIN).next_to(teacher, UP, buff=0.12)
        old = self.code_block("Drive Forward 300 mm", GREEN, 5.2).move_to([1.2, 2.2, 0])
        new = self.code_block("Drive Forward 500 mm", GREEN, 5.2).move_to(old)
        lane = Line([-0.35, 0.25, 0], [3.9, 0.25, 0], color=GRAY, stroke_width=5)
        marker_300 = Line([2.2, -0.25, 0], [2.2, 0.75, 0], color=INPUT, stroke_width=7)
        marker_500 = Line([3.65, -0.25, 0], [3.65, 0.75, 0], color=OUTPUT, stroke_width=7)
        robot = self.robot().scale(0.62).move_to([0.3, 0.95, 0])
        option_a = Text("A  Brain order changes", font="Arial", font_size=25, weight=BOLD, color=BLACK).move_to([0.65, -1.2, 0])
        option_b = Text("B  Driving distance changes", font="Arial", font_size=25, weight=BOLD, color=BLACK).move_to([0.65, -2.2, 0])
        no = Text("NO", font="Arial", font_size=31, weight=BOLD, color=RED).next_to(option_a, RIGHT, buff=0.28)
        yes = Text("YES", font="Arial", font_size=31, weight=BOLD, color=GREEN).next_to(option_b, RIGHT, buff=0.28)
        caption = self.caption(
            "Predict: If 300 becomes 500 millimeters, which output changes?",
            "ลองทายดู: ถ้าเปลี่ยน 300 เป็น 500 มิลลิเมตร เอาต์พุตใดจะเปลี่ยน?",
            BRAIN,
        )
        group = VGroup(title, teacher, shadow, question, old, lane, marker_300, marker_500, robot, option_a, option_b, no, yes, caption)
        self.play(FadeIn(title), FadeIn(teacher), FadeIn(shadow), FadeIn(question, shift=DOWN * 0.3), FadeIn(old), FadeIn(caption), run_time=1.2)
        self.play(Transform(old, new), Flash(old, color=BRAIN, flash_radius=2.2), run_time=2.0)
        self.play(Create(lane), Create(marker_300), FadeIn(robot, shift=LEFT * 0.3), run_time=1.0)
        self.play(Create(marker_500), robot.animate.move_to([3.1, 0.95, 0]), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(option_a, shift=LEFT * 0.3), FadeIn(option_b, shift=LEFT * 0.3), FadeIn(no, scale=0.4), FadeIn(yes, scale=0.4), run_time=1.5)
        self.wait(2.0)
        return group

    def repository_scene(self, previous: VGroup) -> None:
        self.play(FadeOut(previous), run_time=0.8)
        teacher = self.figure("bow", 0.72).move_to([-3.35, 2.2, 0])
        shadow = self.floor_shadow(1.2).move_to([-3.35, 1.0, 0])
        title = Text("OPEN-SOURCE LESSON PACKAGE", font="Arial", font_size=34, weight=BOLD, color=BLACK)
        title.scale_to_fit_width(7.5).move_to([0, 5.2, 0])
        caption = self.caption(
            "Download open-source materials below. Input your logic, spark their world.",
            "ดาวน์โหลดสื่อโอเพนซอร์สด้านล่าง ใส่ลอจิกของคุณ แล้วจุดประกายโลกของพวกเขา",
            INPUT,
        )
        self.play(FadeIn(teacher, shift=UP * 0.35), FadeIn(shadow), FadeIn(title), FadeIn(caption), run_time=0.8)
        self.play(teacher.animate.rotate(-0.22, about_point=teacher.get_bottom()), run_time=1.5)
        card_shadow = RoundedRectangle(width=7.25, height=2.35, corner_radius=0.25, stroke_width=0, fill_color=BLACK, fill_opacity=0.1).move_to([0.08, 2.15, 0])
        card = RoundedRectangle(width=7.25, height=2.35, corner_radius=0.25, color=INPUT, stroke_width=5, fill_color=WHITE, fill_opacity=0.96).move_to([0, 2.24, 0])
        repo = Text("Silent Sparks / EP01", font="Arial", font_size=37, weight=BOLD, color=BLACK).move_to([0, 2.7, 0])
        url = Text("github.com/mummurnext-byte/sen-accessible-vex-agent", font="Arial", font_size=21, color=GRAY)
        url.scale_to_fit_width(6.5).move_to([0, 1.9, 0])
        self.play(FadeIn(card_shadow, shift=UP * 0.5), FadeIn(card, shift=UP * 0.5), FadeIn(repo, shift=UP * 0.5), FadeIn(url, shift=UP * 0.5), run_time=1.5)
        cards = VGroup()
        for label, color in (("PDF", INPUT), ("BLOCKS", BRAIN), ("TEACHER", OUTPUT)):
            box = RoundedRectangle(width=2.12, height=1.2, corner_radius=0.16, color=color, stroke_width=4, fill_color=WHITE, fill_opacity=0.96)
            text = Text(label, font="Arial", font_size=22, weight=BOLD, color=BLACK)
            cards.add(VGroup(box, text))
        cards.arrange(RIGHT, buff=0.28).move_to([0, 0.1, 0])
        self.play(LaggedStart(*[FadeIn(item, shift=UP * 0.4) for item in cards], lag_ratio=0.2), run_time=1.5)
        credit = Text("Created by Sen with Codex", font="Arial", font_size=27, weight=BOLD, color=BLACK).move_to([0, -1.15, 0])
        mission = Text(
            "This channel is an AI-assisted open research log\nfor accessible STEM education.",
            font="Arial",
            font_size=24,
            color=GRAY,
            line_spacing=0.9,
        ).scale_to_fit_width(5.35).move_to([0.85, -2.05, 0])
        self.play(FadeIn(credit), FadeIn(mission), run_time=1.5)
        point_pose = self.figure("point", 0.62).move_to([-3.15, -2.75, 0])
        down = Arrow([-2.05, -3.0, 0], [-2.05, -4.0, 0], color=INPUT, stroke_width=7)
        rings = VGroup(*[Circle(0.28 + i * 0.16, color=INPUT, stroke_width=4).set_opacity(0.46 - i * 0.08) for i in range(4)]).move_to(down.get_end())
        self.play(Transform(teacher, point_pose), shadow.animate.move_to([-3.15, -3.7, 0]), GrowArrow(down), LaggedStart(*[Create(r) for r in rings], lag_ratio=0.12), run_time=1.2)
        self.wait(6.2)
