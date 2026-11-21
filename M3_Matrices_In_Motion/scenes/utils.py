"""
utils.py — Reusable UI, Typography, and Mathematical Components for Manim
Designed to render crisply without external LaTeX dependencies.
"""

from manim import *
import numpy as np

# ── Color Palette ──
BG_COLOR = "#0a0e27"
GRID_COLOR = "#1a3a5c"
AXIS_COLOR = "#3a7ecf"
E1_COLOR = "#ffe600"       # Standard basis vector e₁ (Yellow)
E2_COLOR = "#ffe600"       # Standard basis vector e₂ (Yellow)
COL1_COLOR = "#00ff88"     # Column 1 / Image of e₁ (Vibrant Green)
COL2_COLOR = "#ff8c00"     # Column 2 / Image of e₂ (Vibrant Orange)
VEC_COLOR = "#ffffff"      # General vector v (Crisp White)
ACCENT_COLOR = "#00e5ff"   # Accents / Highlights (Electric Cyan)
RED_COLOR = "#ff4444"      # Collapse / Null space warning (Coral Red)


def create_plane(x_range=[-4, 4, 1], y_range=[-4, 4, 1], x_length=7, y_length=7):
    """Creates a stylized coordinate plane matching the visual theme."""
    return NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        background_line_style={
            "stroke_color": GRID_COLOR,
            "stroke_width": 1.2,
            "stroke_opacity": 0.45,
        },
        axis_config={
            "stroke_color": AXIS_COLOR,
            "stroke_width": 2.2,
            "include_tip": True,
            "tip_length": 0.16,
        },
    )


def create_matrix_mobject(a, b, c, d, name="A", col1_color=COL1_COLOR, col2_color=COL2_COLOR, font_size=26):
    """
    Creates an elegant, bracketed 2x2 matrix mobject with highlighted columns.
    A = [ a  b ]
        [ c  d ]
    """
    col1 = VGroup(
        Text(str(a), font_size=font_size, color=col1_color, weight=BOLD),
        Text(str(c), font_size=font_size, color=col1_color, weight=BOLD),
    ).arrange(DOWN, buff=0.28)

    col2 = VGroup(
        Text(str(b), font_size=font_size, color=col2_color, weight=BOLD),
        Text(str(d), font_size=font_size, color=col2_color, weight=BOLD),
    ).arrange(DOWN, buff=0.28)

    cols = VGroup(col1, col2).arrange(RIGHT, buff=0.45)

    bracket_l = Text("[", font_size=font_size * 2.0, color=WHITE, weight=BOLD).next_to(cols, LEFT, buff=0.12)
    bracket_r = Text("]", font_size=font_size * 2.0, color=WHITE, weight=BOLD).next_to(cols, RIGHT, buff=0.12)

    mat_core = VGroup(bracket_l, cols, bracket_r)

    if name:
        label = Text(f"{name}  =", font_size=font_size * 1.1, color=WHITE, weight=BOLD).next_to(mat_core, LEFT, buff=0.22)
        return VGroup(label, mat_core)
    return mat_core


def create_vector_col(x, y, name=None, color=WHITE, font_size=26):
    """
    Creates a bracketed column vector [ x , y ]^T.
    """
    vals = VGroup(
        Text(str(x), font_size=font_size, color=color, weight=BOLD),
        Text(str(y), font_size=font_size, color=color, weight=BOLD),
    ).arrange(DOWN, buff=0.26)

    bracket_l = Text("[", font_size=font_size * 2.0, color=color, weight=BOLD).next_to(vals, LEFT, buff=0.1)
    bracket_r = Text("]", font_size=font_size * 2.0, color=color, weight=BOLD).next_to(vals, RIGHT, buff=0.1)

    core = VGroup(bracket_l, vals, bracket_r)

    if name:
        label = Text(f"{name} =", font_size=font_size, color=color, weight=BOLD).next_to(core, LEFT, buff=0.2)
        return VGroup(label, core)
    return core


def create_unit_square(plane, fill_color=ACCENT_COLOR, stroke_color=ACCENT_COLOR, opacity=0.18):
    """Creates a unit square polygon with corners at (0,0), (1,0), (1,1), (0,1)."""
    return Polygon(
        plane.c2p(0, 0), plane.c2p(1, 0),
        plane.c2p(1, 1), plane.c2p(0, 1),
        color=stroke_color,
        fill_color=fill_color,
        fill_opacity=opacity,
        stroke_width=2.5,
    )


def create_transformed_square(plane, matrix, fill_color=COL2_COLOR, stroke_color=COL2_COLOR, opacity=0.2):
    """Creates the transformed parallelogram polygon given a 2x2 matrix."""
    m = np.array(matrix)
    corners_orig = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    corners_trans = (m @ corners_orig.T).T
    pts = [plane.c2p(pt[0], pt[1]) for pt in corners_trans]
    return Polygon(
        *pts,
        color=stroke_color,
        fill_color=fill_color,
        fill_opacity=opacity,
        stroke_width=2.5,
    )
