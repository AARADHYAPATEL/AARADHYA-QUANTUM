from braket.circuits import Circuit
from braket.devices import LocalSimulator

def superdense_coding():
    circuit = Circuit().h(0).cnot(0, 1).x(0).z(0)
    simulator = LocalSimulator()
    result = simulator.run(circuit, shots=1).result()

    print("Superdense Coding Result:")
    print("Measurement result:", result.measurement_counts)

superdense_coding()
