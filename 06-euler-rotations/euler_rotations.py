"""
Euler's Formula and Rotations
Python script demonstrating the most beautiful equation in mathematics
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def demonstrate_euler_formula():
    """Demonstrate Euler's formula"""
    print("=" * 60)
    print("EULER'S FORMULA: e^(iθ) = cos θ + i sin θ")
    print("=" * 60)
    
    angles = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    angle_names = ["0", "π/6", "π/4", "π/3", "π/2", "π", "3π/2", "2π"]
    
    print("\nVerification for various angles:")
    print("-" * 60)
    for theta, name in zip(angles, angle_names):
        euler = np.exp(1j * theta)
        trig = np.cos(theta) + 1j * np.sin(theta)
        print(f"θ = {name:>6} ({theta:6.3f} rad)")
        print(f"  e^(iθ)        = {euler:.4f}")
        print(f"  cos θ + i sin θ = {trig:.4f}")
        print(f"  Match: {np.allclose(euler, trig)} ✓\n")

def euler_identity():
    """Demonstrate Euler's identity"""
    print("=" * 60)
    print("EULER'S IDENTITY: e^(iπ) + 1 = 0")
    print("=" * 60)
    
    result = np.exp(1j * np.pi)
    print(f"\ne^(iπ) = {result}")
    print(f"e^(iπ) + 1 = {result + 1}")
    print(f"\nVerification:")
    print(f"  e^(iπ) = cos π + i sin π")
    print(f"        = {np.cos(np.pi):.10f} + i{np.sin(np.pi):.10f}")
    print(f"        ≈ -1 + 0i")
    print(f"  Therefore: e^(iπ) + 1 = 0 ✓")
    
    print(f"\nThis connects five fundamental constants:")
    print(f"  e  ≈ {np.e:.5f} (Euler's number)")
    print(f"  i  = √-1 (imaginary unit)")
    print(f"  π  ≈ {np.pi:.5f} (pi)")
    print(f"  1  (multiplicative identity)")
    print(f"  0  (additive identity)")

