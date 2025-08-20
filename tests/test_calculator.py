import pytest
from toolbox.calculator import calculate


def test_arithmetic():
    assert calculate("2 * (3 + 4) ** 2") == 98
    assert calculate("-5 + 3") == -2
    assert calculate("17 % 5") == 2
    assert calculate("7 // 2") == 3


def test_rejects_code_and_names():
    for bad in ["__import__('os')", "a + 1", "len('x')", "1; 2", "x.y", "[1,2][0]"]:
        with pytest.raises(ValueError):
            calculate(bad)


def test_division_by_zero():
    with pytest.raises(ValueError):
        calculate("1/0")
