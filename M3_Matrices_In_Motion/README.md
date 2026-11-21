# Matrices in Motion: How Matrices Transform Space
**Linear Algebra and Calculus (M3) — Internal Assessment Project**  
*Newton School of Technology*

---

## 📌 Project Overview
This project presents a cinematic, mathematically rigorous educational animation video that visualizes the geometric essence of 2D linear algebra:

> **"A matrix is not just a static table of numbers. It describes how space transforms, and its columns reveal exactly where the standard basis vectors land."**

Developed as part of the **Mathematics-3 (M3) Internal Assessment (10% Weightage)**, this animation translates the theoretical foundations from **Lecture Sheet 10: Matrices in Motion** into intuitive, dynamic geometric animations using **Python** and **Manim Community Edition**.

---

## 🎯 Educational Objectives & Core Concepts
By watching this animation, a linear algebra student will be able to:
1. **Read Matrix Columns as Basis Vector Landing Points:**  
   For any matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, the first column $\begin{bmatrix} a \\ c \end{bmatrix}$ is the transformed landing site of $\mathbf{e}_1 = (1, 0)$, and the second column $\begin{bmatrix} b \\ d \end{bmatrix}$ is the landing site of $\mathbf{e}_2 = (0, 1)$.
2. **Understand Linear Combinations in Motion:**  
   Since every vector $\mathbf{v} = (x, y) = x\mathbf{e}_1 + y\mathbf{e}_2$, its transformed image is strictly $A\mathbf{v} = x(A\mathbf{e}_1) + y(A\mathbf{e}_2)$. Thus, tracking two basis vectors dictates the fate of the entire infinite plane.
3. **Explore Key Geometric Transformations (Lecture Sheet 10):**
   - **Shear ($S = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$):** One axis shifts while the other remains fixed; $(x, y) \mapsto (x, x+y)$.
   - **Quarter-Turn Rotation ($R = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$):** 90° clockwise rotation preserving lengths and angles ($R^4 = I$).
   - **Horizontal Stretch ($A = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}$):** Grid spacing doubles along the horizontal axis.
   - **Reflection ($A = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$):** Reflection across the x-axis with orientation reversal.
   - **Dimension Collapse ($C = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$):** Both basis vectors collapse to the line $y = x$; non-zero vector $(1, -1)$ maps to the origin $(0, 0)$ (demonstrating Null Space and Rank = 1).
4. **Unit Square & Determinant Interpretation:**  
   The unit square corners $(0, \mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_1+\mathbf{e}_2)$ transform into $(0, A\mathbf{e}_1, A\mathbf{e}_2, A\mathbf{e}_1+A\mathbf{e}_2)$. The determinant $|\det(A)|$ represents the exact geometric area-scaling factor.
5. **Axioms of Linearity:**  
   Visual demonstration of Additivity $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ and Homogeneity $T(c\mathbf{u}) = cT(\mathbf{u})$, proving that the origin remains fixed ($T(\mathbf{0}) = \mathbf{0}$) and straight grid lines never curve.
6. **Matrix Synthesis:**  
   Given an abstract transformation rule $T(x, y) = (x+y, x-y)$, constructing $M_T = [T(\mathbf{e}_1) \mid T(\mathbf{e}_2)] = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$.

---

## 🎬 Video Specifications & Storyboard Structure
- **Format:** 16:9 Landscape, 1080p Full HD MP4 (60 fps / 30 fps)
- **Target Duration:** ~5 Minutes (Strict maximum: 7 minutes)
- **Color Palette System:**
  - Background: Deep Navy (`#0a0e27`)
  - Original Coordinate Grid: Cyan / Blue (`#1a3a5c`, `#3a7ecf`)
  - Standard Basis Vectors ($\mathbf{e}_1, \mathbf{e}_2$): Vibrant Yellow (`#ffe600`)
  - Column 1 / Transformed $\mathbf{e}_1$: Vibrant Green (`#00ff88`)
  - Column 2 / Transformed $\mathbf{e}_2$: Vibrant Orange (`#ff8c00`)
  - General Vectors: Crisp White (`#ffffff`)
  - Null Space / Warning: Coral Red (`#ff4444`)

### Official 6-Scene Storyboard Alignment:
| Scene | Title | Duration | Purpose & Mathematical Content |
|---|---|---|---|
| **Scene 1** | **Hook / Context** | ~0:25 | Motivates topic with sudden dynamic grid deformation, stretching, shearing, and title reveal. |
| **Scene 2** | **Concept Introduction** | ~0:35 | Introduces matrix machine, basis vectors $\mathbf{e}_1, \mathbf{e}_2$, and column-to-vector correspondence. |
| **Scene 3** | **Visual Intuition** | ~0:45 | Shows $\mathbf{v} = x\mathbf{e}_1 + y\mathbf{e}_2$ and demonstrates the 5-step progression from basis to entire grid. |
| **Scene 4** | **Worked Example (Gallery)** | ~1:15 | Step-by-step walkthrough of Shear, Clockwise Quarter-turn, Stretch, Reflection, and Collapse. |
| **Scene 5** | **Interpretation & Linearity** | ~1:15 | Transformed unit square area scaling ($\det(A)$), linearity axioms, and constructing $M_T$ from $T(x, y)$. |
| **Scene 6** | **Summary & Credits** | ~0:25 | 5 core takeaways, closing quote ("Mathematics is geometry in motion"), and academic credits. |

---

