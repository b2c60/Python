def fib_memo():
    memo = {0: 0, 1: 1}
    def sub(n):
        if n not in memo:
            memo[n] = sub(n-1) + sub(n-2)
        return memo[n]
    return sub
fib_m = fib_memo()

