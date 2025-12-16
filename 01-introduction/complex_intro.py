"""
Introduction to Complex Numbers in Quantum Computing
Python script demonstrating why complex numbers are essential
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def demonstrate_real_vs_complex():
    """Show why real numbers are insufficient for quantum mechanics"""
    print("=" * 60)
    print("WHY COMPLEX NUMBERS IN QUANTUM COMPUTING?")
    print("=" * 60)
    
    real_number = 5.0
    print(f"\nReal number: {real_number}")
    print(f"Information: Magnitude only = {abs(real_number)}")
    
    complex_number = 3 + 4j
    magnitude = np.abs(complex_number)
    phase = np.angle(complex_number)
    
    print(f"\nComplex number: {complex_number}")
    print(f"Information: Magnitude = {magnitude:.2f}, Phase = {phase:.2f} radians ({np.degrees(phase):.2f}°)")
    print("\n✓ Complex numbers encode BOTH magnitude and phase!")

def quantum_state_example():
    """Demonstrate quantum states with complex amplitudes"""
    print("\n" + "=" * 60)
    print("QUANTUM STATE REPRESENTATION")
    print("=" * 60)
    
    alpha = 1/np.sqrt(2)  # Amplitude for |0⟩
    beta = 1j/np.sqrt(2)  # Amplitude for |1⟩ with phase
    
    print(f"\nQuantum state: |ψ⟩ = α|0⟩ + β|1⟩")
    print(f"α = {alpha:.4f} (real)")
    print(f"β = {beta:.4f} (imaginary)")
    
    prob_0 = np.abs(alpha)**2
    prob_1 = np.abs(beta)**2
    
    print(f"\nMeasurement probabilities:")
    print(f"P(|0⟩) = |α|² = {prob_0:.4f}")
    print(f"P(|1⟩) = |β|² = {prob_1:.4f}")
    print(f"Total probability = {prob_0 + prob_1:.4f} ✓")
    
    phase_alpha = np.angle(alpha)
    phase_beta = np.angle(beta)
    relative_phase = phase_beta - phase_alpha
    
    print(f"\nPhase information:")
    print(f"Phase of α = {np.degrees(phase_alpha):.2f}°")
    print(f"Phase of β = {np.degrees(phase_beta):.2f}°")
    print(f"Relative phase = {np.degrees(relative_phase):.2f}°")
    print("\n✓ The relative phase affects interference patterns!")

def interference_demonstration():
    """Show how complex phases create interference"""
    print("\n" + "=" * 60)
    print("QUANTUM INTERFERENCE")
    print("=" * 60)
    
    state_plus = (1/np.sqrt(2)) * np.array([1, 1])  # |+⟩ = (|0⟩ + |1⟩)/√2
    state_minus = (1/np.sqrt(2)) * np.array([1, -1])  # |−⟩ = (|0⟩ − |1⟩)/√2
    
    print("\nState |+⟩ = (|0⟩ + |1⟩)/√2")
    print(f"Amplitudes: {state_plus}")
    print("→ Constructive interference (positive phase)")
    
    print("\nState |−⟩ = (|0⟩ − |1⟩)/√2")
    print(f"Amplitudes: {state_minus}")
    print("→ Destructive interference (negative phase)")
    
    print("\n✓ Same probabilities, different interference!")
    print(f"  |+⟩: P(0) = P(1) = 0.5")
    print(f"  |−⟩: P(0) = P(1) = 0.5")
    print("  But they behave differently under quantum gates!")

def quantum_gate_example():
    """Demonstrate quantum gates with complex numbers"""
    print("\n" + "=" * 60)
    print("QUANTUM GATES WITH COMPLEX NUMBERS")
    print("=" * 60)
    
    S_gate = np.array([[1, 0], 
                       [0, 1j]], dtype=complex)
    
    print("\nS Gate (Phase gate):")
    print(S_gate)
    
    state_1 = np.array([0, 1], dtype=complex)
    result = S_gate @ state_1
    
    print(f"\nApplying S to |1⟩:")
    print(f"Before: {state_1}")
    print(f"After:  {result}")
    print(f"\n✓ The state gains a phase of i (90° rotation)!")
    
    T_gate = np.array([[1, 0], 
                       [0, np.exp(1j * np.pi/4)]], dtype=complex)
    
    print("\nT Gate (π/8 gate):")
    print(T_gate)
    print(f"\n✓ Applies a phase of e^(iπ/4) = {np.exp(1j * np.pi/4):.4f}")

def visualize_complex_plane():
    """Create visualization of complex numbers in quantum context"""
    print("\n" + "=" * 60)
    print("VISUALIZING COMPLEX AMPLITUDES")
    print("=" * 60)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.set_xlabel('Real Part', fontsize=12)
    ax1.set_ylabel('Imaginary Part', fontsize=12)
    ax1.set_title('Complex Amplitudes in Quantum States', fontsize=14, fontweight='bold')
    
    amplitudes = [
        (1/np.sqrt(2), 0, '|0⟩ component'),
        (0, 1/np.sqrt(2), '|1⟩ component'),
        (1/np.sqrt(2) * np.exp(1j * np.pi/4), 'Rotated amplitude'),
        (1/np.sqrt(2) * np.exp(1j * np.pi/2), 'i/√2'),
    ]
    
    colors = ['blue', 'red', 'green', 'purple']
    for (amp, label), color in zip(amplitudes[:3], colors):
        if isinstance(amp, complex):
            ax1.arrow(0, 0, amp.real, amp.imag, head_width=0.08, head_length=0.08,
                     fc=color, ec=color, linewidth=2, label=label)
            ax1.plot(amp.real, amp.imag, 'o', color=color, markersize=10)
    
    theta = np.linspace(0, 2*np.pi, 100)
    ax1.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3, linewidth=1)
    ax1.legend(fontsize=10)
    
    ax2.set_xlim(0, 2*np.pi)
    ax2.set_ylim(0, 1.2)
    ax2.set_xlabel('Phase (radians)', fontsize=12)
    ax2.set_ylabel('Magnitude', fontsize=12)
    ax2.set_title('Magnitude and Phase of Quantum Amplitudes', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    phases = np.linspace(0, 2*np.pi, 50)
    magnitude = 1/np.sqrt(2)  # Normalized amplitude
    
    ax2.plot(phases, [magnitude]*len(phases), 'b-', linewidth=2, label='Constant magnitude')
    ax2.scatter([0, np.pi/4, np.pi/2, np.pi], [magnitude]*4, 
               c=['blue', 'green', 'purple', 'red'], s=100, zorder=5)
    
    special_phases = [0, np.pi/4, np.pi/2, np.pi]
    labels = ['0', 'π/4', 'π/2', 'π']
    for phase, label in zip(special_phases, labels):
        ax2.annotate(label, (phase, magnitude), xytext=(phase, magnitude+0.1),
                    fontsize=10, ha='center')
    
    ax2.legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig('complex_amplitudes_visualization.png', dpi=150, bbox_inches='tight')
    print("\n✓ Visualization saved as 'complex_amplitudes_visualization.png'")
    plt.close()

def main():
    """Run all demonstrations"""
    print("\n" + "🌀" * 30)
    print("COMPLEX NUMBERS IN QUANTUM COMPUTING")
    print("Mathematical Foundation and Physical Significance")
    print("🌀" * 30)
    
    demonstrate_real_vs_complex()
    quantum_state_example()
    interference_demonstration()
    quantum_gate_example()
    visualize_complex_plane()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("1. Complex numbers encode BOTH magnitude and phase")
    print("2. Quantum states require complex amplitudes")
    print("3. Phase differences create interference patterns")
    print("4. Quantum gates manipulate complex phases")
    print("5. Real numbers alone cannot describe quantum mechanics")
    print("\n✓ Complex numbers are FUNDAMENTAL to quantum computing!")
    print("=" * 60)

if __name__ == "__main__":
    main()
