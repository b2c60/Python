from io import open
try:
    fin = open('test.txt', 'r', encoding='utf-8')
    try:
        for line in fin:
            print(line)
    except UnicoderError as e:
        print('Error while reading file: ' + str(e))
    except Exception as e:
        print('Error while reading file: ' + str(e))
    finally:
        fin.close()
except Exception as e:
    print('Error while opening file: ' + str(e))
