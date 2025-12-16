"""
Definition of Complex Numbers
Python script demonstrating the structure and properties
"""

import numpy as np
import matplotlib.pyplot as plt

def basic_definition():
    """Demonstrate basic definition"""
    print("=" * 60)
    print("DEFINITION: z = a + bi")
    print("=" * 60)
    
    z1 = 3 + 4j
    z2 = 1 - 2j
    
    print(f"\nz₁ = {z1}")
    print(f"  Real part: {z1.real}")
    print(f"  Imaginary part: {z1.imag}")
    
    print(f"\nz₂ = {z2}")
    print(f"  Real part: {z2.real}")
    print(f"  Imaginary part: {z2.imag}")

def imaginary_unit():
    """Demonstrate powers of i"""
    print("\n" + "=" * 60)
    print("POWERS OF i")
    print("=" * 60)
    
    i = 1j
    for n in range(9):
        print(f"i^{n} = {i**n}")

def visualize():
    """Create visualizations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATION")
    print("=" * 60)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    examples = [3+4j, 1-2j, -2+3j, 4-1j]
    
    for z in examples:
        ax.arrow(0, 0, z.real, z.imag, head_width=0.3, head_length=0.3,
                fc='blue', ec='blue', linewidth=2, alpha=0.7)
        ax.plot(z.real, z.imag, 'ro', markersize=10)
    
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Real', fontsize=12)
    ax.set_ylabel('Imaginary', fontsize=12)
    ax.set_title('Complex Numbers', fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    
    plt.savefig('complex_definition.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'complex_definition.png'")
    plt.close()

def main():
    print("\n" + "📐" * 30)
    print("DEFINITION OF COMPLEX NUMBERS")
    print("📐" * 30)
    
    basic_definition()
    imaginary_unit()
    visualize()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. z = a + bi where a, b ∈ ℝ")
    print("2. i² = -1")
    print("3. Real part: Re(z) = a")
    print("4. Imaginary part: Im(z) = b")
    print("=" * 60)

if __name__ == "__main__":
    main()
