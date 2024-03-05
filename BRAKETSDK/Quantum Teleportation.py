from braket.circuits import Circuit
from braket.devices import LocalSimulator

def quantum_teleportation():
    circuit = Circuit().h(1).cnot(1, 2).h(0).cnot(0, 1).cnot(1, 2)
    simulator = LocalSimulator()
    result = simulator.run(circuit, shots=1).result()

    print("Teleported qubit:")
    print("Measurement result:", result.measurement_counts)

quantum_teleportation()
