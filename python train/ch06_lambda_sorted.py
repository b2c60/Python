li = [('apple', 25), ('orange', 10), ('fig', 12), ('apricot', 20)]

def by_name(item):
    return item[0]
def by_name_len(item):
    return len(item[0])
def by_value(item):
    return item[1]

print(sorted(li, key=by_name))
print(sorted(li, key=by_name_len))
print(sorted(li, key=by_value))
