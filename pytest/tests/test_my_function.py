import pytest
import source.my_function as my_function
import time

def test_add():
    result = my_function.add(1, 4)
    assert result == 5

def test_divide():
    result = my_function.divide(10, 5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
         my_function.divide(10, 0)

def test_add_strings():
    result = my_function.add("i like ", "burgers")
    assert result == "i like burgers"

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_function.divide(10,5)
    assert result == 2


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_function.add(1, 2) == 3


@pytest.mark.xfail(reason="we know we cannot divide by zero")
def test_divide_zero_broken():
    my_function.divide(4, 0)