"""
Quantum States with Complex Amplitudes
Python script demonstrating quantum superposition and measurement
"""

import numpy as np
import matplotlib.pyplot as plt

def demonstrate_qubit_state():
    """Demonstrate basic qubit state representation"""
    print("=" * 60)
    print("QUBIT STATE: |ψ⟩ = α|0⟩ + β|1⟩")
    print("=" * 60)
    
    alpha = 1/np.sqrt(2)
    beta = 1/np.sqrt(2)
    
    print(f"\nEqual superposition state:")
    print(f"α = {alpha:.4f}")
    print(f"β = {beta:.4f}")
    print(f"|ψ⟩ = {alpha:.4f}|0⟩ + {beta:.4f}|1⟩")
    
    prob_0 = np.abs(alpha)**2
    prob_1 = np.abs(beta)**2
    
    print(f"\nProbabilities:")
    print(f"P(0) = |α|² = {prob_0:.4f} ({prob_0*100:.1f}%)")
    print(f"P(1) = |β|² = {prob_1:.4f} ({prob_1*100:.1f}%)")
    print(f"Total: {prob_0 + prob_1:.4f} ✓")

def standard_states():
    """Demonstrate standard quantum states"""
    print("\n" + "=" * 60)
    print("STANDARD QUANTUM STATES")
    print("=" * 60)
    
    states = {
        "|0⟩": (1, 0),
        "|1⟩": (0, 1),
        "|+⟩": (1/np.sqrt(2), 1/np.sqrt(2)),
        "|−⟩": (1/np.sqrt(2), -1/np.sqrt(2)),
        "|R⟩": (1/np.sqrt(2), 1j/np.sqrt(2)),
        "|L⟩": (1/np.sqrt(2), -1j/np.sqrt(2))
    }
    
    for name, (alpha, beta) in states.items():
        prob_0 = np.abs(alpha)**2
        prob_1 = np.abs(beta)**2
        print(f"\n{name} state:")
        print(f"  α = {alpha}")
        print(f"  β = {beta}")
        print(f"  P(0) = {prob_0:.4f}, P(1) = {prob_1:.4f}")
        print(f"  Normalized: {np.allclose(prob_0 + prob_1, 1)} ✓")

def complex_amplitudes():
    """Demonstrate states with complex amplitudes"""
    print("\n" + "=" * 60)
    print("COMPLEX AMPLITUDES WITH PHASE")
    print("=" * 60)
    
    alpha = 1/np.sqrt(2)
    beta = np.exp(1j * np.pi/4) / np.sqrt(2)
    
    print(f"\nState with relative phase:")
    print(f"α = {alpha:.4f}")
    print(f"β = {beta:.4f}")
    print(f"|ψ⟩ = {alpha:.4f}|0⟩ + {beta:.4f}|1⟩")
    
    mag_alpha = np.abs(alpha)
    mag_beta = np.abs(beta)
    phase_alpha = np.angle(alpha)
    phase_beta = np.angle(beta)
    
    print(f"\nMagnitudes:")
    print(f"|α| = {mag_alpha:.4f}")
    print(f"|β| = {mag_beta:.4f}")
    
    print(f"\nPhases:")
    print(f"φ_α = {phase_alpha:.4f} rad = {np.degrees(phase_alpha):.1f}°")
    print(f"φ_β = {phase_beta:.4f} rad = {np.degrees(phase_beta):.1f}°")
    print(f"Relative phase: {phase_beta - phase_alpha:.4f} rad = {np.degrees(phase_beta - phase_alpha):.1f}°")
    
    print(f"\nProbabilities:")
    print(f"P(0) = {np.abs(alpha)**2:.4f}")
    print(f"P(1) = {np.abs(beta)**2:.4f}")

