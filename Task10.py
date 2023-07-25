# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

import random

number_coin = int(input("Введите количество монет: "))

obverse = 0
reverse = 0
coins = [0, 1]
for i in range(number_coin):
    random.shuffle(coins)
    print(f"положение монет {coins}")
    if int(coins[0]) == 0:
        obverse += 1
    if int(coins[0]) == 1:
        reverse += 1
print(f"Монет орлом вверх {obverse} и решкой вверх {reverse}.")
if obverse > reverse:
    turn = reverse
else:
    turn = obverse
print(f"Нужно перевернуть {turn}")

