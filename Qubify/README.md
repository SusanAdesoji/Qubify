---

```markdown
#### Qubify 🧩⚡

![Qubify Banner](./Qubify/readme.png)

Qubify is a lightweight **quantum computing simulator** built from scratch using **NumPy**.  
The goal is to explore the foundations of quantum computing — **qubits, gates, superposition, entanglement, and measurement** — while practicing efficient **NumPy array operations**, **linear algebra**, and optimization techniques like `einsum` and `fft`.

---

#### Features
- Represent **qubit states** as NumPy complex arrays  
- Apply **single- and multi-qubit gates** (H, X, Z, CNOT, SWAP, …)  
- Simulate **superposition** and **entanglement**  
- Perform **projective measurements** with Born rule sampling  
- Build and execute **quantum circuits** step-by-step  
- Visualize **probabilities** and results (with matplotlib)  
- Educational and extensible — build your own gates & circuits  

---

#### Project Structure
```

Qubify/
│── **init**.py        # Package initialization
│── main.py            # Entry point for simple tests
│── states.py          # Define qubit states (|0>, |1>, superpositions)
│── gates.py           # Quantum gate matrices (X, H, CNOT, etc.)
│── utils.py           # Helper functions (tensor products, normalization)
│── circuit.py         # Circuit builder/execution engine
tests/
│── test\_states.py
│── test\_gates.py
│── test\_circuit.py
requirements.txt
.gitignore
README.md

````

---

#### Installation
Clone the repo:
```bash
git clone git@github.com:SusanAdesoji/Qubify.git
cd Qubify
````

Install dependencies:

```bash
pip install -r requirements.txt
```

---

Run a simple test:

```bash
python -m Qubify.main
```

Example output:

```
Welcome to Qubify — Quantum Simulator
Final state vector: [0.70710678+0.j 0.70710678+0.j]
Measurement results: ['0', '1', '0', '1', ...]
```

* [x] State-vector representation
* [x] Basic single-qubit gates
* [ ] Multi-qubit gates (CNOT, CZ, SWAP)
* [ ] Measurement & sampling
* [ ] Circuit builder class
* [ ] Visualization (probabilities, Bloch sphere, ASCII diagrams)
* [ ] Noise models (Kraus operators)
* [ ] Optimizations (`einsum`, sparse ops, GPU acceleration)

---
Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Submit a Pull Request

---
MIT License © 2025 **Susan Adesoji**

```