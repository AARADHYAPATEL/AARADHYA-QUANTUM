// Quantum teleportation algorithm
operation Teleportation() : Unit {
    using ((msg, alice, bob) = (Qubit(), Qubit(), Qubit())) {
        H(alice);
        CNOT(alice, bob);
        H(alice);
        CNOT(msg, alice);
        CZ(alice, bob);
    }
}
