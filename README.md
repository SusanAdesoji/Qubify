# Qubify 🧩⚡

![Qubify Banner](./A_2D_digital_illustration_infographic_illustrates_.png)

A lightweight **quantum computing simulator** built from scratch using **NumPy**.  
Qubify is an educational project to explore the fundamentals of **quantum information** — qubits, gates, superposition, entanglement, and measurement — while learning efficient **NumPy array operations**, **linear algebra**, and advanced tools like `einsum` and `fft`.

---

## 🚀 Features
- Represent **qubit states** as NumPy complex arrays  
- Apply **single- and multi-qubit gates** (H, X, Z, CNOT, SWAP, …)  
- Simulate **superposition** and **entanglement**  
- Perform **projective measurements** with Born rule sampling  
- Build and execute **quantum circuits**  
- Optimize large circuits with `einsum`, sparse ops, and gate fusion  
- Visualize **probabilities**, **Bloch spheres**, and simple **circuit diagrams**  

---

## 🛠 Installation
Clone the repo:
```bash
git clone git@github.com:SusanAdesoji/Qubify.git
cd Qubify
Install dependencies:

bash
Copy code
pip install -r requirements.txt
📖 Usage
Run a simple test script:

bash
Copy code
python Qubify/main.py
Or open the project in Jupyter:

bash
Copy code
jupyter notebook
📚 Roadmap
 Project scaffold & environment setup

 State-vector representation

 Basic single-qubit gates (X, Y, Z, H, S, T, rotations)

 Multi-qubit gates (CNOT, CZ, SWAP)

 Measurement & sampling

 Circuit builder class

 Visualization (probabilities, Bloch sphere, ASCII circuits)

 Noise models (Kraus ops, Monte Carlo)

 Optimizations (einsum, gate fusion, sparse ops, GPU)

 CLI tool (qsim run circuit.yaml)

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a feature branch

Submit a Pull Request with tests

📜 License
MIT License © 2025 Susan Adesoji
