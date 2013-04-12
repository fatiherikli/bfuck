Brainfuck interpreter


    >>> from bfuck import interpret
    >>> tape = [0, 0, 0]
    >>> interpret("++>++>+><<+", tape)
    >>> tape
    [2, 3, 1]

