"""
Conjugate, Magnitude, and Argument of Complex Numbers
Python script demonstrating these essential properties
"""

import numpy as np
import matplotlib.pyplot as plt

def demonstrate_conjugate():
    """Demonstrate complex conjugate"""
    print("=" * 60)
    print("COMPLEX CONJUGATE: z* = a − bi")
    print("=" * 60)
    
    z = 3 + 4j
    z_conj = np.conj(z)
    
    print(f"\nOriginal: z = {z}")
    print(f"Conjugate: z* = {z_conj}")
    
    print(f"\nProperties:")
    print(f"1. (z*)* = z: {np.conj(z_conj)} = {z} ✓")
    print(f"2. z + z* = {z + z_conj} (real number)")
    print(f"3. z − z* = {z - z_conj} (imaginary number)")
    print(f"4. zz* = {z * z_conj} (magnitude squared)")
    
    examples = [2-5j, -1+3j, 4-2j, -3-6j]
    print(f"\nMore examples:")
    for ex in examples:
        print(f"  z = {ex:>10} → z* = {np.conj(ex):>10}")

def demonstrate_magnitude():
    """Demonstrate magnitude calculation"""
    print("\n" + "=" * 60)
    print("MAGNITUDE: |z| = √(a² + b²)")
    print("=" * 60)
    
    z = 3 + 4j
    magnitude = np.abs(z)
    
    print(f"\nz = {z}")
    print(f"|z| = √({z.real}² + {z.imag}²)")
    print(f"|z| = √({z.real**2} + {z.imag**2})")
    print(f"|z| = √{z.real**2 + z.imag**2}")
    print(f"|z| = {magnitude}")
    
    mag_squared = (z * np.conj(z)).real
    print(f"\nVerification using zz*:")
    print(f"zz* = {z} × {np.conj(z)} = {z * np.conj(z)}")
    print(f"|z|² = {mag_squared}")
    print(f"|z| = √{mag_squared} = {np.sqrt(mag_squared)} ✓")
    
    z1, z2 = 2+3j, 1-1j
    print(f"\nProperties:")
    print(f"z₁ = {z1}, z₂ = {z2}")
    print(f"|z₁z₂| = |z₁||z₂|: {np.abs(z1*z2):.3f} = {np.abs(z1):.3f} × {np.abs(z2):.3f} = {np.abs(z1)*np.abs(z2):.3f} ✓")
    print(f"|z₁/z₂| = |z₁|/|z₂|: {np.abs(z1/z2):.3f} = {np.abs(z1):.3f} / {np.abs(z2):.3f} = {np.abs(z1)/np.abs(z2):.3f} ✓")

def demonstrate_argument():
    """Demonstrate argument calculation"""
    print("\n" + "=" * 60)
    print("ARGUMENT: θ = arctan(b/a)")
    print("=" * 60)
    
    z = 3 + 4j
    argument_rad = np.angle(z)
    argument_deg = np.degrees(argument_rad)
    
    print(f"\nz = {z}")
    print(f"θ = arctan({z.imag}/{z.real})")
    print(f"θ = arctan({z.imag/z.real:.3f})")
    print(f"θ = {argument_rad:.3f} radians")
    print(f"θ = {argument_deg:.1f}°")
    
    print(f"\nArguments in different quadrants:")
    quadrants = [
        (3+4j, "Quadrant I"),
        (-3+4j, "Quadrant II"),
        (-3-4j, "Quadrant III"),
        (3-4j, "Quadrant IV")
    ]
    
    for z_quad, name in quadrants:
        arg_rad = np.angle(z_quad)
        arg_deg = np.degrees(arg_rad)
        print(f"  {name}: z = {z_quad:>10} → θ = {arg_rad:>7.3f} rad ({arg_deg:>7.1f}°)")
    
    z1, z2 = 2+3j, 1-1j
    arg_product = np.angle(z1 * z2)
    arg_sum = np.angle(z1) + np.angle(z2)
    print(f"\nProperty: arg(z₁z₂) = arg(z₁) + arg(z₂)")
    print(f"arg({z1} × {z2}) = {arg_product:.3f}")
    print(f"arg({z1}) + arg({z2}) = {np.angle(z1):.3f} + {np.angle(z2):.3f} = {arg_sum:.3f} ✓")

def polar_form():
    """Demonstrate polar form representation"""
    print("\n" + "=" * 60)
    print("POLAR FORM: z = |z|e^(iθ) = |z|(cos θ + i sin θ)")
    print("=" * 60)
    
    z = 3 + 4j
    r = np.abs(z)
    theta = np.angle(z)
    
    print(f"\nCartesian form: z = {z}")
    print(f"Magnitude: |z| = {r}")
    print(f"Argument: θ = {theta:.3f} rad")
    print(f"\nPolar form: z = {r}e^(i{theta:.3f})")
    print(f"Exponential: z = {r}(cos {theta:.3f} + i sin {theta:.3f})")
    
    z_reconstructed = r * np.exp(1j * theta)
    print(f"\nVerification:")
    print(f"z = {r} × e^(i{theta:.3f})")
    print(f"z = {r} × (cos {theta:.3f} + i sin {theta:.3f})")
    print(f"z = {r} × ({np.cos(theta):.3f} + i{np.sin(theta):.3f})")
    print(f"z = {z_reconstructed}")
    print(f"Matches original: {np.allclose(z, z_reconstructed)} ✓")

