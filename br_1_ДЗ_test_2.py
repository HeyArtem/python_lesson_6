# Тестирование буду проводить на функции, которая проверяет число на простоту
print('   Тестирование буду проводить на функции, которая проверяет число на простоту')
print('Полуавтоматичесский Тест 2')

from br_1_ДЗ_function import isPrime

print()
# Полуавтоматичесский Тест 2
print('Полуавтоматичесский Тест 2')

def function_test():
    n=12000 # На выходе должны получить 'Data error'
    resault_out = isPrime(n)
    if resault_out == 'Data error':
        print('Test 2 is OK')
    else:
        print('Test 2 is failed!')
function_test()