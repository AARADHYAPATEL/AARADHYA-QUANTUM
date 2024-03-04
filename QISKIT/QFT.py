from qiskit import QuantumCircuit, Aer, transpile, assemble
import numpy as np

def qft(n):
    qc = QuantumCircuit(n)
    for j in range(n):
        for k in range(j):
            qc.cp(np.pi/float(2**(j-k)), k, j)
        qc.h(j)
    return qc

# Create a 4-qubit QFT circuit
n = 4
qft_circuit = qft(n)

# Simulate the QFT circuit
sim = Aer.get_backend('aer_simulator')
compiled_circuit = transpile(qft_circuit, sim)
result = sim.run(assemble(compiled_circuit)).result()

# Display the result
print(result.get_counts())
