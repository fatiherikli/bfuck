from functools import partial


def interpret(source, tape):
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


run = partial(interpret, tape=[0] * 3000)
