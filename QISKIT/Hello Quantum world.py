from qiskit import QuantumCircuit, transpile, Aer, assemble

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to create a superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Simulate the quantum circuit
sim = Aer.get_backend('aer_simulator')
compiled_circuit = transpile(qc, sim)
result = sim.run(assemble(compiled_circuit)).result()

# Display the result
print(result.get_counts())
