import numpy as np
import matplotlib.pyplot as plt
import subprocess
import sys
import os

# 1. Define the x range for the plot
x = np.linspace(-2.5, 1.5, 400)

# 2. Define the equations
# Curve 1: y = x^2
y1 = x**2

# Curve 2: y = -x^2 - 2x - 1
y2 = -x**2 - 2*x - 1

# Common Chord (Radical Axis): 2x + 2y + 1 = 0 => y = -x - 0.5
y_chord = -x - 0.5

# 3. Create the plot
plt.figure(figsize=(8, 8))
plt.plot(x, y1, label=r'\(C_1: y = x^2\)', color='blue', linewidth=2)
plt.plot(x, y2, label=r'\(C_2: y = -x^2 - 2x - 1\)', color='red', linewidth=2)
plt.plot(x, y_chord, label=r'Common Chord: \(2x + 2y + 1 = 0\)', 
         color='green', linestyle='--', linewidth=2)

# 4. Formatting the graph
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-2.5, 1.5)
plt.ylim(-2.5, 3.5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.title("Intersection of Two Parabolas\n(No Real Intersection - Answer: 0 points)", fontsize=14, fontweight='bold')
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.legend(fontsize=11, loc='upper right')

# Add text to show the complex roots
plt.text(-2.3, 2.8, "Complex Intersection Points:\n\(x = \\frac{-1 \\pm i}{2}\)", 
         fontsize=12, bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))

# 5. Save the graph as a PDF
pdf_filename = "Conics_Intersection_Graph.pdf"
plt.savefig(pdf_filename, format='pdf', bbox_inches='tight')
print(f"✅ Graph saved successfully as: {pdf_filename}")

# 6. Use subprocess to open the PDF automatically based on the Operating System
def open_pdf(filepath):
    if sys.platform.startswith('darwin'):  # macOS
        subprocess.call(('open', filepath))
    elif os.name == 'nt':  # Windows
        os.startfile(filepath)
    elif os.name == 'posix':  # Linux (Ubuntu, etc.)
        subprocess.call(('xdg-open', filepath))

# Open the PDF
open_pdf(pdf_filename)
print("Opening the PDF...")
