from . import states, gates, utils, circuit

def main():
    print("🚀 Welcome to Qubify — Quantum Simulator")

    # Example: create |0> state and apply Hadamard
    qc = circuit.QuantumCircuit(1)
    qc.set_state(states.zero)
    qc.add_gate(gates.H)
    final_state = qc.run()

    print("Final state vector:", final_state)
    results = utils.measure(final_state, num_shots=10)
    print("Measurement results:", results)

if __name__ == "__main__":
    main()
