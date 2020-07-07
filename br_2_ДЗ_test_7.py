# Автоматичесское тестирование с помощью библиотеки pytest Тест 7
print('Автоматичесское тестирование с помощью библиотеки pytest Тест 7')



from br_1_ДЗ_function import f

def test_f():
    n = 100
    assert 'Глофера' not in f(n)