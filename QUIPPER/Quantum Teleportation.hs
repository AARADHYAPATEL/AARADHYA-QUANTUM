import Quipper

teleport :: (Qubit, Qubit, Qubit) -> Circ (Qubit, Qubit, Qubit)
teleport (alice, bob, msg) = do
    entanglement (alice, bob)
    qnot_at msg `controlled` alice
    hadamard_at msg
    bob <- observe_at Bob True bob
    msg <- observe_at Bob True msg
    return (alice, bob, msg)

main :: IO ()
main = print_simple Preview (teleport . triple) 
