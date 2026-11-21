"""
transformations.py — Scene 4: Transformation Gallery + Scene 5: Transformed Square
Fully constrained layout: The 2D plane stays strictly inside its left-side frame,
rotates smoothly by 90° clockwise without clipping or flying off,
and anchors strictly about its own origin for all linear maps.
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
        ACCENT_COLOR, RED_COLOR, create_plane, create_unit_square,
        create_transformed_square, create_matrix_mobject
    )
except ImportError:
    from utils import (
        BG_COLOR, E1_COLOR, E2_COLOR, COL1_COLOR, COL2_COLOR,
        ACCENT_COLOR, RED_COLOR, create_plane, create_unit_square,
        create_transformed_square, create_matrix_mobject
    )


def run_transformation_panel(scene, matrix, name, a, b, c, d, ae1_coords, ae2_coords, title_text, desc_text, rule_text, is_rotation=False):
    # Anchor coordinate plane strictly on the left side
    plane = create_plane(x_range=[-2.5, 2.5, 1], y_range=[-2.5, 2.5, 1], x_length=4.6, y_length=4.6).shift(LEFT * 3.4 + DOWN * 0.2)
    origin = plane.c2p(0, 0)

    # Frame boundary to visually contain the coordinate plane
    frame = RoundedRectangle(
        corner_radius=0.15,
        width=5.0,
        height=5.0,
        fill_color="#070c22",
        fill_opacity=0.55,
        stroke_color="#1e3a66",
        stroke_width=1.5
    ).move_to(origin)

    e1 = Arrow(origin, plane.c2p(1, 0), buff=0, color=E1_COLOR, stroke_width=4.5)
    e2 = Arrow(origin, plane.c2p(0, 1), buff=0, color=E2_COLOR, stroke_width=4.5)
    unit_sq = create_unit_square(plane)

    mat = create_matrix_mobject(a, b, c, d, name=name, col1_color=COL1_COLOR, col2_color=COL2_COLOR, font_size=24)
    mat.shift(RIGHT * 3.3 + UP * 2.3)

    col1_info = Text(f"{name} e₁ = ({ae1_coords[0]}, {ae1_coords[1]})  [Col 1]", font_size=18, color=COL1_COLOR, weight=BOLD).shift(RIGHT * 3.3 + UP * 1.3)
    col2_info = Text(f"{name} e₂ = ({ae2_coords[0]}, {ae2_coords[1]})  [Col 2]", font_size=18, color=COL2_COLOR, weight=BOLD).shift(RIGHT * 3.3 + UP * 0.7)

    title = Text(title_text, font_size=24, color=ACCENT_COLOR, weight=BOLD).shift(RIGHT * 3.3 + DOWN * 0.5)
    desc = Text(desc_text, font_size=16, color=WHITE).next_to(title, DOWN, buff=0.2)
    rule = Text(rule_text, font_size=16, color=COL1_COLOR, weight=BOLD).next_to(desc, DOWN, buff=0.2)

    scene.play(
        FadeIn(frame), Create(plane), Create(unit_sq),
        GrowArrow(e1), GrowArrow(e2),
        FadeIn(mat),
        run_time=0.9,
    )
    scene.play(FadeIn(col1_info), FadeIn(col2_info), run_time=0.7)
    scene.wait(1.2)

    if is_rotation:
        # A rigid, smooth 90° clockwise rotation about the plane's own origin
        # Preserves angles, lengths, and fixes the origin in place
        ae1 = Arrow(origin, plane.c2p(0, -1), buff=0, color=COL1_COLOR, stroke_width=4.5)
        ae2 = Arrow(origin, plane.c2p(1, 0), buff=0, color=COL2_COLOR, stroke_width=4.5)
        trans_sq = create_transformed_square(plane, matrix)

        scene.play(
            Rotate(plane, -90 * DEGREES, about_point=origin),
            Transform(e1, ae1),
            Transform(e2, ae2),
            Transform(unit_sq, trans_sq),
            run_time=2.2,
            rate_func=smooth,
        )
    else:
        # Linear map: transform vectors and unit square, then deform grid strictly about origin
        ae1 = Arrow(origin, plane.c2p(*ae1_coords), buff=0, color=COL1_COLOR, stroke_width=4.5)
        ae2 = Arrow(origin, plane.c2p(*ae2_coords), buff=0, color=COL2_COLOR, stroke_width=4.5)
        trans_sq = create_transformed_square(plane, matrix)

        scene.play(
            Transform(e1, ae1),
            Transform(e2, ae2),
            Transform(unit_sq, trans_sq),
            run_time=1.8,
            rate_func=smooth,
        )
        # about_point=origin guarantees origin never moves or flies off
        scene.play(plane.animate.apply_matrix(matrix, about_point=origin), run_time=2.0, rate_func=smooth)

    scene.play(FadeIn(title), FadeIn(desc), FadeIn(rule), run_time=0.8)
    scene.wait(4.0)

    scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.6)
    scene.wait(0.3)


def run_collapse_panel(scene):
    matrix = [[1, 1], [1, 1]]
    plane = create_plane(x_range=[-2.5, 2.5, 1], y_range=[-2.5, 2.5, 1], x_length=4.6, y_length=4.6).shift(LEFT * 3.4 + DOWN * 0.2)
    origin = plane.c2p(0, 0)

    frame = RoundedRectangle(
        corner_radius=0.15,
        width=5.0,
        height=5.0,
        fill_color="#070c22",
        fill_opacity=0.55,
        stroke_color="#1e3a66",
        stroke_width=1.5
    ).move_to(origin)

    e1 = Arrow(origin, plane.c2p(1, 0), buff=0, color=E1_COLOR, stroke_width=4.5)
    e2 = Arrow(origin, plane.c2p(0, 1), buff=0, color=E2_COLOR, stroke_width=4.5)
    unit_sq = create_unit_square(plane)

    mat = create_matrix_mobject("1", "1", "1", "1", name="C", col1_color=COL1_COLOR, col2_color=COL2_COLOR, font_size=24)
    mat.shift(RIGHT * 3.3 + UP * 2.3)

    c1_info = Text("C e₁ = (1, 1)  [Col 1]", font_size=18, color=COL1_COLOR, weight=BOLD).shift(RIGHT * 3.3 + UP * 1.3)
    c2_info = Text("C e₂ = (1, 1)  [Col 2]", font_size=18, color=COL2_COLOR, weight=BOLD).shift(RIGHT * 3.3 + UP * 0.7)
    warning = Text("Both columns are IDENTICAL!", font_size=18, color=RED_COLOR, weight=BOLD).shift(RIGHT * 3.3 + UP * 0.1)

    scene.play(
        FadeIn(frame), Create(plane), Create(unit_sq),
        GrowArrow(e1), GrowArrow(e2),
        FadeIn(mat),
        run_time=0.9,
    )
    scene.play(FadeIn(c1_info), FadeIn(c2_info), FadeIn(warning), run_time=0.8)
    scene.wait(1.5)

    ae_both = Arrow(origin, plane.c2p(1, 1), buff=0, color=COL1_COLOR, stroke_width=5)
    collapse_line = Line(plane.c2p(0, 0), plane.c2p(2, 2), color=COL2_COLOR, stroke_width=3.5)

    scene.play(
        Transform(e1, ae_both.copy()),
        Transform(e2, ae_both),
        Transform(unit_sq, collapse_line),
        run_time=2.0,
        rate_func=smooth,
    )

    null_vec = Arrow(origin, plane.c2p(1, -1), buff=0, color=RED_COLOR, stroke_width=4)
    null_tag = Text("v = (1, -1)", font_size=16, color=RED_COLOR, weight=BOLD).next_to(plane.c2p(1, -1), DR, buff=0.1)
    scene.play(GrowArrow(null_vec), FadeIn(null_tag), run_time=0.7)
    scene.wait(0.8)

    zero_pt = Dot(origin, color=RED_COLOR, radius=0.12)
    zero_tag = Text("Cv = (0, 0)  ➔ NULL SPACE!", font_size=16, color=RED_COLOR, weight=BOLD).next_to(origin, DL, buff=0.18)
    scene.play(Transform(null_vec, zero_pt), Transform(null_tag, zero_tag), run_time=1.4)
    scene.wait(1.0)

    # Deform strictly about origin
    scene.play(plane.animate.apply_matrix(matrix, about_point=origin), run_time=2.2, rate_func=smooth)

    title = Text("E. COLLAPSE (DIMENSION LOSS)", font_size=22, color=RED_COLOR, weight=BOLD).shift(RIGHT * 3.3 + DOWN * 1.5)
    sub1 = Text("2D Plane squashes into 1D Line y = x", font_size=16, color=WHITE).next_to(title, DOWN, buff=0.18)
    sub2 = Text("Rank = 1  |  Nullity = 1", font_size=16, color=ACCENT_COLOR, weight=BOLD).next_to(sub1, DOWN, buff=0.18)

    scene.play(FadeIn(title), FadeIn(sub1), FadeIn(sub2), run_time=0.8)
    scene.wait(4.5)

    scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.8)
    scene.wait(0.4)


def run_transformation_gallery(scene):
    sec_title = Text("TRANSFORMATION GALLERY", font_size=40, color=WHITE, weight=BOLD)
    sec_sub = Text("How Different Matrices Reshape Space", font_size=22, color=ACCENT_COLOR).next_to(sec_title, DOWN, buff=0.25)
    scene.play(FadeIn(sec_title, shift=UP * 0.25), FadeIn(sec_sub, shift=UP * 0.15), run_time=0.8)
    scene.wait(2.0)
    scene.play(FadeOut(sec_title), FadeOut(sec_sub), run_time=0.4)

    # A. SHEAR
    run_transformation_panel(
        scene,
        matrix=[[1, 0], [1, 1]],
        name="S",
        a="1", b="0", c="1", d="1",
        ae1_coords=(1, 1), ae2_coords=(0, 1),
        title_text="A. SHEAR",
        desc_text="One direction shifts, the other stays fixed",
        rule_text="(x, y) ➔ (x, x + y)",
    )

    # B. ROTATION (Clockwise quarter-turn)
    run_transformation_panel(
        scene,
        matrix=[[0, 1], [-1, 0]],
        name="R",
        a="0", b="1", c="-1", d="0",
        ae1_coords=(0, -1), ae2_coords=(1, 0),
        title_text="B. QUARTER-TURN CLOCKWISE",
        desc_text="90° rotation — lengths & angles preserved",
        rule_text="(x, y) ➔ (y, -x)  |  R⁴ = I",
        is_rotation=True,
    )

    # C. STRETCH
    run_transformation_panel(
        scene,
        matrix=[[1.8, 0], [0, 1]],
        name="A",
        a="2", b="0", c="0", d="1",
        ae1_coords=(2, 0), ae2_coords=(0, 1),
        title_text="C. HORIZONTAL STRETCH",
        desc_text="Horizontal spacing doubles, vertical intact",
        rule_text="(x, y) ➔ (2x, y)",
    )

    # D. REFLECTION
    run_transformation_panel(
        scene,
        matrix=[[1, 0], [0, -1]],
        name="A",
        a="1", b="0", c="0", d="-1",
        ae1_coords=(1, 0), ae2_coords=(0, -1),
        title_text="D. REFLECTION OVER X-AXIS",
        desc_text="e₁ remains fixed, e₂ flips downwards",
        rule_text="(x, y) ➔ (x, -y)",
    )

    # E. COLLAPSE
    run_collapse_panel(scene)


class TransformationGallery(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        run_transformation_gallery(self)


class UnitSquareScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("THE TRANSFORMED UNIT SQUARE & DETERMINANT", font_size=30, color=WHITE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.7)

        plane = create_plane(x_range=[-1, 3.5, 1], y_range=[-1, 2.5, 1], x_length=5.2, y_length=4.2).shift(LEFT * 3.3 + DOWN * 0.4)
        origin = plane.c2p(0, 0)

        frame = RoundedRectangle(
            corner_radius=0.15,
            width=5.6,
            height=4.6,
            fill_color="#070c22",
            fill_opacity=0.55,
            stroke_color="#1e3a66",
            stroke_width=1.5
        ).move_to(plane)

        unit_sq = create_unit_square(plane)
        c0 = Text("0", font_size=16, color=WHITE).next_to(plane.c2p(0, 0), DL, buff=0.1)
        c1 = Text("e₁", font_size=16, color=E1_COLOR, weight=BOLD).next_to(plane.c2p(1, 0), DR, buff=0.1)
        c2 = Text("e₂", font_size=16, color=E2_COLOR, weight=BOLD).next_to(plane.c2p(0, 1), UL, buff=0.1)
        c3 = Text("e₁+e₂", font_size=15, color=WHITE).next_to(plane.c2p(1, 1), UR, buff=0.1)

        self.play(FadeIn(frame), Create(plane), Create(unit_sq), FadeIn(c0), FadeIn(c1), FadeIn(c2), FadeIn(c3), run_time=1.0)

        info_title = Text("Unit Square Geometry:", font_size=20, color=ACCENT_COLOR, weight=BOLD).shift(RIGHT * 3.3 + UP * 1.8)
        info1 = Text("Corners: 0,  e₁,  e₂,  e₁ + e₂", font_size=17, color=WHITE).next_to(info_title, DOWN, buff=0.2)
        info2 = Text("Original Area = 1", font_size=18, color=COL1_COLOR, weight=BOLD).next_to(info1, DOWN, buff=0.2)
        self.play(FadeIn(info_title), FadeIn(info1), FadeIn(info2), run_time=0.8)
        self.wait(2.0)

        mat = create_matrix_mobject("2", "0", "0", "1", name="A", font_size=24).shift(RIGHT * 3.3 + DOWN * 0.2)
        trans_sq = create_transformed_square(plane, [[2, 0], [0, 1]])

        new_c1 = Text("Ae₁ = (2, 0)", font_size=15, color=COL1_COLOR, weight=BOLD).next_to(plane.c2p(2, 0), DR, buff=0.1)
        new_c3 = Text("Ae₁+Ae₂", font_size=15, color=WHITE).next_to(plane.c2p(2, 1), UR, buff=0.1)

        self.play(FadeIn(mat), run_time=0.7)
        self.play(
            Transform(unit_sq, trans_sq),
            Transform(c1, new_c1),
            Transform(c3, new_c3),
            run_time=1.8,
        )

        det_calc = Text("det(A) = (2)(1) − (0)(0) = 2", font_size=18, color=COL1_COLOR, weight=BOLD).next_to(mat, DOWN, buff=0.3)
        area_scale = Text("Area Scaling Factor = |det(A)| = 2", font_size=18, color=COL2_COLOR, weight=BOLD).next_to(det_calc, DOWN, buff=0.22)
        self.play(FadeIn(det_calc), FadeIn(area_scale), run_time=0.9)
        self.wait(3.5)

        self.play(
            FadeOut(mat), FadeOut(det_calc), FadeOut(area_scale),
            run_time=0.6
        )

        mat_c = create_matrix_mobject("1", "1", "1", "1", name="C", font_size=24).shift(RIGHT * 3.3 + DOWN * 0.2)
        collapse_line = Line(plane.c2p(0, 0), plane.c2p(2, 2), color=RED_COLOR, stroke_width=3.5)
        det_c = Text("det(C) = (1)(1) − (1)(1) = 0", font_size=18, color=RED_COLOR, weight=BOLD).next_to(mat_c, DOWN, buff=0.3)
        area_zero = Text("Area = 0  ➔ 2D Flattened to 1D!", font_size=18, color=RED_COLOR, weight=BOLD).next_to(det_c, DOWN, buff=0.22)

        self.play(FadeIn(mat_c), run_time=0.6)
        self.play(Transform(unit_sq, collapse_line), run_time=1.6)
        self.play(FadeIn(det_c), FadeIn(area_zero), run_time=0.8)
        self.wait(4.5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
        self.wait(0.4)
