import cirq
import numpy as np

# Define a simple VQE circuit
qubit = cirq.GridQubit(0, 0)
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Parametrized gate
    cirq.measure(qubit, key='result')
)

# Evaluate the circuit for different parameter values
for angle in np.linspace(0, 2*np.pi, 10):
    resolver = cirq.ParamResolver({'θ': angle})
    result = cirq.Simulator().run(circuit, resolver=resolver)
    print(f"θ={angle}: {result.measurements['result'][0]}")
