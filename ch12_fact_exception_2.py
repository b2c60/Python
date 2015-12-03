
def fact(n):
    if type(n) is not int:
        raise TypeError('Argument must be type int')
    if n < 0:
        raise ValueError('Argument must be non-negative')
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

while True:
    try:
        s = input('input n: ')
        f = fact(int(s))
    except TypeError as e:
        print('Error: ' + str(e))
    except ValueError as e:
        print('Error: ' + str(e))
    except:
        print('Error: unknown error')
    else:
        print('%s! = %d' % (s, f))
    
