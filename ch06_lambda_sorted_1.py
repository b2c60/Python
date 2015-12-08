li = [('apple', 25), ('orange', 10), ('fig', 12), ('apricot', 20)]


print(sorted(li, key=lambda item: item[0]))
print(sorted(li, key=lambda item: len(item[0])))
print(sorted(li, key=lambda item: item[1]))
