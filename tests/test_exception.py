import pytest

from activity.main import *

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        zero_division_thrower(1, 0)

def test_key_error():
    with pytest.raises(KeyError):
        key_error_thrower({1: 'one', 2: 'two'}, 3)

def test_index_error():
    with pytest.raises(IndexError):
        index_error_thrower([0, 1, 2], 3)

def test_attribute_error_thrower():
    with pytest.raises(AttributeError):
        attribute_error_thrower()

def test_type_error_thrower():
    with pytest.raises(TypeError):
        type_error_thrower([0, 1, 2], "bla")

def test_name_error_thrower():
    with pytest.raises(NameError):
        name_error_thrower()

def test_value_error_thrower():
    with pytest.raises(ValueError):
        value_error_thrower()

def test_unbound_local_error_thrower():
    with pytest.raises(UnboundLocalError):
        unbound_local_error_thrower()

def test_overflow_error_thrower():
    with pytest.raises(OverflowError):
        overflow_error_thrower()
