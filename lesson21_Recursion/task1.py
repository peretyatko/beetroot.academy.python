from typing import Optional
# def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
#     """
#     Returns  x ^ exp
#
#     >>> to_power(2, 3) == 8
#     True
#
#     >>> to_power(3.5, 2) == 12.25
#     True
#
#     >>> to_power(2, -1)
#     ValueError: This function works only with exp > 0.
#     """
#     pass

def to_power(b, n):
    if n < 0:
        raise ValueError("This function works only with exp > 0")
    if n == 0:
        return 1
    return b * to_power(b, n-1)

print(to_power(2, 3))
print(to_power(3.5, 2))
print(to_power(2, -1))