def demonstrate_rotations():
    """Demonstrate rotations using Euler's formula"""
    print("\n" + "=" * 60)
    print("ROTATIONS IN THE COMPLEX PLANE")
    print("=" * 60)
    
    z = 1 + 0j  # Start with 1
    angles = [np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    angle_names = ["90°", "180°", "270°", "360°"]
    
    print(f"\nStarting point: z = {z}")
    print("\nRotating by multiplying with e^(iθ):")
    print("-" * 60)
    
    for theta, name in zip(angles, angle_names):
        rotation = np.exp(1j * theta)
        z_rotated = z * rotation
        print(f"\nRotate by {name} (θ = {theta:.4f}):")
        print(f"  z' = z × e^(iθ)")
        print(f"  z' = {z} × {rotation:.4f}")
        print(f"  z' = {z_rotated:.4f}")

def rotate_complex_number():
    """Demonstrate rotating an arbitrary complex number"""
    print("\n" + "=" * 60)
    print("ROTATING ARBITRARY COMPLEX NUMBERS")
    print("=" * 60)
    
    z = 3 + 4j
    theta = np.pi / 3  # 60 degrees
    
    print(f"\nOriginal: z = {z}")
    print(f"Rotation angle: θ = {theta:.4f} rad = {np.degrees(theta):.1f}°")
    
    z_rotated = z * np.exp(1j * theta)
    print(f"\nMethod 1: Direct multiplication")
    print(f"  z' = z × e^(iθ)")
    print(f"  z' = {z} × e^(i{theta:.4f})")
    print(f"  z' = {z_rotated:.4f}")
    
    a, b = z.real, z.imag
    cos_theta, sin_theta = np.cos(theta), np.sin(theta)
    real_part = a * cos_theta - b * sin_theta
    imag_part = a * sin_theta + b * cos_theta
    z_rotated_formula = real_part + 1j * imag_part
    
    print(f"\nMethod 2: Using rotation formula")
    print(f"  z' = (a cos θ - b sin θ) + i(a sin θ + b cos θ)")
    print(f"  z' = ({a} × {cos_theta:.4f} - {b} × {sin_theta:.4f}) + i({a} × {sin_theta:.4f} + {b} × {cos_theta:.4f})")
    print(f"  z' = {real_part:.4f} + i{imag_part:.4f}")
    print(f"  z' = {z_rotated_formula:.4f}")
    
    print(f"\nVerification: Both methods match: {np.allclose(z_rotated, z_rotated_formula)} ✓")
    
    print(f"\nMagnitude preservation:")
    print(f"  |z|  = {np.abs(z):.4f}")
    print(f"  |z'| = {np.abs(z_rotated):.4f}")
    print(f"  Preserved: {np.allclose(np.abs(z), np.abs(z_rotated))} ✓")

def quantum_phase_gates():
    """Demonstrate quantum phase gates"""
    print("\n" + "=" * 60)
    print("QUANTUM PHASE GATES")
    print("=" * 60)
    
    print("\nPhase gates apply rotations to quantum states:")
    
    print("\n1. S GATE (Phase π/2):")
    print("   P(π/2) = [1  0]")
    print("            [0  i]")
    s_phase = np.exp(1j * np.pi/2)
    print(f"   e^(iπ/2) = {s_phase:.4f}")
    print(f"   Applies phase of 90° to |1⟩ state")
    
    print("\n2. T GATE (Phase π/4):")
    print("   P(π/4) = [1      0     ]")
    print("            [0  e^(iπ/4)]")
    t_phase = np.exp(1j * np.pi/4)
    print(f"   e^(iπ/4) = {t_phase:.4f}")
    print(f"   Applies phase of 45° to |1⟩ state")
    
    print("\n3. Z GATE (Phase π):")
    print("   P(π) = [1   0]")
    print("          [0  -1]")
    z_phase = np.exp(1j * np.pi)
    print(f"   e^(iπ) = {z_phase:.4f}")
    print(f"   Applies phase of 180° (flips sign) to |1⟩ state")
    
    print("\n4. EXAMPLE: Apply S gate to |+⟩ state")
    print("   |+⟩ = (|0⟩ + |1⟩)/√2")
    alpha = 1/np.sqrt(2)
    beta = 1/np.sqrt(2)
    print(f"   Before: α = {alpha:.4f}, β = {beta:.4f}")
    
    beta_after = beta * s_phase
    print(f"   After S gate: α = {alpha:.4f}, β = {beta_after:.4f}")
    print(f"   Result: |ψ⟩ = (|0⟩ + i|1⟩)/√2")

def quantum_fourier_transform():
    """Demonstrate roots of unity for QFT"""
    print("\n" + "=" * 60)
    print("QUANTUM FOURIER TRANSFORM - ROOTS OF UNITY")
    print("=" * 60)
    
    N = 8
    print(f"\n{N}-th roots of unity: ω_N = e^(2πi/N)")
    print(f"These are evenly spaced points on the unit circle:")
    print("-" * 60)
    
    for k in range(N):
        omega = np.exp(2j * np.pi * k / N)
        angle = 2 * np.pi * k / N
        print(f"ω_{N}^{k} = e^(2πi×{k}/{N}) = e^(i{angle:.4f}) = {omega:.4f}")
    
    print(f"\nProperty: (ω_N)^N = 1")
    omega_N = np.exp(2j * np.pi / N)
    result = omega_N ** N
    print(f"(ω_{N})^{N} = {result:.4f} ≈ 1 ✓")

def time_evolution():
    """Demonstrate quantum time evolution"""
    print("\n" + "=" * 60)
    print("QUANTUM TIME EVOLUTION")
    print("=" * 60)
    
    print("\nQuantum states evolve according to:")
    print("  |ψ(t)⟩ = e^(-iHt/ℏ)|ψ(0)⟩")
    print("\nFor a simple two-level system with energy E:")
    
    E = 1.0  # Energy in arbitrary units
    hbar = 1.0  # Set ℏ = 1 for simplicity
    times = [0, np.pi/(2*E), np.pi/E, 3*np.pi/(2*E), 2*np.pi/E]
    
    print(f"\nInitial state: |ψ(0)⟩ = |1⟩")
    print(f"Energy: E = {E}")
    print("-" * 60)
    
    for t in times:
        phase = -E * t / hbar
        evolution = np.exp(1j * phase)
        print(f"\nt = {t:.4f}:")
        print(f"  Phase: φ = -Et/ℏ = {phase:.4f}")
        print(f"  e^(iφ) = {evolution:.4f}")
        print(f"  |ψ(t)⟩ = {evolution:.4f}|1⟩")

def visualize():
    """Create comprehensive visualizations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig = plt.figure(figsize=(16, 12))
    
    ax1 = plt.subplot(2, 3, 1)
    theta_range = np.linspace(0, 2*np.pi, 100)
    x = np.cos(theta_range)
    y = np.sin(theta_range)
    
    ax1.plot(x, y, 'b-', linewidth=2, label='Unit circle')
    
    special_angles = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4]
    special_labels = ['0', 'π/4', 'π/2', '3π/4', 'π', '5π/4', '3π/2', '7π/4']
    
    for theta, label in zip(special_angles, special_labels):
        x_pt = np.cos(theta)
        y_pt = np.sin(theta)
        ax1.plot(x_pt, y_pt, 'ro', markersize=8)
        ax1.text(x_pt*1.2, y_pt*1.2, label, fontsize=10, ha='center', va='center')
        ax1.plot([0, x_pt], [0, y_pt], 'r--', alpha=0.3)
    
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Real (cos θ)', fontsize=12)
    ax1.set_ylabel('Imaginary (sin θ)', fontsize=12)
    ax1.set_title('Euler\'s Formula on Unit Circle\ne^(iθ) = cos θ + i sin θ', fontsize=14, fontweight='bold')
    ax1.set_aspect('equal')
    ax1.legend(fontsize=10)
    
    ax2 = plt.subplot(2, 3, 2)
    z = 2 + 1j
    angles_rot = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
    colors = ['blue', 'green', 'orange', 'red', 'purple']
    
    for i, (theta, color) in enumerate(zip(angles_rot, colors)):
        z_rot = z * np.exp(1j * theta)
        ax2.arrow(0, 0, z_rot.real, z_rot.imag, head_width=0.15, head_length=0.15,
                  fc=color, ec=color, linewidth=2, label=f'{np.degrees(theta):.0f}°')
    
    r = np.abs(z)
    circle_theta = np.linspace(0, np.pi, 50)
    ax2.plot(r * np.cos(circle_theta), r * np.sin(circle_theta), 'k--', alpha=0.3)
    
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=0, color='k', linewidth=0.5)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Real', fontsize=12)
    ax2.set_ylabel('Imaginary', fontsize=12)
    ax2.set_title('Rotation by Multiplication\nz\' = z × e^(iθ)', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.set_aspect('equal')
    
    ax3 = plt.subplot(2, 3, 3)
    theta_identity = np.linspace(0, np.pi, 100)
    x_identity = np.cos(theta_identity)
    y_identity = np.sin(theta_identity)
    
    ax3.plot(x_identity, y_identity, 'b-', linewidth=3, label='e^(iθ) path')
    ax3.plot([1, -1], [0, 0], 'ro-', markersize=12, linewidth=2, label='θ: 0 → π')
    ax3.arrow(0, 0, -1, 0, head_width=0.1, head_length=0.1, fc='red', ec='red', linewidth=3)
    
    ax3.text(1, -0.2, 'e^(i×0) = 1', fontsize=11, ha='center')
    ax3.text(-1, -0.2, 'e^(iπ) = -1', fontsize=11, ha='center')
    ax3.text(0, 0.15, 'e^(iπ) + 1 = 0', fontsize=13, ha='center', 
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    ax3.axhline(y=0, color='k', linewidth=0.5)
    ax3.axvline(x=0, color='k', linewidth=0.5)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlabel('Real', fontsize=12)
    ax3.set_ylabel('Imaginary', fontsize=12)
    ax3.set_title('Euler\'s Identity\nThe Most Beautiful Equation', fontsize=14, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.set_aspect('equal')
    
    ax4 = plt.subplot(2, 3, 4)
    phases = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
    phase_labels = ['0', 'π/4 (T)', 'π/2 (S)', '3π/4', 'π (Z)']
    
    for i, (phase, label) in enumerate(zip(phases, phase_labels)):
        gate_phase = np.exp(1j * phase)
        ax4.arrow(0, 0, gate_phase.real, gate_phase.imag, head_width=0.05, head_length=0.05,
                  fc=f'C{i}', ec=f'C{i}', linewidth=2)
        ax4.text(gate_phase.real*1.3, gate_phase.imag*1.3, label, fontsize=10, ha='center')
    
    circle = plt.Circle((0, 0), 1, fill=False, color='gray', linestyle='--', linewidth=1)
    ax4.add_patch(circle)
    
    ax4.axhline(y=0, color='k', linewidth=0.5)
    ax4.axvline(x=0, color='k', linewidth=0.5)
    ax4.grid(True, alpha=0.3)
    ax4.set_xlabel('Real', fontsize=12)
    ax4.set_ylabel('Imaginary', fontsize=12)
    ax4.set_title('Quantum Phase Gates\nP(θ) applies e^(iθ) to |1⟩', fontsize=14, fontweight='bold')
    ax4.set_aspect('equal')
    ax4.set_xlim(-1.5, 1.5)
    ax4.set_ylim(-1.5, 1.5)
    
    ax5 = plt.subplot(2, 3, 5)
    N = 8
    for k in range(N):
        omega = np.exp(2j * np.pi * k / N)
        ax5.plot(omega.real, omega.imag, 'o', markersize=12, label=f'ω^{k}')
        ax5.text(omega.real*1.2, omega.imag*1.2, f'{k}', fontsize=11, ha='center', va='center')
        ax5.plot([0, omega.real], [0, omega.imag], 'b--', alpha=0.3)
    
    circle = plt.Circle((0, 0), 1, fill=False, color='gray', linestyle='-', linewidth=2)
    ax5.add_patch(circle)
    
    ax5.axhline(y=0, color='k', linewidth=0.5)
    ax5.axvline(x=0, color='k', linewidth=0.5)
    ax5.grid(True, alpha=0.3)
    ax5.set_xlabel('Real', fontsize=12)
    ax5.set_ylabel('Imaginary', fontsize=12)
    ax5.set_title(f'{N}-th Roots of Unity\nUsed in Quantum Fourier Transform', fontsize=14, fontweight='bold')
    ax5.set_aspect('equal')
    
    ax6 = plt.subplot(2, 3, 6)
    times = np.linspace(0, 4*np.pi, 100)
    E = 1.0
    phases = -E * times
    
    ax6.plot(times, np.cos(phases), 'b-', linewidth=2, label='Real part')
    ax6.plot(times, np.sin(phases), 'r-', linewidth=2, label='Imaginary part')
    ax6.axhline(y=0, color='k', linewidth=0.5)
    ax6.grid(True, alpha=0.3)
    ax6.set_xlabel('Time t', fontsize=12)
    ax6.set_ylabel('Amplitude', fontsize=12)
    ax6.set_title('Quantum Time Evolution\n|ψ(t)⟩ = e^(-iEt/ℏ)|ψ(0)⟩', fontsize=14, fontweight='bold')
    ax6.legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig('euler_rotations.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'euler_rotations.png'")
    plt.close()

def main():
    print("\n" + "🔄" * 30)
    print("EULER'S FORMULA AND ROTATIONS")
    print("🔄" * 30)
    
    demonstrate_euler_formula()
    euler_identity()
    demonstrate_rotations()
    rotate_complex_number()
    quantum_phase_gates()
    quantum_fourier_transform()
    time_evolution()
    visualize()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Euler's formula: e^(iθ) = cos θ + i sin θ")
    print("2. Euler's identity: e^(iπ) + 1 = 0")
    print("3. Multiplication by e^(iθ) rotates by angle θ")
    print("4. Quantum phase gates use e^(iθ) for rotations")
    print("5. Roots of unity are crucial for QFT")
    print("6. Time evolution uses e^(-iHt/ℏ)")
    print("7. Rotations preserve magnitude, only change phase")
    print("=" * 60)

if __name__ == "__main__":
    main()
