// Creating an entangled pair of qubits
operation Entanglement() : Unit {
    using (qubits = (Qubit(), Qubit())) {
        H(qubits[0]);
        CNOT(qubits[0], qubits[1]);
    }
}
