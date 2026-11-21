"""
create_thumbnail.py — Generates an eye-catching, cinematic 1920x1080 mathematical thumbnail
for 'Matrices in Motion: How Matrices Transform Space'.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from manim import *
import numpy as np
from scenes.utils import (
    BG_COLOR, GRID_COLOR, AXIS_COLOR, E1_COLOR, E2_COLOR,
    COL1_COLOR, COL2_COLOR, ACCENT_COLOR, RED_COLOR, VEC_COLOR
)

class ThumbnailScene(Scene):
    def construct(self):
        self.camera.background_color = "#060919"  # Ultra deep cinematic navy

        # ── 1. BACKGROUND GLOW & ACCENT GRADIENTS ──
        # Subtle glowing circles in background
        bg_glow_left = Dot(point=[-3.5, 0, 0], radius=4.5, color="#122554").set_opacity(0.35)
        bg_glow_right = Dot(point=[3.5, 0.5, 0], radius=4.0, color="#1b3a6b").set_opacity(0.40)
        self.add(bg_glow_left, bg_glow_right)

        # ── 2. DYNAMIC TRANSFORMED GRID (Right side) ──
        plane_center = np.array([2.8, -0.4, 0])
        
        # Original subtle faint grid
        orig_plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6.5,
            y_length=6.5,
            background_line_style={"stroke_color": "#1a355e", "stroke_width": 1.0, "stroke_opacity": 0.3},
            axis_config={"stroke_color": "#28558a", "stroke_width": 1.5, "include_tip": False}
        ).move_to(plane_center)
        self.add(orig_plane)

        # Transformed grid lines (Shear + Stretch: [2, 0.8], [0.6, 1.8])
        tf_matrix = np.array([[1.8, 0.7], [0.5, 1.6]])
        
        # Draw dynamic deformed grid lines
        tf_grid = VGroup()
        for x in np.arange(-3, 3.5, 1):
            p1 = plane_center + np.array([tf_matrix[0][0]*x + tf_matrix[0][1]*(-3), tf_matrix[1][0]*x + tf_matrix[1][1]*(-3), 0]) * 0.95
            p2 = plane_center + np.array([tf_matrix[0][0]*x + tf_matrix[0][1]*(3), tf_matrix[1][0]*x + tf_matrix[1][1]*(3), 0]) * 0.95
            tf_grid.add(Line(p1, p2, stroke_color="#ff9900", stroke_width=1.8, stroke_opacity=0.35))
            
        for y in np.arange(-3, 3.5, 1):
            p1 = plane_center + np.array([tf_matrix[0][0]*(-3) + tf_matrix[0][1]*y, tf_matrix[1][0]*(-3) + tf_matrix[1][1]*y, 0]) * 0.95
            p2 = plane_center + np.array([tf_matrix[0][0]*(3) + tf_matrix[0][1]*y, tf_matrix[1][0]*(3) + tf_matrix[1][1]*y, 0]) * 0.95
            tf_grid.add(Line(p1, p2, stroke_color="#ff9900", stroke_width=1.8, stroke_opacity=0.35))
        self.add(tf_grid)

        # Transformed Unit Parallelogram (Glowing)
        origin_pt = plane_center
        v1_pt = plane_center + np.array([tf_matrix[0][0], tf_matrix[1][0], 0]) * 1.35
        v2_pt = plane_center + np.array([tf_matrix[0][1], tf_matrix[1][1], 0]) * 1.35
        v12_pt = plane_center + np.array([tf_matrix[0][0] + tf_matrix[0][1], tf_matrix[1][0] + tf_matrix[1][1], 0]) * 1.35

        poly = Polygon(origin_pt, v1_pt, v12_pt, v2_pt,
                       fill_color="#00e5ff", fill_opacity=0.25,
                       stroke_color="#00e5ff", stroke_width=3.5)
        self.add(poly)

        # Transformed Vector Arrows
        arrow1 = Arrow(origin_pt, v1_pt, buff=0, color=COL1_COLOR, stroke_width=7, max_tip_length_to_length_ratio=0.22)
        arrow2 = Arrow(origin_pt, v2_pt, buff=0, color=COL2_COLOR, stroke_width=7, max_tip_length_to_length_ratio=0.22)
        
        lbl_v1 = Text("T(e₁)", font_size=26, color=COL1_COLOR, weight=BOLD).next_to(v1_pt, DR, buff=0.15)
        lbl_v2 = Text("T(e₂)", font_size=26, color=COL2_COLOR, weight=BOLD).next_to(v2_pt, UL, buff=0.15)
        self.add(arrow1, arrow2, lbl_v1, lbl_v2)

        # ── 3. LEFT SIDE: CATCHY HIGH-IMPACT TYPOGRAPHY ──
        # Top Badge
        badge_box = RoundedRectangle(corner_radius=0.18, width=4.6, height=0.55,
                                     fill_color="#0d2347", fill_opacity=0.85,
                                     stroke_color=ACCENT_COLOR, stroke_width=1.8).to_corner(UL, buff=0.7)
        badge_text = Text("LINEAR ALGEBRA (M3) • VISUALIZED", font_size=18, color=ACCENT_COLOR, weight=BOLD).move_to(badge_box)
        self.add(badge_box, badge_text)

        # Main Big Title (High contrast, bold, catchy)
        title_word1 = Text("MATRICES", font_size=74, color="#ffe600", weight=BOLD)
        title_word2 = Text("IN MOTION", font_size=74, color="#00e5ff", weight=BOLD)
        title_group = VGroup(title_word1, title_word2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        title_group.next_to(badge_box, DOWN, buff=0.45).align_to(badge_box, LEFT)
        self.add(title_group)

        # Catchy Subtitle Banner
        sub_text = Text("HOW MATRICES TRANSFORM SPACE", font_size=23, color=WHITE, weight=BOLD)
        sub_box = RoundedRectangle(corner_radius=0.15, width=sub_text.width + 0.5, height=0.62,
                                   fill_color="#182c54", fill_opacity=0.9,
                                   stroke_color="#ff8c00", stroke_width=2.0)
        sub_box.next_to(title_group, DOWN, buff=0.32).align_to(title_group, LEFT)
        sub_text.move_to(sub_box)
        self.add(sub_box, sub_text)

        # Hook / Insight Pill: "COLUMNS = WHERE BASIS LANDS"
        hook_box = RoundedRectangle(corner_radius=0.2, width=5.6, height=0.9,
                                    fill_color="#0a1832", fill_opacity=0.95,
                                    stroke_color=COL1_COLOR, stroke_width=2.2)
        hook_box.next_to(sub_box, DOWN, buff=0.35).align_to(sub_box, LEFT)
        
        hook_t1 = Text("SECRET REVEALED:", font_size=15, color="#8bb2e8", weight=BOLD)
        hook_t2 = Text("Columns = Transformed Basis Vectors", font_size=20, color=COL1_COLOR, weight=BOLD)
        hook_content = VGroup(hook_t1, hook_t2).arrange(DOWN, buff=0.08, aligned_edge=LEFT).move_to(hook_box).shift(RIGHT * 0.1)
        self.add(hook_box, hook_content)

        # ── 4. FLOATING GLASS MATRIX CARD ──
        mat_card = RoundedRectangle(corner_radius=0.22, width=4.8, height=1.75,
                                    fill_color="#071329", fill_opacity=0.92,
                                    stroke_color="#436499", stroke_width=1.6)
        mat_card.next_to(hook_box, DOWN, buff=0.32).align_to(hook_box, LEFT)

        # Inside Matrix Card:
        # A = [ T(e₁)  T(e₂) ]
        col1_disp = VGroup(
            Text("2", font_size=32, color=COL1_COLOR, weight=BOLD),
            Text("1", font_size=32, color=COL1_COLOR, weight=BOLD)
        ).arrange(DOWN, buff=0.22)

        col2_disp = VGroup(
            Text("1", font_size=32, color=COL2_COLOR, weight=BOLD),
            Text("3", font_size=32, color=COL2_COLOR, weight=BOLD)
        ).arrange(DOWN, buff=0.22)

        cols_disp = VGroup(col1_disp, col2_disp).arrange(RIGHT, buff=0.6)
        
        brk_l = Text("[", font_size=65, color=WHITE, weight=BOLD).next_to(cols_disp, LEFT, buff=0.15)
        brk_r = Text("]", font_size=65, color=WHITE, weight=BOLD).next_to(cols_disp, RIGHT, buff=0.15)
        matrix_mobj = VGroup(brk_l, cols_disp, brk_r)

        mat_title = Text("A  =", font_size=32, color=WHITE, weight=BOLD).next_to(matrix_mobj, LEFT, buff=0.25)
        full_mat = VGroup(mat_title, matrix_mobj).move_to(mat_card).shift(LEFT * 0.4)

        # Labels pointing to columns
        lbl_c1 = Text("Col 1", font_size=15, color=COL1_COLOR, weight=BOLD).next_to(col1_disp, UP, buff=0.12)
        lbl_c2 = Text("Col 2", font_size=15, color=COL2_COLOR, weight=BOLD).next_to(col2_disp, UP, buff=0.12)
        
        self.add(mat_card, full_mat, lbl_c1, lbl_c2)

        # Bottom Right Submitter credit tag
        credit_tag = Text("Devesh Gupta • Newton School of Technology", font_size=15, color="#6b8dbf", weight=NORMAL).to_corner(DR, buff=0.45)
        self.add(credit_tag)

        # 4K / 60FPS badge at top right
        quality_box = RoundedRectangle(corner_radius=0.12, width=2.2, height=0.45,
                                       fill_color="#1a1100", fill_opacity=0.85,
                                       stroke_color="#ffb700", stroke_width=1.5).to_corner(UR, buff=0.7)
        quality_text = Text("1080p • 60 FPS", font_size=14, color="#ffc83b", weight=BOLD).move_to(quality_box)
        self.add(quality_box, quality_text)
