"""
Exercises: Complex Numbers in Quantum Computing
Python script solving all exercises with visualizations
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def exercise_1():
    """Exercise 1: Complex Number Arithmetic"""
    print("=" * 60)
    print("EXERCISE 1: COMPLEX NUMBER ARITHMETIC")
    print("=" * 60)
    
    z1 = 3 + 4j
    z2 = 1 - 2j
    
    print(f"\nGiven:")
    print(f"z₁ = {z1}")
    print(f"z₂ = {z2}")
    
    add = z1 + z2
    print(f"\na) z₁ + z₂ = {add}")
    print(f"   Real part: {add.real}, Imaginary part: {add.imag}")
    
    sub = z1 - z2
    print(f"\nb) z₁ − z₂ = {sub}")
    print(f"   Real part: {sub.real}, Imaginary part: {sub.imag}")
    
    mul = z1 * z2
    print(f"\nc) z₁ · z₂ = {mul}")
    print(f"   Real part: {mul.real}, Imaginary part: {mul.imag}")
    
    div = z1 / z2
    print(f"\nd) z₁ / z₂ = {div}")
    print(f"   Real part: {div.real}, Imaginary part: {div.imag}")
    
    print(f"\nVerification: (z₁/z₂) · z₂ = {div * z2}")
    print(f"Should equal z₁ = {z1}")
    print(f"Match: {np.allclose(div * z2, z1)}")

def exercise_2():
    """Exercise 2: Magnitude and Phase"""
    print("\n" + "=" * 60)
    print("EXERCISE 2: MAGNITUDE AND PHASE")
    print("=" * 60)
    
    z = 1 + 1j * np.sqrt(3)
    
    print(f"\nGiven: z = 1 + i√3 = {z}")
    
    magnitude = np.abs(z)
    print(f"\na) Magnitude |z| = {magnitude}")
    print(f"   Calculation: √(1² + (√3)²) = √4 = 2")
    
    argument = np.angle(z)
    print(f"\nb) Argument arg(z) = {argument} radians")
    print(f"   = {np.degrees(argument)}°")
    print(f"   = π/3 radians")
    
    print(f"\nc) Polar form:")
    print(f"   z = r(cos θ + i sin θ)")
    print(f"   z = {magnitude}(cos({argument:.4f}) + i sin({argument:.4f}))")
    print(f"   z = 2(cos(π/3) + i sin(π/3))")
    
    print(f"\nd) Euler's formula:")
    print(f"   z = re^(iθ)")
    print(f"   z = {magnitude}e^(i{argument:.4f})")
    print(f"   z = 2e^(iπ/3)")
    
    z_polar = magnitude * np.exp(1j * argument)
    print(f"\nVerification: {z_polar}")
    print(f"Original: {z}")
    print(f"Match: {np.allclose(z, z_polar)}")

def exercise_3():
    """Exercise 3: Quantum State Representation"""
    print("\n" + "=" * 60)
    print("EXERCISE 3: QUANTUM STATE REPRESENTATION")
    print("=" * 60)
    
    alpha = 1 / np.sqrt(2)
    beta = 1j / np.sqrt(2)
    state = np.array([alpha, beta], dtype=complex)
    
    print(f"\nGiven: |ψ⟩ = (1/√2)|0⟩ + (i/√2)|1⟩")
    print(f"State vector: {state}")
    
    norm_squared = np.abs(alpha)**2 + np.abs(beta)**2
    print(f"\na) Normalization:")
    print(f"   ||ψ||² = |α|² + |β|²")
    print(f"   = |1/√2|² + |i/√2|²")
    print(f"   = {np.abs(alpha)**2} + {np.abs(beta)**2}")
    print(f"   = {norm_squared}")
    print(f"   Valid quantum state: {np.allclose(norm_squared, 1)}")
    
    prob0 = np.abs(alpha)**2
    print(f"\nb) P(0) = |α|² = {prob0}")
    print(f"   = 50%")
    
    prob1 = np.abs(beta)**2
    print(f"\nc) P(1) = |β|² = {prob1}")
    print(f"   = 50%")
    
    print(f"\n   Total probability: {prob0 + prob1}")
    
    theta = 2 * np.arccos(np.abs(alpha))
    phi = np.angle(beta / np.sin(theta / 2)) if np.abs(np.sin(theta / 2)) > 1e-10 else 0
    
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    
    print(f"\nd) Bloch sphere representation:")
    print(f"   θ = {theta} radians = π/2")
    print(f"   φ = {phi} radians = π/2")
    print(f"   Cartesian: ({x:.4f}, {y:.4f}, {z:.4f})")
    print(f"   This is the |i⟩ state on the equator!")

def exercise_4():
    """Exercise 4: Quantum Gate Application"""
    print("\n" + "=" * 60)
    print("EXERCISE 4: QUANTUM GATE APPLICATION")
    print("=" * 60)
    
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    S = np.array([[1, 0], [0, 1j]], dtype=complex)
    
    ket0 = np.array([1, 0], dtype=complex)
    
    print(f"\nInitial state: |0⟩ = {ket0}")
    
    state_h = H @ ket0
    print(f"\na) H|0⟩:")
    print(f"   H = (1/√2)[1  1]")
    print(f"              [1 −1]")
    print(f"   H|0⟩ = {state_h}")
    print(f"   = (1/√2)(|0⟩ + |1⟩) = |+⟩")
    
    state_sh = S @ state_h
    print(f"\nb) S(H|0⟩):")
    print(f"   S = [1  0]")
    print(f"       [0  i]")
    print(f"   S|+⟩ = {state_sh}")
    print(f"   = (1/√2)(|0⟩ + i|1⟩) = |i⟩")
    
    norm_squared = np.vdot(state_sh, state_sh).real
    print(f"\nc) Normalization:")
    print(f"   ||ψ||² = {norm_squared}")
    print(f"   Normalized: {np.allclose(norm_squared, 1)}")
    
    prob0 = np.abs(state_sh[0])**2
    prob1 = np.abs(state_sh[1])**2
    
    print(f"\nd) Measurement probabilities:")
    print(f"   P(0) = |α|² = {prob0} = 50%")
    print(f"   P(1) = |β|² = {prob1} = 50%")
    print(f"   Total: {prob0 + prob1}")
    
    print(f"\n   Note: Same probabilities as |+⟩, but different phase!")
    print(f"   |+⟩ = (1/√2)(|0⟩ + |1⟩)")
    print(f"   |i⟩ = (1/√2)(|0⟩ + i|1⟩)")

def exercise_5():
    """Exercise 5: Inner Product and Orthogonality"""
    print("\n" + "=" * 60)
    print("EXERCISE 5: INNER PRODUCT AND ORTHOGONALITY")
    print("=" * 60)
    
    psi_unnorm = np.array([3 + 4j, 1 - 2j], dtype=complex)
    phi_unnorm = np.array([1 + 1j, 2 - 1j], dtype=complex)
    
    print(f"\nGiven:")
    print(f"|ψ⟩ = (3+4i)|0⟩ + (1−2i)|1⟩ = {psi_unnorm}")
    print(f"|φ⟩ = (1+i)|0⟩ + (2−i)|1⟩ = {phi_unnorm}")
    
    norm_psi = np.linalg.norm(psi_unnorm)
    norm_phi = np.linalg.norm(phi_unnorm)
    
    psi = psi_unnorm / norm_psi
    phi = phi_unnorm / norm_phi
    
    print(f"\na) Normalization:")
    print(f"   ||ψ|| = √(|3+4i|² + |1−2i|²)")
    print(f"        = √({np.abs(psi_unnorm[0])**2} + {np.abs(psi_unnorm[1])**2})")
    print(f"        = √{norm_psi**2}")
    print(f"        = {norm_psi}")
    
    print(f"\n   ||φ|| = √(|1+i|² + |2−i|²)")
    print(f"        = √({np.abs(phi_unnorm[0])**2} + {np.abs(phi_unnorm[1])**2})")
    print(f"        = √{norm_phi**2}")
    print(f"        = {norm_phi}")
    
    print(f"\n   |ψ⟩ₙ = {psi}")
    print(f"   |φ⟩ₙ = {phi}")
    
    inner = np.vdot(psi, phi)
    print(f"\nb) Inner product ⟨ψ|φ⟩:")
    print(f"   ⟨ψ|φ⟩ = ψ₁*φ₁ + ψ₂*φ₂")
    print(f"   ψ₁* = {np.conj(psi[0])}")
    print(f"   φ₁ = {phi[0]}")
    print(f"   ψ₁*φ₁ = {np.conj(psi[0]) * phi[0]}")
    print(f"   ψ₂* = {np.conj(psi[1])}")
    print(f"   φ₂ = {phi[1]}")
    print(f"   ψ₂*φ₂ = {np.conj(psi[1]) * phi[1]}")
    print(f"   ⟨ψ|φ⟩ = {inner}")
    
    overlap = np.abs(inner)**2
    print(f"\nc) Overlap |⟨ψ|φ⟩|²:")
    print(f"   |⟨ψ|φ⟩|² = {overlap}")
    print(f"   = {overlap * 100:.2f}%")
    print(f"   This is the fidelity between the states!")
    
    print(f"\nd) Orthogonality:")
    print(f"   ⟨ψ|φ⟩ = {inner}")
    print(f"   |⟨ψ|φ⟩| = {np.abs(inner)}")
    
    if np.abs(inner) < 1e-10:
        print(f"   States are orthogonal!")
    else:
        print(f"   States are NOT orthogonal.")
        print(f"   They have {overlap * 100:.2f}% overlap.")

def visualize():
    """Create visualizations for all exercises"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig = plt.figure(figsize=(20, 12))
    
    ax1 = fig.add_subplot(2, 3, 1)
    z1 = 3 + 4j
    z2 = 1 - 2j
    
    ax1.arrow(0, 0, z1.real, z1.imag, head_width=0.3, head_length=0.3,
             fc='blue', ec='blue', linewidth=2, label='z₁')
    ax1.arrow(0, 0, z2.real, z2.imag, head_width=0.3, head_length=0.3,
             fc='red', ec='red', linewidth=2, label='z₂')
    ax1.arrow(0, 0, (z1+z2).real, (z1+z2).imag, head_width=0.3, head_length=0.3,
             fc='green', ec='green', linewidth=2, label='z₁+z₂')
    
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Real', fontsize=12)
    ax1.set_ylabel('Imaginary', fontsize=12)
    ax1.set_title('Exercise 1: Complex Arithmetic', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.set_aspect('equal')
    
    ax2 = fig.add_subplot(2, 3, 2, projection='polar')
    z = 1 + 1j * np.sqrt(3)
    r = np.abs(z)
    theta = np.angle(z)
    
    ax2.plot([0, theta], [0, r], 'b-', linewidth=3, marker='o', markersize=10)
    ax2.set_title('Exercise 2: Polar Form\nr=2, θ=π/3', fontsize=14, fontweight='bold', pad=20)
    
    ax3 = fig.add_subplot(2, 3, 3)
    alpha = 1 / np.sqrt(2)
    beta = 1j / np.sqrt(2)
    
    x = [0, 1]
    probs = [np.abs(alpha)**2, np.abs(beta)**2]
    
    ax3.bar(x, probs, color=['blue', 'red'], alpha=0.7)
    ax3.set_xticks(x)
    ax3.set_xticklabels(['|0⟩', '|1⟩'])
    ax3.set_ylabel('Probability', fontsize=12)
    ax3.set_title('Exercise 3: Measurement Probabilities', fontsize=14, fontweight='bold')
    ax3.set_ylim(0, 1)
    ax3.grid(True, alpha=0.3, axis='y')
    
    ax4 = fig.add_subplot(2, 3, 4)
    
    states = ['|0⟩', 'H|0⟩', 'SH|0⟩']
    ket0 = np.array([1, 0], dtype=complex)
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    S = np.array([[1, 0], [0, 1j]], dtype=complex)
    
    state_list = [ket0, H @ ket0, S @ H @ ket0]
    
    for i, (state, label) in enumerate(zip(state_list, states)):
        prob0 = np.abs(state[0])**2
        prob1 = np.abs(state[1])**2
        ax4.bar([i - 0.2, i + 0.2], [prob0, prob1], width=0.4, 
               color=['blue', 'red'], alpha=0.7)
    
    ax4.set_xticks(range(len(states)))
    ax4.set_xticklabels(states)
    ax4.set_ylabel('Probability', fontsize=12)
    ax4.set_title('Exercise 4: Gate Evolution', fontsize=14, fontweight='bold')
    ax4.set_ylim(0, 1)
    ax4.grid(True, alpha=0.3, axis='y')
    
    ax5 = fig.add_subplot(2, 3, 5)
    
    psi_unnorm = np.array([3 + 4j, 1 - 2j], dtype=complex)
    phi_unnorm = np.array([1 + 1j, 2 - 1j], dtype=complex)
    
    psi = psi_unnorm / np.linalg.norm(psi_unnorm)
    phi = phi_unnorm / np.linalg.norm(phi_unnorm)
    
    inner = np.vdot(psi, phi)
    overlap = np.abs(inner)**2
    
    ax5.bar(['Overlap', 'Orthogonal\nComponent'], [overlap, 1 - overlap],
           color=['green', 'gray'], alpha=0.7)
    ax5.set_ylabel('Magnitude', fontsize=12)
    ax5.set_title('Exercise 5: State Overlap', fontsize=14, fontweight='bold')
    ax5.set_ylim(0, 1)
    ax5.grid(True, alpha=0.3, axis='y')
    
    ax6 = fig.add_subplot(2, 3, 6)
    
    exercises = ['Ex 1\nArithmetic', 'Ex 2\nPolar', 'Ex 3\nState', 'Ex 4\nGates', 'Ex 5\nInner']
    complexity = [1, 2, 3, 4, 5]
    
    ax6.bar(range(len(exercises)), complexity, color='purple', alpha=0.7)
    ax6.set_xticks(range(len(exercises)))
    ax6.set_xticklabels(exercises)
    ax6.set_ylabel('Complexity Level', fontsize=12)
    ax6.set_title('Exercise Progression', fontsize=14, fontweight='bold')
    ax6.set_ylim(0, 6)
    ax6.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('exercises.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'exercises.png'")
    plt.close()

def main():
    print("\n" + "📝" * 30)
    print("EXERCISES: COMPLEX NUMBERS IN QUANTUM COMPUTING")
    print("📝" * 30)
    
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    visualize()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("All 5 exercises demonstrate the essential role of")
    print("complex numbers in quantum computing:")
    print("1. Complex arithmetic for state manipulation")
    print("2. Polar form for geometric insight")
    print("3. Complex amplitudes for probability and phase")
    print("4. Complex gates for phase control")
    print("5. Complex conjugation for inner products")
    print("=" * 60)

if __name__ == "__main__":
    main()
