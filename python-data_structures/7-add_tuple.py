#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds 2 tuples.
    Args:
        tuple_a: the first tuple
        tuple_b: the second tuple
    Returns:
        A tuple with 2 integers:
        The first element is the addition of the first element of each argument
        The second element is the addition of the second element of each argument
    """
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    
    return (a1 + b1, a2 + b2)
