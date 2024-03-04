import Quipper

deutsch :: (Qubit, Qubit) -> Circ (Qubit, Qubit)
deutsch (input, output) = do
    hadamard input
    x <- qinit False
    hadamard x `controlled` input
    return (input, output)

main :: IO ()
main = print_simple Preview (deutsch . pair) 
