import math


def zero_division_thrower(a, b):
    return a/b


def key_error_thrower(dict, key):
    a = dict[key]


def index_error_thrower(list, index):
    value = list[index]


def attribute_error_thrower():
    list = []
    list.jog()


def type_error_thrower(list, index):
    value = list[index]


def name_error_thrower():
    print(message)


def value_error_thrower():
    math.sqrt(-10)


def unbound_local_error_thrower():
    print(message)
    message = "oops"


def overflow_error_thrower():
    math.exp(100000000)