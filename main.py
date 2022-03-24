import pytest


def always_returns_true():
    return True


def test_always_returns_true():
    assert always_returns_true()

def multiple(num1, num2):
    return num1 * num2

def print_hello():
    print("Hello everyone!")

print_hello()
