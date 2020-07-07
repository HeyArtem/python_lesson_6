# Автоматичесское тестирование с помощью библиотеки pytest Тест 6
print('Автоматичесское тестирование с помощью библиотеки pytest Тест 6')


from br_1_ДЗ_function import f

def test_f():
    n = 5
    assert len(f(n)) == n