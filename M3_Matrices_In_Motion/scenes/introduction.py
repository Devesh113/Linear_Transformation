"""
introduction.py — Scene 2: The Basic Idea of a Matrix
Duration target: ~35 seconds
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
        ACCENT_COLOR, create_plane, create_matrix_mobject, create_vector_col
    )
except ImportError:
    from utils import (
        BG_COLOR, E1_COLOR, E2_COLOR, COL1_COLOR, COL2_COLOR,
        ACCENT_COLOR, create_plane, create_matrix_mobject, create_vector_col
    )


class MatrixIntroduction(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        machine_title = Text("A Matrix Is a Transformation Machine", font_size=32, color=WHITE, weight=BOLD).to_edge(UP, buff=0.6)
        self.play(FadeIn(machine_title, shift=UP * 0.2), run_time=0.8)

        input_vec = create_vector_col("x", "y", name=None, color=WHITE, font_size=24).shift(LEFT * 3.8 + DOWN * 0.2)
        arrow_in = Arrow(LEFT * 2.5, LEFT * 1.1, color=ACCENT_COLOR, stroke_width=3.5).shift(DOWN * 0.2)

        box = RoundedRectangle(
            corner_radius=0.18, width=2.2, height=1.6,
            color=ACCENT_COLOR, fill_color=ACCENT_COLOR, fill_opacity=0.12, stroke_width=2.5
        ).shift(DOWN * 0.2)
        box_text = Text("Matrix A", font_size=24, color=ACCENT_COLOR, weight=BOLD).move_to(box)
        matrix_box = VGroup(box, box_text)

        arrow_out = Arrow(RIGHT * 1.1, RIGHT * 2.5, color=COL2_COLOR, stroke_width=3.5).shift(DOWN * 0.2)
        output_vec = create_vector_col("ax + by", "cx + dy", name=None, color=COL2_COLOR, font_size=20).shift(RIGHT * 4.2 + DOWN * 0.2)

        machine = VGroup(input_vec, arrow_in, matrix_box, arrow_out, output_vec)

        self.play(
            FadeIn(input_vec, shift=RIGHT * 0.2),
            GrowArrow(arrow_in),
            FadeIn(matrix_box),
            run_time=1.2
        )
        self.play(
            GrowArrow(arrow_out),
            FadeIn(output_vec, shift=RIGHT * 0.2),
            run_time=1.2
        )
        self.wait(3.5)

        self.play(FadeOut(machine), FadeOut(machine_title), run_time=0.8)

        plane = create_plane(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=5.6, y_length=5.6).shift(LEFT * 2.8)
        origin = plane.c2p(0, 0)

        e1_arrow = Arrow(origin, plane.c2p(1, 0), buff=0, color=E1_COLOR, stroke_width=5)
        e2_arrow = Arrow(origin, plane.c2p(0, 1), buff=0, color=E2_COLOR, stroke_width=5)

        e1_lbl = Text("e₁ = (1, 0)", font_size=18, color=E1_COLOR, weight=BOLD).next_to(e1_arrow, DOWN, buff=0.16)
        e2_lbl = Text("e₂ = (0, 1)", font_size=18, color=E2_COLOR, weight=BOLD).next_to(e2_arrow, LEFT, buff=0.16)

        self.play(Create(plane), run_time=1.0)
        self.play(
            GrowArrow(e1_arrow), FadeIn(e1_lbl),
            GrowArrow(e2_arrow), FadeIn(e2_lbl),
            run_time=1.0,
        )
        self.wait(2.2)

        mat = create_matrix_mobject("2", "1", "1", "3", name="A", col1_color=COL1_COLOR, col2_color=COL2_COLOR, font_size=26)
        mat.shift(RIGHT * 3.4 + UP * 2.0)
        self.play(FadeIn(mat, shift=DOWN * 0.2), run_time=0.8)
        self.wait(1.8)

        # Column 1 -> Ae₁
        ae1_text = Text("A e₁ = [ 2 , 1 ]ᵀ  (Column 1)", font_size=20, color=COL1_COLOR, weight=BOLD).shift(RIGHT * 3.4 + UP * 0.6)
        ae1_arrow = Arrow(origin, plane.c2p(2, 1), buff=0, color=COL1_COLOR, stroke_width=5)
        ae1_pt_lbl = Text("Ae₁ = (2, 1)", font_size=17, color=COL1_COLOR, weight=BOLD).next_to(plane.c2p(2, 1), UR, buff=0.1)

        self.play(
            FadeIn(ae1_text, shift=UP * 0.1),
            TransformFromCopy(e1_arrow, ae1_arrow),
            FadeIn(ae1_pt_lbl),
            run_time=1.5,
        )
        self.wait(2.5)

        # Column 2 -> Ae₂
        ae2_text = Text("A e₂ = [ 1 , 3 ]ᵀ  (Column 2)", font_size=20, color=COL2_COLOR, weight=BOLD).shift(RIGHT * 3.4 + DOWN * 0.4)
        ae2_arrow = Arrow(origin, plane.c2p(1, 3), buff=0, color=COL2_COLOR, stroke_width=5)
        ae2_pt_lbl = Text("Ae₂ = (1, 3)", font_size=17, color=COL2_COLOR, weight=BOLD).next_to(plane.c2p(1, 3), UL, buff=0.1)

        self.play(
            FadeIn(ae2_text, shift=UP * 0.1),
            TransformFromCopy(e2_arrow, ae2_arrow),
            FadeIn(ae2_pt_lbl),
            run_time=1.5,
        )
        self.wait(2.5)

        banner1 = Text("COLUMN 1  ➔  Image of e₁", font_size=22, color=COL1_COLOR, weight=BOLD).shift(RIGHT * 3.4 + DOWN * 1.8)
        banner2 = Text("COLUMN 2  ➔  Image of e₂", font_size=22, color=COL2_COLOR, weight=BOLD).next_to(banner1, DOWN, buff=0.28)

        box_takeaway = SurroundingRectangle(VGroup(banner1, banner2), color=ACCENT_COLOR, buff=0.2, corner_radius=0.12)

        self.play(
            FadeIn(banner1, shift=UP * 0.15),
            FadeIn(banner2, shift=UP * 0.15),
            Create(box_takeaway),
            run_time=1.0,
        )
        self.wait(4.5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
        self.wait(0.4)
