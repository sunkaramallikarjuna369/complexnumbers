"""
Complex Plane Representation
Python script demonstrating Cartesian, Polar, and Exponential forms
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cartesian_form():
    """Demonstrate Cartesian form of complex numbers"""
    print("=" * 60)
    print("CARTESIAN FORM: z = a + bi")
    print("=" * 60)
    
    z = 1 + 1j
    print(f"\nComplex number: z = {z}")
    print(f"Real part (a): {z.real}")
    print(f"Imaginary part (b): {z.imag}")
    print(f"\nGeometric interpretation:")
    print(f"  Point in complex plane: ({z.real}, {z.imag})")
    print(f"  Vector from origin to ({z.real}, {z.imag})")

def polar_form():
    """Demonstrate Polar form of complex numbers"""
    print("\n" + "=" * 60)
    print("POLAR FORM: z = r(cos θ + i sin θ)")
    print("=" * 60)
    
    z = 1 + 1j
    r = np.abs(z)
    theta = np.angle(z)
    theta_deg = np.degrees(theta)
    
    print(f"\nComplex number: z = {z}")
    print(f"\nConversion to polar form:")
    print(f"  Magnitude (r) = √(a² + b²) = √({z.real}² + {z.imag}²) = {r:.4f}")
    print(f"  Argument (θ) = tan⁻¹(b/a) = tan⁻¹({z.imag}/{z.real}) = {theta:.4f} rad")
    print(f"  Argument (θ) = {theta_deg:.2f}°")
    
    print(f"\nPolar form: z = {r:.4f}(cos {theta_deg:.2f}° + i sin {theta_deg:.2f}°)")
    
    a_verify = r * np.cos(theta)
    b_verify = r * np.sin(theta)
    print(f"\nVerification (Polar → Cartesian):")
    print(f"  a = r cos θ = {r:.4f} × cos({theta_deg:.2f}°) = {a_verify:.4f}")
    print(f"  b = r sin θ = {r:.4f} × sin({theta_deg:.2f}°) = {b_verify:.4f}")
    print(f"  z = {a_verify:.4f} + {b_verify:.4f}i ✓")

def exponential_form():
    """Demonstrate Exponential form using Euler's formula"""
    print("\n" + "=" * 60)
    print("EXPONENTIAL FORM: z = re^(iθ)")
    print("=" * 60)
    
    z = 1 + 1j
    r = np.abs(z)
    theta = np.angle(z)
    
    print(f"\nComplex number: z = {z}")
    print(f"Magnitude: r = {r:.4f}")
    print(f"Argument: θ = {theta:.4f} rad")
    
    print(f"\nExponential form: z = {r:.4f}e^(i{theta:.4f})")
    
    z_euler = r * np.exp(1j * theta)
    print(f"\nVerification using Euler's formula:")
    print(f"  e^(iθ) = cos θ + i sin θ")
    print(f"  z = {r:.4f} × e^(i{theta:.4f})")
    print(f"  z = {z_euler}")
    print(f"  Matches original: {np.allclose(z, z_euler)} ✓")

def visualize_complex_plane():
    """Create comprehensive visualizations of the complex plane"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig = plt.figure(figsize=(16, 10))
    
    ax1 = fig.add_subplot(2, 3, 1)
    z = 1 + 1j
    
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.grid(True, alpha=0.3)
    
    ax1.arrow(0, 0, z.real, z.imag, head_width=0.15, head_length=0.15,
             fc='blue', ec='blue', linewidth=3, label='z = 1+i')
    ax1.plot([0, z.real], [0, 0], 'r--', linewidth=2, label='Real part')
    ax1.plot([z.real, z.real], [0, z.imag], 'g--', linewidth=2, label='Imaginary part')
    
    theta = np.angle(z)
    arc_theta = np.linspace(0, theta, 30)
    arc_r = 0.3
    ax1.plot(arc_r * np.cos(arc_theta), arc_r * np.sin(arc_theta), 'y-', linewidth=2)
    
    ax1.plot(z.real, z.imag, 'yo', markersize=12, markeredgecolor='black', markeredgewidth=2)
    ax1.set_xlabel('Real axis', fontsize=12)
    ax1.set_ylabel('Imaginary axis', fontsize=12)
    ax1.set_title('Cartesian Form', fontsize=14, fontweight='bold')
    ax1.set_xlim(-0.5, 2)
    ax1.set_ylim(-0.5, 2)
    ax1.set_aspect('equal')
    ax1.legend(fontsize=10)
    
    ax2 = fig.add_subplot(2, 3, 2, projection='polar')
    r = np.abs(z)
    theta = np.angle(z)
    ax2.plot([0, theta], [0, r], 'b-', linewidth=3, marker='o', markersize=10)
    ax2.set_title('Polar Form', fontsize=14, fontweight='bold', pad=20)
    ax2.grid(True)
    
    ax3 = fig.add_subplot(2, 3, 3)
    theta_circle = np.linspace(0, 2*np.pi, 100)
    ax3.plot(np.cos(theta_circle), np.sin(theta_circle), 'k-', linewidth=2)
    
    special_angles = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
    for angle in special_angles:
        z = np.exp(1j * angle)
        ax3.plot(z.real, z.imag, 'ro', markersize=10)
        ax3.arrow(0, 0, z.real*0.9, z.imag*0.9, head_width=0.05, head_length=0.05,
                 fc='blue', ec='blue', linewidth=1.5, alpha=0.5)
    
    ax3.axhline(y=0, color='k', linewidth=0.5)
    ax3.axvline(x=0, color='k', linewidth=0.5)
    ax3.grid(True, alpha=0.3)
    ax3.set_title('Unit Circle', fontsize=14, fontweight='bold')
    ax3.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig('complex_plane_visualization.png', dpi=150, bbox_inches='tight')
    print("\n✓ Visualization saved as 'complex_plane_visualization.png'")
    plt.close()

def main():
    """Run all demonstrations"""
    print("\n" + "🗺️" * 30)
    print("COMPLEX PLANE REPRESENTATION")
    print("🗺️" * 30)
    
    cartesian_form()
    polar_form()
    exponential_form()
    visualize_complex_plane()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Cartesian: z = a + bi")
    print("2. Polar: z = r(cos θ + i sin θ)")
    print("3. Exponential: z = re^(iθ)")
    print("4. All three forms represent the same complex number!")
    print("=" * 60)

if __name__ == "__main__":
    main()
