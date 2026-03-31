# Antenna Radiation Pattern Analysis (Group 4)

## 📡 Course
ECEG 4304 – Antenna and Radiowave Propagation  

## 👥 Group
Group 4 – Uniform Linear Array of 4 Isotropic Elements  

---

## 📌 Objective

The objective of this assignment is to generate, visualize, and analyze antenna radiation patterns in both 2D and 3D. This includes identifying key features such as the main lobe, side lobes, nulls, and beamwidth.

---

## 🧮 Given Radiation Function

The normalized radiation pattern for our group is:

F(θ) = sin(2π cosθ) / [4 sin((π/2) cosθ)]

Where:
- θ is the polar angle (0° to 180°)
- Element spacing d = λ/2
- The array consists of 4 isotropic elements

---

## 🛠️ Tools Used

- Python 3
- NumPy
- Matplotlib

---

## 📂 Project Structure

.
├── 2d-plot-v2.py
├── 3d_plot_v2.py
├── requirements.txt
└── README.md

---

## 📊 Implementations

### 1. 2D Radiation Pattern (2d-plot-v2.py)

- Generates polar plots of F(θ)
- Includes:
  - Linear scale
  - Decibel (dB) scale using: 20 log10(F(θ))

---

### 2. 3D Radiation Pattern (3d_plot_v2.py)

Assumptions:
- Rotational symmetry about the z-axis

Conversion from spherical to Cartesian:

x = r sinθ cosφ  
y = r sinθ sinφ  
z = r cosθ  

Where:
- r = F(θ)
- φ ranges from 0 to 2π

---

## 🔍 Analysis

### Main Lobe
- Maximum radiation occurs at θ ≈ 90° (broadside direction)

### Nulls
- Occur when: sin(2π cosθ) = 0  
- Which gives: cosθ = n / 2

### Side Lobes
- Present due to interference between array elements

### Beamwidth
- FNBW: Between first nulls  
- HPBW: At -3 dB points  

---

## 📈 Observations

- The pattern is symmetric about θ = 90°
- The 3D plot is rotationally symmetric about the z-axis
- The shape resembles a toroidal (donut-like) radiation pattern
- Increasing the number of elements increases directivity but introduces side lobes

---

## ⚠️ Challenges Faced

- Division by zero in the radiation equation
- Matplotlib backend issues on Linux (Fedora)
- Proper normalization of the radiation pattern
- Creating smooth 3D visualizations

---

## 🚀 How to Run

### Requirements
- Python 3.x
- pip

---

### Windows

1. Install Python:
   https://www.python.org/downloads/  
   (Make sure to check "Add Python to PATH" during installation)

2. Create and activate a virtual environment:
       python -m venv venv
       venv\Scripts\activate

3. Install dependencies:
       pip install -r requirements.txt

4. Run 2D plot:
       python 2d-plot-v2.py

5. Run 3D plot:
       python 3d_plot_v2.py

---

### Linux (Fedora / Ubuntu / etc.)

1. Install Python, pip, and venv prerequisites:

   Fedora:
       sudo dnf install python3 python3-pip

   Ubuntu/Debian:
       sudo apt install python3 python3-pip python3-venv

2. Create and activate a virtual environment:
       python3 -m venv venv
       source venv/bin/activate

3. Install dependencies:
       pip install -r requirements.txt

4. (Optional – for GUI display if you run into backend errors)

   Fedora:
       sudo dnf install python3-tkinter

   Ubuntu/Debian:
       sudo apt install python3-tk

5. Run 2D plot:
       python 2d-plot-v2.py

6. Run 3D plot:
       python 3d_plot_v2.py

---

### Output

- The plots are displayed in a window using matplotlib.
