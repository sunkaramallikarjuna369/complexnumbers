"""
Arithmetic Operations on Complex Numbers
Python script demonstrating addition, multiplication, and division
"""

import numpy as np
import matplotlib.pyplot as plt

def addition():
    """Demonstrate complex number addition"""
    print("=" * 60)
    print("ADDITION: z₁ + z₂ = (a₁ + a₂) + i(b₁ + b₂)")
    print("=" * 60)
    
    z1 = 3 + 4j
    z2 = 1 - 2j
    result = z1 + z2
    
    print(f"\nz₁ = {z1}")
    print(f"z₂ = {z2}")
    print(f"\nAddition:")
    print(f"  Real parts: {z1.real} + {z2.real} = {result.real}")
    print(f"  Imaginary parts: {z1.imag} + {z2.imag} = {result.imag}")
    print(f"\nResult: z₁ + z₂ = {result}")
    
    print(f"\nVerification: {z1} + {z2} = {result} ✓")

def multiplication():
    """Demonstrate complex number multiplication"""
    print("\n" + "=" * 60)
    print("MULTIPLICATION: z₁z₂ = (a₁a₂ − b₁b₂) + i(a₁b₂ + a₂b₁)")
    print("=" * 60)
    
    z1 = 3 + 4j
    z2 = 1 - 2j
    result = z1 * z2
    
    print(f"\nz₁ = {z1}")
    print(f"z₂ = {z2}")
    print(f"\nMultiplication (step by step):")
    print(f"  (3 + 4i)(1 − 2i)")
    print(f"  = 3(1) + 3(−2i) + 4i(1) + 4i(−2i)")
    print(f"  = 3 − 6i + 4i − 8i²")
    print(f"  = 3 − 2i + 8  (since i² = −1)")
    print(f"  = 11 − 2i")
    print(f"\nResult: z₁ × z₂ = {result}")
    
    r1, theta1 = np.abs(z1), np.angle(z1)
    r2, theta2 = np.abs(z2), np.angle(z2)
    r_result = r1 * r2
    theta_result = theta1 + theta2
    
    print(f"\nPolar form:")
    print(f"  z₁ = {r1:.3f}e^(i{theta1:.3f})")
    print(f"  z₂ = {r2:.3f}e^(i{theta2:.3f})")
    print(f"  z₁z₂ = {r_result:.3f}e^(i{theta_result:.3f})")
    print(f"  Multiply magnitudes: {r1:.3f} × {r2:.3f} = {r_result:.3f}")
    print(f"  Add arguments: {theta1:.3f} + {theta2:.3f} = {theta_result:.3f}")

def division():
    """Demonstrate complex number division"""
    print("\n" + "=" * 60)
    print("DIVISION: z₁/z₂ (multiply by conjugate)")
    print("=" * 60)
    
    z1 = 3 + 4j
    z2 = 1 - 2j
    result = z1 / z2
    
    print(f"\nz₁ = {z1}")
    print(f"z₂ = {z2}")
    print(f"\nDivision (step by step):")
    print(f"  (3 + 4i) / (1 − 2i)")
    print(f"  Multiply by conjugate (1 + 2i)/(1 + 2i):")
    print(f"  = (3 + 4i)(1 + 2i) / (1 − 2i)(1 + 2i)")
    print(f"  = (3 + 6i + 4i + 8i²) / (1 − 4i²)")
    print(f"  = (3 + 10i − 8) / (1 + 4)")
    print(f"  = (−5 + 10i) / 5")
    print(f"  = −1 + 2i")
    print(f"\nResult: z₁ / z₂ = {result}")
    
    r1, theta1 = np.abs(z1), np.angle(z1)
    r2, theta2 = np.abs(z2), np.angle(z2)
    r_result = r1 / r2
    theta_result = theta1 - theta2
    
    print(f"\nPolar form:")
    print(f"  z₁ = {r1:.3f}e^(i{theta1:.3f})")
    print(f"  z₂ = {r2:.3f}e^(i{theta2:.3f})")
    print(f"  z₁/z₂ = {r_result:.3f}e^(i{theta_result:.3f})")
    print(f"  Divide magnitudes: {r1:.3f} / {r2:.3f} = {r_result:.3f}")
    print(f"  Subtract arguments: {theta1:.3f} − {theta2:.3f} = {theta_result:.3f}")

