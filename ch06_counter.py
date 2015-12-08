def counter(n):
    def bar(x):
        nonlocal n
        n += x
        return n
    return bar

