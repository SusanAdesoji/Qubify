import numpy as np

"""
gates.py
--------
Defines common quantum gates as NumPy matrices.
"""

# Single-qubit gates
I = np.array([[1, 0], [0, 1]], dtype=complex)  # Identity
X = np.array([[0, 1], [1, 0]], dtype=complex)  # Pauli-X (NOT)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)  # Pauli-Y
Z = np.array([[1, 0], [0, -1]], dtype=complex)  # Pauli-Z
H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)  # Hadamard

# Two-qubit gates
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], dtype=complex)

SWAP = np.array([
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
], dtype=complex)

def apply_gate(state, gate, num_qubits=1, target_qubits=None):
    """
    Apply a gate to a quantum state.
    For now: works only with full-size gates (no decomposition).
    """
    return gate @ state
