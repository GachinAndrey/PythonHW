# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму чисел <= 1000: "))
p = int(input("Введите произведение чисел <= 1000: "))

a = (s - int((s ** 2 - 4 * p) ** 0.5)) // 2
b = (s + int((s ** 2 - 4 * p) ** 0.5)) // 2
if a >= 1001 or b >= 1001:
    print("Петя обманул, одно из чисел больше 1000.")
print(f'Задуманные Петей числа {a, b}.')