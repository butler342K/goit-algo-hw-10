import timeit

def find_coins_greedy(sum, coins):
    coins_count = {}
    
    for coin in coins:
        #coin = 50
        count = sum // coin
        # count = 2
        if count > 0:
            coins_count[coin] = count #coins_count.get(coin, count)
        sum -= coin * count
        if sum == 0:
            break
    return coins_count

def find_min_coins(sum, coins):
    coins = sorted(coins)
    min_coins_required = [0] + [float('inf')] * sum
    coin_used = [0] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin

    coins_count = {}

    current_sum = sum
    
    while current_sum > 0:
        coin = coin_used[current_sum]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_sum -= coin

    coins_count_ordered = {coin: coins_count.get(coin, 0) for coin in coins if coin in coins_count}
    return coins_count_ordered

if __name__ == '__main__':

    cases = [([50, 25, 10, 5, 2, 1], 113),
             ([50, 25, 10, 5, 2, 1], 9873)]
    functions = [find_coins_greedy, find_min_coins]
    cnt = 1000

    for coins, cash_amount in cases:
        print(f"\n\tCase for {coins} and sum: {cash_amount}")
        for fun in functions:
            time = timeit.timeit(lambda: fun(cash_amount, coins), number=cnt)
            print("Result for {}: {}".format(fun.__name__, fun(cash_amount, coins)))
            print("Time taken for {} {} times: {:.6f} seconds".format(fun.__name__, cnt, time))