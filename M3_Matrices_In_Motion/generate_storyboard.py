"""
generate_storyboard.py
Generates the official 6-scene storyboard PDF for the M3 Video Project
following the exact specifications from:
1. M3 Animation Video Project Instructions
2. M3 Lecture Sheet 10: Matrices in Motion
"""

import fitz  # PyMuPDF
import os

def create_storyboard():
    doc = fitz.open()
    
    # 2 pages: landscape A4 (842 x 595 pt) or portrait A4 (595 x 842 pt)
    # Storyboard works best in landscape or clean portrait. Let's make a beautiful 3-page portrait A4 document.
    
    PAGE_WIDTH = 595.28
    PAGE_HEIGHT = 842.0
    
    # ── PAGE 1: Title, Project Metadata, & Scenes 1-2 ──
    page1 = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
    
    # Dark header background
    header_rect = fitz.Rect(0, 0, PAGE_WIDTH, 110)
    page1.draw_rect(header_rect, color=(0.04, 0.08, 0.18), fill=(0.04, 0.08, 0.18))
    
    # Accent stripe
    accent_rect = fitz.Rect(0, 107, PAGE_WIDTH, 110)
    page1.draw_rect(accent_rect, color=(0, 0.9, 1), fill=(0, 0.9, 1))
    
    # Header text
    page1.insert_text(fitz.Point(36, 38), "NEWTON SCHOOL OF TECHNOLOGY", fontsize=11, fontname="helv", color=(0.6, 0.8, 1))
    page1.insert_text(fitz.Point(36, 62), "LINEAR ALGEBRA & CALCULUS (M3) — INTERNAL ASSESSMENT", fontsize=15, fontname="hebo", color=(1, 1, 1))
    page1.insert_text(fitz.Point(36, 85), "Official 6-Scene Storyboard: Matrices in Motion (How Matrices Transform Space)", fontsize=11, fontname="helv", color=(0, 0.9, 1))
    page1.insert_text(fitz.Point(36, 100), "Target Video Duration: ~5 Minutes (Strict Maximum: 7 Minutes) | Format: 16:9 Landscape 1080p", fontsize=9, fontname="helv", color=(0.8, 0.8, 0.8))
    
    # Metadata Box
    meta_rect = fitz.Rect(36, 125, PAGE_WIDTH - 36, 185)
    page1.draw_rect(meta_rect, color=(0.85, 0.88, 0.95), fill=(0.95, 0.97, 1.0), width=1)
    
    page1.insert_text(fitz.Point(48, 142), "PROJECT SPECIFICATION & LEARNING OBJECTIVE", fontsize=10, fontname="hebo", color=(0.04, 0.08, 0.2))
    page1.insert_text(fitz.Point(48, 158), "Concept: Linear Transformations & Matrix Representation (Lecture Sheet 10: Matrices in Motion)", fontsize=9, fontname="helv", color=(0.2, 0.2, 0.2))
    page1.insert_text(fitz.Point(48, 172), 'Guiding Idea: "A matrix is not just a collection of numbers. It describes how space transforms,', fontsize=9, fontname="helv", color=(0.1, 0.3, 0.6))
    page1.insert_text(fitz.Point(48, 183), 'and its columns reveal where the standard basis vectors e1 and e2 land."', fontsize=9, fontname="helv", color=(0.1, 0.3, 0.6))

    def draw_scene_card(page, y_start, scene_num, title, duration, purpose, visual_plan, math_plan, narration_plan):
        card_rect = fitz.Rect(36, y_start, PAGE_WIDTH - 36, y_start + 185)
        page.draw_rect(card_rect, color=(0.8, 0.85, 0.9), fill=(1, 1, 1), width=1)
        
        # Header banner inside card
        banner_rect = fitz.Rect(36, y_start, PAGE_WIDTH - 36, y_start + 28)
        page.draw_rect(banner_rect, color=(0.08, 0.15, 0.3), fill=(0.08, 0.15, 0.3))
        
        page.insert_text(fitz.Point(48, y_start + 19), f"SCENE {scene_num}: {title.upper()}", fontsize=11, fontname="hebo", color=(1, 1, 1))
        page.insert_text(fitz.Point(PAGE_WIDTH - 160, y_start + 19), f"Duration: {duration}", fontsize=10, fontname="hebo", color=(0, 0.9, 1))
        
        # Content sections
        curr_y = y_start + 45
        
        # Purpose
        page.insert_text(fitz.Point(48, curr_y), "Purpose:", fontsize=9, fontname="hebo", color=(0.1, 0.2, 0.4))
        page.insert_text(fitz.Point(125, curr_y), purpose, fontsize=9, fontname="helv", color=(0.2, 0.2, 0.2))
        curr_y += 24
        
        # Visual Plan
        page.insert_text(fitz.Point(48, curr_y), "Visual Plan:", fontsize=9, fontname="hebo", color=(0.1, 0.2, 0.4))
        for line in visual_plan:
            page.insert_text(fitz.Point(125, curr_y), line, fontsize=8.5, fontname="helv", color=(0.2, 0.2, 0.2))
            curr_y += 13
        curr_y += 6
        
        # Math Plan
        page.insert_text(fitz.Point(48, curr_y), "Mathematical Content:", fontsize=9, fontname="hebo", color=(0.1, 0.2, 0.4))
        for line in math_plan:
            page.insert_text(fitz.Point(175, curr_y), line, fontsize=8.5, fontname="helv", color=(0.1, 0.3, 0.6))
            curr_y += 13
        curr_y += 6
        
        # Narration Plan
        page.insert_text(fitz.Point(48, curr_y), "Narration & Pacing:", fontsize=9, fontname="hebo", color=(0.1, 0.2, 0.4))
        for line in narration_plan:
            page.insert_text(fitz.Point(175, curr_y), line, fontsize=8.5, fontname="helv", color=(0.3, 0.3, 0.3))
            curr_y += 13

    # Scene 1: Hook / Context
    draw_scene_card(
        page1, y_start=205, scene_num="1", title="Hook / Context (Matrices in Motion)",
        duration="0:00 - 0:25 (25s)",
        purpose="Spark curiosity and motivate the geometric nature of matrices.",
        visual_plan=[
            "Clean dark coordinate plane with axes, standard basis vectors e1, e2, and unit square.",
            "Coordinate grid suddenly undergoes dynamic morphing: stretches, shears, rotates, and scales.",
            "Visual chaos settles into bold title: 'MATRICES IN MOTION: How Matrices Transform Space'."
        ],
        math_plan=[
            "Initial basis: e1 = (1, 0), e2 = (0, 1). Unit square with area = 1.",
            "Dynamic deformations: stretching [[2, 0], [0, 1]], shearing [[1, 0.5], [0, 1]], rotation."
        ],
        narration_plan=[
            "Intentional visual silence and musical hook to engage the audience.",
            "Sets up guiding question: What does a matrix actually do to 2D space?"
        ]
    )
    
    # Scene 2: Concept Introduction
    draw_scene_card(
        page1, y_start=410, scene_num="2", title="Concept Introduction (The Basis Vector Secret)",
        duration="0:25 - 0:55 (30s)",
        purpose="Define a matrix as a transformation machine and connect columns to basis vectors.",
        visual_plan=[
            "Visual 'transformation machine' box: input vector enters, matrix acts, output emerges.",
            "Coordinate plane highlights standard basis vectors e1 and e2 in vivid yellow.",
            "Matrix A = [[2, 1], [1, 3]] appears. First column highlights in green as e1 moves to (2, 1).",
            "Second column highlights in orange as e2 moves to (1, 3)."
        ],
        math_plan=[
            "A = [[a, b], [c, d]]. Ae1 = [a, c]^T (column 1); Ae2 = [b, d]^T (column 2).",
            "Core insight: Column 1 = Image of e1, Column 2 = Image of e2."
        ],
        narration_plan=[
            "Explains that a matrix is not a static table of numbers, but a function T: R^2 -> R^2.",
            "Emphasizes the central breakthrough: tracking just two basis vectors unlocks the whole matrix."
        ]
    )
    
    page1.insert_text(fitz.Point(PAGE_WIDTH / 2 - 40, PAGE_HEIGHT - 20), "Page 1 of 3 — M3 Storyboard", fontsize=8, fontname="helv", color=(0.5, 0.5, 0.5))

    # ── PAGE 2: Scenes 3 & 4 ──
    page2 = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
    
    # Mini header
    mini_header = fitz.Rect(0, 0, PAGE_WIDTH, 45)
    page2.draw_rect(mini_header, color=(0.04, 0.08, 0.18), fill=(0.04, 0.08, 0.18))
    page2.insert_text(fitz.Point(36, 28), "M3 ANIMATION VIDEO STORYBOARD — VISUAL INTUITION & WORKED EXAMPLES", fontsize=11, fontname="hebo", color=(1, 1, 1))

    # Scene 3: Visual Intuition
    draw_scene_card(
        page2, y_start=60, scene_num="3", title="Visual Intuition (How the Whole Plane Follows)",
        duration="0:55 - 1:40 (45s)",
        purpose="Build geometric understanding: linear combinations dictate the fate of all vectors.",
        visual_plan=[
            "Decomposition of arbitrary vector v = (3, 2) into 3e1 + 2e2 shown with vector steps.",
            "Formula Av = xAe1 + yAe2 appears prominently at top.",
            "Five-step progression: (1) Transform e1 -> (2) Transform e2 -> (3) Transform v ->",
            "(4) Transform unit square -> (5) Transform entire infinite coordinate grid."
        ],
        math_plan=[
            "v = x*e1 + y*e2  ==>  T(v) = x*T(e1) + y*T(e2) = x*Ae1 + y*Ae2.",
            "Grid lines remain parallel and evenly spaced; origin remains strictly stationary at (0, 0)."
        ],
        narration_plan=[
            "Clear explanation that because space is linear, knowing e1 and e2 determines every point.",
            "Pacing allows the student to witness the grid bending smoothly to match the basis vectors."
        ]
    )

    # Scene 4: Worked Example (Transformation Gallery)
    draw_scene_card(
        page2, y_start=265, scene_num="4", title="Worked Example (The Transformation Gallery)",
        duration="1:40 - 2:55 (75s)",
        purpose="Walk step-by-step through core transformations directly from Lecture Sheet 10.",
        visual_plan=[
            "Sequential gallery panels with split view (plane on left, matrix calculations on right):",
            "  A. Shear S = [[1, 0], [1, 1]]: e2 fixed at (0, 1), e1 shifts to (1, 1). Square becomes rhombus.",
            "  B. Quarter-Turn R = [[0, 1], [-1, 0]]: 90 deg clockwise. e1 -> (0, -1), e2 -> (1, 0). Lengths kept.",
            "  C. Horizontal Stretch A = [[2, 0], [0, 1]]: e1 doubles to (2, 0), e2 stays (0, 1).",
            "  D. Reflection A = [[1, 0], [0, -1]]: Plane flips across x-axis. e2 reverses direction.",
            "  E. Collapse C = [[1, 1], [1, 1]]: Both e1, e2 map to (1, 1). (1, -1) collapses to origin (0, 0)!"
        ],
        math_plan=[
            "Shear: (x, y) |-> (x, x+y). Rotation: (x, y) |-> (y, -x). R^4 = I.",
            "Collapse: Output lies on line y = x. Nonzero vector (1, -1) in Null Space maps to (0, 0). Rank = 1."
        ],
        narration_plan=[
            "Deliberate step-by-step narration detailing how each column predicts the geometric outcome.",
            "Highlights information loss during dimension collapse."
        ]
    )
    
    # Scene 5: Interpretation (starts on page 2)
    draw_scene_card(
        page2, y_start=470, scene_num="5", title="Interpretation (Unit Square Geometry & Area Scaling)",
        duration="2:55 - 3:35 (40s)",
        purpose="Connect algebraic numbers back to geometric area scaling and determinants.",
        visual_plan=[
            "Unit square corners tracked: 0, e1, e2, e1+e2 ==> 0, Ae1, Ae2, Ae1+Ae2.",
            "Stretch matrix A = [[2, 0], [0, 1]]: square doubles in area to 2. Box shows det(A) = 2.",
            "Collapse matrix C = [[1, 1], [1, 1]]: square flattens to 1D line segment; det(C) = 0, area = 0."
        ],
        math_plan=[
            "Corners of transformed parallelogram: 0, Ae1, Ae2, Ae1 + Ae2.",
            "Area scaling factor = |det(A)|. det([[2,0],[0,1]]) = 2; det([[1,1],[1,1]]) = 1(1) - 1(1) = 0."
        ],
        narration_plan=[
            "Brief, intuitive bridge linking matrix columns to parallelogram area and determinant.",
            "Explains why det = 0 signifies total collapse into lower dimension."
        ]
    )

    page2.insert_text(fitz.Point(PAGE_WIDTH / 2 - 40, PAGE_HEIGHT - 20), "Page 2 of 3 — M3 Storyboard", fontsize=8, fontname="helv", color=(0.5, 0.5, 0.5))

    # ── PAGE 3: Scenes 6, 7, 8 & Evaluation Criteria ──
    page3 = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
    
    mini_header3 = fitz.Rect(0, 0, PAGE_WIDTH, 45)
    page3.draw_rect(mini_header3, color=(0.04, 0.08, 0.18), fill=(0.04, 0.08, 0.18))
    page3.insert_text(fitz.Point(36, 28), "M3 ANIMATION VIDEO STORYBOARD — LINEARITY, SYNTHESIS & CREDITS", fontsize=11, fontname="hebo", color=(1, 1, 1))

    # Scene 6 & 7 combined in Storyboard Scene 5/6 structure
    draw_scene_card(
        page3, y_start=60, scene_num="5B/6A", title="Linearity & Matrix Construction",
        duration="3:07 - 4:15 (68s)",
        purpose="Demonstrate linearity axioms and construct a matrix from an algebraic rule.",
        visual_plan=[
            "Linearity test: T(u+v) = T(u) + T(v) animated via vector parallelogram addition before & after.",
            "Scalar test: T(cu) = cT(u) showing vector scaling before and after transformation match.",
            "Reverse problem (Lecture Sheet 10 Page 11): Given T(x, y) = (x+y, x-y), apply to basis:",
            "  T(e1) = T(1, 0) = (1, 1)  ==> Column 1; T(e2) = T(0, 1) = (1, -1) ==> Column 2.",
            "Columns slide into place to form M = [[1, 1], [1, -1]]. Verify M[x, y]^T = [x+y, x-y]^T."
        ],
        math_plan=[
            "Axiom 1: Additivity T(u + v) = T(u) + T(v). Axiom 2: Homogeneity T(cu) = cT(u).",
            "Every linear map preserves the origin: T(0) = 0. Matrix construction: M_T = [ T(e1) | T(e2) ]."
        ],
        narration_plan=[
            "Explains the geometric meaning of linearity: straight lines remain straight, grid origin never shifts.",
            "Delivers the main takeaway: 'The columns of the matrix ARE the transformed standard basis vectors.'"
        ]
    )

    # Scene 8 / Storyboard Scene 6: Summary & Credits
    draw_scene_card(
        page3, y_start=265, scene_num="6", title="Summary & Credits",
        duration="4:08 - 4:43 (35s)",
        purpose="Reinforce 5 core mathematical takeaways and present required academic credits.",
        visual_plan=[
            "Transformed grid ripples gently in background.",
            "Five numbered takeaways appear with clean bullet typography and checkmarks.",
            "Elegant closing philosophical quote: 'MATHEMATICS IS MORE THAN NUMBERS. IT IS GEOMETRY IN MOTION.'",
            "Full credit card: Student Name, ID, Course M3, Newton School of Technology, AI disclosure."
        ],
        math_plan=[
            "1. Matrix = vector transformation. 2. Columns = basis images.",
            "3. Transformed basis dictates entire grid. 4. Linearity preserves addition & scaling.",
            "5. Geometry reveals what matrix multiplication actually computes."
        ],
        narration_plan=[
            "Concluding remarks summarizing the journey from static numbers to dynamic geometric motion.",
            "Invites viewer to think of every future matrix by picturing where e1 and e2 land."
        ]
    )

    # Evaluation Checklist & Viva Prep Box
    eval_rect = fitz.Rect(36, 470, PAGE_WIDTH - 36, 800)
    page3.draw_rect(eval_rect, color=(0.8, 0.85, 0.9), fill=(0.96, 0.98, 1.0), width=1)
    
    page3.insert_text(fitz.Point(48, 490), "M3 INTERNAL ASSESSMENT EVALUATION CRITERIA & VIVA PREPARATION", fontsize=10, fontname="hebo", color=(0.04, 0.08, 0.2))
    
    criteria = [
        ("Conceptual Correctness (10%):", "All transformations, basis vectors, matrix multiplications, and null spaces verified."),
        ("Clear Explanation:", "Logical flow: Hook -> Basis Concept -> Linear Combination -> Gallery -> Linearity -> Matrix Synthesis."),
        ("Visual & Pacing Craft:", "16:9 1080p, dark navy theme (#0a0e27), cyan original grid, orange transformed grid, yellow basis."),
        ("Original Effort & Artifacts:", "Custom Manim Community Edition code, modular scene architecture, 6-scene storyboard PDF."),
        ("Viva / Q&A Readiness:", "Prepared to explain: (1) Why T(0)=0 is necessary; (2) Rank-Nullity of Collapse matrix C;"),
        ("", "(3) How matrix multiplication AB represents composition of two geometric transformations.")
    ]
    
    ey = 508
    for title, desc in criteria:
        if title:
            page3.insert_text(fitz.Point(48, ey), title, fontsize=8.5, fontname="hebo", color=(0.1, 0.2, 0.4))
            page3.insert_text(fitz.Point(190, ey), desc, fontsize=8.5, fontname="helv", color=(0.2, 0.2, 0.2))
        else:
            page3.insert_text(fitz.Point(190, ey), desc, fontsize=8.5, fontname="helv", color=(0.2, 0.2, 0.2))
        ey += 15

    page3.insert_text(fitz.Point(PAGE_WIDTH / 2 - 40, PAGE_HEIGHT - 20), "Page 3 of 3 — M3 Storyboard", fontsize=8, fontname="helv", color=(0.5, 0.5, 0.5))

    output_path = "/Users/deveshgupta/Desktop/MATHS_VIDEO_LINEAR_TRANSFORMATION/M3_Matrices_In_Motion/storyboard.pdf"
    doc.save(output_path)
    doc.close()
    print(f"Storyboard saved successfully to {output_path}")

if __name__ == "__main__":
    create_storyboard()
