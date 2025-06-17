import random


def int_entity(c):
    return "&#{};".format(ord(c))


def hex_entity(c):
    return "&#x{:x};".format(ord(c))


def mangle(s):
    funcs = [str, int_entity, hex_entity]
    s = "".join([random.choice(funcs)(c) for c in s])
    return s.replace("@", hex_entity("@"))


def max_column_length(array, col):
    return max([len(row[col]) for row in array])
