from braket.circuits import Circuit
from braket.devices import LocalSimulator

def grover_search():
    circuit = Circuit().h(0).h(1).h(2).x(2).h(2).cnot(0, 1).h(2).cnot(1, 2).h(2).cnot(0, 1).h(1).cnot(1, 2).h(2)
    simulator = LocalSimulator()
    result = simulator.run(circuit, shots=1).result()

    print("Grover's Search Result:")
    print("Measurement result:", result.measurement_counts)

grover_search()
