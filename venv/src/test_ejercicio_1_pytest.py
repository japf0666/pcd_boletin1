import pytest

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError("Input must be a string")
    return x.capitalize()

def test_capital_case():
    assert capital_case("semáforo") == "Semáforo"

def test_raises_exception_on_non_string_argument():
    with pytest.raises(TypeError):
        capital_case(9)
