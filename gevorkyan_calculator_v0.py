import math

print("Добро пожаловать в Калькулятор Python!")
print("Вы можете выполнять следующие операции:")
print("1. Сложение (+)")
print("2. Вычитание (-)")
print("3. Умножение (*)")
print("4. Деление (/)")
print("5. Целочисленное деление (//)")
print("6. Взятие остатка (%)")
print("7. Возведение в степень (^)")
print("8. Квадратный корень (√)")
print("9. Перевод из другой системы счисления в десятичную")
print("10. Анализ числа")


def get_number_input():
    while True:
        try:
            number = float(input("Введите число: "))
            return number
        except ValueError:
            print("Ошибка! Введите действительное число.")


def analyze_number(number):
    number1 = number
    number_str = str(int(number))
    num_digits = len(number_str)
    even_odd = "четное" if number % 2 == 0 else "нечетное"
    digit_sum = sum(int(digit) for digit in number_str)
    square_root = round(math.sqrt(number))
    cube_root = round(number ** (1 / 3))
    prime_factors = []
    is_prime = True

    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            prime_factors.append(i)
            number //= i
            is_prime = False

    if number > 1:
        prime_factors.append(int(number))

    print(f"1. Количество разрядов: {num_digits}")
    print(f"2. Количество цифр в числе:")
    for digit in range(10):
        count = number_str.count(str(digit))
        if count > 0:
            print(f"   {digit}: {count} раз(а)")
    print(f"3. Число {even_odd}")
    print(f"4. Сумма цифр: {digit_sum}")
    if is_prime:
        print(f"5. Число простое")
    else:
        print(f"5. Число не является простым. Делители: {', '.join(map(str, prime_factors))}")
    if square_root ** 2 == number1:
        print(f"6. Число является полным квадратом, корень: {square_root}")
    if cube_root ** 3 == number1:
        print(f"7. Число является полным кубом, корень: {cube_root}")


def from_base_to_decimal():
    try:
        number_str = input("Введите число в другой системе счисления: ")
        base = int(input("Введите базу системы счисления: "))
        decimal_number = int(number_str, base)
        print(f"Число {number_str} в десятичной системе счисления: {decimal_number}")
    except ValueError:
        print("Ошибка! Неправильный ввод.")


while True:
    try:
        num1 = get_number_input()
        operation = input("Введите операцию (+, -, *, /, //, %, ^, √, d для перевода, или a для анализа числа): ")

        if operation == 'a':
            analyze_number(num1)
        elif operation == 'd':
            from_base_to_decimal()
        else:
            num2 = get_number_input()
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            elif operation == '//':
                result = num1 // num2
            elif operation == '%':
                result = num1 % num2
            elif operation == '^':
                result = num1 ** num2
            elif operation == '√':
                result = math.sqrt(num1)
            else:
                print("Ошибка! Неправильная операция.")
                continue

            print("Результат:", result)

    except ZeroDivisionError:
        print("Ошибка! Деление на ноль.")
    except ValueError:
        print("Ошибка! Неправильный ввод.")

    another_operation = input("Выполнить еще операцию? (да/нет): ").strip().lower()
    if another_operation != 'да':
        print("Спасибо за использование Калькулятора Python!")
        break
