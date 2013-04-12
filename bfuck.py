def run(source, tape):
    tokens = [c for c in source if c in '<>-+.,[]']
    jumps = []
    pointer, action = 0, 0
    while action < len(tokens):
        token = tokens[action]
        if token == "<":
            pointer -= 1
        elif token == ">":
            pointer += 1
        elif token == "-":
            tape[pointer] -= 1
        elif token == "+":
            tape[pointer] += 1
        elif token == ",":
            tape[pointer] = ord(raw_input()[0])
        elif token == ".":
            print chr(tape[pointer])
        elif token == "[":
            jumps.append(action)
        elif token == "]":
            if tape[pointer] > 0:
                action = jumps[-1]
            else:
                jumps.pop()
        action += 1

run("""

+++++ +++++             initialize counter (cell #0) to 10
[                       use loop to set the next four cells to 70/100/30/10
    > +++++ ++              add  7 to cell #1
    > +++++ +++++           add 10 to cell #2
    > +++                   add  3 to cell #3
    > +                     add  1 to cell #4
    <<<< -                  decrement counter (cell #0)
]
> ++ .                  print 'H'
> + .                   print 'e'
+++++ ++ .              print 'l'
.                       print 'l'
+++ .                   print 'o'
> ++ .                  print ' '
<< +++++ +++++ +++++ .  print 'W'
> .                     print 'o'
+++ .                   print 'r'
----- - .               print 'l'
----- --- .             print 'd'
> + .                   print '!'
> .                     print '\n'
""", [0] * 3000)