def quantum_applications():
    """Demonstrate quantum computing applications"""
    print("\n" + "=" * 60)
    print("QUANTUM COMPUTING APPLICATIONS")
    print("=" * 60)
    
    print("\n1. PROBABILITY CALCULATION")
    print("-" * 40)
    alpha = (3 + 4j) / 5
    prob = np.abs(alpha)**2
    print(f"Amplitude: α = {alpha}")
    print(f"Probability: P = |α|² = {prob:.3f}")
    print(f"Verification: αα* = {alpha * np.conj(alpha):.3f} ✓")
    
    print("\n2. NORMALIZED QUANTUM STATE")
    print("-" * 40)
    alpha = (3 + 4j) / 5
    beta = 0j
    total_prob = np.abs(alpha)**2 + np.abs(beta)**2
    print(f"|ψ⟩ = α|0⟩ + β|1⟩")
    print(f"α = {alpha}, β = {beta}")
    print(f"|α|² + |β|² = {np.abs(alpha)**2:.3f} + {np.abs(beta)**2:.3f} = {total_prob:.3f}")
    print(f"Normalized: {np.allclose(total_prob, 1)} ✓")
    
    print("\n3. PHASE IN QUANTUM STATES")
    print("-" * 40)
    r = 1/np.sqrt(2)
    theta = np.pi/4
    psi = r * np.exp(1j * theta)
    print(f"|ψ⟩ = {r:.3f}e^(i{theta:.3f})|0⟩")
    print(f"Magnitude: |ψ| = {np.abs(psi):.3f}")
    print(f"Phase: θ = {np.angle(psi):.3f} rad = {np.degrees(np.angle(psi)):.1f}°")
    
    print("\n4. INNER PRODUCT")
    print("-" * 40)
    psi = (1 + 2j) / np.sqrt(5)
    phi = (2 - 1j) / np.sqrt(5)
    inner_product = np.conj(psi) * phi
    print(f"|ψ⟩ = {psi}")
    print(f"|φ⟩ = {phi}")
    print(f"⟨ψ|φ⟩ = ψ*φ = {np.conj(psi)} × {phi} = {inner_product}")
    print(f"|⟨ψ|φ⟩| = {np.abs(inner_product):.3f}")