def normalization():
    """Demonstrate normalization condition"""
    print("\n" + "=" * 60)
    print("NORMALIZATION CONDITION")
    print("=" * 60)
    
    print("\nFor a valid quantum state: |α|² + |β|² = 1")
    
    alpha1 = 3/5
    beta1 = 4j/5
    norm1 = np.abs(alpha1)**2 + np.abs(beta1)**2
    
    print(f"\nExample 1:")
    print(f"α = {alpha1}, β = {beta1}")
    print(f"|α|² + |β|² = {np.abs(alpha1)**2:.4f} + {np.abs(beta1)**2:.4f} = {norm1:.4f}")
    print(f"Normalized: {np.allclose(norm1, 1)} ✓")
    
    alpha2 = 1
    beta2 = 1
    norm2 = np.abs(alpha2)**2 + np.abs(beta2)**2
    
    print(f"\nExample 2:")
    print(f"α = {alpha2}, β = {beta2}")
    print(f"|α|² + |β|² = {np.abs(alpha2)**2:.4f} + {np.abs(beta2)**2:.4f} = {norm2:.4f}")
    print(f"Normalized: {np.allclose(norm2, 1)} ✗")
    
    norm_factor = np.sqrt(norm2)
    alpha2_norm = alpha2 / norm_factor
    beta2_norm = beta2 / norm_factor
    norm2_fixed = np.abs(alpha2_norm)**2 + np.abs(beta2_norm)**2
    
    print(f"\nAfter normalization:")
    print(f"α = {alpha2_norm:.4f}, β = {beta2_norm:.4f}")
    print(f"|α|² + |β|² = {norm2_fixed:.4f} ✓")

def measurement_simulation():
    """Simulate quantum measurement"""
    print("\n" + "=" * 60)
    print("QUANTUM MEASUREMENT SIMULATION")
    print("=" * 60)
    
    alpha = 3/5
    beta = 4j/5
    
    print(f"\nState: |ψ⟩ = {alpha}|0⟩ + {beta}|1⟩")
    
    prob_0 = np.abs(alpha)**2
    prob_1 = np.abs(beta)**2
    
    print(f"\nTheoretical probabilities:")
    print(f"P(0) = {prob_0:.4f} ({prob_0*100:.1f}%)")
    print(f"P(1) = {prob_1:.4f} ({prob_1*100:.1f}%)")
    
    n_measurements = 10000
    outcomes = np.random.choice([0, 1], size=n_measurements, p=[prob_0, prob_1])
    
    count_0 = np.sum(outcomes == 0)
    count_1 = np.sum(outcomes == 1)
    
    print(f"\nSimulation ({n_measurements} measurements):")
    print(f"Outcome 0: {count_0} times ({count_0/n_measurements*100:.1f}%)")
    print(f"Outcome 1: {count_1} times ({count_1/n_measurements*100:.1f}%)")
    
    print(f"\nExperimental vs Theoretical:")
    print(f"P(0): {count_0/n_measurements:.4f} vs {prob_0:.4f}")
    print(f"P(1): {count_1/n_measurements:.4f} vs {prob_1:.4f}")

def interference():
    """Demonstrate quantum interference"""
    print("\n" + "=" * 60)
    print("QUANTUM INTERFERENCE")
    print("=" * 60)
    
    print("\nConstructive Interference:")
    print("-" * 40)
    amp1 = 1/np.sqrt(2)
    amp2 = 1/np.sqrt(2)
    total = amp1 + amp2
    prob = np.abs(total)**2
    
    print(f"Amplitude 1: {amp1:.4f}")
    print(f"Amplitude 2: {amp2:.4f}")
    print(f"Total amplitude: {total:.4f}")
    print(f"Probability: |{total:.4f}|² = {prob:.4f}")
    print(f"Enhancement factor: {prob / (np.abs(amp1)**2 + np.abs(amp2)**2):.2f}x")
    
    print("\nDestructive Interference:")
    print("-" * 40)
    amp1 = 1/np.sqrt(2)
    amp2 = -1/np.sqrt(2)
    total = amp1 + amp2
    prob = np.abs(total)**2
    
    print(f"Amplitude 1: {amp1:.4f}")
    print(f"Amplitude 2: {amp2:.4f}")
    print(f"Total amplitude: {total:.4f}")
    print(f"Probability: |{total:.4f}|² = {prob:.4f}")
    print(f"Suppression: Complete cancellation!")
    
    print("\nPartial Interference (with phase):")
    print("-" * 40)
    amp1 = 1/np.sqrt(2)
    amp2 = np.exp(1j * np.pi/3) / np.sqrt(2)
    total = amp1 + amp2
    prob = np.abs(total)**2
    
    print(f"Amplitude 1: {amp1:.4f}")
    print(f"Amplitude 2: {amp2:.4f}")
    print(f"Total amplitude: {total:.4f}")
    print(f"Probability: {prob:.4f}")

