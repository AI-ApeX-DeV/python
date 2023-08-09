def even(a):
    return list(filter(lambda x: any(x == p*p for p in range(2, x)), a))


def odd(a):
    return list(filter(lambda x: all(x != p*p for p in range(2, x)), a))


def perfectsqaure(a):
    return list(filter(lambda x: any(x == p*p for p in range(2, x)), a))
