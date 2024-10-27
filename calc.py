number1 = int(input("Введите сумму которую вы хотите дать в фонд Кати "))
sign = input("Введите символ: ")
number2 = int(input("Введите число на сколько вы меня любите "))

if sign == "+":
    print(number1 + number2)
elif sign == "-":
    print(number1 - number2)
    if number1 > number2:
        print(number1 - number2)
    else:
        print(number2 - number1)
elif sign == "/" and number2 != 0:
    print(number1 / number2)
elif sign == "*":
    print(number1 * number2)
else:
    print("Я не знаю, скорее всего вы бот)")