def bloch_sphere_coordinates():
    """Calculate Bloch sphere coordinates for states"""
    print("\n" + "=" * 60)
    print("BLOCH SPHERE REPRESENTATION")
    print("=" * 60)
    
    print("\nBloch sphere coordinates for standard states:")
    
    states = {
        "|0⟩": (1, 0),
        "|1⟩": (0, 1),
        "|+⟩": (1/np.sqrt(2), 1/np.sqrt(2)),
        "|−⟩": (1/np.sqrt(2), -1/np.sqrt(2)),
        "|R⟩": (1/np.sqrt(2), 1j/np.sqrt(2)),
        "|L⟩": (1/np.sqrt(2), -1j/np.sqrt(2))
    }
    
    for name, (alpha, beta) in states.items():
        
        x = 2 * np.real(alpha * np.conj(beta))
        y = 2 * np.imag(alpha * np.conj(beta))
        z = np.abs(alpha)**2 - np.abs(beta)**2
        
        print(f"\n{name}:")
        print(f"  α = {alpha}, β = {beta}")
        print(f"  Bloch coordinates: ({x:.3f}, {y:.3f}, {z:.3f})")
        print(f"  Radius: {np.sqrt(x**2 + y**2 + z**2):.3f}")

def visualize():
    """Create comprehensive visualizations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig = plt.figure(figsize=(16, 12))
    
    ax1 = plt.subplot(2, 3, 1)
    
    states = {
        "|0⟩": (1, 0, 'blue'),
        "|1⟩": (0, 1, 'red'),
        "|+⟩": (1/np.sqrt(2), 1/np.sqrt(2), 'green'),
        "|−⟩": (1/np.sqrt(2), -1/np.sqrt(2), 'orange'),
        "|R⟩": (1/np.sqrt(2), 1j/np.sqrt(2), 'purple'),
        "|L⟩": (1/np.sqrt(2), -1j/np.sqrt(2), 'brown')
    }
    
    for name, (alpha, beta, color) in states.items():
        ax1.arrow(0, 0, alpha.real, alpha.imag, head_width=0.05, head_length=0.05,
                  fc=color, ec=color, linewidth=2, alpha=0.7, label=f'{name} α')
        ax1.arrow(0, 0, beta.real, beta.imag, head_width=0.05, head_length=0.05,
                  fc=color, ec=color, linewidth=2, alpha=0.4, linestyle='--')
    
    circle = plt.Circle((0, 0), 1, fill=False, color='gray', linestyle='--')
    ax1.add_patch(circle)
    
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Real', fontsize=12)
    ax1.set_ylabel('Imaginary', fontsize=12)
    ax1.set_title('Standard States\nAmplitudes on Complex Plane', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=8, loc='upper right')
    ax1.set_aspect('equal')
    ax1.set_xlim(-1.2, 1.2)
    ax1.set_ylim(-1.2, 1.2)
    
    ax2 = plt.subplot(2, 3, 2)
    
    state_names = list(states.keys())
    probs_0 = [np.abs(states[name][0])**2 for name in state_names]
    probs_1 = [np.abs(states[name][1])**2 for name in state_names]
    
    x = np.arange(len(state_names))
    width = 0.35
    
    ax2.bar(x - width/2, probs_0, width, label='P(0)', color='blue', alpha=0.7)
    ax2.bar(x + width/2, probs_1, width, label='P(1)', color='red', alpha=0.7)
    
    ax2.set_xlabel('State', fontsize=12)
    ax2.set_ylabel('Probability', fontsize=12)
    ax2.set_title('Measurement Probabilities', fontsize=14, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(state_names)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, axis='y')
    
    ax3 = plt.subplot(2, 3, 3)
    
    alpha = 3/5
    beta = 4j/5
    prob_0 = np.abs(alpha)**2
    prob_1 = np.abs(beta)**2
    
    n_measurements = 1000
    outcomes = np.random.choice([0, 1], size=n_measurements, p=[prob_0, prob_1])
    
    running_avg_0 = np.cumsum(outcomes == 0) / np.arange(1, n_measurements + 1)
    running_avg_1 = np.cumsum(outcomes == 1) / np.arange(1, n_measurements + 1)
    
    ax3.plot(running_avg_0, 'b-', linewidth=2, label='Experimental P(0)')
    ax3.axhline(y=prob_0, color='b', linestyle='--', linewidth=2, label='Theoretical P(0)')
    ax3.plot(running_avg_1, 'r-', linewidth=2, label='Experimental P(1)')
    ax3.axhline(y=prob_1, color='r', linestyle='--', linewidth=2, label='Theoretical P(1)')
    
    ax3.set_xlabel('Number of Measurements', fontsize=12)
    ax3.set_ylabel('Probability', fontsize=12)
    ax3.set_title('Measurement Convergence\n|ψ⟩ = (3|0⟩ + 4i|1⟩)/5', fontsize=14, fontweight='bold')
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)
    
    ax4 = plt.subplot(2, 3, 4)
    
    phases = np.linspace(0, 2*np.pi, 100)
    amp1 = 1/np.sqrt(2)
    
    probs = []
    for phase in phases:
        amp2 = np.exp(1j * phase) / np.sqrt(2)
        total = amp1 + amp2
        probs.append(np.abs(total)**2)
    
    ax4.plot(phases, probs, 'b-', linewidth=3)
    ax4.axhline(y=1, color='r', linestyle='--', linewidth=2, label='Classical (no interference)')
    ax4.fill_between(phases, probs, alpha=0.3)
    
    ax4.set_xlabel('Relative Phase (radians)', fontsize=12)
    ax4.set_ylabel('Probability', fontsize=12)
    ax4.set_title('Quantum Interference\nProbability vs Relative Phase', fontsize=14, fontweight='bold')
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)
    ax4.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax4.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
    
    ax5 = plt.subplot(2, 3, 5, projection='3d')
    
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x_sphere = np.outer(np.cos(u), np.sin(v))
    y_sphere = np.outer(np.sin(u), np.sin(v))
    z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
    ax5.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.1, color='gray')
    
    for name, (alpha, beta, color) in states.items():
        x = 2 * np.real(alpha * np.conj(beta))
        y = 2 * np.imag(alpha * np.conj(beta))
        z = np.abs(alpha)**2 - np.abs(beta)**2
        
        ax5.scatter([x], [y], [z], color=color, s=100, label=name)
        ax5.plot([0, x], [0, y], [0, z], color=color, linewidth=2, alpha=0.6)
    
    ax5.set_xlabel('X', fontsize=10)
    ax5.set_ylabel('Y', fontsize=10)
    ax5.set_zlabel('Z', fontsize=10)
    ax5.set_title('Bloch Sphere\nQuantum State Representation', fontsize=14, fontweight='bold')
    ax5.legend(fontsize=8, loc='upper right')
    
    ax6 = plt.subplot(2, 3, 6)
    
    times = np.linspace(0, 2*np.pi, 100)
    E0 = 1.0
    E1 = 1.5
    
    alpha_t = 1/np.sqrt(2) * np.exp(-1j * E0 * times)
    beta_t = 1/np.sqrt(2) * np.exp(-1j * E1 * times)
    
    prob_0_t = np.abs(alpha_t)**2
    prob_1_t = np.abs(beta_t)**2
    
    ax6.plot(times, prob_0_t, 'b-', linewidth=2, label='P(0)')
    ax6.plot(times, prob_1_t, 'r-', linewidth=2, label='P(1)')
    
    ax6.set_xlabel('Time (arbitrary units)', fontsize=12)
    ax6.set_ylabel('Probability', fontsize=12)
    ax6.set_title('Time Evolution\nDifferent Energy Levels', fontsize=14, fontweight='bold')
    ax6.legend(fontsize=10)
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('quantum_states.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'quantum_states.png'")
    plt.close()

def main():
    print("\n" + "⚛️" * 30)
    print("QUANTUM STATES WITH COMPLEX AMPLITUDES")
    print("⚛️" * 30)
    
    demonstrate_qubit_state()
    standard_states()
    complex_amplitudes()
    normalization()
    measurement_simulation()
    interference()
    bloch_sphere_coordinates()
    visualize()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Qubit state: |ψ⟩ = α|0⟩ + β|1⟩")
    print("2. Complex amplitudes α and β")
    print("3. Normalization: |α|² + |β|² = 1")
    print("4. Probability: P(k) = |amplitude|²")
    print("5. Superposition enables quantum parallelism")
    print("6. Phase determines interference patterns")
    print("7. Measurement collapses superposition")
    print("=" * 60)

if __name__ == "__main__":
    main()
