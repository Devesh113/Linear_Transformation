"""
basis_vectors.py — Scene 3: How the Whole Plane Follows
Duration target: ~45 seconds (Paced for voice-over)
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
        VEC_COLOR, ACCENT_COLOR, create_plane, create_unit_square, create_transformed_square
    )
except ImportError:
    from utils import (
        BG_COLOR, E1_COLOR, E2_COLOR, COL1_COLOR, COL2_COLOR,
        VEC_COLOR, ACCENT_COLOR, create_plane, create_unit_square, create_transformed_square
    )


class BasisVectorsScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 1. Vector Decomposition v = xe₁ + ye₂ ──
        plane = create_plane(x_range=[-5, 5, 1], y_range=[-4, 4, 1], x_length=9.5, y_length=7.5)
        origin = plane.c2p(0, 0)
        self.play(Create(plane), run_time=1.0)

        # Basis vectors
        e1 = Arrow(origin, plane.c2p(1, 0), buff=0, color=E1_COLOR, stroke_width=4.5)
        e2 = Arrow(origin, plane.c2p(0, 1), buff=0, color=E2_COLOR, stroke_width=4.5)
        e1_lbl = Text("e₁", font_size=20, color=E1_COLOR, weight=BOLD).next_to(e1, DOWN, buff=0.12)
        e2_lbl = Text("e₂", font_size=20, color=E2_COLOR, weight=BOLD).next_to(e2, LEFT, buff=0.12)

        self.play(
            GrowArrow(e1), GrowArrow(e2),
            FadeIn(e1_lbl), FadeIn(e2_lbl),
            run_time=0.8,
        )

        vx, vy = 3, 2

        # 3 copies along x, 2 copies along y
        e1_scaled = Arrow(origin, plane.c2p(vx, 0), buff=0, color=E1_COLOR, stroke_width=3.5)
        e1_s_lbl = Text(f"{vx} e₁", font_size=18, color=E1_COLOR, weight=BOLD).next_to(plane.c2p(vx / 2, 0), DOWN, buff=0.16)

        e2_scaled = Arrow(plane.c2p(vx, 0), plane.c2p(vx, vy), buff=0, color=E2_COLOR, stroke_width=3.5)
        e2_s_lbl = Text(f"{vy} e₂", font_size=18, color=E2_COLOR, weight=BOLD).next_to(plane.c2p(vx, vy / 2), RIGHT, buff=0.16)

        v_arrow = Arrow(origin, plane.c2p(vx, vy), buff=0, color=VEC_COLOR, stroke_width=5)
        v_lbl = Text("v = (3, 2)", font_size=20, color=VEC_COLOR, weight=BOLD).next_to(plane.c2p(vx, vy), UR, buff=0.12)

        formula = Text("v = x e₁ + y e₂", font_size=28, color=WHITE, weight=BOLD).to_edge(UP, buff=0.4)
        formula2 = Text("A v = x (A e₁) + y (A e₂)", font_size=28, color=ACCENT_COLOR, weight=BOLD).next_to(formula, DOWN, buff=0.25)

        self.play(Write(formula), run_time=0.8)
        self.wait(1.0)
        self.play(GrowArrow(e1_scaled), FadeIn(e1_s_lbl), run_time=0.8)
        self.play(GrowArrow(e2_scaled), FadeIn(e2_s_lbl), run_time=0.8)
        self.play(GrowArrow(v_arrow), FadeIn(v_lbl), run_time=0.9)
        self.wait(2.5)

        self.play(Write(formula2), run_time=1.2)
        self.wait(3.5)

        # Clear decomposition
        self.play(
            FadeOut(e1_scaled), FadeOut(e1_s_lbl),
            FadeOut(e2_scaled), FadeOut(e2_s_lbl),
            FadeOut(v_arrow), FadeOut(v_lbl),
            FadeOut(formula), FadeOut(formula2),
            FadeOut(e1_lbl), FadeOut(e2_lbl),
            FadeOut(e1), FadeOut(e2),
            run_time=0.7,
        )

        # ── 2. Progressive 5-Step Transformation ──
        matrix = [[2, 1], [0, 1]]

        # Re-add basis vectors and unit square
        e1 = Arrow(origin, plane.c2p(1, 0), buff=0, color=E1_COLOR, stroke_width=5)
        e2 = Arrow(origin, plane.c2p(0, 1), buff=0, color=E2_COLOR, stroke_width=5)
        e1_tag = Text("e₁", font_size=18, color=E1_COLOR, weight=BOLD).next_to(e1, DOWN, buff=0.1)
        e2_tag = Text("e₂", font_size=18, color=E2_COLOR, weight=BOLD).next_to(e2, LEFT, buff=0.1)

        unit_sq = create_unit_square(plane)
        arb_vec = Arrow(origin, plane.c2p(2, 1.5), buff=0, color=VEC_COLOR, stroke_width=4.5)
        arb_tag = Text("v = (2, 1.5)", font_size=17, color=VEC_COLOR, weight=BOLD).next_to(arb_vec.get_end(), UR, buff=0.1)

        self.play(GrowArrow(e1), FadeIn(e1_tag), run_time=0.5)

        # Step 1: Transform e₁
        s1 = Text("Step 1: Transform e₁  ➔  (2, 0)", font_size=20, color=COL1_COLOR, weight=BOLD).to_corner(UR, buff=0.45)
        self.play(FadeIn(s1), run_time=0.5)
        ae1 = Arrow(origin, plane.c2p(2, 0), buff=0, color=COL1_COLOR, stroke_width=5)
        ae1_tag = Text("Ae₁ = (2, 0)", font_size=18, color=COL1_COLOR, weight=BOLD).next_to(plane.c2p(2, 0), DOWN, buff=0.14)
        self.play(Transform(e1, ae1), Transform(e1_tag, ae1_tag), run_time=1.4)
        self.wait(1.5)

        # Step 2: Transform e₂
        s2 = Text("Step 2: Transform e₂  ➔  (1, 1)", font_size=20, color=COL2_COLOR, weight=BOLD).to_corner(UR, buff=0.45)
        self.play(GrowArrow(e2), FadeIn(e2_tag), FadeOut(s1), FadeIn(s2), run_time=0.5)
        ae2 = Arrow(origin, plane.c2p(1, 1), buff=0, color=COL2_COLOR, stroke_width=5)
        ae2_tag = Text("Ae₂ = (1, 1)", font_size=18, color=COL2_COLOR, weight=BOLD).next_to(plane.c2p(1, 1), UR, buff=0.12)
        self.play(Transform(e2, ae2), Transform(e2_tag, ae2_tag), run_time=1.4)
        self.wait(1.5)

        # Step 3: Transform arbitrary vector
        s3 = Text("Step 3: Transform vector v  ➔  (5.5, 1.5)", font_size=20, color=VEC_COLOR, weight=BOLD).to_corner(UR, buff=0.45)
        self.play(GrowArrow(arb_vec), FadeIn(arb_tag), FadeOut(s2), FadeIn(s3), run_time=0.5)
        av = Arrow(origin, plane.c2p(5.5, 1.5), buff=0, color=VEC_COLOR, stroke_width=4.5)
        av_tag = Text("Av = (5.5, 1.5)", font_size=17, color=VEC_COLOR, weight=BOLD).next_to(plane.c2p(5.5, 1.5), UR, buff=0.1)
        self.play(Transform(arb_vec, av), Transform(arb_tag, av_tag), run_time=1.4)
        self.wait(1.5)

        # Step 4: Transform unit square
        s4 = Text("Step 4: Unit square becomes parallelogram", font_size=20, color=ACCENT_COLOR, weight=BOLD).to_corner(UR, buff=0.45)
        self.play(Create(unit_sq), FadeOut(s3), FadeIn(s4), run_time=0.5)
        trans_sq = create_transformed_square(plane, matrix)
        self.play(Transform(unit_sq, trans_sq), run_time=1.4)
        self.wait(1.5)

        # Step 5: Transform entire grid
        s5 = Text("Step 5: The ENTIRE grid follows the basis!", font_size=22, color=COL1_COLOR, weight=BOLD).to_corner(UR, buff=0.45)
        self.play(FadeOut(s4), FadeIn(s5), run_time=0.5)
        self.play(
            plane.animate.apply_matrix(matrix),
            run_time=3.0,
            rate_func=smooth,
        )
        self.wait(4.0)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
        self.wait(0.4)
