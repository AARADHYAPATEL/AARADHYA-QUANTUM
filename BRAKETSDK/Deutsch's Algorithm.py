from braket.circuits import Circuit
from braket.devices import LocalSimulator

def deutsch_algorithm(is_constant):
    circuit = Circuit().h(0)

    if is_constant:
        circuit.x(0)

    simulator = LocalSimulator()
    result = simulator.run(circuit, shots=1).result()

    print("Deutsch's Algorithm Result:")
    print("Measurement result:", result.measurement_counts)

deutsch_algorithm(True)
