"""
main.py — Master orchestrator for Matrices in Motion
Renders the complete 5-minute educational animation video.
"""

import sys
import os
from manim import *

# Ensure current directory and scenes/ are on python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "scenes"))

from scenes.hook import HookScene
from scenes.introduction import MatrixIntroduction
from scenes.basis_vectors import BasisVectorsScene
from scenes.transformations import run_transformation_gallery, UnitSquareScene
from scenes.linearity import LinearityScene
from scenes.build_matrix import BuildMatrixScene
from scenes.summary import SummaryScene


class MatricesInMotion(Scene):
    """
    Complete 5-minute Master Video:
    Sequences smoothly through all 8 pedagogical chapters:
    1. Cinematic Hook (0:00 - 0:25)
    2. Concept Introduction: Basis Vectors & Matrix Columns (0:25 - 0:55)
    3. How the Whole Plane Follows (0:55 - 1:40)
    4. Transformation Gallery: Shear, Rotation, Stretch, Reflection, Collapse (1:40 - 2:55)
    5. The Transformed Unit Square & Area Scaling (2:55 - 3:35)
    6. What Makes a Transformation Linear? (3:35 - 4:10)
    7. Build a Matrix from a Transformation (4:10 - 4:40)
    8. Key Takeaways & Closing Credits (4:40 - 5:00)
    """

    def construct(self):
        # Chapter 1: Cinematic Hook
        HookScene.construct(self)

        # Chapter 2: The Basic Idea of a Matrix
        MatrixIntroduction.construct(self)

        # Chapter 3: How the Whole Plane Follows
        BasisVectorsScene.construct(self)

        # Chapter 4: Transformation Gallery (Shear, Quarter-turn, Stretch, Reflect, Collapse)
        run_transformation_gallery(self)

        # Chapter 5: What Does the Transformed Square Tell Us?
        UnitSquareScene.construct(self)

        # Chapter 6: What Makes a Transformation Linear?
        LinearityScene.construct(self)

        # Chapter 7: Build a Matrix from a Transformation
        BuildMatrixScene.construct(self)

        # Chapter 8: Five Core Takeaways & Closing Credits
        SummaryScene.construct(self)


if __name__ == "__main__":
    os.system("/opt/homebrew/bin/manim -qh main.py MatricesInMotion")
