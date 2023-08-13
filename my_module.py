def even(a):
    return list(filter(lambda x: x % 2 == 0, a))


def odd(a):
    return list(filter(lambda x: x % 2 != 0, a))


def perfectsquare(a):
    return list(filter(lambda x: any(x == p*p for p in range(2, x)), a))
