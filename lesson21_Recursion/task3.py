from typing import Optional
# def mult(a: int, n: int) -> int:
#     """
#     This function works only with positive integers
#
#     >>> mult(2, 4) == 8
#     True
#
#     >>> mult(2, 0) == 0
#     True
#
#     >>> mult(2, -4)
#     ValueError("This function works only with postive integers")
#     """
def mult(a: int, b: int) -> int:
    if b < 0:
        raise ValueError("This function works only with exp > 0")
    if b == 0:
        return 1
    return b + mult(b, a -1)

print(mult(2, 4))
print(mult(2, 0))
print(mult(2, -4))