# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

line1= "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".upper()
# переводим всю строку в заглавные буквы
print(line1)

new_line=line1.split()
print(new_line)

unique_new_line=set(new_line)  #Создаем множество

print("В тексте всего ", len(unique_new_line), "уникальных слов")
