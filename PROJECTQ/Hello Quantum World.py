from projectq import MainEngine

def hello_quantum_world():
    eng = MainEngine()
    print("Hello Quantum World!")
    eng.flush()

hello_quantum_world()
