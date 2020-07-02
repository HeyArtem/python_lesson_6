# 6.3. Полуавтоматические методы тестирования

# Полуавтоматические тесты ("Наивные тесты")

def test_function(list_enter):
    '''

    вход: list
    выход: list, содержащий только числа из list

    '''
    list_temp = []
    i = 0
    while(type(list_enter[i]) == int):
        list_temp.append(list_enter[i])
        i += 1
    return list_temp

# list_temp = [1, 2, 3, 'abc']
# print(test_function(list_temp))  # Я их закоментил, т.к. буду проверять полуавтоматической функцией

print()
# Пишем полкавтоматическую функцию для проверки test_function Test 1
print('   Пишем полкавтоматическую функцию для проверки test_function Test 1')
def function_test():
    list_temp = [1, 2, 3, 'abc'] #[1, 2, 3,]
    list_out = test_function(list_temp)
    if list_out == [1, 2, 3]:
        print('Test 1 is OK')
    else:
        print('Test 1 is failed')
function_test()

print()
# Пишем полкавтоматическую функцию для проверки test_function Test 2
print('Пишем полкавтоматическую функцию для проверки test_function Test 2')

def function_test():
    list_temp = [1, 2, 3, 'abc', 4]  #[1, 2, 3, 4] <- добавили 4
    list_out = test_function(list_temp)
    if list_out == [1, 2, 3, 4]:
        print('Test 2 is OK')
    else:
        print('Test 2 is failed') # Тест будет if failed, т.к. while работает до первой встречи с не int-ом
function_test()

print()
# меняем в функции while на for
print('   меняем в функции while на for')

def test_function(list_in):
    '''

    вход: list
    выход: list, содержащий только числа из list

    '''
    list_temp = []
    for i in range(len(list_in)):
        if type (list_in[i]) == int:
            list_temp.append(list_in[i])
    return list_temp

# ... и тестируем Test 3
print('   ... и тестируем  Test 3')


def function_test():
    list_temp = [1, 2, 3, 'abc', 4]
    list_out = test_function(list_temp)
    if list_out == [1, 2, 3, 4]:
        print('Test 3 is OK')
    else:
        print('Test 3 is failed') # Тест будет if failed, т.к. while работает до первой встречи с не int-ом
function_test()



print()
# Усложняем, допустим будут еще подаваться числа в виде строки Test 4
print('   Усложняем, допустим будут еще подаваться числа в виде строки Test 4')

def test_function(list_in):
    '''

    вход: list
    выход: list, содержащий только числа из list

    '''
    list_temp = []
    for i in range(len(list_in)):
        if type (list_in[i]) == int:
            list_temp.append(list_in[i])
    return list_temp


# дальше полуавтоматич фу-я для проверки, мы увидим ошибку

def function_test():
    list_temp = [1, 2, 3, '5', 'abc', 4]  # [1, 2, 3, 5, 4] Здесь 5 в виде строки
    list_out = test_function(list_temp)
    if list_out == [1, 2, 3, 5, 4]:
        print('Test 4 is OK')
    else:
        print('Test 4 is failed') # Тест будет if failed, т.к. while работает до первой встречи с не int-ом
function_test()


print()
# перепишем функцию которая извлекает числа Test 5
print('   перепишем функцию которая извлекает числа Test 5')

def test_function(list_in):
    '''

    вход: list
    выход: list, содержащий только числа из list

    '''
    list_temp = []
    for i in range(len(list_in)):
        if type (list_in[i]) == int:
            list_temp.append(list_in[i])
        elif type (list_in[i]) == str:
            if list_in[i].isdigit():
                list_temp.append(int(list_in[i]))
    return list_temp

# Дальше опять функция проверки
def function_test():
    list_temp = [1, 2, 3, '5', 'abc', 4]  # [1, 2, 3, 5, 4] Здесь 5 в виде строки
    list_out = test_function(list_temp)
    if list_out == [1, 2, 3, 5, 4]:
        print('Test 5 is OK')
    else:
        print('Test 5 is failed') # Тест будет if failed, т.к. while работает до первой встречи с не int-ом
function_test()