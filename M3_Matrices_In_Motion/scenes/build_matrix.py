"""
build_matrix.py — Scene 7: Build a Matrix from a Transformation
Duration target: ~30 seconds (Paced for voice-over)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from manim import *
import numpy as np

try:
    from scenes.utils import (
        BG_COLOR, E1_COLOR, E2_COLOR, COL1_COLOR, COL2_COLOR,
        ACCENT_COLOR, create_plane, create_matrix_mobject
    )
except ImportError:
    from utils import (
        BG_COLOR, E1_COLOR, E2_COLOR, COL1_COLOR, COL2_COLOR,
        ACCENT_COLOR, create_plane, create_matrix_mobject
    )


class BuildMatrixScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("BUILD A MATRIX FROM A TRANSFORMATION", font_size=28, color=WHITE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.7)

        rule_box = Text("Given:  T(x, y) = (x + y,  x − y)", font_size=26, color=ACCENT_COLOR, weight=BOLD).shift(UP * 2.0)
        self.play(FadeIn(rule_box), run_time=0.8)
        self.wait(2.5)

        s1 = Text("Step 1: Apply T to basis vector e₁ = (1, 0)", font_size=20, color=COL1_COLOR, weight=BOLD).shift(UP * 0.9)
        calc1 = Text("T(e₁) = T(1, 0) = (1 + 0,  1 − 0) = (1, 1)  ➔  COLUMN 1", font_size=21, color=COL1_COLOR, weight=BOLD).next_to(s1, DOWN, buff=0.18)

        self.play(FadeIn(s1), FadeIn(calc1), run_time=1.0)
        self.wait(3.5)

        s2 = Text("Step 2: Apply T to basis vector e₂ = (0, 1)", font_size=20, color=COL2_COLOR, weight=BOLD).shift(DOWN * 0.3)
        calc2 = Text("T(e₂) = T(0, 1) = (0 + 1,  0 − 1) = (1, −1)  ➔  COLUMN 2", font_size=21, color=COL2_COLOR, weight=BOLD).next_to(s2, DOWN, buff=0.18)

        self.play(FadeIn(s2), FadeIn(calc2), run_time=1.0)
        self.wait(4.0)

        self.play(
            FadeOut(s1), FadeOut(s2),
            rule_box.animate.scale(0.8).to_corner(UL, buff=0.4),
            calc1.animate.scale(0.75).to_corner(UL, buff=1.0),
            calc2.animate.scale(0.75).to_corner(UL, buff=1.5),
            FadeOut(title),
            run_time=0.7
        )

        s3 = Text("Step 3: Assemble Matrix Columns  M_T = [ T(e₁) | T(e₂) ]", font_size=22, color=ACCENT_COLOR, weight=BOLD).shift(UP * 1.8 + RIGHT * 1.5)
        mat = create_matrix_mobject("1", "1", "1", "-1", name="M_T", col1_color=COL1_COLOR, col2_color=COL2_COLOR, font_size=28).shift(UP * 0.7 + RIGHT * 2.5)

        self.play(FadeIn(s3), FadeIn(mat), run_time=1.0)
        self.wait(2.5)

        plane = create_plane(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=4.5, y_length=4.5).shift(LEFT * 3.4 + DOWN * 1.2)
        origin = plane.c2p(0, 0)

        e1_orig = Arrow(origin, plane.c2p(1, 0), buff=0, color=E1_COLOR, stroke_width=4)
        e2_orig = Arrow(origin, plane.c2p(0, 1), buff=0, color=E2_COLOR, stroke_width=4)
        te1_arrow = Arrow(origin, plane.c2p(1, 1), buff=0, color=COL1_COLOR, stroke_width=4.5)
        te2_arrow = Arrow(origin, plane.c2p(1, -1), buff=0, color=COL2_COLOR, stroke_width=4.5)

        self.play(Create(plane), GrowArrow(e1_orig), GrowArrow(e2_orig), run_time=0.8)
        self.play(
            Transform(e1_orig, te1_arrow),
            Transform(e2_orig, te2_arrow),
            run_time=1.4,
        )

        verify = Text("Verification:  M_T [x, y]ᵀ = [x + y,  x − y]ᵀ  ✓", font_size=20, color=WHITE, weight=BOLD).shift(RIGHT * 2.5 + DOWN * 0.7)
        self.play(FadeIn(verify), run_time=0.8)
        self.wait(3.0)

        grand_takeaway = Text(
            '"The columns of the matrix ARE\nthe transformed standard basis vectors."',
            font_size=22,
            color=COL1_COLOR,
            weight=BOLD,
            line_spacing=1.3,
        ).shift(RIGHT * 2.5 + DOWN * 2.2)

        box_grand = SurroundingRectangle(grand_takeaway, color=ACCENT_COLOR, buff=0.25, corner_radius=0.15)
        self.play(FadeIn(grand_takeaway), Create(box_grand), run_time=1.0)
        self.wait(6.0)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
        self.wait(0.4)
