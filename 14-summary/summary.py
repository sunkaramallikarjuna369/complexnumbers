"""
Summary: Complex Numbers in Quantum Computing
Python script providing comprehensive overview and quick reference
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def print_concept_summary():
    """Print summary of all 14 concepts"""
    print("=" * 80)
    print("COMPLEX NUMBERS IN QUANTUM COMPUTING - COMPLETE SUMMARY")
    print("=" * 80)
    
    concepts = [
        {
            'num': 1,
            'name': 'Introduction',
            'formula': 'z = a + bi',
            'application': 'Foundation of quantum mechanics',
            'complexity': '⭐'
        },
        {
            'num': 2,
            'name': 'Definition',
            'formula': 'i² = −1',
            'application': 'Imaginary unit in quantum states',
            'complexity': '⭐'
        },
        {
            'num': 3,
            'name': 'Complex Plane',
            'formula': 'z = (a, b)',
            'application': 'Geometric representation',
            'complexity': '⭐⭐'
        },
        {
            'num': 4,
            'name': 'Arithmetic',
            'formula': 'z₁ · z₂ = (ac−bd) + (ad+bc)i',
            'application': 'State manipulation',
            'complexity': '⭐⭐'
        },
        {
            'num': 5,
            'name': 'Conjugate & Magnitude',
            'formula': '|z| = √(a² + b²)',
            'application': 'Probability calculation',
            'complexity': '⭐⭐'
        },
        {
            'num': 6,
            'name': "Euler's Formula",
            'formula': 'e^(iθ) = cos θ + i sin θ',
            'application': 'Quantum rotations',
            'complexity': '⭐⭐⭐'
        },
        {
            'num': 7,
            'name': 'Quantum States',
            'formula': '|ψ⟩ = α|0⟩ + β|1⟩',
            'application': 'Qubit representation',
            'complexity': '⭐⭐⭐'
        },
        {
            'num': 8,
            'name': 'Python Operations',
            'formula': 'numpy.complex128',
            'application': 'Quantum simulation',
            'complexity': '⭐⭐'
        },
        {
            'num': 9,
            'name': 'Probability Amplitudes',
            'formula': 'P(x) = |α|²',
            'application': 'Measurement outcomes',
            'complexity': '⭐⭐⭐'
        },
        {
            'num': 10,
            'name': 'Inner Products',
            'formula': '⟨ψ|φ⟩ = Σ ψᵢ*φᵢ',
            'application': 'State overlap & fidelity',
            'complexity': '⭐⭐⭐⭐'
        },
        {
            'num': 11,
            'name': 'Quantum Gates',
            'formula': 'U†U = I',
            'application': 'Unitary transformations',
            'complexity': '⭐⭐⭐⭐'
        },
        {
            'num': 12,
            'name': 'Bloch Sphere',
            'formula': '|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩',
            'application': '3D state visualization',
            'complexity': '⭐⭐⭐⭐⭐'
        },
        {
            'num': 13,
            'name': 'Exercises',
            'formula': 'Practice problems',
            'application': 'Hands-on learning',
            'complexity': '⭐⭐⭐⭐'
        },
        {
            'num': 14,
            'name': 'Summary',
            'formula': 'Complete overview',
            'application': 'Quick reference',
            'complexity': '⭐⭐⭐'
        }
    ]
    
    print("\n{:<5} {:<25} {:<40} {:<30} {:<10}".format(
        "#", "Concept", "Key Formula", "Quantum Application", "Level"
    ))
    print("-" * 110)
    
    for concept in concepts:
        print("{:<5} {:<25} {:<40} {:<30} {:<10}".format(
            concept['num'],
            concept['name'],
            concept['formula'],
            concept['application'],
            concept['complexity']
        ))

def essential_formulas():
    """Display essential formulas"""
    print("\n" + "=" * 80)
    print("ESSENTIAL FORMULAS QUICK REFERENCE")
    print("=" * 80)
    
    formulas = {
        'Complex Basics': [
            ('Standard form', 'z = a + bi'),
            ('Imaginary unit', 'i² = −1'),
            ('Real part', 'Re(z) = a'),
            ('Imaginary part', 'Im(z) = b')
        ],
        'Operations': [
            ('Addition', '(a+bi) + (c+di) = (a+c) + (b+d)i'),
            ('Multiplication', '(a+bi)(c+di) = (ac−bd) + (ad+bc)i'),
            ('Conjugate', 'z* = a − bi'),
            ('Magnitude', '|z| = √(a² + b²)')
        ],
        'Polar Form': [
            ("Euler's formula", 'e^(iθ) = cos θ + i sin θ'),
            ('Polar form', 'z = re^(iθ)'),
            ('Argument', 'arg(z) = arctan(b/a)'),
            ('De Moivre', '(re^(iθ))ⁿ = rⁿe^(inθ)')
        ],
        'Quantum States': [
            ('Qubit state', '|ψ⟩ = α|0⟩ + β|1⟩'),
            ('Normalization', '|α|² + |β|² = 1'),
            ('Born rule', 'P(x) = |⟨x|ψ⟩|²'),
            ('Inner product', '⟨ψ|φ⟩ = Σ ψᵢ*φᵢ')
        ],
        'Quantum Gates': [
            ('Unitary', 'U†U = I'),
            ('Hadamard', 'H = (1/√2)[1 1; 1 −1]'),
            ('Pauli Y', 'Y = [0 −i; i 0]'),
            ('Phase gate', 'S = [1 0; 0 i]')
        ],
        'Bloch Sphere': [
            ('Parametrization', '|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩'),
            ('Cartesian', 'x = sin(θ)cos(φ), y = sin(θ)sin(φ), z = cos(θ)'),
            ('Probability', 'P(0) = cos²(θ/2), P(1) = sin²(θ/2)'),
            ('Phase', 'φ determines position on equator')
        ]
    }
    
    for category, items in formulas.items():
        print(f"\n{category}:")
        print("-" * 80)
        for name, formula in items:
            print(f"  {name:20s}: {formula}")

def why_complex_numbers():
    """Explain why complex numbers are essential"""
    print("\n" + "=" * 80)
    print("WHY COMPLEX NUMBERS IN QUANTUM COMPUTING?")
    print("=" * 80)
    
    print("\n1. SUPERPOSITION")
    print("   Complex amplitudes allow qubits to exist in multiple states:")
    print("   |ψ⟩ = α|0⟩ + β|1⟩ where α, β ∈ ℂ")
    print("   Without complex numbers: only 2 states (|0⟩ or |1⟩)")
    print("   With complex numbers: infinite states on Bloch sphere")
    
    print("\n2. PHASE INFORMATION")
    print("   Complex phases enable quantum interference:")
    print("   e^(iφ) = cos φ + i sin φ")
    print("   Phase differences create constructive/destructive interference")
    print("   Example: |+⟩ vs |i⟩ - same probabilities, different phases!")
    
    print("\n3. UNITARY EVOLUTION")
    print("   Quantum gates are complex unitary matrices:")
    print("   U†U = I (preserves probability)")
    print("   Example: Pauli Y = [0 −i; i 0] has imaginary entries")
    
    print("\n4. INNER PRODUCTS")
    print("   Complex conjugation is essential for proper inner products:")
    print("   ⟨ψ|φ⟩ = Σ ψᵢ*φᵢ")
    print("   Measures state overlap and fidelity")
    
    print("\n5. QUANTUM ALGORITHMS")
    print("   All quantum algorithms rely on complex numbers:")
    print("   - Shor's algorithm: Quantum Fourier Transform with phases")
    print("   - Grover's algorithm: Phase inversion for amplification")
    print("   - VQE: Complex variational parameters")

def demonstrate_examples():
    """Demonstrate key examples"""
    print("\n" + "=" * 80)
    print("KEY EXAMPLES")
    print("=" * 80)
    
    print("\nExample 1: Complex Arithmetic")
    z1 = 3 + 4j
    z2 = 1 - 2j
    print(f"z₁ = {z1}")
    print(f"z₂ = {z2}")
    print(f"z₁ + z₂ = {z1 + z2}")
    print(f"z₁ · z₂ = {z1 * z2}")
    print(f"|z₁| = {np.abs(z1):.4f}")
    
    print("\nExample 2: Euler's Formula")
    theta = np.pi / 4
    z = np.exp(1j * theta)
    print(f"e^(iπ/4) = {z}")
    print(f"         = {np.cos(theta):.4f} + {np.sin(theta):.4f}i")
    print(f"         = cos(π/4) + i·sin(π/4)")
    
    print("\nExample 3: Quantum State")
    alpha = 1 / np.sqrt(2)
    beta = 1j / np.sqrt(2)
    state = np.array([alpha, beta], dtype=complex)
    print(f"|ψ⟩ = {state}")
    print(f"    = (1/√2)|0⟩ + (i/√2)|1⟩")
    print(f"P(0) = |α|² = {np.abs(alpha)**2:.4f}")
    print(f"P(1) = |β|² = {np.abs(beta)**2:.4f}")
    
    print("\nExample 4: Quantum Gate (Hadamard)")
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    ket0 = np.array([1, 0], dtype=complex)
    result = H @ ket0
    print(f"H|0⟩ = {result}")
    print(f"     = (1/√2)(|0⟩ + |1⟩)")
    print(f"     = |+⟩")
    
    print("\nExample 5: Inner Product")
    psi = np.array([1, 1j], dtype=complex) / np.sqrt(2)
    phi = np.array([1, 1], dtype=complex) / np.sqrt(2)
    inner = np.vdot(psi, phi)
    print(f"|ψ⟩ = {psi}")
    print(f"|φ⟩ = {phi}")
    print(f"⟨ψ|φ⟩ = {inner}")
    print(f"|⟨ψ|φ⟩|² = {np.abs(inner)**2:.4f}")

def visualize_summary():
    """Create comprehensive summary visualization"""
    print("\n" + "=" * 80)
    print("CREATING SUMMARY VISUALIZATION")
    print("=" * 80)
    
    fig = plt.figure(figsize=(20, 12))
    
    ax1 = fig.add_subplot(2, 3, 1)
    
    concepts = ['Intro', 'Def', 'Plane', 'Arith', 'Conj', 'Euler', 
                'States', 'Python', 'Prob', 'Inner', 'Gates', 'Bloch']
    complexity = [1, 1, 2, 2, 2, 3, 3, 2, 3, 4, 4, 5]
    
    colors = ['green' if c <= 2 else 'yellow' if c <= 3 else 'red' for c in complexity]
    
    ax1.bar(range(len(concepts)), complexity, color=colors, alpha=0.7)
    ax1.set_xticks(range(len(concepts)))
    ax1.set_xticklabels(concepts, rotation=45, ha='right')
    ax1.set_ylabel('Complexity Level', fontsize=12)
    ax1.set_title('Concept Progression', fontsize=14, fontweight='bold')
    ax1.set_ylim(0, 6)
    ax1.grid(True, alpha=0.3, axis='y')
    
    ax2 = fig.add_subplot(2, 3, 2)
    
    numbers = [
        (1, 0, '1', 'blue'),
        (0, 1, 'i', 'red'),
        (1, 1, '1+i', 'green'),
        (-1, 0, '−1', 'orange'),
        (0, -1, '−i', 'purple'),
        (np.cos(np.pi/4), np.sin(np.pi/4), 'e^(iπ/4)', 'brown')
    ]
    
    for real, imag, label, color in numbers:
        ax2.arrow(0, 0, real, imag, head_width=0.1, head_length=0.1,
                 fc=color, ec=color, linewidth=2, alpha=0.7)
        ax2.text(real*1.2, imag*1.2, label, fontsize=10, ha='center')
    
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=0, color='k', linewidth=0.5)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Real', fontsize=12)
    ax2.set_ylabel('Imaginary', fontsize=12)
    ax2.set_title('Complex Plane', fontsize=14, fontweight='bold')
    ax2.set_aspect('equal')
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)
    
    ax3 = fig.add_subplot(2, 3, 3)
    
    states = ['|0⟩', '|1⟩', '|+⟩', '|−⟩', '|i⟩', '|−i⟩']
    state_vectors = [
        np.array([1, 0]),
        np.array([0, 1]),
        np.array([1, 1]) / np.sqrt(2),
        np.array([1, -1]) / np.sqrt(2),
        np.array([1, 1j]) / np.sqrt(2),
        np.array([1, -1j]) / np.sqrt(2)
    ]
    
    x = np.arange(len(states))
    prob0 = [np.abs(s[0])**2 for s in state_vectors]
    prob1 = [np.abs(s[1])**2 for s in state_vectors]
    
    width = 0.35
    ax3.bar(x - width/2, prob0, width, label='P(0)', alpha=0.8)
    ax3.bar(x + width/2, prob1, width, label='P(1)', alpha=0.8)
    
    ax3.set_xticks(x)
    ax3.set_xticklabels(states)
    ax3.set_ylabel('Probability', fontsize=12)
    ax3.set_title('Quantum State Probabilities', fontsize=14, fontweight='bold')
    ax3.legend()
    ax3.set_ylim(0, 1)
    ax3.grid(True, alpha=0.3, axis='y')
    
    ax4 = fig.add_subplot(2, 3, 4)
    
    gates = ['I', 'X', 'Y', 'Z', 'H', 'S', 'T']
    has_complex = [0, 0, 1, 0, 0, 1, 1]
    
    colors = ['blue' if c == 0 else 'red' for c in has_complex]
    
    ax4.bar(range(len(gates)), [1]*len(gates), color=colors, alpha=0.7)
    ax4.set_xticks(range(len(gates)))
    ax4.set_xticklabels(gates)
    ax4.set_ylabel('Gate Type', fontsize=12)
    ax4.set_title('Quantum Gates (Red = Complex Coefficients)', fontsize=14, fontweight='bold')
    ax4.set_ylim(0, 1.5)
    ax4.set_yticks([])
    
    ax5 = fig.add_subplot(2, 3, 5)
    
    categories = ['Basic', 'Polar', 'States', 'Gates', 'Bloch']
    formula_counts = [4, 4, 4, 4, 4]
    
    ax5.barh(range(len(categories)), formula_counts, color='purple', alpha=0.7)
    ax5.set_yticks(range(len(categories)))
    ax5.set_yticklabels(categories)
    ax5.set_xlabel('Number of Key Formulas', fontsize=12)
    ax5.set_title('Formula Categories', fontsize=14, fontweight='bold')
    ax5.grid(True, alpha=0.3, axis='x')
    
    ax6 = fig.add_subplot(2, 3, 6)
    
    levels = ['Beginner\n(1-5)', 'Intermediate\n(6-9)', 'Advanced\n(10-12)', 'Practice\n(13-14)']
    concepts_per_level = [5, 4, 3, 2]
    
    ax6.bar(range(len(levels)), concepts_per_level, color=['green', 'yellow', 'red', 'blue'], alpha=0.7)
    ax6.set_xticks(range(len(levels)))
    ax6.set_xticklabels(levels)
    ax6.set_ylabel('Number of Concepts', fontsize=12)
    ax6.set_title('Learning Path', fontsize=14, fontweight='bold')
    ax6.set_ylim(0, 6)
    ax6.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('summary.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'summary.png'")
    plt.close()

def main():
    print("\n" + "📚" * 40)
    print("SUMMARY: COMPLEX NUMBERS IN QUANTUM COMPUTING")
    print("📚" * 40)
    
    print_concept_summary()
    essential_formulas()
    why_complex_numbers()
    demonstrate_examples()
    visualize_summary()
    
    print("\n" + "=" * 80)
    print("FINAL THOUGHTS")
    print("=" * 80)
    print("\nComplex numbers are the LANGUAGE of quantum mechanics.")
    print("\nEvery quantum algorithm, every quantum gate, and every quantum state")
    print("relies on complex numbers to function correctly.")
    print("\nWithout complex numbers:")
    print("  ❌ No quantum superposition")
    print("  ❌ No quantum interference")
    print("  ❌ No quantum entanglement")
    print("  ❌ No quantum advantage")
    print("\nWith complex numbers:")
    print("  ✅ Full quantum state space")
    print("  ✅ Phase control and interference")
    print("  ✅ Unitary evolution")
    print("  ✅ Quantum computing power!")
    print("\n" + "=" * 80)
    print("Thank you for exploring complex numbers in quantum computing!")
    print("=" * 80)

if __name__ == "__main__":
    main()