def properties():
    """Demonstrate properties of complex arithmetic"""
    print("\n" + "=" * 60)
    print("PROPERTIES OF COMPLEX ARITHMETIC")
    print("=" * 60)
    
    z1, z2, z3 = 2+3j, 1-1j, 4+2j
    
    print("\nCommutative Property:")
    print(f"  z₁ + z₂ = {z1 + z2}")
    print(f"  z₂ + z₁ = {z2 + z1}")
    print(f"  Equal: {z1 + z2 == z2 + z1} ✓")
    
    print(f"\n  z₁ × z₂ = {z1 * z2}")
    print(f"  z₂ × z₁ = {z2 * z1}")
    print(f"  Equal: {z1 * z2 == z2 * z1} ✓")
    
    print("\nAssociative Property:")
    print(f"  (z₁ + z₂) + z₃ = {(z1 + z2) + z3}")
    print(f"  z₁ + (z₂ + z₃) = {z1 + (z2 + z3)}")
    print(f"  Equal: {np.allclose((z1 + z2) + z3, z1 + (z2 + z3))} ✓")
    
    print("\nDistributive Property:")
    print(f"  z₁(z₂ + z₃) = {z1 * (z2 + z3)}")
    print(f"  z₁z₂ + z₁z₃ = {z1*z2 + z1*z3}")
    print(f"  Equal: {np.allclose(z1 * (z2 + z3), z1*z2 + z1*z3)} ✓")

def visualize():
    """Create visualizations of arithmetic operations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    z1 = 3 + 4j
    z2 = 1 - 2j
    
    ax = axes[0, 0]
    result_add = z1 + z2
    
    ax.arrow(0, 0, z1.real, z1.imag, head_width=0.3, head_length=0.3,
             fc='blue', ec='blue', linewidth=2, label='z₁')
    ax.arrow(z1.real, z1.imag, z2.real, z2.imag, head_width=0.3, head_length=0.3,
             fc='red', ec='red', linewidth=2, label='z₂')
    ax.arrow(0, 0, result_add.real, result_add.imag, head_width=0.3, head_length=0.3,
             fc='yellow', ec='yellow', linewidth=3, label='z₁+z₂', linestyle='--')
    
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Real', fontsize=12)
    ax.set_ylabel('Imaginary', fontsize=12)
    ax.set_title('Addition: Vector Sum', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.set_aspect('equal')
    
    ax = axes[0, 1]
    result_mult = z1 * z2
    
    ax.arrow(0, 0, z1.real, z1.imag, head_width=0.5, head_length=0.5,
             fc='blue', ec='blue', linewidth=2, label='z₁')
    ax.arrow(0, 0, z2.real, z2.imag, head_width=0.5, head_length=0.5,
             fc='red', ec='red', linewidth=2, label='z₂')
    ax.arrow(0, 0, result_mult.real, result_mult.imag, head_width=0.5, head_length=0.5,
             fc='yellow', ec='yellow', linewidth=3, label='z₁×z₂')
    
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Real', fontsize=12)
    ax.set_ylabel('Imaginary', fontsize=12)
    ax.set_title('Multiplication: Scale & Rotate', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.set_aspect('equal')
    
    ax = axes[1, 0]
    result_div = z1 / z2
    
    ax.arrow(0, 0, z1.real, z1.imag, head_width=0.3, head_length=0.3,
             fc='blue', ec='blue', linewidth=2, label='z₁')
    ax.arrow(0, 0, z2.real, z2.imag, head_width=0.3, head_length=0.3,
             fc='red', ec='red', linewidth=2, label='z₂')
    ax.arrow(0, 0, result_div.real, result_div.imag, head_width=0.3, head_length=0.3,
             fc='yellow', ec='yellow', linewidth=3, label='z₁/z₂')
    
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Real', fontsize=12)
    ax.set_ylabel('Imaginary', fontsize=12)
    ax.set_title('Division', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.set_aspect('equal')
    
    ax = axes[1, 1]
    ax = plt.subplot(2, 2, 4, projection='polar')
    
    r1, theta1 = np.abs(z1), np.angle(z1)
    r2, theta2 = np.abs(z2), np.angle(z2)
    r_mult = r1 * r2
    theta_mult = theta1 + theta2
    
    ax.plot([0, theta1], [0, r1], 'b-o', linewidth=2, markersize=8, label='z₁')
    ax.plot([0, theta2], [0, r2], 'r-o', linewidth=2, markersize=8, label='z₂')
    ax.plot([0, theta_mult], [0, r_mult], 'y-o', linewidth=3, markersize=10, label='z₁×z₂')
    
    ax.set_title('Multiplication in Polar Form', fontsize=14, fontweight='bold', pad=20)
    ax.legend(fontsize=10, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('arithmetic_operations.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'arithmetic_operations.png'")
    plt.close()

def main():
    print("\n" + "➕" * 30)
    print("ARITHMETIC OPERATIONS ON COMPLEX NUMBERS")
    print("➕" * 30)
    
    addition()
    multiplication()
    division()
    properties()
    visualize()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Addition: Add real and imaginary parts separately")
    print("2. Multiplication: Use FOIL and i² = −1")
    print("3. Division: Multiply by conjugate of denominator")
    print("4. Polar form simplifies multiplication and division")
    print("5. All field properties hold for complex numbers")
    print("=" * 60)

if __name__ == "__main__":
    main()
