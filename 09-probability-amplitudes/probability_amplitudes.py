"""
Probability Amplitudes and Measurement
Python script demonstrating the Born rule and quantum measurement
"""

import numpy as np
import matplotlib.pyplot as plt

def born_rule():
    """Demonstrate the Born rule"""
    print("=" * 60)
    print("THE BORN RULE: P(outcome) = |amplitude|²")
    print("=" * 60)
    
    alpha = 3/5
    beta = 4j/5
    
    print(f"\nQuantum state: |ψ⟩ = {alpha}|0⟩ + {beta}|1⟩")
    
    prob_0 = np.abs(alpha)**2
    prob_1 = np.abs(beta)**2
    
    print(f"\nAmplitudes:")
    print(f"α = {alpha}")
    print(f"β = {beta}")
    
    print(f"\nMagnitudes:")
    print(f"|α| = {np.abs(alpha):.4f}")
    print(f"|β| = {np.abs(beta):.4f}")
    
    print(f"\nProbabilities (Born rule):")
    print(f"P(0) = |α|² = {prob_0:.4f} ({prob_0*100:.1f}%)")
    print(f"P(1) = |β|² = {prob_1:.4f} ({prob_1*100:.1f}%)")
    print(f"Total: {prob_0 + prob_1:.4f} ✓")

def measurement_simulation():
    """Simulate quantum measurements"""
    print("\n" + "=" * 60)
    print("MEASUREMENT SIMULATION")
    print("=" * 60)
    
    alpha = 1/np.sqrt(2)
    beta = 1/np.sqrt(2)
    
    print(f"\nState: |ψ⟩ = {alpha:.4f}|0⟩ + {beta:.4f}|1⟩")
    
    prob_0 = np.abs(alpha)**2
    prob_1 = np.abs(beta)**2
    
    print(f"\nTheoretical probabilities:")
    print(f"P(0) = {prob_0:.4f}")
    print(f"P(1) = {prob_1:.4f}")
    
    n_measurements = [10, 100, 1000, 10000]
    
    print(f"\nSimulation results:")
    print("-" * 60)
    for n in n_measurements:
        outcomes = np.random.choice([0, 1], size=n, p=[prob_0, prob_1])
        count_0 = np.sum(outcomes == 0)
        count_1 = np.sum(outcomes == 1)
        
        print(f"\n{n} measurements:")
        print(f"  Outcome 0: {count_0} ({count_0/n*100:.1f}%)")
        print(f"  Outcome 1: {count_1} ({count_1/n*100:.1f}%)")
        print(f"  Error: {abs(count_0/n - prob_0):.4f}")

def state_collapse():
    """Demonstrate state collapse"""
    print("\n" + "=" * 60)
    print("STATE COLLAPSE")
    print("=" * 60)
    
    alpha = 1/np.sqrt(2)
    beta = 1/np.sqrt(2)
    psi_before = np.array([alpha, beta])
    
    print(f"\nBefore measurement:")
    print(f"|ψ⟩ = {psi_before}")
    print(f"State is in superposition!")
    
    prob_0 = np.abs(alpha)**2
    outcome = 0 if np.random.random() < prob_0 else 1
    
    print(f"\nMeasurement outcome: {outcome}")
    
    if outcome == 0:
        psi_after = np.array([1, 0])
        print(f"\nAfter measurement:")
        print(f"|ψ⟩ → |0⟩ = {psi_after}")
    else:
        psi_after = np.array([0, 1])
        print(f"\nAfter measurement:")
        print(f"|ψ⟩ → |1⟩ = {psi_after}")
    
    print(f"\nSuperposition has collapsed!")

def interference_demonstration():
    """Demonstrate quantum interference"""
    print("\n" + "=" * 60)
    print("QUANTUM INTERFERENCE")
    print("=" * 60)
    
    print("\nConstructive Interference:")
    print("-" * 40)
    amp1 = 1/np.sqrt(2)
    amp2 = 1/np.sqrt(2)
    total_amp = amp1 + amp2
    prob = np.abs(total_amp)**2
    
    print(f"Path 1 amplitude: {amp1:.4f}")
    print(f"Path 2 amplitude: {amp2:.4f}")
    print(f"Total amplitude: {total_amp:.4f}")
    print(f"Probability: |{total_amp:.4f}|² = {prob:.4f}")
    
    classical_prob = np.abs(amp1)**2 + np.abs(amp2)**2
    print(f"Classical (no interference): {classical_prob:.4f}")
    print(f"Enhancement factor: {prob/classical_prob:.2f}x")
    
    print("\nDestructive Interference:")
    print("-" * 40)
    amp1 = 1/np.sqrt(2)
    amp2 = -1/np.sqrt(2)
    total_amp = amp1 + amp2
    prob = np.abs(total_amp)**2
    
    print(f"Path 1 amplitude: {amp1:.4f}")
    print(f"Path 2 amplitude: {amp2:.4f}")
    print(f"Total amplitude: {total_amp:.4f}")
    print(f"Probability: |{total_amp:.4f}|² = {prob:.4f}")
    print(f"Complete cancellation!")
    
    print("\nPhase-Dependent Interference:")
    print("-" * 40)
    phases = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
    
    for phase in phases:
        amp1 = 1/np.sqrt(2)
        amp2 = np.exp(1j * phase) / np.sqrt(2)
        total_amp = amp1 + amp2
        prob = np.abs(total_amp)**2
        print(f"Phase = {phase:.4f} ({np.degrees(phase):.0f}°): P = {prob:.4f}")

