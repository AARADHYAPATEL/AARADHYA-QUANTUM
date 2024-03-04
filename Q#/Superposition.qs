// Creating a superposition state
operation Superposition() : Unit {
    using (qubit = Qubit()) {
        H(qubit);
    }
}
