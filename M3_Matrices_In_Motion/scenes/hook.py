"""
hook.py — Scene 1: Cinematic Hook
Duration target: ~25 seconds
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from manim import *
import numpy as np

try:
    from scenes.utils import (
        BG_COLOR, GRID_COLOR, AXIS_COLOR, E1_COLOR, E2_COLOR,
        ACCENT_COLOR, create_plane, create_unit_square
    )
except ImportError:
    from utils import (
        BG_COLOR, GRID_COLOR, AXIS_COLOR, E1_COLOR, E2_COLOR,
        ACCENT_COLOR, create_plane, create_unit_square
    )


class HookScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        plane = create_plane(x_range=[-5, 5, 1], y_range=[-4, 4, 1], x_length=10, y_length=8)
        origin = plane.c2p(0, 0)
        e1_vec = Arrow(origin, plane.c2p(1, 0), buff=0, color=E1_COLOR, stroke_width=4.5)
        e2_vec = Arrow(origin, plane.c2p(0, 1), buff=0, color=E2_COLOR, stroke_width=4.5)

        e1_label = Text("e₁", font_size=24, color=E1_COLOR, weight=BOLD).next_to(e1_vec, DOWN, buff=0.15)
        e2_label = Text("e₂", font_size=24, color=E2_COLOR, weight=BOLD).next_to(e2_vec, LEFT, buff=0.15)
        unit_square = create_unit_square(plane)

        self.play(Create(plane), run_time=1.8, rate_func=smooth)
        self.play(
            GrowArrow(e1_vec), GrowArrow(e2_vec),
            FadeIn(e1_label), FadeIn(e2_label),
            Create(unit_square),
            run_time=1.2,
        )
        self.wait(1.8)

        self.play(FadeOut(e1_label), FadeOut(e2_label), run_time=0.4)

        transform_group = VGroup(plane, e1_vec, e2_vec, unit_square)

        # Transformation 1: Horizontal Stretch [[2, 0], [0, 1]]
        self.play(
            transform_group.animate.apply_matrix([[2, 0], [0, 1]]),
            run_time=2.0,
            rate_func=smooth,
        )
        self.wait(1.0)

        # Transformation 2: Shear [[1, 0.5], [0, 1]]
        self.play(
            transform_group.animate.apply_matrix([[1, 0.5], [0, 1]]),
            run_time=2.0,
            rate_func=smooth,
        )
        self.wait(1.0)

        # Transformation 3: Rotation (45 degrees)
        angle = PI / 4
        rot_matrix = [[np.cos(angle), -np.sin(angle)],
                      [np.sin(angle),  np.cos(angle)]]
        self.play(
            transform_group.animate.apply_matrix(rot_matrix),
            run_time=2.0,
            rate_func=smooth,
        )
        self.wait(1.0)

        # Transformation 4: Scale down
        self.play(
            transform_group.animate.apply_matrix([[0.45, 0], [0, 0.45]]),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(1.0)

        self.play(FadeOut(transform_group), run_time=0.9)

        title = Text("MATRICES IN MOTION", font_size=54, color=WHITE, weight=BOLD)
        subtitle = Text("How Matrices Transform Space", font_size=26, color=ACCENT_COLOR).next_to(title, DOWN, buff=0.35)
        line = Line(LEFT * 3.5, RIGHT * 3.5, color=ACCENT_COLOR, stroke_width=1.5).next_to(title, DOWN, buff=0.18)

        self.play(Write(title), run_time=1.6)
        self.play(Create(line), FadeIn(subtitle, shift=UP * 0.25), run_time=1.2)
        self.wait(3.5)

        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(line), run_time=0.8)
        self.wait(0.5)