def multi_qubit_probabilities():
    """Demonstrate multi-qubit probabilities"""
    print("\n" + "=" * 60)
    print("MULTI-QUBIT PROBABILITIES")
    print("=" * 60)
    
    print("\nBell State |Φ+⟩ = (|00⟩ + |11⟩)/√2")
    bell_state = np.array([1, 0, 0, 1]) / np.sqrt(2)
    
    print(f"State vector: {bell_state}")
    
    probs = np.abs(bell_state)**2
    print(f"\nProbabilities:")
    print(f"P(00) = {probs[0]:.4f}")
    print(f"P(01) = {probs[1]:.4f}")
    print(f"P(10) = {probs[2]:.4f}")
    print(f"P(11) = {probs[3]:.4f}")
    print(f"Total: {np.sum(probs):.4f} ✓")
    
    print(f"\nPartial measurement (first qubit):")
    prob_first_0 = probs[0] + probs[1]
    prob_first_1 = probs[2] + probs[3]
    print(f"P(first = 0) = {prob_first_0:.4f}")
    print(f"P(first = 1) = {prob_first_1:.4f}")

def amplitude_amplification():
    """Demonstrate amplitude amplification concept"""
    print("\n" + "=" * 60)
    print("AMPLITUDE AMPLIFICATION")
    print("=" * 60)
    
    print("\nGrover's Algorithm Concept:")
    print("-" * 40)
    
    N = 8
    initial_amp = 1/np.sqrt(N)
    print(f"\n1. Start with equal superposition over {N} states")
    print(f"   Each amplitude: {initial_amp:.4f}")
    print(f"   Each probability: {initial_amp**2:.4f}")
    
    marked_amp = -initial_amp
    print(f"\n2. Mark target state (phase flip)")
    print(f"   Target amplitude: {marked_amp:.4f}")
    
    target_amp_final = 0.95
    other_amp_final = -0.05
    print(f"\n3. After ~√N amplification steps:")
    print(f"   Target amplitude: {target_amp_final:.4f}")
    print(f"   Target probability: {target_amp_final**2:.4f}")
    print(f"   Other amplitudes: {other_amp_final:.4f}")
    print(f"   Other probabilities: {other_amp_final**2:.4f}")
    
    print(f"\n4. Measurement gives target with ~90% probability!")

