# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.Пользователь его не вводит


# Решение №1

# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] # список из разных библиотеек
# new_set = set() # Создали новое множество
# for dict_i in dictionary:  # Походимся по элементам списка, т.е по словорям
#     for value in dict_i.values(): # Проходимся по значения каждого словоря
#         new_set.add(value)  # Добавляем значение в множество
# print(new_set)



# Решение №2

# dictionary = [{"V": "S001", "VV": "S00123"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# new_set = set()
# for dict_i in dictionary:
#     new_set.update(dict_i.values()) # функция update распаковывает и добавляет элементы в множество
# print(new_set)


# Решение №3

dictionary_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

new_set = set()

for dct_i in dictionary_1:                    # Походимся по элементам списка, т.е по словорям
    new_set.add(*dct_i.values())               # добовляем значения в новое множество.  *-это распаковка
    
print(new_set)


