# Standard Library
from fractions import Fraction as Frac
from typing import List

ONE = Frac(1, 1)
ZERO = Frac(0, 1)
FracVec = List[Frac]
FracMatrix = List[FracVec]

def fail_msg(where: str, issue: str, expected: Any, got: Any) -> str:
    return f"[FAIL] [{where}] {issue}, EXPECTED: {expected}, GOT: {got}"

def print_heading(heading: str) -> None:
    print(heading, '\n', '-' * len(heading))

def print_matrix(m: FracMatrix) -> None:
    for i in range(len(m)):
        print('[ ', end='')
        for j in range(len(m[i])):
            print("%2.2f" % float(m[i][j]), end=' ')
        print(']')