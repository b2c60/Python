
#-*- Read txt file -*-

fin = open('Multipeer.txt')
fout = open('Multipeer2.txt', 'w')
#print('-' * 20)
#print(fin.readline())
#print(fin.read(5))
for line in fin:  
    print(line)
    fout.write(line)
fin.close()
fout.close()
