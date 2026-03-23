"""
Tests for the sample Guardian test app.
pytest will run these during Jenkins build.
"""

import numpy as np


def test_numpy_mean():
    arr = np.array([1, 2, 3, 4, 5])
    assert np.mean(arr) == 3.0


def test_numpy_sum():
    arr = np.array([1, 2, 3, 4, 5])
    assert np.sum(arr) == 15


def test_numpy_shape():
    arr = np.array([[1, 2], [3, 4]])
    assert arr.shape == (2, 2)


def test_basic_math():
    assert 1 + 1 == 2


def test_string_ops():
    msg = "guardian test"
    assert msg.upper() == "GUARDIAN TEST"
    assert len(msg) == 13
