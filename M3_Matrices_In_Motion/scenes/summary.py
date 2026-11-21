"""
summary.py — Scene 8: Summary and Ending
Includes a crystal-clear, high-contrast, beautifully formatted closing credits screen.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from manim import *
import numpy as np

try:
    from scenes.utils import (
        BG_COLOR, E1_COLOR, COL1_COLOR, COL2_COLOR,
        ACCENT_COLOR, create_plane
    )
except ImportError:
    from utils import (
        BG_COLOR, E1_COLOR, COL1_COLOR, COL2_COLOR,
        ACCENT_COLOR, create_plane
    )


class SummaryScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 1. Transformed Coordinate Plane Background for Takeaways ──
        plane = create_plane(x_range=[-6, 6, 1], y_range=[-5, 5, 1], x_length=12, y_length=9)
        plane.apply_matrix([[1.4, 0.4], [-0.3, 1.2]])
        self.play(FadeIn(plane, run_time=1.2))

        # ── 2. Five Core Takeaways ──
        summary_title = Text("FIVE CORE TAKEAWAYS", font_size=32, color=WHITE, weight=BOLD).to_edge(UP, buff=0.6)

        points = VGroup(
            Text("1. A matrix is an engine of spatial transformation.", font_size=21, color=WHITE, weight=BOLD),
            Text("2. The columns reveal exactly where the basis vectors land.", font_size=21, color=COL1_COLOR, weight=BOLD),
            Text("3. Linear combinations dictate how the entire plane follows.", font_size=21, color=ACCENT_COLOR, weight=BOLD),
            Text("4. Linearity preserves vector addition and scalar multiplication.", font_size=21, color=COL2_COLOR, weight=BOLD),
            Text("5. Geometry reveals what matrix multiplication actually computes.", font_size=21, color=WHITE, weight=BOLD),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).shift(DOWN * 0.2)

        bg_card = BackgroundRectangle(
            VGroup(summary_title, points),
            fill_color=BG_COLOR,
            fill_opacity=0.92,
            buff=0.35,
        )

        self.play(FadeIn(bg_card), FadeIn(summary_title), run_time=0.8)
        for p in points:
            self.play(FadeIn(p, shift=RIGHT * 0.25), run_time=0.45)
        self.wait(18.0)

        # Clear takeaways AND the background plane for a pure, clean credits canvas
        self.play(
            FadeOut(bg_card), FadeOut(summary_title), FadeOut(points), FadeOut(plane),
            run_time=0.8
        )

        # ── 3. Philosophical Closing Quote ──
        q1 = Text("MATHEMATICS IS MORE THAN NUMBERS.", font_size=34, color=WHITE, weight=BOLD)
        q2 = Text("IT IS GEOMETRY IN MOTION.", font_size=34, color=ACCENT_COLOR, weight=BOLD).next_to(q1, DOWN, buff=0.35)

        self.play(Write(q1), run_time=1.4)
        self.play(Write(q2), run_time=1.2)
        self.wait(5.0)
        self.play(FadeOut(q1), FadeOut(q2), run_time=0.8)

        # ── 4. High-Clarity Academic Credits Card ──
        # Distinct, beautiful, large-typography card
        card_box = RoundedRectangle(
            corner_radius=0.25,
            width=11.5,
            height=6.2,
            color=ACCENT_COLOR,
            fill_color="#070b1e",
            fill_opacity=0.98,
            stroke_width=2.5,
        )

        # Card Header
        main_title = Text("MATRICES IN MOTION", font_size=34, color=WHITE, weight=BOLD)
        sub_title = Text(
            "Linear Algebra and Calculus (M3) — Internal Assessment Project",
            font_size=20,
            color=ACCENT_COLOR,
            weight=BOLD
        ).next_to(main_title, DOWN, buff=0.18)

        divider = Line(LEFT * 5.2, RIGHT * 5.2, color=ACCENT_COLOR, stroke_width=1.5).next_to(sub_title, DOWN, buff=0.22)

        header_grp = VGroup(main_title, sub_title, divider)

        # Content Table Rows (Left Label: Col1, Value: Col2)
        def make_credit_row(label, value, value_color=WHITE, font_size=21):
            lbl = Text(label, font_size=font_size, color="#8ba3c7", weight=BOLD)
            val = Text(value, font_size=font_size, color=value_color, weight=BOLD)
            # Arrange horizontally
            lbl.to_left(buff=1.5)
            val.next_to(lbl, RIGHT, buff=0.4)
            return VGroup(lbl, val)

        row1_lbl = Text("Student Author :", font_size=22, color="#8ba3c7", weight=BOLD)
        row1_val = Text("Devesh Gupta", font_size=24, color=COL1_COLOR, weight=BOLD)
        r1 = VGroup(row1_lbl, row1_val).arrange(RIGHT, buff=0.35)

        row2_lbl = Text("Institution :", font_size=21, color="#8ba3c7", weight=BOLD)
        row2_val = Text("Newton School of Technology", font_size=21, color=WHITE, weight=BOLD)
        r2 = VGroup(row2_lbl, row2_val).arrange(RIGHT, buff=0.35)

        row3_lbl = Text("Core Concept :", font_size=21, color="#8ba3c7", weight=BOLD)
        row3_val = Text("Linear Transformations & Matrix Representation", font_size=21, color=COL2_COLOR, weight=BOLD)
        r3 = VGroup(row3_lbl, row3_val).arrange(RIGHT, buff=0.35)

        row4_lbl = Text("Primary Reference :", font_size=21, color="#8ba3c7", weight=BOLD)
        row4_val = Text("M3 Lecture Sheet 10 (Matrices in Motion)", font_size=21, color=WHITE, weight=BOLD)
        r4 = VGroup(row4_lbl, row4_val).arrange(RIGHT, buff=0.35)

        row5_lbl = Text("Animation Engine :", font_size=20, color="#8ba3c7", weight=BOLD)
        row5_val = Text("Python 3  •  Manim Community Edition (v0.22.1)", font_size=20, color=ACCENT_COLOR, weight=BOLD)
        r5 = VGroup(row5_lbl, row5_val).arrange(RIGHT, buff=0.35)

        row6_lbl = Text("AI Disclosure :", font_size=19, color="#8ba3c7", weight=BOLD)
        row6_val = Text("Assisted by Google Antigravity AI for coding & motion design", font_size=19, color="#d0d8e8")
        r6 = VGroup(row6_lbl, row6_val).arrange(RIGHT, buff=0.35)

        rows = VGroup(r1, r2, r3, r4, r5, r6).arrange(DOWN, buff=0.24, aligned_edge=LEFT)

        # Assemble Full Credits Card
        card_content = VGroup(header_grp, rows).arrange(DOWN, buff=0.32).move_to(card_box)

        full_card = VGroup(card_box, card_content).shift(DOWN * 0.1)

        # Animate reveal of the credits card
        self.play(FadeIn(card_box), FadeIn(header_grp), run_time=1.0)
        self.play(FadeIn(rows, shift=UP * 0.2), run_time=1.2)
        self.wait(8.0)  # Extended wait time so every line can be read comfortably

        # Smooth, elegant final fade out
        self.play(FadeOut(full_card), run_time=1.5)
        self.wait(0.8)
