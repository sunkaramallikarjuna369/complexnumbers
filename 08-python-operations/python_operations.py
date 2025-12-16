"""
Python Operations with Complex Numbers
Comprehensive guide to using Python and NumPy for quantum computing
"""

import numpy as np
import matplotlib.pyplot as plt

def basic_operations():
    """Demonstrate basic Python complex number operations"""
    print("=" * 60)
    print("BASIC PYTHON COMPLEX NUMBER OPERATIONS")
    print("=" * 60)
    
    z1 = 3 + 4j
    z2 = complex(1, -2)
    
    print(f"\nCreating complex numbers:")
    print(f"z1 = 3 + 4j = {z1}")
    print(f"z2 = complex(1, -2) = {z2}")
    
    print(f"\nArithmetic operations:")
    print(f"z1 + z2 = {z1 + z2}")
    print(f"z1 - z2 = {z1 - z2}")
    print(f"z1 * z2 = {z1 * z2}")
    print(f"z1 / z2 = {z1 / z2}")
    print(f"z1 ** 2 = {z1 ** 2}")
    
    print(f"\nProperties:")
    print(f"z1.real = {z1.real}")
    print(f"z1.imag = {z1.imag}")
    print(f"z1.conjugate() = {z1.conjugate()}")
    print(f"abs(z1) = {abs(z1)}")

def numpy_operations():
    """Demonstrate NumPy complex number operations"""
    print("\n" + "=" * 60)
    print("NUMPY COMPLEX NUMBER OPERATIONS")
    print("=" * 60)
    
    z_array = np.array([1+2j, 3+4j, 5+6j])
    print(f"\nComplex array:")
    print(f"z_array = {z_array}")
    
    print(f"\nNumPy functions:")
    print(f"np.conj(z_array) = {np.conj(z_array)}")
    print(f"np.abs(z_array) = {np.abs(z_array)}")
    print(f"np.angle(z_array) = {np.angle(z_array)}")
    
    print(f"\nElement-wise operations:")
    print(f"z_array ** 2 = {z_array ** 2}")
    print(f"np.exp(1j * np.pi/4) = {np.exp(1j * np.pi/4)}")
    
    print(f"\nAggregations:")
    print(f"np.sum(z_array) = {np.sum(z_array)}")
    print(f"np.prod(z_array) = {np.prod(z_array)}")

def quantum_states():
    """Demonstrate quantum state operations"""
    print("\n" + "=" * 60)
    print("QUANTUM STATE OPERATIONS")
    print("=" * 60)
    
    ket_0 = np.array([1, 0])
    ket_1 = np.array([0, 1])
    
    print(f"\nBasis states:")
    print(f"|0⟩ = {ket_0}")
    print(f"|1⟩ = {ket_1}")
    
    ket_plus = np.array([1, 1]) / np.sqrt(2)
    ket_minus = np.array([1, -1]) / np.sqrt(2)
    
    print(f"\nSuperposition states:")
    print(f"|+⟩ = {ket_plus}")
    print(f"|−⟩ = {ket_minus}")
    
    alpha = 3/5
    beta = 4j/5
    psi = np.array([alpha, beta])
    
    print(f"\nComplex superposition:")
    print(f"|ψ⟩ = {psi}")
    print(f"Normalization: |α|² + |β|² = {np.sum(np.abs(psi)**2):.4f}")
    
    probs = np.abs(psi)**2
    print(f"P(0) = {probs[0]:.4f}")
    print(f"P(1) = {probs[1]:.4f}")

def inner_products():
    """Demonstrate inner product calculations"""
    print("\n" + "=" * 60)
    print("INNER PRODUCTS")
    print("=" * 60)
    
    psi = np.array([1, 1j]) / np.sqrt(2)
    phi = np.array([1, -1j]) / np.sqrt(2)
    
    print(f"\n|ψ⟩ = {psi}")
    print(f"|φ⟩ = {phi}")
    
    inner1 = np.vdot(psi, phi)
    print(f"\nMethod 1 - np.vdot:")
    print(f"⟨ψ|φ⟩ = {inner1}")
    
    inner2 = np.sum(np.conj(psi) * phi)
    print(f"\nMethod 2 - manual:")
    print(f"⟨ψ|φ⟩ = {inner2}")
    
    overlap = np.abs(inner1)**2
    print(f"\nOverlap probability:")
    print(f"|⟨ψ|φ⟩|² = {overlap:.4f}")

def quantum_gates():
    """Demonstrate quantum gate operations"""
    print("\n" + "=" * 60)
    print("QUANTUM GATE OPERATIONS")
    print("=" * 60)
    
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.array([[1, 0], [0, -1]])
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    
    print("\nPauli gates:")
    print(f"X (NOT) gate:\n{X}")
    print(f"\nY gate:\n{Y}")
    print(f"\nZ gate:\n{Z}")
    print(f"\nHadamard gate:\n{H}")
    
    ket_0 = np.array([1, 0])
    
    print(f"\nApplying gates to |0⟩:")
    print(f"X|0⟩ = {X @ ket_0}")
    print(f"H|0⟩ = {H @ ket_0}")
    print(f"Z|0⟩ = {Z @ ket_0}")
    
    S = np.array([[1, 0], [0, 1j]])
    T = np.array([[1, 0], [0, np.exp(1j*np.pi/4)]])
    
    print(f"\nPhase gates:")
    print(f"S gate:\n{S}")
    print(f"T gate:\n{T}")
    
    H_dag = np.conj(H.T)
    is_unitary = np.allclose(H_dag @ H, np.eye(2))
    print(f"\nH is unitary: {is_unitary}")

