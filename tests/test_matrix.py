from aster.matrix import multiply

import pytest

def test_multiply_two_square_matrices():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    result = multiply(a, b)
    assert result == [[19, 22], [43, 50]]



def test_multiply_rectangular_matrices():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]

    assert multiply(a, b) == [[58, 64], [139, 154]]

def test_multiply_rejects_incompatible_dimensions():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10]]

    with pytest.raises(ValueError, match="columns.*rows"):
        multiply(a, b)

def test_multiply_rejects_empty_matrix():
    with pytest.raises(ValueError, match="non-empty"):
        multiply([], [[1]])