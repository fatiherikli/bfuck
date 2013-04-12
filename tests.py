import unittest

from bfuck import interpret


class InterpreterTest(unittest.TestCase):

    def test_increment(self):
        tape = [0]
        interpret("+", tape)
        self.assertEqual(tape, [1])

    def test_decrement(self):
        tape = [1]
        interpret("-", tape)
        self.assertEqual(tape, [0])

    def test_pointer(self):
        tape = [1, 2]
        interpret(">-<+", tape)
        self.assertEqual(tape, [2, 1])

    def test_jumps(self):
        tape = [0, 0]
        interpret("+++[>+<-]", tape)
        self.assertEqual(tape, [0, 3])

unittest.main()