def two_qubit_operations():
    """Demonstrate two-qubit operations"""
    print("\n" + "=" * 60)
    print("TWO-QUBIT OPERATIONS")
    print("=" * 60)
    
    ket_0 = np.array([1, 0])
    ket_1 = np.array([0, 1])
    
    ket_00 = np.kron(ket_0, ket_0)
    ket_01 = np.kron(ket_0, ket_1)
    ket_10 = np.kron(ket_1, ket_0)
    ket_11 = np.kron(ket_1, ket_1)
    
    print("\nComputational basis states:")
    print(f"|00⟩ = {ket_00}")
    print(f"|01⟩ = {ket_01}")
    print(f"|10⟩ = {ket_10}")
    print(f"|11⟩ = {ket_11}")
    
    CNOT = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]])
    
    print(f"\nCNOT gate:\n{CNOT}")
    
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    H_I = np.kron(H, np.eye(2))
    
    psi = ket_00
    psi = H_I @ psi
    psi = CNOT @ psi
    
    print(f"\nBell state |Φ+⟩:")
    print(f"{psi}")
    print(f"Probabilities: {np.abs(psi)**2}")

def time_evolution():
    """Demonstrate time evolution"""
    print("\n" + "=" * 60)
    print("TIME EVOLUTION")
    print("=" * 60)
    
    E0, E1 = 0, 1
    H = np.diag([E0, E1])
    
    print(f"\nHamiltonian:\n{H}")
    
    psi_0 = np.array([1, 1]) / np.sqrt(2)
    print(f"\nInitial state: {psi_0}")
    
    times = [0, np.pi/4, np.pi/2, np.pi]
    
    print(f"\nTime evolution:")
    for t in times:
        U = np.diag([np.exp(-1j*E0*t), np.exp(-1j*E1*t)])
        psi_t = U @ psi_0
        probs = np.abs(psi_t)**2
        print(f"t = {t:.4f}: |ψ(t)⟩ = {psi_t}, P(0) = {probs[0]:.4f}, P(1) = {probs[1]:.4f}")

