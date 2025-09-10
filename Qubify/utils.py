import numpy as np

"""
utils.py
--------
Helper functions for measurement and visualization.
"""

def measure(state, num_shots=1):
    """
    Measure a quantum state in the computational basis.
    Returns bitstring results.
    """
    num_qubits = int(np.log2(len(state)))
    probabilities = np.abs(state) ** 2

    outcomes = np.random.choice(
        range(len(state)),
        size=num_shots,
        p=probabilities
    )

    # Convert outcomes to binary strings
    return [format(o, f'0{num_qubits}b') for o in outcomes]
