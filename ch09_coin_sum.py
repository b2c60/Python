def coin_sum_r(total, coins):
    if len(coins) == 1:
        return 1
    elif total < coins[-1]:
        return coin_sum_r(total, coins[:-1])
    else:
        return (coin_sum_r(total-coins[-1], coins) + coin_sum_r(total, coins[:-1]))


#coins_england = (1, 2, 5, 10, 20, 50, 100, 200)
coins_england = (1, 2, 5)
print(coin_sum_r(12, coins_england))

