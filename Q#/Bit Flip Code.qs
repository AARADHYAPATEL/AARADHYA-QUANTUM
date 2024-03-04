// Bit flip quantum error correction
operation BitFlipCode() : Unit {
    using (qubits = Qubit[3]) {
        X(qubits[0]);
        Controlled X([qubits[0]], qubits[1]);
        Controlled X([qubits[0]], qubits[2]);
        // Error on qubits[1]
        X(qubits[1]);
        // Correct the error
        Controlled X([qubits[0]], qubits[1]);
        Controlled X([qubits[0]], qubits[2]);
    }
}
