def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Return the matrix product of a and b"""
    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(b[i])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)

    return result