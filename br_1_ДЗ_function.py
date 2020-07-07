# ДЗ после 6 главы. Функции которые будем тестировать
print('   ДЗ после 6 главы. Функции которые будем тестировать')


def number_1_1000(n):
    '''

    Функция проверяет полученное число, что бы
    оно нахлдилось в промежутке между 1 и 1000
    :param n: получает число для проверки
    :return: Возвращает вводимое число если оно в промежутке
             м/у 1 и 100 и выдаст None, если число вне заданного промежутка

    '''
    if n in (i for i in range(1, 1001)):
        return (n)
    else:
        return None


print(number_1_1000(25))


# Проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами)
print('   Проверка числа на простоту (простые числа - это те числа\n    у которых делители единица и они сами)')


def isPrime(n):
    '''

    Функция получает число, сначала проверяет его через функцию
    def number_1_1000(n), и убедившись, что оно находится в промежутке м/у
    1 и 1000., проверяет, является ли оно простым (простое, делится только
    на 1 и самого себя)

    :param n: получает число, которое нужно проверить на простототу
    :return: 'Простое число' -> если число простое
              'Составное число' -> если число не простое
              'Data error' -> если число не находиться в промежутке м/у 1 и 1000

    '''
    if number_1_1000(n):
        lst = []
        for i in range(2, n + 1):
            for j in lst:
                if i % j == 0:
                    break
            else:
                lst.append(i)
        if n in lst:
            return ('Простое число')
        else:
            return ('Составное число')
    else:
        return 'Data error'

print(isPrime(79))
