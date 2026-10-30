import math


def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Return the matrix product of a and b"""
    if not a or not b:
        raise ValueError("matrices must be non-empty")
    if not isinstance(a, list) or not all(isinstance(row, list) for row in a):
        raise ValueError("a must be a list of rows")
    if not isinstance(b, list) or not all(isinstance(row, list) for row in b):
        raise ValueError("b must be a list of rows")

    if not all(
        isinstance(value, (int, float)) and not isinstance(value, bool)
        and math.isfinite(value)
        for matrix in (a, b)
        for row in matrix
        for value in row
    ):
        raise ValueError("matrix entries must be numbers")

    if len(a[0]) == 0 or len(b[0]) == 0:
        raise ValueError("matrices must have at least one column")

    if len(a) == 0 or len(b) == 0:
        raise ValueError("use non-empty matrices")
    if len(a[0]) != len(b):
        raise ValueError("columns of a must match rows of b")
    for row in a:
        if len(row) != len(a[0]):
            raise ValueError("a must be a rectangular")
    for row in b:
        if len(row) != len(b[0]):
            raise ValueError("b must be a rectangular")
    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)

    return result