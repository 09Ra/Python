# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Решение №1 мое решение

# list_1=['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
# list_2=['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
# list_3=['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
# list_4=['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
# list_5=['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
# list_8=['J', 'X', 'Ш', 'Э', 'Ю']
# list_10=['Q', 'Z', 'Ф', 'Щ', 'Ъ']

# sum_1=0

# word_0=str(input("Введите слово: "))
# word_1=str(word_0.upper())

# for i in range (len(word_1)):
#     for j in range(len(list_1)):
#         if word_1[i]==list_1[j]:
#             sum_1+=1
#     for j in range(len(list_2)):
#         if word_1[i]==list_2[j]:
#             sum_1+=2
#     for j in range(len(list_3)):
#         if word_1[i]==list_3[j]:
#             sum_1+=3
#     for j in range(len(list_4)):
#         if word_1[i]==list_4[j]:
#             sum_1+=4
#     for j in range(len(list_5)):
#         if word_1[i]==list_5[j]:
#             sum_1+=5
#     for j in range(len(list_8)):
#         if word_1[i]==list_8[j]:
#             sum_1+=8
#     for j in range(len(list_10)):
#         if word_1[i]==list_10[j]:
#             sum_1+=10 
# print(sum_1)                                                           


# Решение №2 Эталонное решение
k="ноутбук"
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)

