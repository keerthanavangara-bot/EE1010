import os
import platform
import subprocess
import numpy as np
import matplotlib.pyplot as plt

def main():
    # 1. Define the matrix A
    A = np.array([[9.0, 15.0], [15.0, 50.0]])

    # 2. Cholesky decomposition computed from scratch (A = L * L^T)
    l11 = np.sqrt(A[0, 0])
    l21 = A[1, 0] / l11
    l22 = np.sqrt(A[1, 1] - l21**2)
    
    L = np.array([[l11, 0.0], [l21, l22]])
    
    print("Matrix A:")
    print(A)
    print("\nLower Triangular Matrix L (computed manually):")
    print(L)
    print(f"Verified l22 value: {l22:.0f}")

    # 3. Create a summary visualization figure to save as PDF
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis('off')
    
    text_content = (
        f"Cholesky Decomposition Verification (GATE Q.27)\n\n"
        f"Original Matrix A:\n{A}\n\n"
        f"Lower Triangular Matrix L:\n{L}\n\n"
        f"Result: l22 = {l22:.0f}"
    )
    
    ax.text(0.1, 0.5, text_content, fontsize=12, family='monospace', 
            verticalalignment='center', bbox=dict(boxstyle='round,pad=1', facecolor='cyan', alpha=0.3))

    # Save to PDF in Downloads folder (or current directory fallback)
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    filepath = os.path.join(downloads_path if os.path.exists(downloads_path) else '.', 'cholesky_verification.pdf')
    
    fig.savefig(filepath, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"\nVerification summary saved to: {filepath}")

    
    system = platform.system()
    try:
        if system == 'Darwin':
            subprocess.run(['open', filepath])
        elif system == 'Windows':
            os.startfile(filepath)
        else:
            subprocess.run(['xdg-open', filepath])
    except Exception as e:
        print(f"PDF ready. Open manually if needed: {e}")

if __name__ == "__main__":
    main()

