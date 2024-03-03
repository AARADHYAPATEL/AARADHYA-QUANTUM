from qiskit import QuantumCircuit, Aer, transpile, assemble

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2, 2)

# Apply Hadamard gate and CNOT gate to create entanglement
qc.h(0)
qc.cx(0, 1)

# Measure the qubits
qc.measure([0, 1], [0, 1])

# Simulate the quantum circuit
sim = Aer.get_backend('aer_simulator')
compiled_circuit = transpile(qc, sim)
result = sim.run(assemble(compiled_circuit)).result()

# Display the result
print(result.get_counts())
