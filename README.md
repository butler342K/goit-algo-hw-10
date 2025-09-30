### Дослідження ефективності жадібного та динамічного алгоритмів 
- find_coins_greedy - жадібний
- find_min_coins - динамічний

### Результати дослідження
        Case for [50, 25, 10, 5, 2, 1] and sum: 113
Result for find_coins_greedy: {50: 2, 10: 1, 2: 1, 1: 1}

Time taken for find_coins_greedy 1000 times: 0.001120 seconds

Result for find_min_coins: {1: 1, 2: 1, 10: 1, 50: 2}

Time taken for find_min_coins 1000 times: 0.113049 seconds

        Case for [50, 25, 10, 5, 2, 1] and sum: 9873
Result for find_coins_greedy: {50: 197, 10: 2, 2: 1, 1: 1}

Time taken for find_coins_greedy 1000 times: 0.001063 seconds

Result for find_min_coins: {1: 1, 2: 1, 10: 2, 50: 197}

Time taken for find_min_coins 1000 times: 7.753459 seconds

### Висновки
Жадібний алгоритм показав високу швидкість виконання як для малих так і для великих сум. 
Динамічний алгоритм витратив в 100 разів більше часу на малих сумах, та в 7000 разів на більших сумах.
Але ж динамічний алгоритм перевіряє всі можливі комбінації, тому й займає значно більше часу.