def visualize():
    """Create comprehensive visualizations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig = plt.figure(figsize=(16, 12))
    
    ax1 = plt.subplot(2, 3, 1)
    z = 3 + 4j
    z_conj = np.conj(z)
    
    ax1.arrow(0, 0, z.real, z.imag, head_width=0.3, head_length=0.3,
              fc='blue', ec='blue', linewidth=2, label='z')
    ax1.arrow(0, 0, z_conj.real, z_conj.imag, head_width=0.3, head_length=0.3,
              fc='red', ec='red', linewidth=2, label='z*', linestyle='--')
    
    ax1.axhline(y=0, color='gray', linewidth=1, linestyle='-', alpha=0.5)
    ax1.plot([z.real, z_conj.real], [z.imag, z_conj.imag], 'g--', alpha=0.3)
    
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Real', fontsize=12)
    ax1.set_ylabel('Imaginary', fontsize=12)
    ax1.set_title('Complex Conjugate\nReflection across real axis', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.set_aspect('equal')
    
    ax2 = plt.subplot(2, 3, 2)
    z = 3 + 4j
    r = np.abs(z)
    
    theta_circle = np.linspace(0, 2*np.pi, 100)
    ax2.plot(r * np.cos(theta_circle), r * np.sin(theta_circle), 'y-', linewidth=2, label=f'|z| = {r}')
    
    ax2.arrow(0, 0, z.real, z.imag, head_width=0.3, head_length=0.3,
              fc='blue', ec='blue', linewidth=2, label='z')
    
    ax2.plot([0, z.real], [0, z.imag], 'r--', linewidth=2, label='magnitude')
    
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=0, color='k', linewidth=0.5)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Real', fontsize=12)
    ax2.set_ylabel('Imaginary', fontsize=12)
    ax2.set_title('Magnitude\nDistance from origin', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.set_aspect('equal')
    
    ax3 = plt.subplot(2, 3, 3)
    z = 3 + 4j
    theta = np.angle(z)
    
    ax3.arrow(0, 0, z.real, z.imag, head_width=0.3, head_length=0.3,
              fc='blue', ec='blue', linewidth=2, label='z')
    
    arc_theta = np.linspace(0, theta, 50)
    arc_r = 1.5
    ax3.plot(arc_r * np.cos(arc_theta), arc_r * np.sin(arc_theta), 'r-', linewidth=2)
    ax3.text(arc_r * np.cos(theta/2) + 0.3, arc_r * np.sin(theta/2), f'θ = {theta:.2f}', fontsize=12)
    
    ax3.axhline(y=0, color='k', linewidth=0.5)
    ax3.axvline(x=0, color='k', linewidth=0.5)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlabel('Real', fontsize=12)
    ax3.set_ylabel('Imaginary', fontsize=12)
    ax3.set_title('Argument (Phase)\nAngle from real axis', fontsize=14, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.set_aspect('equal')
    
    ax4 = plt.subplot(2, 3, 4)
    quadrants = [3+4j, -3+4j, -3-4j, 3-4j]
    colors = ['blue', 'green', 'red', 'orange']
    labels = ['Q I', 'Q II', 'Q III', 'Q IV']
    
    for z_quad, color, label in zip(quadrants, colors, labels):
        ax4.arrow(0, 0, z_quad.real, z_quad.imag, head_width=0.3, head_length=0.3,
                  fc=color, ec=color, linewidth=2, label=label, alpha=0.7)
        theta = np.angle(z_quad)
        ax4.text(z_quad.real + 0.5, z_quad.imag + 0.5, f'{np.degrees(theta):.1f}°', fontsize=10)
    
    ax4.axhline(y=0, color='k', linewidth=1)
    ax4.axvline(x=0, color='k', linewidth=1)
    ax4.grid(True, alpha=0.3)
    ax4.set_xlabel('Real', fontsize=12)
    ax4.set_ylabel('Imaginary', fontsize=12)
    ax4.set_title('Arguments in All Quadrants', fontsize=14, fontweight='bold')
    ax4.legend(fontsize=10)
    ax4.set_aspect('equal')
    
    ax5 = plt.subplot(2, 3, 5)
    alphas = [(3+4j)/5, (1+0j)/np.sqrt(2), (0+1j)/np.sqrt(2), (1+1j)/2]
    labels_q = ['(3+4i)/5', '1/√2', 'i/√2', '(1+i)/2']
    
    for i, (alpha, label) in enumerate(zip(alphas, labels_q)):
        prob = np.abs(alpha)**2
        ax5.bar(i, prob, color='blue', alpha=0.7, label=label if i == 0 else '')
        ax5.text(i, prob + 0.02, f'{prob:.3f}', ha='center', fontsize=10)
        
        ax5_inset = fig.add_axes([0.12 + i*0.18, 0.15, 0.08, 0.08])
        ax5_inset.arrow(0, 0, alpha.real, alpha.imag, head_width=0.05, head_length=0.05,
                        fc='blue', ec='blue', linewidth=1)
        ax5_inset.set_xlim(-0.8, 0.8)
        ax5_inset.set_ylim(-0.8, 0.8)
        ax5_inset.axhline(y=0, color='k', linewidth=0.5)
        ax5_inset.axvline(x=0, color='k', linewidth=0.5)
        ax5_inset.set_xticks([])
        ax5_inset.set_yticks([])
    
    ax5.set_xlabel('Amplitude', fontsize=12)
    ax5.set_ylabel('Probability |α|²', fontsize=12)
    ax5.set_title('Quantum Probabilities\nP = |α|² = αα*', fontsize=14, fontweight='bold')
    ax5.set_xticks(range(len(alphas)))
    ax5.set_xticklabels(labels_q)
    ax5.grid(True, alpha=0.3, axis='y')
    
    ax6 = plt.subplot(2, 3, 6, projection='polar')
    examples = [3+4j, 2-3j, -1+2j, -2-1j]
    colors_polar = ['blue', 'red', 'green', 'orange']
    
    for z_ex, color in zip(examples, colors_polar):
        r = np.abs(z_ex)
        theta = np.angle(z_ex)
        ax6.plot([0, theta], [0, r], 'o-', color=color, linewidth=2, markersize=8,
                 label=f'r={r:.2f}, θ={np.degrees(theta):.0f}°')
    
    ax6.set_title('Polar Form Representation', fontsize=14, fontweight='bold', pad=20)
    ax6.legend(fontsize=9, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('conjugate_magnitude_argument.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'conjugate_magnitude_argument.png'")
    plt.close()

def main():
    print("\n" + "🔄" * 30)
    print("CONJUGATE, MAGNITUDE, AND ARGUMENT")
    print("🔄" * 30)
    
    demonstrate_conjugate()
    demonstrate_magnitude()
    demonstrate_argument()
    polar_form()
    quantum_applications()
    visualize()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Conjugate z* reflects z across the real axis")
    print("2. Magnitude |z| is the distance from origin")
    print("3. Argument θ is the angle from the real axis")
    print("4. zz* = |z|² connects conjugate and magnitude")
    print("5. Polar form: z = |z|e^(iθ)")
    print("6. Quantum probability: P = |α|² = αα*")
    print("7. Phase determines quantum interference")
    print("=" * 60)

if __name__ == "__main__":
    main()