def visualize():
    """Create comprehensive visualizations"""
    print("\n" + "=" * 60)
    print("CREATING VISUALIZATIONS")
    print("=" * 60)
    
    fig = plt.figure(figsize=(16, 12))
    
    ax1 = plt.subplot(2, 3, 1)
    
    amplitudes = np.linspace(-1, 1, 50)
    probabilities = amplitudes**2
    
    ax1.plot(amplitudes, probabilities, 'b-', linewidth=3)
    ax1.fill_between(amplitudes, probabilities, alpha=0.3)
    
    ax1.set_xlabel('Amplitude', fontsize=12)
    ax1.set_ylabel('Probability', fontsize=12)
    ax1.set_title('Born Rule: P = |amplitude|²', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    
    ax2 = plt.subplot(2, 3, 2)
    
    alpha = 3/5
    beta = 4j/5
    prob_0_theory = np.abs(alpha)**2
    prob_1_theory = np.abs(beta)**2
    
    n_measurements = 1000
    outcomes = np.random.choice([0, 1], size=n_measurements, p=[prob_0_theory, prob_1_theory])
    
    running_avg_0 = np.cumsum(outcomes == 0) / np.arange(1, n_measurements + 1)
    running_avg_1 = np.cumsum(outcomes == 1) / np.arange(1, n_measurements + 1)
    
    ax2.plot(running_avg_0, 'b-', linewidth=2, label='Experimental P(0)')
    ax2.axhline(y=prob_0_theory, color='b', linestyle='--', linewidth=2, label='Theoretical P(0)')
    ax2.plot(running_avg_1, 'r-', linewidth=2, label='Experimental P(1)')
    ax2.axhline(y=prob_1_theory, color='r', linestyle='--', linewidth=2, label='Theoretical P(1)')
    
    ax2.set_xlabel('Number of Measurements', fontsize=12)
    ax2.set_ylabel('Probability', fontsize=12)
    ax2.set_title('Measurement Convergence', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    
    ax3 = plt.subplot(2, 3, 3)
    
    phases = np.linspace(0, 2*np.pi, 100)
    amp1 = 1/np.sqrt(2)
    
    probs = []
    for phase in phases:
        amp2 = np.exp(1j * phase) / np.sqrt(2)
        total = amp1 + amp2
        probs.append(np.abs(total)**2)
    
    ax3.plot(phases, probs, 'b-', linewidth=3)
    ax3.axhline(y=1, color='r', linestyle='--', linewidth=2, label='Classical (no interference)')
    ax3.fill_between(phases, probs, alpha=0.3)
    
    ax3.set_xlabel('Relative Phase (radians)', fontsize=12)
    ax3.set_ylabel('Probability', fontsize=12)
    ax3.set_title('Quantum Interference Pattern', fontsize=14, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)
    ax3.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax3.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
    
    ax4 = plt.subplot(2, 3, 4)
    
    stages = ['Before\nMeasurement', 'Measurement', 'After\nMeasurement']
    probs_before = [0.5, 0.5]
    probs_after = [1.0, 0.0]  # Assuming outcome 0
    
    x = np.arange(2)
    width = 0.35
    
    ax4.bar(x - width, probs_before, width, label='Before', alpha=0.7, color='purple')
    ax4.bar(x, [0.5, 0.5], width, label='During', alpha=0.5, color='gray')
    ax4.bar(x + width, probs_after, width, label='After', alpha=0.7, color='blue')
    
    ax4.set_xlabel('Outcome', fontsize=12)
    ax4.set_ylabel('Probability', fontsize=12)
    ax4.set_title('State Collapse During Measurement', fontsize=14, fontweight='bold')
    ax4.set_xticks(x)
    ax4.set_xticklabels(['|0⟩', '|1⟩'])
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3, axis='y')
    
    ax5 = plt.subplot(2, 3, 5)
    
    bell_state = np.array([1, 0, 0, 1]) / np.sqrt(2)
    probs = np.abs(bell_state)**2
    
    ax5.bar(range(4), probs, color=['blue', 'red', 'green', 'orange'], alpha=0.7)
    ax5.set_xlabel('Basis State', fontsize=12)
    ax5.set_ylabel('Probability', fontsize=12)
    ax5.set_title('Bell State Probabilities\n|Φ+⟩ = (|00⟩ + |11⟩)/√2', fontsize=14, fontweight='bold')
    ax5.set_xticks(range(4))
    ax5.set_xticklabels(['|00⟩', '|01⟩', '|10⟩', '|11⟩'])
    ax5.grid(True, alpha=0.3, axis='y')
    
    ax6 = plt.subplot(2, 3, 6)
    
    N = 8
    steps = np.arange(0, 4)
    
    target_probs = []
    other_probs = []
    
    for step in steps:
        if step == 0:
            target_probs.append(1/N)
            other_probs.append(1/N)
        else:
            target_probs.append(min(1.0, target_probs[-1] * 2.5))
            other_probs.append(max(0.0, (1 - target_probs[-1]) / (N-1)))
    
    ax6.plot(steps, target_probs, 'bo-', linewidth=3, markersize=10, label='Target state')
    ax6.plot(steps, other_probs, 'ro-', linewidth=2, markersize=8, label='Other states')
    
    ax6.set_xlabel('Grover Iterations', fontsize=12)
    ax6.set_ylabel('Probability', fontsize=12)
    ax6.set_title('Amplitude Amplification\n(Simplified Grover)', fontsize=14, fontweight='bold')
    ax6.legend(fontsize=10)
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('probability_amplitudes.png', dpi=150, bbox_inches='tight')
    print("✓ Saved as 'probability_amplitudes.png'")
    plt.close()

def main():
    print("\n" + "📊" * 30)
    print("PROBABILITY AMPLITUDES AND MEASUREMENT")
    print("📊" * 30)
    
    born_rule()
    measurement_simulation()
    state_collapse()
    interference_demonstration()
    multi_qubit_probabilities()
    amplitude_amplification()
    visualize()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Born rule: P(outcome) = |amplitude|²")
    print("2. Amplitudes can be complex, probabilities are real")
    print("3. Measurement collapses superposition")
    print("4. Amplitudes add, then square for probability")
    print("5. Interference: constructive and destructive")
    print("6. Multi-qubit: probabilities for all basis states")
    print("7. Amplitude amplification enables quantum speedup")
    print("=" * 60)

if __name__ == "__main__":
    main()
