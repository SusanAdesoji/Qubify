import numpy as np 

"""
states.py
----------
Defines basic qubit states and utilities for creating multi-qubit systems.

"""

# Single-qubit basis states
zero = np.array([1, 0], dtype=complex)  # |0>
one = np.array([0, 1], dtype=complex)   # |1>

import numpy as np

"""
states.py
----------
Defines basic qubit states and utilities for creating multi-qubit systems.
"""

# Single-qubit basis states
zero = np.array([1, 0], dtype=complex)  # |0>
one = np.array([0, 1], dtype=complex)   # |1>

def tensor_product(*states):
    """
    Compute the tensor product of multiple states.
    Example: tensor_product(zero, one) = |01>
    """
    result = states[0]
    for state in states[1:]:
        result = np.kron(result, state)
    return result

def normalize(state):
    """
    Normalize a quantum state vector.
    """
    norm = np.linalg.norm(state)
    if norm == 0:
        raise ValueError("State vector has zero norm.")
    return state / norm


