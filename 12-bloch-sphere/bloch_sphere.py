"""
Bloch Sphere Representation
Python script demonstrating the Bloch sphere and quantum state visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

def bloch_coordinates(theta, phi):
    """Convert spherical to Cartesian coordinates"""
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return x, y, z

def state_from_bloch(theta, phi):
    """Get quantum state from Bloch sphere angles"""
    alpha = np.cos(theta / 2)
    beta = np.exp(1j * phi) * np.sin(theta / 2)
    return np.array([alpha, beta], dtype=complex)

def bloch_from_state(state):
    """Get Bloch sphere angles from quantum state"""
    alpha, beta = state
    
    norm = np.sqrt(np.abs(alpha)**2 + np.abs(beta)**2)
    alpha /= norm
    beta /= norm
    
    theta = 2 * np.arccos(np.abs(alpha))
    
    if np.abs(beta) < 1e-10:
        phi = 0
    else:
        phi = np.angle(beta / np.sin(theta / 2)) if np.abs(np.sin(theta / 2)) > 1e-10 else 0
    
    return theta, phi

def demonstrate_basis_states():
    """Demonstrate basis states on Bloch sphere"""
    print("=" * 60)
    print("BASIS STATES ON BLOCH SPHERE")
    print("=" * 60)
    
    states = {
        '|0⟩': (0, 0),
        '|1⟩': (np.pi, 0),
        '|+⟩': (np.pi/2, 0),
        '|−⟩': (np.pi/2, np.pi),
        '|i⟩': (np.pi/2, np.pi/2),
        '|−i⟩': (np.pi/2, 3*np.pi/2)
    }
    
    for name, (theta, phi) in states.items():
        x, y, z = bloch_coordinates(theta, phi)
        state = state_from_bloch(theta, phi)
        
        print(f"\n{name}:")
        print(f"  Angles: θ = {theta:.4f}, φ = {phi:.4f}")
        print(f"  Cartesian: ({x:.4f}, {y:.4f}, {z:.4f})")
        print(f"  State: {state}")
        print(f"  P(0) = {np.abs(state[0])**2:.4f}, P(1) = {np.abs(state[1])**2:.4f}")

def demonstrate_rotations():
    """Demonstrate gate operations as rotations"""
    print("\n" + "=" * 60)
    print("GATE OPERATIONS AS ROTATIONS")
    print("=" * 60)
    
    ket0 = np.array([1, 0], dtype=complex)
    theta0, phi0 = bloch_from_state(ket0)
    x0, y0, z0 = bloch_coordinates(theta0, phi0)
    
    print(f"\nInitial state |0⟩:")
    print(f"  Position: ({x0:.4f}, {y0:.4f}, {z0:.4f})")
    
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    state_x = X @ ket0
    theta_x, phi_x = bloch_from_state(state_x)
    x_x, y_x, z_x = bloch_coordinates(theta_x, phi_x)
    
    print(f"\nAfter Pauli X (π rotation around X):")
    print(f"  State: {state_x} = |1⟩")
    print(f"  Position: ({x_x:.4f}, {y_x:.4f}, {z_x:.4f})")
    
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    state_h = H @ ket0
    theta_h, phi_h = bloch_from_state(state_h)
    x_h, y_h, z_h = bloch_coordinates(theta_h, phi_h)
    
    print(f"\nAfter Hadamard:")
    print(f"  State: {state_h} = |+⟩")
    print(f"  Position: ({x_h:.4f}, {y_h:.4f}, {z_h:.4f})")
    
    S = np.array([[1, 0], [0, 1j]], dtype=complex)
    state_s = S @ state_h
    theta_s, phi_s = bloch_from_state(state_s)
    x_s, y_s, z_s = bloch_coordinates(theta_s, phi_s)
    
    print(f"\nAfter S gate on |+⟩ (π/2 rotation around Z):")
    print(f"  State: {state_s} = |i⟩")
    print(f"  Position: ({x_s:.4f}, {y_s:.4f}, {z_s:.4f})")

def demonstrate_measurement():
    """Demonstrate measurement probabilities"""
    print("\n" + "=" * 60)
    print("MEASUREMENT PROBABILITIES")
    print("=" * 60)
    
    theta = np.pi / 3
    phi = np.pi / 4
    state = state_from_bloch(theta, phi)
    x, y, z = bloch_coordinates(theta, phi)
    
    print(f"\nState: θ = {theta:.4f}, φ = {phi:.4f}")
    print(f"Position: ({x:.4f}, {y:.4f}, {z:.4f})")
    print(f"|ψ⟩ = {state}")
    
    prob0 = np.abs(state[0])**2
    prob1 = np.abs(state[1])**2
    
    print(f"\nComputational basis (Z-basis):")
    print(f"  P(0) = cos²(θ/2) = {prob0:.4f}")
    print(f"  P(1) = sin²(θ/2) = {prob1:.4f}")
    print(f"  Total: {prob0 + prob1:.4f}")
    
    ket_plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    ket_minus = np.array([1, -1], dtype=complex) / np.sqrt(2)
    
    prob_plus = np.abs(np.vdot(ket_plus, state))**2
    prob_minus = np.abs(np.vdot(ket_minus, state))**2
    
    print(f"\nHadamard basis (X-basis):")
    print(f"  P(+) = (1 + sin(θ)cos(φ))/2 = {prob_plus:.4f}")
    print(f"  P(−) = (1 − sin(θ)cos(φ))/2 = {prob_minus:.4f}")
    print(f"  Total: {prob_plus + prob_minus:.4f}")
    
    ket_i = np.array([1, 1j], dtype=complex) / np.sqrt(2)
    ket_minus_i = np.array([1, -1j], dtype=complex) / np.sqrt(2)
    
    prob_i = np.abs(np.vdot(ket_i, state))**2
    prob_minus_i = np.abs(np.vdot(ket_minus_i, state))**2
    
    print(f"\nY-basis:")
    print(f"  P(i) = (1 + sin(θ)sin(φ))/2 = {prob_i:.4f}")
    print(f"  P(−i) = (1 − sin(θ)sin(φ))/2 = {prob_minus_i:.4f}")
    print(f"  Total: {prob_i + prob_minus_i:.4f}")

def demonstrate_phase_importance():
    """Demonstrate why complex phase matters"""
    print("\n" + "=" * 60)
    print("IMPORTANCE OF COMPLEX PHASE")
    print("=" * 60)
    
    state1 = np.array([1, 1], dtype=complex) / np.sqrt(2)  # |+⟩
    state2 = np.array([1, 1j], dtype=complex) / np.sqrt(2)  # |i⟩
    
    print("\nTwo states with same measurement probabilities:")
    print(f"|+⟩ = {state1}")
    print(f"|i⟩ = {state2}")
    
    print(f"\nProbabilities:")
    print(f"  |+⟩: P(0) = {np.abs(state1[0])**2:.4f}, P(1) = {np.abs(state1[1])**2:.4f}")
    print(f"  |i⟩: P(0) = {np.abs(state2[0])**2:.4f}, P(1) = {np.abs(state2[1])**2:.4f}")
    print("  Identical probabilities!")
    
    theta1, phi1 = bloch_from_state(state1)
    theta2, phi2 = bloch_from_state(state2)
    x1, y1, z1 = bloch_coordinates(theta1, phi1)
    x2, y2, z2 = bloch_coordinates(theta2, phi2)
    
    print(f"\nBloch sphere positions:")
    print(f"  |+⟩: ({x1:.4f}, {y1:.4f}, {z1:.4f}), φ = {phi1:.4f}")
    print(f"  |i⟩: ({x2:.4f}, {y2:.4f}, {z2:.4f}), φ = {phi2:.4f}")
    print("  Different positions due to phase!")
    
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    
    result1 = H @ state1
    result2 = H @ state2
    
    print(f"\nAfter Hadamard gate:")
    print(f"  H|+⟩ = {result1} = |0⟩")
    print(f"  H|i⟩ = {result2}")
    print("  Different results due to phase!")

def state_evolution():
    """Demonstrate state evolution on Bloch sphere"""
    print("\n" + "=" * 60)
    print("STATE EVOLUTION")
    print("=" * 60)
    
    state = np.array([1, 0], dtype=complex)
    print(f"\nInitial state: |0⟩ = {state}")
    
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    S = np.array([[1, 0], [0, 1j]], dtype=complex)
    T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
    
    gates = [('H', H), ('S', S), ('T', T), ('H', H)]
    
    for name, gate in gates:
        state = gate @ state
        theta, phi = bloch_from_state(state)
        x, y, z = bloch_coordinates(theta, phi)
        
        print(f"\nAfter {name}:")
        print(f"  State: {state}")
        print(f"  Position: ({x:.4f}, {y:.4f}, {z:.4f})")
        print(f"  Angles: θ = {theta:.4f}, φ = {phi:.4f}")

def visualize():
    """Create visualizations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig = plt.figure(figsize=(20, 12))
    
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')
    
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x_sphere = np.outer(np.cos(u), np.sin(v))
    y_sphere = np.outer(np.sin(u), np.sin(v))
    z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
    
    ax1.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.1, color='cyan')
    
    ax1.plot([0, 0], [0, 0], [-1.5, 1.5], 'b-', linewidth=2, label='Z')
    ax1.plot([0, 1.5], [0, 0], [0, 0], 'r-', linewidth=2, label='X')
    ax1.plot([0, 0], [0, 1.5], [0, 0], 'g-', linewidth=2, label='Y')
    
    states = {
        '|0⟩': (0, 0, 1, 'blue'),
        '|1⟩': (0, 0, -1, 'red'),
        '|+⟩': (1, 0, 0, 'green'),
        '|−⟩': (-1, 0, 0, 'orange'),
        '|i⟩': (0, 1, 0, 'purple'),
        '|−i⟩': (0, -1, 0, 'brown')
    }
    
    for name, (x, y, z, color) in states.items():
        ax1.scatter([x], [y], [z], c=color, s=100, marker='o')
        ax1.text(x*1.2, y*1.2, z*1.2, name, fontsize=10)
    
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('Bloch Sphere with Basis States', fontsize=14, fontweight='bold')
    ax1.legend()
    
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')
    
    ax2.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.1, color='cyan')
    
    state = np.array([1, 0], dtype=complex)
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    
    path_x, path_y, path_z = [], [], []
    
    for i in range(20):
        theta, phi = bloch_from_state(state)
        x, y, z = bloch_coordinates(theta, phi)
        path_x.append(x)
        path_y.append(y)
        path_z.append(z)
        
        angle = np.pi / 10
        Rz = np.array([[np.exp(-1j*angle/2), 0], [0, np.exp(1j*angle/2)]], dtype=complex)
        state = Rz @ state
    
    ax2.plot(path_x, path_y, path_z, 'r-', linewidth=2, label='Evolution path')
    ax2.scatter(path_x[0], path_y[0], path_z[0], c='green', s=100, marker='o', label='Start')
    ax2.scatter(path_x[-1], path_y[-1], path_z[-1], c='red', s=100, marker='o', label='End')
    
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title('State Evolution on Bloch Sphere', fontsize=14, fontweight='bold')
    ax2.legend()
    
    ax3 = fig.add_subplot(2, 3, 3)
    
    thetas = np.linspace(0, np.pi, 100)
    prob0 = np.cos(thetas / 2)**2
    prob1 = np.sin(thetas / 2)**2
    
    ax3.plot(thetas, prob0, label='P(0)', linewidth=2)
    ax3.plot(thetas, prob1, label='P(1)', linewidth=2)
    ax3.axhline(y=0.5, color='k', linewidth=0.5, linestyle='--')
    ax3.grid(True, alpha=0.3)
    ax3.set_xlabel('θ (radians)', fontsize=12)
    ax3.set_ylabel('Probability', fontsize=12)
    ax3.set_title('Measurement Probabilities vs θ', fontsize=14, fontweight='bold')
    ax3.legend()
    ax3.set_xlim(0, np.pi)
    ax3.set_ylim(0, 1)
    
    ax4 = fig.add_subplot(2, 3, 4)
    
    phis = np.linspace(0, 2*np.pi, 100)
    theta_fixed = np.pi / 2
    
    x_coords = np.sin(theta_fixed) * np.cos(phis)
    y_coords = np.sin(theta_fixed) * np.sin(phis)
    
    ax4.plot(phis, x_coords, label='X coordinate', linewidth=2)
    ax4.plot(phis, y_coords, label='Y coordinate', linewidth=2)
    ax4.axhline(y=0, color='k', linewidth=0.5)
    ax4.grid(True, alpha=0.3)
    ax4.set_xlabel('φ (radians)', fontsize=12)
    ax4.set_ylabel('Coordinate', fontsize=12)
    ax4.set_title('Equator Position vs Phase φ', fontsize=14, fontweight='bold')
    ax4.legend()
    ax4.set_xlim(0, 2*np.pi)
    
    ax5 = fig.add_subplot(2, 3, 5, projection='3d')
    
    ax5.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.1, color='cyan')
    
    ket0 = np.array([1, 0], dtype=complex)
    
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    
    gates_dict = {'X': (X, 'red'), 'Y': (Y, 'green'), 'Z': (Z, 'blue')}
    
    for name, (gate, color) in gates_dict.items():
        state = gate @ ket0
        theta, phi = bloch_from_state(state)
        x, y, z = bloch_coordinates(theta, phi)
        
        arrow = Arrow3D([0, x], [0, y], [1, z], mutation_scale=20, 
                       lw=2, arrowstyle='->', color=color, label=f'{name}|0⟩')
        ax5.add_artist(arrow)
    
    ax5.scatter([0], [0], [1], c='yellow', s=100, marker='o', label='|0⟩')
    
    ax5.set_xlabel('X')
    ax5.set_ylabel('Y')
    ax5.set_zlabel('Z')
    ax5.set_title('Pauli Gate Rotations', fontsize=14, fontweight='bold')
    ax5.legend()
    
    ax6 = fig.add_subplot(2, 3, 6)
    
    n_theta = 20
    n_phi = 40
    thetas = np.linspace(0, np.pi, n_theta)
    phis = np.linspace(0, 2*np.pi, n_phi)
    
    ref_state = np.array([1, 1], dtype=complex) / np.sqrt(2)
    
    fidelities = np.zeros((n_theta, n_phi))
    
    for i, theta in enumerate(thetas):
        for j, phi in enumerate(phis):
            state = state_from_bloch(theta, phi)
            fidelities[i, j] = np.abs(np.vdot(ref_state, state))**2
    
    im = ax6.imshow(fidelities, aspect='auto', cmap='viridis', 
                    extent=[0, 2*np.pi, np.pi, 0], vmin=0, vmax=1)
    ax6.set_xlabel('φ (radians)', fontsize=12)
    ax6.set_ylabel('θ (radians)', fontsize=12)
    ax6.set_title('Fidelity with |+⟩ State', fontsize=14, fontweight='bold')
    plt.colorbar(im, ax=ax6)
    
    plt.tight_layout()
    plt.savefig('bloch_sphere.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'bloch_sphere.png'")
    plt.close()

def main():
    print("\n" + "🌐" * 30)
    print("BLOCH SPHERE REPRESENTATION")
    print("🌐" * 30)
    
    demonstrate_basis_states()
    demonstrate_rotations()
    demonstrate_measurement()
    demonstrate_phase_importance()
    state_evolution()
    visualize()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Bloch sphere: |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩")
    print("2. Complex phase φ determines position on sphere")
    print("3. All pure qubit states map to sphere surface")
    print("4. Quantum gates = rotations on sphere")
    print("5. Measurement probabilities from θ coordinate")
    print("6. Phase matters for interference and gates")
    print("=" * 60)

if __name__ == "__main__":
    main()
