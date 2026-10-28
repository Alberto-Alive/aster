from aster.matrix import multiply



def test_multiply_two_square_matrices():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    result = multiply(a, b)
    assert result == [[19, 22], [43, 50]]