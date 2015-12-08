fin = open('test.txt')
print(fin.readline())
for line in fin:
    print(line)
fin.close()
