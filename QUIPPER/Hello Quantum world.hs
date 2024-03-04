import Quipper

hello :: Qubit -> Circ Qubit
hello q = do
    hadamard q
    return q

main :: IO ()
main = print_simple Preview hello
