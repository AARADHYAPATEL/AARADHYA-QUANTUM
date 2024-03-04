// Superdense coding algorithm
operation SuperdenseCoding(message: Int) : Unit {
    using ((alice, bob) = (Qubit(), Qubit())) {
        H(alice);
        CNOT(alice, bob);
        if (message == 1) {
            Z(alice);
        }
        if (message == 2) {
            X(alice);
        }
        CNOT(alice, bob);
        H(alice);
    }
}