def visualize():
    """Create visualizations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig = plt.figure(figsize=(16, 10))
    
    ax1 = plt.subplot(2, 3, 1)
    z_array = np.array([1+2j, 2+1j, 3+0j, 2-1j, 1-2j])
    
    ax1.scatter(z_array.real, z_array.imag, s=100, c='blue', alpha=0.7)
    for i, z in enumerate(z_array):
        ax1.arrow(0, 0, z.real, z.imag, head_width=0.1, head_length=0.1,
                  fc='blue', ec='blue', alpha=0.3)
        ax1.text(z.real+0.2, z.imag+0.2, f'z{i}', fontsize=10)
    
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Real', fontsize=12)
    ax1.set_ylabel('Imaginary', fontsize=12)
    ax1.set_title('NumPy Complex Array', fontsize=14, fontweight='bold')
    ax1.set_aspect('equal')
    
    ax2 = plt.subplot(2, 3, 2)
    
    states = {
        '|0⟩': np.array([1, 0]),
        '|1⟩': np.array([0, 1]),
        '|+⟩': np.array([1, 1])/np.sqrt(2),
        '|−⟩': np.array([1, -1])/np.sqrt(2),
        '|ψ⟩': np.array([3/5, 4j/5])
    }
    
    state_names = list(states.keys())
    probs_0 = [np.abs(states[name][0])**2 for name in state_names]
    probs_1 = [np.abs(states[name][1])**2 for name in state_names]
    
    x = np.arange(len(state_names))
    width = 0.35
    
    ax2.bar(x - width/2, probs_0, width, label='P(0)', color='blue', alpha=0.7)
    ax2.bar(x + width/2, probs_1, width, label='P(1)', color='red', alpha=0.7)
    
    ax2.set_xlabel('State', fontsize=12)
    ax2.set_ylabel('Probability', fontsize=12)
    ax2.set_title('Quantum State Probabilities', fontsize=14, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(state_names)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, axis='y')
    
    ax3 = plt.subplot(2, 3, 3)
    
    ket_0 = np.array([1, 0])
    gates = {
        'I': np.eye(2),
        'X': np.array([[0, 1], [1, 0]]),
        'H': np.array([[1, 1], [1, -1]])/np.sqrt(2),
        'S': np.array([[1, 0], [0, 1j]]),
        'T': np.array([[1, 0], [0, np.exp(1j*np.pi/4)]])
    }
    
    gate_names = list(gates.keys())
    results = [gates[name] @ ket_0 for name in gate_names]
    
    for i, (name, result) in enumerate(zip(gate_names, results)):
        ax3.arrow(0, i, result[0].real, 0, head_width=0.2, head_length=0.05,
                  fc='blue', ec='blue', alpha=0.7)
        ax3.arrow(0, i, 0, result[1].imag, head_width=0.2, head_length=0.05,
                  fc='red', ec='red', alpha=0.7)
        ax3.text(-0.5, i, name, fontsize=12, ha='right')
    
    ax3.set_xlabel('Amplitude', fontsize=12)
    ax3.set_ylabel('Gate', fontsize=12)
    ax3.set_title('Gate|0⟩ Results', fontsize=14, fontweight='bold')
    ax3.set_yticks(range(len(gate_names)))
    ax3.set_yticklabels(gate_names)
    ax3.grid(True, alpha=0.3)
    ax3.axvline(x=0, color='k', linewidth=0.5)
    
    ax4 = plt.subplot(2, 3, 4)
    
    basis_states = [
        np.array([1, 0]),
        np.array([0, 1]),
        np.array([1, 1])/np.sqrt(2),
        np.array([1, -1])/np.sqrt(2)
    ]
    labels = ['|0⟩', '|1⟩', '|+⟩', '|−⟩']
    
    n = len(basis_states)
    inner_matrix = np.zeros((n, n), dtype=complex)
    
    for i in range(n):
        for j in range(n):
            inner_matrix[i, j] = np.vdot(basis_states[i], basis_states[j])
    
    im = ax4.imshow(np.abs(inner_matrix), cmap='viridis', vmin=0, vmax=1)
    
    for i in range(n):
        for j in range(n):
            text = ax4.text(j, i, f'{np.abs(inner_matrix[i, j]):.2f}',
                           ha="center", va="center", color="w", fontsize=12)
    
    ax4.set_xticks(range(n))
    ax4.set_yticks(range(n))
    ax4.set_xticklabels(labels)
    ax4.set_yticklabels(labels)
    ax4.set_title('Inner Product Matrix |⟨i|j⟩|', fontsize=14, fontweight='bold')
    plt.colorbar(im, ax=ax4)
    
    ax5 = plt.subplot(2, 3, 5)
    
    times = np.linspace(0, 4*np.pi, 200)
    E0, E1 = 0, 1
    psi_0 = np.array([1, 1])/np.sqrt(2)
    
    probs_0 = []
    probs_1 = []
    
    for t in times:
        U = np.diag([np.exp(-1j*E0*t), np.exp(-1j*E1*t)])
        psi_t = U @ psi_0
        probs = np.abs(psi_t)**2
        probs_0.append(probs[0])
        probs_1.append(probs[1])
    
    ax5.plot(times, probs_0, 'b-', linewidth=2, label='P(0)')
    ax5.plot(times, probs_1, 'r-', linewidth=2, label='P(1)')
    ax5.fill_between(times, probs_0, alpha=0.3, color='blue')
    ax5.fill_between(times, probs_1, alpha=0.3, color='red')
    
    ax5.set_xlabel('Time', fontsize=12)
    ax5.set_ylabel('Probability', fontsize=12)
    ax5.set_title('Time Evolution of Superposition', fontsize=14, fontweight='bold')
    ax5.legend(fontsize=10)
    ax5.grid(True, alpha=0.3)
    
    ax6 = plt.subplot(2, 3, 6)
    
    steps = ['|00⟩', 'H⊗I|00⟩', 'CNOT(H⊗I|00⟩)']
    
    ket_00 = np.array([1, 0, 0, 0])
    H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
    H_I = np.kron(H, np.eye(2))
    CNOT = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]])
    
    states = [
        ket_00,
        H_I @ ket_00,
        CNOT @ (H_I @ ket_00)
    ]
    
    for i, (step, state) in enumerate(zip(steps, states)):
        probs = np.abs(state)**2
        ax6.bar(np.arange(4) + i*5, probs, width=0.8, alpha=0.7, label=step)
    
    ax6.set_xlabel('Basis State', fontsize=12)
    ax6.set_ylabel('Probability', fontsize=12)
    ax6.set_title('Bell State Creation Steps', fontsize=14, fontweight='bold')
    ax6.set_xticks([1.5, 6.5, 11.5])
    ax6.set_xticklabels(steps, rotation=15)
    ax6.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('python_operations.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'python_operations.png'")
    plt.close()

def main():
    print("\n" + "🐍" * 30)
    print("PYTHON OPERATIONS WITH COMPLEX NUMBERS")
    print("🐍" * 30)
    
    basic_operations()
    numpy_operations()
    quantum_states()
    inner_products()
    quantum_gates()
    two_qubit_operations()
    time_evolution()
    visualize()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Python: use j for imaginary unit")
    print("2. NumPy: powerful array operations")
    print("3. np.vdot() for inner products")
    print("4. np.kron() for tensor products")
    print("5. @ operator for matrix multiplication")
    print("6. np.conj(A.T) for Hermitian conjugate")
    print("7. Quantum gates are unitary matrices")
    print("=" * 60)

if __name__ == "__main__":
    main()
