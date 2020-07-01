# Создадим прочтую ф-ю вычисления среднего арифметич. и будем ее дебагать

list_temp = [1, 5, 2, 2, 6, 12.2, 2, 53]
sum = 0
for el in list_temp:
    sum += el
print(sum/len(list_temp))


# специально накосячим для debud-ера

list_temp = [1, 5, 2, 2, 6, '12', 12.2, 2, 53]
sum = 0
if (len(list_temp)) > 0:
    for el in list_temp:
        sum += el  # что бы ошики не было, нужно записать: sum += float(el) или второй вар. пишу ниже
    print(sum/len(list_temp))
else:
    print('list_temp is empty!')

# II вар, исправления
list_temp = [1, 5, 2, 2, 6, '12', 12.2, 2, 53]
sum = 0
if (len(list_temp)) > 0:
    for el in list_temp:
        if type(el) == float:
            sum += el  # что бы ошики не было, нужно записать: sum += float(el) или второй вар. пишу ниже
    print(sum/len(list_temp))
else:
    print('list_temp is empty!')
