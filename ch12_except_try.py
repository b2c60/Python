
try:
    return 'try'
    print('try')
except IndexError as e:
    exc = e
    print(exc)
finally:
    print('finally')
