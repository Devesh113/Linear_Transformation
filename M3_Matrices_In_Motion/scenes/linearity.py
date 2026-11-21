"""
linearity.py — Scene 6: What Makes a Transformation Linear?
Duration target: ~35 seconds (Paced for voice-over)
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
        VEC_COLOR, ACCENT_COLOR, create_plane
    )
except ImportError:
    from utils import (
        BG_COLOR, E1_COLOR, E2_COLOR, COL1_COLOR, COL2_COLOR,
        VEC_COLOR, ACCENT_COLOR, create_plane
    )


class LinearityScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("WHAT MAKES A TRANSFORMATION LINEAR?", font_size=30, color=WHITE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.7)

        cond1 = Text("1. Additivity:  T(u + v) = T(u) + T(v)", font_size=24, color=COL1_COLOR, weight=BOLD).shift(UP * 1.6)
        cond2 = Text("2. Homogeneity:  T(c u) = c T(u)", font_size=24, color=COL2_COLOR, weight=BOLD).next_to(cond1, DOWN, buff=0.35)

        self.play(FadeIn(cond1, shift=UP * 0.15), run_time=0.9)
        self.play(FadeIn(cond2, shift=UP * 0.15), run_time=0.9)
        self.wait(3.5)

        self.play(
            cond1.animate.scale(0.7).to_corner(UL, buff=0.4),
            cond2.animate.scale(0.7).to_corner(UL, buff=1.0),
            FadeOut(title),
            run_time=0.6,
        )

        plane_l = create_plane(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=4.8, y_length=4.8).shift(LEFT * 3.2 + DOWN * 0.6)
        origin_l = plane_l.c2p(0, 0)

        lbl_before = Text("Before: Input Space", font_size=18, color=ACCENT_COLOR, weight=BOLD).next_to(plane_l, UP, buff=0.18)

        u_vec = Arrow(origin_l, plane_l.c2p(1, 0), buff=0, color=COL1_COLOR, stroke_width=4.5)
        v_vec = Arrow(origin_l, plane_l.c2p(0, 1), buff=0, color=COL2_COLOR, stroke_width=4.5)
        uv_sum = Arrow(origin_l, plane_l.c2p(1, 1), buff=0, color=VEC_COLOR, stroke_width=4.5)

        u_lbl = Text("u", font_size=16, color=COL1_COLOR, weight=BOLD).next_to(u_vec, DOWN, buff=0.1)
        v_lbl = Text("v", font_size=16, color=COL2_COLOR, weight=BOLD).next_to(v_vec, LEFT, buff=0.1)
        uv_lbl = Text("u + v", font_size=16, color=VEC_COLOR, weight=BOLD).next_to(plane_l.c2p(1, 1), UR, buff=0.1)

        self.play(Create(plane_l), FadeIn(lbl_before), run_time=0.8)
        self.play(GrowArrow(u_vec), FadeIn(u_lbl), GrowArrow(v_vec), FadeIn(v_lbl), run_time=0.8)
        self.play(GrowArrow(uv_sum), FadeIn(uv_lbl), run_time=0.8)
        self.wait(2.5)

        plane_r = create_plane(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=4.8, y_length=4.8).shift(RIGHT * 3.2 + DOWN * 0.6)
        origin_r = plane_r.c2p(0, 0)

        lbl_after = Text("After: Output Space", font_size=18, color=COL2_COLOR, weight=BOLD).next_to(plane_r, UP, buff=0.18)

        tu_vec = Arrow(origin_r, plane_r.c2p(1, 1), buff=0, color=COL1_COLOR, stroke_width=4.5)
        tv_vec = Arrow(origin_r, plane_r.c2p(1, -1), buff=0, color=COL2_COLOR, stroke_width=4.5)
        tuv_sum = Arrow(origin_r, plane_r.c2p(2, 0), buff=0, color=VEC_COLOR, stroke_width=4.5)

        tu_lbl = Text("T(u) = (1, 1)", font_size=15, color=COL1_COLOR, weight=BOLD).next_to(plane_r.c2p(1, 1), UL, buff=0.1)
        tv_lbl = Text("T(v) = (1, -1)", font_size=15, color=COL2_COLOR, weight=BOLD).next_to(plane_r.c2p(1, -1), DR, buff=0.1)
        tuv_lbl = Text("T(u+v) = (2, 0)", font_size=15, color=VEC_COLOR, weight=BOLD).next_to(plane_r.c2p(2, 0), UR, buff=0.1)

        check_sum = Text("T(u + v)  =  T(u) + T(v)  [ (1,1) + (1,-1) = (2,0) ]  ✓", font_size=17, color=COL1_COLOR, weight=BOLD).shift(DOWN * 3.3)

        self.play(Create(plane_r), FadeIn(lbl_after), run_time=0.8)
        self.play(GrowArrow(tu_vec), FadeIn(tu_lbl), GrowArrow(tv_vec), FadeIn(tv_lbl), run_time=0.8)
        self.play(GrowArrow(tuv_sum), FadeIn(tuv_lbl), run_time=0.8)
        self.play(FadeIn(check_sum), run_time=0.8)
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.7)

        geo_title = Text("Geometric Signatures of Linear Transformations", font_size=28, color=WHITE, weight=BOLD).to_edge(UP, buff=0.8)

        props = VGroup(
            Text("✔  The origin is strictly stationary:  T(0) = 0", font_size=21, color=COL1_COLOR, weight=BOLD),
            Text("✔  Vector addition is preserved:  T(u + v) = T(u) + T(v)", font_size=21, color=COL1_COLOR, weight=BOLD),
            Text("✔  Scalar multiplication is preserved:  T(c u) = c T(u)", font_size=21, color=COL1_COLOR, weight=BOLD),
            Text("✔  Straight lines remain straight (never curve)", font_size=21, color=ACCENT_COLOR, weight=BOLD),
            Text("✔  Grid lines remain parallel and evenly spaced", font_size=21, color=ACCENT_COLOR, weight=BOLD),
            Text("✔  Space may stretch, shear, rotate, reflect, or collapse", font_size=21, color=WHITE),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).shift(DOWN * 0.2)

        box_props = SurroundingRectangle(props, color=ACCENT_COLOR, buff=0.3, corner_radius=0.15)

        self.play(FadeIn(geo_title), Create(box_props), run_time=0.8)
        for p in props:
            self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.38)
        self.wait(4.5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
        self.wait(0.4)
