#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 1 and tuple_a[0] is not None:
        a1 = tuple_a[0]
    else:
        a1 = 0

    if len(tuple_b) >= 1 and tuple_b[0] is not None:
        b1 = tuple_b[0]
    else:
        b1 = 0

    if len(tuple_a) >= 2 and tuple_a[1] is not None:
        a2 = tuple_a[1]
    else:
        a2 = 0

    if len(tuple_b) >= 2 and tuple_b[1] is not None:
        b2 = tuple_b[1]
    else:
        b2 = 0

    return (a1 + b1, a2 + b2)
