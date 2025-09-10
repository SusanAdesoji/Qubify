import numpy as np
from .states.py import normalize
from .gates import apply_gate

"""
circuit.py
----------
Defines a simple quantum circuit class that stores states and gates.
"""

class QuantumCircuit:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = None
        self.gates = []

    def set_state(self, state):
        self.state = normalize(state)

    def add_gate(self, gate):
        self.gates.append(gate)

    def run(self):
        """
        Apply all gates in sequence to the state
        """
        state = self.state
        for gate in self.gates:
            state = apply_gate(state, gate)
        self.state = normalize(state)
        return self.state