## 📁 Repository Directory Structure
```
M3_Matrices_In_Motion/
├── main.py                     # Master orchestrator to render the full 5-minute video
├── generate_storyboard.py      # Standalone generator for the 3-page official storyboard PDF
├── storyboard.pdf              # Official 6-scene storyboard document
├── scene_timing_guide.txt       # Comprehensive timestamped voice-over recording script
├── requirements.txt            # Python dependencies
├── final_video.mp4             # Final rendered 1080p educational animation video
├── README.md                   # Project documentation and mathematical guide
├── .gitignore                  # Clean git rules excluding render cache
└── scenes/
    ├── __init__.py
    ├── utils.py                # Reusable color palette, vector plane, and typography engine
    ├── hook.py                 # Scene 1: Cinematic hook & grid deformation
    ├── introduction.py         # Scene 2: Transformation machine & column secret
    ├── basis_vectors.py        # Scene 3: Linear combination & grid following
    ├── transformations.py      # Scene 4 & 5: Gallery (Shear, Rotate, Stretch, Reflect, Collapse, Area)
    ├── linearity.py            # Scene 6: Linearity axioms & geometric signatures
    ├── build_matrix.py         # Scene 7: Synthesizing matrix from transformation rule
    └── summary.py              # Scene 8: Core takeaways & closing credits
```

---

## 🛠️ Software & Installation

### Requirements:
- Python 3.9+ (or Python 3.11 / 3.12 / 3.15)
- [Manim Community Edition](https://www.manim.community/) (v0.18.0+)
- FFmpeg (v4.0+)

### Setup on macOS / Linux / Windows:
```bash
# Clone the repository
git clone https://github.com/<your-username>/M3_Matrices_In_Motion.git
cd M3_Matrices_In_Motion

# Install Manim Community Edition via Homebrew (recommended on macOS)
brew install manim

# Or install dependencies via pip
pip install -r requirements.txt
```

---

## 🚀 How to Render the Video

### 1. Render the Complete 5-Minute Master Video (1080p 60fps):
```bash
manim -qh main.py MatricesInMotion
```
The output file will be generated in `media/videos/main/1080p60/MatricesInMotion.mp4` and copied to `final_video.mp4`.

### 2. Fast Low-Resolution Test (480p 15fps):
```bash
manim -ql main.py MatricesInMotion
```

### 3. Render Individual Scenes:
```bash
manim -ql scenes/hook.py HookScene
manim -ql scenes/introduction.py MatrixIntroduction
manim -ql scenes/basis_vectors.py BasisVectorsScene
manim -ql scenes/transformations.py TransformationGallery
manim -ql scenes/transformations.py UnitSquareScene
manim -ql scenes/linearity.py LinearityScene
manim -ql scenes/build_matrix.py BuildMatrixScene
manim -ql scenes/summary.py SummaryScene
```

### 4. Regenerate Storyboard PDF & Thumbnail:
```bash
python3 generate_storyboard.py
manim -s -qh create_thumbnail.py ThumbnailScene -o thumbnail.png
```

---

## 🖼️ Video Thumbnail & Splash Intro
A high-impact cinematic thumbnail (1920×1080) is provided in both PNG and JPEG formats:
- [`thumbnail.png`](./thumbnail.png) — Lossless high-res cover
- [`thumbnail.jpg`](./thumbnail.jpg) — Web preview cover
- **Built-in Splash Intro:** The thumbnail is prepended as a **2.0-second title card** directly at the start of [`final_video.mp4`](./final_video.mp4) before the animations begin, ensuring immediate visual impact when played in any classroom or LMS player.
- **Embedded Container Art:** Also embedded as the video file's native poster art icon.

---

## 🎙️ Voice-Over Recording Instructions
This animation was purposefully designed without pre-baked audio to allow the student to record their own voice-over.
- Refer to [`scene_timing_guide.txt`](./scene_timing_guide.txt) for exact sentence-by-sentence timestamps, visual cues, and explanation talking points.
- Key formulas and transformation labels remain visible with intentional pauses (2–3 seconds) to ensure clear, unhurried articulation.

---

## 🎓 Viva / Q&A Preparation Guide
During the project viva examination, be prepared to answer:
1. **Why does $T(\mathbf{0}) = \mathbf{0}$ for every linear transformation?**  
   *Answer:* By homogeneity, $T(\mathbf{0}) = T(0\mathbf{u}) = 0 \cdot T(\mathbf{u}) = \mathbf{0}$. If a transformation moves the origin (e.g. translation $T(x, y) = (x+2, y)$), it is an affine transformation, not linear.
2. **What is the rank and nullity of the collapse matrix $C = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$?**  
   *Answer:* The column space is $\text{span}\{(1, 1)\}$, which is 1-dimensional, so $\text{Rank}(C) = 1$. The null space is the line $x + y = 0$ (such as vector $(1, -1)$), so $\text{Nullity}(C) = 1$. By the Rank-Nullity Theorem: $\text{Rank} + \text{Nullity} = 1 + 1 = 2$.
3. **What is the geometric meaning of matrix multiplication $AB$?**  
   *Answer:* Multiplying matrices represents function composition: first apply transformation $B$, then apply transformation $A$ to the resulting space.
4. **Why is the determinant equal to the signed area scaling factor?**  
   *Answer:* The unit square has area 1. The transformed square has area given by the absolute value of the cross product / shoelace formula of the column vectors: $ad - bc$. If $\det(A) < 0$, the orientation of space has been flipped (reflected).

---

## 🤖 AI Assistance Disclosure
In accordance with course guidelines for the M3 Internal Assessment:
- **Antigravity AI (Google DeepMind)** was utilized as an assistive developer tool for:
  - Designing the mathematical modular architecture in Manim Community Edition.
  - Generating LaTeX-independent Pango/Cairo typographical wrappers for cross-platform rendering reliability.
  - Formatting the official 6-scene storyboard PDF structure and timing calculation guide.
- All mathematical derivations, transformation matrices, vector computations, and pedagogical choices were cross-checked and verified against **Lecture Sheet 10: Matrices in Motion**.
