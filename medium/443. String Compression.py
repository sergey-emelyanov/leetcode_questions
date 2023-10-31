"""
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
"""


def compress(chars):
    read_index = 0 # Инициализируем индекс для чтения
    write_index = 0 # Инициализируем индекс для записи

    while read_index < len(chars):
        char = chars[read_index] # Берем букву исходного списка
        count = 0 # Тут будем собирать количество повторений данной буквы

        while read_index < len(chars) and chars[read_index] == char: # Бежим по циклу пока не выйдем за длину исходного массива или не смениться буква
            read_index += 1 # Увеличиваем индекс чтения
            count += 1 # Увеличиваем количество встреченных одинаковых букв

        chars[write_index] = char # Записываем нашу букву с помощью индекса записи
        write_index += 1 # Увеличиваем индекс записи

        if count > 1: # По условию нам надо добавить сколько ра встречалась буква, если она встречалась больше одного раза
            for digit in str(count): # А если в числе несколько разрядов то нам надо записать их по отдельности, для этого преобразуем count в строку и добавим все в итоговый список
                chars[write_index] = digit
                write_index += 1

    del chars[write_index:] # убираем те элементы, что остались от изначального массива
    return len(chars)








