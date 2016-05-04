def make_multipliers():
    result = []
    for i in range(3):
        def m(x):
            return i * x
        result.append(m)
    return result
for m in make_multipliers():
    print(m(5))
