"""
Inner Products and Complex Conjugation
Python script demonstrating inner products in quantum computing
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

def inner_product_basics():
    """Demonstrate basic inner product calculations"""
    print("=" * 60)
    print("INNER PRODUCT BASICS")
    print("=" * 60)
    
    psi = np.array([1, 1j], dtype=complex)
    phi = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)
    
    print(f"\n|ψ⟩ = {psi}")
    print(f"|φ⟩ = {phi}")
    
    inner = np.vdot(psi, phi)  # vdot automatically conjugates first argument
    
    print(f"\n⟨ψ|φ⟩ = {inner:.4f}")
    print(f"|⟨ψ|φ⟩| = {np.abs(inner):.4f}")
    print(f"|⟨ψ|φ⟩|² = {np.abs(inner)**2:.4f}")
    
    print("\nManual calculation:")
    print(f"ψ₁* = {np.conj(psi[0])}")
    print(f"ψ₂* = {np.conj(psi[1])}")
    print(f"⟨ψ|φ⟩ = ψ₁*φ₁ + ψ₂*φ₂")
    print(f"      = {np.conj(psi[0])}·{phi[0]} + {np.conj(psi[1])}·{phi[1]}")
    print(f"      = {np.conj(psi[0])*phi[0]} + {np.conj(psi[1])*phi[1]}")
    print(f"      = {inner:.4f}")

def conjugate_symmetry():
    """Demonstrate conjugate symmetry property"""
    print("\n" + "=" * 60)
    print("CONJUGATE SYMMETRY: ⟨ψ|φ⟩ = ⟨φ|ψ⟩*")
    print("=" * 60)
    
    psi = np.array([1+2j, 3-1j], dtype=complex)
    phi = np.array([2+1j, 1+3j], dtype=complex)
    
    print(f"\n|ψ⟩ = {psi}")
    print(f"|φ⟩ = {phi}")
    
    inner_psi_phi = np.vdot(psi, phi)
    inner_phi_psi = np.vdot(phi, psi)
    
    print(f"\n⟨ψ|φ⟩ = {inner_psi_phi:.4f}")
    print(f"⟨φ|ψ⟩ = {inner_phi_psi:.4f}")
    print(f"⟨φ|ψ⟩* = {np.conj(inner_phi_psi):.4f}")
    
    print(f"\nVerification: ⟨ψ|φ⟩ = ⟨φ|ψ⟩* ? {np.allclose(inner_psi_phi, np.conj(inner_phi_psi))}")

def orthogonality():
    """Demonstrate orthogonal vectors"""
    print("\n" + "=" * 60)
    print("ORTHOGONALITY")
    print("=" * 60)
    
    print("\nComputational basis:")
    ket0 = np.array([1, 0], dtype=complex)
    ket1 = np.array([0, 1], dtype=complex)
    
    print(f"|0⟩ = {ket0}")
    print(f"|1⟩ = {ket1}")
    print(f"⟨0|1⟩ = {np.vdot(ket0, ket1):.4f}")
    print(f"⟨1|0⟩ = {np.vdot(ket1, ket0):.4f}")
    print("Orthogonal: ✓")
    
    print("\nHadamard basis:")
    ket_plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    ket_minus = np.array([1, -1], dtype=complex) / np.sqrt(2)
    
    print(f"|+⟩ = {ket_plus}")
    print(f"|−⟩ = {ket_minus}")
    print(f"⟨+|−⟩ = {np.vdot(ket_plus, ket_minus):.4f}")
    print(f"⟨−|+⟩ = {np.vdot(ket_minus, ket_plus):.4f}")
    print("Orthogonal: ✓")
    
    print("\nBell states:")
    bell_00 = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    bell_01 = np.array([1, 0, 0, -1], dtype=complex) / np.sqrt(2)
    
    print(f"|Φ⁺⟩ = {bell_00}")
    print(f"|Φ⁻⟩ = {bell_01}")
    print(f"⟨Φ⁺|Φ⁻⟩ = {np.vdot(bell_00, bell_01):.4f}")
    print("Orthogonal: ✓")

def orthonormal_basis():
    """Demonstrate orthonormal basis"""
    print("\n" + "=" * 60)
    print("ORTHONORMAL BASIS")
    print("=" * 60)
    
    basis = [
        np.array([1, 0], dtype=complex),
        np.array([0, 1], dtype=complex)
    ]
    
    print("\nComputational basis: {|0⟩, |1⟩}")
    
    print("\nOrthonormality check:")
    for i in range(len(basis)):
        for j in range(len(basis)):
            inner = np.vdot(basis[i], basis[j])
            expected = 1 if i == j else 0
            print(f"⟨{i}|{j}⟩ = {inner:.4f} (expected: {expected})")
    
    print("\nCompleteness relation: Σᵢ |i⟩⟨i| = I")
    identity = sum(np.outer(basis[i], np.conj(basis[i])) for i in range(len(basis)))
    print(f"\nΣᵢ |i⟩⟨i| =")
    print(identity)
    print(f"\nIs identity? {np.allclose(identity, np.eye(2))}")

def measurement_probabilities():
    """Demonstrate measurement probabilities using inner products"""
    print("\n" + "=" * 60)
    print("MEASUREMENT PROBABILITIES")
    print("=" * 60)
    
    psi = np.array([1, 1], dtype=complex) / np.sqrt(2)
    print(f"\n|ψ⟩ = |+⟩ = {psi}")
    
    ket0 = np.array([1, 0], dtype=complex)
    ket1 = np.array([0, 1], dtype=complex)
    
    prob0 = np.abs(np.vdot(ket0, psi))**2
    prob1 = np.abs(np.vdot(ket1, psi))**2
    
    print(f"\nMeasuring in computational basis:")
    print(f"P(0) = |⟨0|ψ⟩|² = {prob0:.4f}")
    print(f"P(1) = |⟨1|ψ⟩|² = {prob1:.4f}")
    print(f"Total probability: {prob0 + prob1:.4f}")
    
    ket_plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    ket_minus = np.array([1, -1], dtype=complex) / np.sqrt(2)
    
    prob_plus = np.abs(np.vdot(ket_plus, psi))**2
    prob_minus = np.abs(np.vdot(ket_minus, psi))**2
    
    print(f"\nMeasuring in Hadamard basis:")
    print(f"P(+) = |⟨+|ψ⟩|² = {prob_plus:.4f}")
    print(f"P(−) = |⟨−|ψ⟩|² = {prob_minus:.4f}")
    print(f"Total probability: {prob_plus + prob_minus:.4f}")

def state_overlap():
    """Demonstrate state overlap and fidelity"""
    print("\n" + "=" * 60)
    print("STATE OVERLAP AND FIDELITY")
    print("=" * 60)
    
    states = {
        '|0⟩': np.array([1, 0], dtype=complex),
        '|1⟩': np.array([0, 1], dtype=complex),
        '|+⟩': np.array([1, 1], dtype=complex) / np.sqrt(2),
        '|−⟩': np.array([1, -1], dtype=complex) / np.sqrt(2),
        '|i⟩': np.array([1, 1j], dtype=complex) / np.sqrt(2)
    }
    
    print("\nFidelity matrix F(ψ, φ) = |⟨ψ|φ⟩|²:")
    print("\n       ", end="")
    for name in states.keys():
        print(f"{name:>8}", end="")
    print()
    
    for name1, state1 in states.items():
        print(f"{name1:>8}", end="")
        for name2, state2 in states.items():
            fidelity = np.abs(np.vdot(state1, state2))**2
            print(f"{fidelity:>8.4f}", end="")
        print()
    
    print("\nInterpretation:")
    print("  1.0000: Identical states")
    print("  0.5000: Maximum overlap for orthogonal basis")
    print("  0.0000: Orthogonal states")

def expectation_values():
    """Demonstrate expectation values using inner products"""
    print("\n" + "=" * 60)
    print("EXPECTATION VALUES")
    print("=" * 60)
    
    psi = np.array([1, 1j], dtype=complex) / np.sqrt(2)
    print(f"\n|ψ⟩ = {psi}")
    
    pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
    pauli_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    pauli_z = np.array([[1, 0], [0, -1]], dtype=complex)
    
    exp_x = np.vdot(psi, pauli_x @ psi)
    exp_y = np.vdot(psi, pauli_y @ psi)
    exp_z = np.vdot(psi, pauli_z @ psi)
    
    print(f"\n⟨X⟩ = ⟨ψ|X|ψ⟩ = {exp_x:.4f}")
    print(f"⟨Y⟩ = ⟨ψ|Y|ψ⟩ = {exp_y:.4f}")
    print(f"⟨Z⟩ = ⟨ψ|Z|ψ⟩ = {exp_z:.4f}")
    
    print(f"\nAll expectation values are real:")
    print(f"  Im(⟨X⟩) = {np.imag(exp_x):.10f}")
    print(f"  Im(⟨Y⟩) = {np.imag(exp_y):.10f}")
    print(f"  Im(⟨Z⟩) = {np.imag(exp_z):.10f}")

def gram_schmidt():
    """Demonstrate Gram-Schmidt orthogonalization"""
    print("\n" + "=" * 60)
    print("GRAM-SCHMIDT ORTHOGONALIZATION")
    print("=" * 60)
    
    v1 = np.array([1, 1], dtype=complex)
    v2 = np.array([1, 2], dtype=complex)
    
    print(f"\nOriginal vectors:")
    print(f"v₁ = {v1}")
    print(f"v₂ = {v2}")
    print(f"⟨v₁|v₂⟩ = {np.vdot(v1, v2):.4f} (not orthogonal)")
    
    u1 = v1 / np.linalg.norm(v1)
    
    projection = np.vdot(u1, v2) * u1
    u2 = v2 - projection
    u2 = u2 / np.linalg.norm(u2)
    
    print(f"\nOrthonormalized vectors:")
    print(f"u₁ = {u1}")
    print(f"u₂ = {u2}")
    print(f"⟨u₁|u₂⟩ = {np.vdot(u1, u2):.4f} (orthogonal!)")
    print(f"⟨u₁|u₁⟩ = {np.vdot(u1, u1):.4f} (normalized!)")
    print(f"⟨u₂|u₂⟩ = {np.vdot(u2, u2):.4f} (normalized!)")

def visualize():
    """Create visualizations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig = plt.figure(figsize=(20, 12))
    
    ax1 = fig.add_subplot(2, 3, 1)
    psi = np.array([3, 4])
    phi = np.array([4, 2])
    
    ax1.arrow(0, 0, psi[0], psi[1], head_width=0.3, head_length=0.3,
             fc='blue', ec='blue', linewidth=2, label='|ψ⟩')
    ax1.arrow(0, 0, phi[0], phi[1], head_width=0.3, head_length=0.3,
             fc='red', ec='red', linewidth=2, label='|φ⟩')
    
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Real', fontsize=12)
    ax1.set_ylabel('Imaginary', fontsize=12)
    ax1.set_title('Inner Product Geometry', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.set_aspect('equal')
    ax1.set_xlim(-1, 5)
    ax1.set_ylim(-1, 5)
    
    ax2 = fig.add_subplot(2, 3, 2)
    basis = [np.array([1, 0]), np.array([0, 1])]
    colors = ['blue', 'red']
    labels = ['|0⟩', '|1⟩']
    
    for i, (vec, color, label) in enumerate(zip(basis, colors, labels)):
        ax2.arrow(0, 0, vec[0], vec[1], head_width=0.1, head_length=0.1,
                 fc=color, ec=color, linewidth=2, label=label)
    
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=0, color='k', linewidth=0.5)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Real', fontsize=12)
    ax2.set_ylabel('Imaginary', fontsize=12)
    ax2.set_title('Orthonormal Basis', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.set_aspect('equal')
    ax2.set_xlim(-0.5, 1.5)
    ax2.set_ylim(-0.5, 1.5)
    
    ax3 = fig.add_subplot(2, 3, 3)
    states = {
        '|0⟩': np.array([1, 0], dtype=complex),
        '|1⟩': np.array([0, 1], dtype=complex),
        '|+⟩': np.array([1, 1], dtype=complex) / np.sqrt(2),
        '|−⟩': np.array([1, -1], dtype=complex) / np.sqrt(2),
        '|i⟩': np.array([1, 1j], dtype=complex) / np.sqrt(2)
    }
    
    n = len(states)
    fidelity_matrix = np.zeros((n, n))
    state_list = list(states.values())
    
    for i in range(n):
        for j in range(n):
            fidelity_matrix[i, j] = np.abs(np.vdot(state_list[i], state_list[j]))**2
    
    im = ax3.imshow(fidelity_matrix, cmap='viridis', aspect='auto', vmin=0, vmax=1)
    ax3.set_xticks(range(n))
    ax3.set_yticks(range(n))
    ax3.set_xticklabels(states.keys())
    ax3.set_yticklabels(states.keys())
    ax3.set_title('Fidelity Matrix F(ψ,φ) = |⟨ψ|φ⟩|²', fontsize=14, fontweight='bold')
    plt.colorbar(im, ax=ax3)
    
    ax4 = fig.add_subplot(2, 3, 4)
    psi = np.array([1, 1], dtype=complex) / np.sqrt(2)
    
    basis_states = {
        'Computational': [np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex)],
        'Hadamard': [np.array([1, 1], dtype=complex)/np.sqrt(2), np.array([1, -1], dtype=complex)/np.sqrt(2)]
    }
    
    x = np.arange(len(basis_states))
    width = 0.35
    
    for i, (basis_name, basis) in enumerate(basis_states.items()):
        probs = [np.abs(np.vdot(b, psi))**2 for b in basis]
        ax4.bar(i, probs[0], width, label=f'{basis_name} |0⟩/|+⟩', alpha=0.8)
        ax4.bar(i + width, probs[1], width, label=f'{basis_name} |1⟩/|−⟩', alpha=0.8)
    
    ax4.set_ylabel('Probability', fontsize=12)
    ax4.set_title('Measurement Probabilities for |+⟩', fontsize=14, fontweight='bold')
    ax4.set_xticks([width/2, 1 + width/2])
    ax4.set_xticklabels(['Computational', 'Hadamard'])
    ax4.legend()
    ax4.grid(True, alpha=0.3, axis='y')
    
    ax5 = fig.add_subplot(2, 3, 5)
    v1 = np.array([1, 1])
    v2 = np.array([1, 2])
    
    u1 = v1 / np.linalg.norm(v1)
    projection = np.dot(u1, v2) * u1
    u2 = v2 - projection
    u2 = u2 / np.linalg.norm(u2)
    
    ax5.arrow(0, 0, v1[0], v1[1], head_width=0.1, head_length=0.1,
             fc='gray', ec='gray', linewidth=2, alpha=0.5, label='v₁ (original)')
    ax5.arrow(0, 0, v2[0], v2[1], head_width=0.1, head_length=0.1,
             fc='gray', ec='gray', linewidth=2, alpha=0.5, label='v₂ (original)')
    
    ax5.arrow(0, 0, u1[0], u1[1], head_width=0.1, head_length=0.1,
             fc='blue', ec='blue', linewidth=2, label='u₁ (orthonormal)')
    ax5.arrow(0, 0, u2[0], u2[1], head_width=0.1, head_length=0.1,
             fc='red', ec='red', linewidth=2, label='u₂ (orthonormal)')
    
    ax5.axhline(y=0, color='k', linewidth=0.5)
    ax5.axvline(x=0, color='k', linewidth=0.5)
    ax5.grid(True, alpha=0.3)
    ax5.set_xlabel('Component 1', fontsize=12)
    ax5.set_ylabel('Component 2', fontsize=12)
    ax5.set_title('Gram-Schmidt Orthogonalization', fontsize=14, fontweight='bold')
    ax5.legend()
    ax5.set_aspect('equal')
    
    ax6 = fig.add_subplot(2, 3, 6)
    
    angles = np.linspace(0, 2*np.pi, 100)
    exp_x = []
    exp_y = []
    exp_z = []
    
    pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
    pauli_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    pauli_z = np.array([[1, 0], [0, -1]], dtype=complex)
    
    for angle in angles:
        psi = np.array([np.cos(angle/2), np.exp(1j*angle)*np.sin(angle/2)], dtype=complex)
        exp_x.append(np.real(np.vdot(psi, pauli_x @ psi)))
        exp_y.append(np.real(np.vdot(psi, pauli_y @ psi)))
        exp_z.append(np.real(np.vdot(psi, pauli_z @ psi)))
    
    ax6.plot(angles, exp_x, label='⟨X⟩', linewidth=2)
    ax6.plot(angles, exp_y, label='⟨Y⟩', linewidth=2)
    ax6.plot(angles, exp_z, label='⟨Z⟩', linewidth=2)
    ax6.axhline(y=0, color='k', linewidth=0.5)
    ax6.grid(True, alpha=0.3)
    ax6.set_xlabel('State Parameter θ', fontsize=12)
    ax6.set_ylabel('Expectation Value', fontsize=12)
    ax6.set_title('Pauli Expectation Values', fontsize=14, fontweight='bold')
    ax6.legend()
    ax6.set_xlim(0, 2*np.pi)
    ax6.set_ylim(-1.2, 1.2)
    
    plt.tight_layout()
    plt.savefig('inner_products.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'inner_products.png'")
    plt.close()

def main():
    print("\n" + "⟨ψ|φ⟩" * 20)
    print("INNER PRODUCTS AND COMPLEX CONJUGATION")
    print("⟨ψ|φ⟩" * 20)
    
    inner_product_basics()
    conjugate_symmetry()
    orthogonality()
    orthonormal_basis()
    measurement_probabilities()
    state_overlap()
    expectation_values()
    gram_schmidt()
    visualize()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Inner product: ⟨ψ|φ⟩ = Σᵢ ψᵢ*φᵢ")
    print("2. Complex conjugation is essential for positive definiteness")
    print("3. Orthogonal states: ⟨ψ|φ⟩ = 0")
    print("4. Measurement probability: P = |⟨ψ|φ⟩|²")
    print("5. Expectation value: ⟨A⟩ = ⟨ψ|A|ψ⟩")
    print("6. Fidelity: F(ψ,φ) = |⟨ψ|φ⟩|²")
    print("=" * 60)

if __name__ == "__main__":
    main()
