"""
Quantum Gates with Complex Coefficients
Python script demonstrating quantum gates and their complex matrix representations
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

def pauli_gates():
    """Demonstrate Pauli gates"""
    print("=" * 60)
    print("PAULI GATES")
    print("=" * 60)
    
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    
    print("\nPauli X (NOT gate):")
    print(X)
    
    print("\nPauli Y (complex coefficients!):")
    print(Y)
    
    print("\nPauli Z (phase flip):")
    print(Z)
    
    ket0 = np.array([1, 0], dtype=complex)
    ket1 = np.array([0, 1], dtype=complex)
    
    print("\nAction on |0⟩:")
    print(f"X|0⟩ = {X @ ket0} = |1⟩")
    print(f"Y|0⟩ = {Y @ ket0} = i|1⟩ (imaginary!)")
    print(f"Z|0⟩ = {Z @ ket0} = |0⟩")
    
    print("\nAction on |1⟩:")
    print(f"X|1⟩ = {X @ ket1} = |0⟩")
    print(f"Y|1⟩ = {Y @ ket1} = -i|0⟩ (imaginary!)")
    print(f"Z|1⟩ = {Z @ ket1} = -|1⟩")

def hadamard_gate():
    """Demonstrate Hadamard gate"""
    print("\n" + "=" * 60)
    print("HADAMARD GATE")
    print("=" * 60)
    
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    
    print("\nHadamard gate:")
    print(H)
    
    ket0 = np.array([1, 0], dtype=complex)
    ket1 = np.array([0, 1], dtype=complex)
    
    ket_plus = H @ ket0
    ket_minus = H @ ket1
    
    print(f"\nH|0⟩ = {ket_plus}")
    print(f"     = (1/√2)(|0⟩ + |1⟩) = |+⟩")
    
    print(f"\nH|1⟩ = {ket_minus}")
    print(f"     = (1/√2)(|0⟩ - |1⟩) = |−⟩")
    
    print("\nSelf-inverse property: H² = I")
    H_squared = H @ H
    print(f"H² = ")
    print(H_squared)
    print(f"Is identity? {np.allclose(H_squared, np.eye(2))}")

def phase_gates():
    """Demonstrate phase gates with complex coefficients"""
    print("\n" + "=" * 60)
    print("PHASE GATES")
    print("=" * 60)
    
    S = np.array([[1, 0], [0, 1j]], dtype=complex)
    
    print("\nS gate (Phase gate):")
    print(S)
    print("Adds π/2 phase to |1⟩")
    
    T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
    
    print("\nT gate (π/8 gate):")
    print(T)
    print("Adds π/4 phase to |1⟩")
    
    ket_plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    
    print(f"\n|+⟩ = {ket_plus}")
    
    s_plus = S @ ket_plus
    print(f"\nS|+⟩ = {s_plus}")
    print(f"     = (1/√2)(|0⟩ + i|1⟩) = |i⟩")
    
    t_plus = T @ ket_plus
    print(f"\nT|+⟩ = {t_plus}")
    print(f"     = (1/√2)(|0⟩ + e^(iπ/4)|1⟩)")
    
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    S_squared = S @ S
    print("\nVerify S² = Z:")
    print(f"S² = ")
    print(S_squared)
    print(f"Z = ")
    print(Z)
    print(f"S² = Z? {np.allclose(S_squared, Z)}")

def rotation_gates():
    """Demonstrate rotation gates"""
    print("\n" + "=" * 60)
    print("ROTATION GATES")
    print("=" * 60)
    
    theta = np.pi / 4
    
    Rx = np.array([
        [np.cos(theta/2), -1j*np.sin(theta/2)],
        [-1j*np.sin(theta/2), np.cos(theta/2)]
    ], dtype=complex)
    
    print(f"\nRx(π/4):")
    print(Rx)
    
    Ry = np.array([
        [np.cos(theta/2), -np.sin(theta/2)],
        [np.sin(theta/2), np.cos(theta/2)]
    ], dtype=complex)
    
    print(f"\nRy(π/4):")
    print(Ry)
    
    Rz = np.array([
        [np.exp(-1j*theta/2), 0],
        [0, np.exp(1j*theta/2)]
    ], dtype=complex)
    
    print(f"\nRz(π/4):")
    print(Rz)
    
    ket0 = np.array([1, 0], dtype=complex)
    
    print(f"\nRx(π/4)|0⟩ = {Rx @ ket0}")
    print(f"Ry(π/4)|0⟩ = {Ry @ ket0}")
    print(f"Rz(π/4)|0⟩ = {Rz @ ket0}")

def unitary_verification():
    """Verify gates are unitary"""
    print("\n" + "=" * 60)
    print("UNITARY VERIFICATION")
    print("=" * 60)
    
    gates = {
        'X': np.array([[0, 1], [1, 0]], dtype=complex),
        'Y': np.array([[0, -1j], [1j, 0]], dtype=complex),
        'Z': np.array([[1, 0], [0, -1]], dtype=complex),
        'H': np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2),
        'S': np.array([[1, 0], [0, 1j]], dtype=complex),
        'T': np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
    }
    
    print("\nVerifying U†U = I for all gates:")
    
    for name, gate in gates.items():
        gate_dagger = np.conj(gate.T)
        product = gate_dagger @ gate
        is_unitary = np.allclose(product, np.eye(2))
        print(f"{name}: {is_unitary} ✓" if is_unitary else f"{name}: {is_unitary} ✗")

def gate_composition():
    """Demonstrate gate composition"""
    print("\n" + "=" * 60)
    print("GATE COMPOSITION")
    print("=" * 60)
    
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    S = np.array([[1, 0], [0, 1j]], dtype=complex)
    T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
    
    print("\nHXH = Z:")
    HXH = H @ X @ H
    print(f"HXH = ")
    print(HXH)
    print(f"Z = ")
    print(Z)
    print(f"Equal? {np.allclose(HXH, Z)}")
    
    print("\nS² = Z:")
    S_squared = S @ S
    print(f"S² = ")
    print(S_squared)
    print(f"Equal? {np.allclose(S_squared, Z)}")
    
    print("\nT² = S:")
    T_squared = T @ T
    print(f"T² = ")
    print(T_squared)
    print(f"Equal? {np.allclose(T_squared, S)}")

def controlled_gates():
    """Demonstrate controlled gates"""
    print("\n" + "=" * 60)
    print("CONTROLLED GATES")
    print("=" * 60)
    
    CNOT = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ], dtype=complex)
    
    print("\nCNOT gate:")
    print(CNOT)
    
    CZ = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1]
    ], dtype=complex)
    
    print("\nControlled-Z gate:")
    print(CZ)
    
    CS = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1j]
    ], dtype=complex)
    
    print("\nControlled-S gate (complex!):")
    print(CS)
    
    ket00 = np.array([1, 0, 0, 0], dtype=complex)
    
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    I = np.eye(2, dtype=complex)
    HI = np.kron(H, I)
    
    state = HI @ ket00
    print(f"\n(H ⊗ I)|00⟩ = {state}")
    
    bell_state = CNOT @ state
    print(f"\nCNOT(H ⊗ I)|00⟩ = {bell_state}")
    print(f"                 = (1/√2)(|00⟩ + |11⟩)")
    print(f"                 = |Φ⁺⟩ (Bell state)")

def quantum_algorithms():
    """Demonstrate gates in quantum algorithms"""
    print("\n" + "=" * 60)
    print("QUANTUM ALGORITHMS")
    print("=" * 60)
    
    print("\nDeutsch Algorithm:")
    print("Uses H, X, and oracle gates")
    
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    
    ket01 = np.array([0, 1, 0, 0], dtype=complex)
    
    HH = np.kron(H, H)
    state = HH @ ket01
    print(f"(H ⊗ H)|01⟩ = {state}")
    
    print("\nGrover's Algorithm:")
    print("Uses H gates and phase inversion")
    
    oracle = np.eye(4, dtype=complex)
    oracle[3, 3] = -1
    
    print("Oracle (marks |11⟩):")
    print(oracle)
    
    print("\nQuantum Fourier Transform:")
    print("Uses H and controlled phase gates")
    
    S = np.array([[1, 0], [0, 1j]], dtype=complex)
    SWAP = np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ], dtype=complex)
    
    print("QFT uses complex phase gates extensively!")

def visualize():
    """Create visualizations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig = plt.figure(figsize=(20, 12))
    
    ax1 = fig.add_subplot(2, 3, 1)
    
    gates = ['X', 'Y', 'Z']
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    
    ket0 = np.array([1, 0], dtype=complex)
    
    results_real = []
    results_imag = []
    
    for gate_matrix in [X, Y, Z]:
        result = gate_matrix @ ket0
        results_real.append(np.abs(result[1].real))
        results_imag.append(np.abs(result[1].imag))
    
    x = np.arange(len(gates))
    width = 0.35
    
    ax1.bar(x - width/2, results_real, width, label='Real part', alpha=0.8)
    ax1.bar(x + width/2, results_imag, width, label='Imaginary part', alpha=0.8)
    
    ax1.set_ylabel('Amplitude', fontsize=12)
    ax1.set_title('Pauli Gates on |0⟩', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(gates)
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='y')
    
    ax2 = fig.add_subplot(2, 3, 2)
    
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    
    states = ['|0⟩', '|1⟩', '|+⟩', '|−⟩']
    ket0 = np.array([1, 0], dtype=complex)
    ket1 = np.array([0, 1], dtype=complex)
    ket_plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    ket_minus = np.array([1, -1], dtype=complex) / np.sqrt(2)
    
    input_states = [ket0, ket1, ket_plus, ket_minus]
    
    for i, (state, label) in enumerate(zip(input_states, states)):
        output = H @ state
        ax2.arrow(i, 0, 0, np.abs(output[0]), head_width=0.2, head_length=0.05,
                 fc='blue', ec='blue', linewidth=2, alpha=0.7)
        ax2.arrow(i, 0, 0, -np.abs(output[1]), head_width=0.2, head_length=0.05,
                 fc='red', ec='red', linewidth=2, alpha=0.7)
    
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.set_xlabel('Input State', fontsize=12)
    ax2.set_ylabel('Output Amplitude', fontsize=12)
    ax2.set_title('Hadamard Gate Action', fontsize=14, fontweight='bold')
    ax2.set_xticks(range(len(states)))
    ax2.set_xticklabels(states)
    ax2.grid(True, alpha=0.3)
    
    ax3 = fig.add_subplot(2, 3, 3, projection='polar')
    
    angles = np.linspace(0, 2*np.pi, 100)
    
    ax3.plot(angles, np.ones_like(angles), 'b-', linewidth=2, label='Input')
    ax3.plot(angles + np.pi/2, np.ones_like(angles), 'r-', linewidth=2, label='After S gate')
    
    ax3.set_title('S Gate Phase Shift', fontsize=14, fontweight='bold', pad=20)
    ax3.legend(loc='upper right')
    
    ax4 = fig.add_subplot(2, 3, 4)
    
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Y_abs = np.abs(Y)
    
    im = ax4.imshow(Y_abs, cmap='viridis', aspect='auto')
    ax4.set_title('Pauli Y Gate (Magnitude)', fontsize=14, fontweight='bold')
    ax4.set_xticks([0, 1])
    ax4.set_yticks([0, 1])
    ax4.set_xticklabels(['|0⟩', '|1⟩'])
    ax4.set_yticklabels(['⟨0|', '⟨1|'])
    plt.colorbar(im, ax=ax4)
    
    ax5 = fig.add_subplot(2, 3, 5)
    
    thetas = np.linspace(0, 2*np.pi, 50)
    prob0 = []
    prob1 = []
    
    ket0 = np.array([1, 0], dtype=complex)
    
    for theta in thetas:
        Ry = np.array([
            [np.cos(theta/2), -np.sin(theta/2)],
            [np.sin(theta/2), np.cos(theta/2)]
        ], dtype=complex)
        
        state = Ry @ ket0
        prob0.append(np.abs(state[0])**2)
        prob1.append(np.abs(state[1])**2)
    
    ax5.plot(thetas, prob0, label='P(0)', linewidth=2)
    ax5.plot(thetas, prob1, label='P(1)', linewidth=2)
    ax5.axhline(y=0.5, color='k', linewidth=0.5, linestyle='--')
    ax5.grid(True, alpha=0.3)
    ax5.set_xlabel('Rotation Angle θ', fontsize=12)
    ax5.set_ylabel('Probability', fontsize=12)
    ax5.set_title('Ry(θ) Gate Probabilities', fontsize=14, fontweight='bold')
    ax5.legend()
    ax5.set_xlim(0, 2*np.pi)
    ax5.set_ylim(0, 1)
    
    ax6 = fig.add_subplot(2, 3, 6)
    
    compositions = ['X', 'Y', 'Z', 'HXH', 'S²', 'T²']
    
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    S = np.array([[1, 0], [0, 1j]], dtype=complex)
    T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
    
    gates_list = [X, Y, Z, H @ X @ H, S @ S, T @ T]
    
    ket0 = np.array([1, 0], dtype=complex)
    
    real_parts = []
    imag_parts = []
    
    for gate in gates_list:
        result = gate @ ket0
        real_parts.append(np.abs(result[1].real))
        imag_parts.append(np.abs(result[1].imag))
    
    x = np.arange(len(compositions))
    width = 0.35
    
    ax6.bar(x - width/2, real_parts, width, label='Real', alpha=0.8)
    ax6.bar(x + width/2, imag_parts, width, label='Imaginary', alpha=0.8)
    
    ax6.set_ylabel('Amplitude', fontsize=12)
    ax6.set_title('Gate Compositions on |0⟩', fontsize=14, fontweight='bold')
    ax6.set_xticks(x)
    ax6.set_xticklabels(compositions, rotation=45)
    ax6.legend()
    ax6.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('quantum_gates.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'quantum_gates.png'")
    plt.close()

def main():
    print("\n" + "🚪" * 30)
    print("QUANTUM GATES WITH COMPLEX COEFFICIENTS")
    print("🚪" * 30)
    
    pauli_gates()
    hadamard_gate()
    phase_gates()
    rotation_gates()
    unitary_verification()
    gate_composition()
    controlled_gates()
    quantum_algorithms()
    visualize()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Pauli Y gate has complex coefficients (±i)")
    print("2. Phase gates (S, T) add complex phases")
    print("3. Rotation gates use complex exponentials")
    print("4. All quantum gates are unitary: U†U = I")
    print("5. Gates compose by matrix multiplication")
    print("6. Complex coefficients enable phase control")
    print("=" * 60)

if __name__ == "__main__":
    main()
