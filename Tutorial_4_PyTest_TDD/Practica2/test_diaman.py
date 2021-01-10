import pytest
from diaman import fibu

def test_fibu():
    num = 10
    assert fibu(num) == [ "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]

