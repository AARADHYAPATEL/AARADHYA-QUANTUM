from braket.circuits import Circuit
from braket.devices import LocalSimulator

def quantum_fourier_transform():
    circuit = Circuit().h(0).cphaseshift(1, 0, 1 / 2).cphaseshift(2, 0, 1 / 4).cphaseshift(2, 1, 1 / 2)
    simulator = LocalSimulator()
    result = simulator.run(circuit, shots=1).result()

    print("Quantum Fourier Transform applied to qubits:")
    print("Measurement result:", result.measurement_counts)

quantum_fourier_transform()
