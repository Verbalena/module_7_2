# - * - coding: utf - 8 -*-
#Задача "Записать и запомнить":
def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_posishion = {}
        for i, string in enumerate(strings):
            start_post = file.tell()
            file.write(string + '\n')
            strings_posishion[(i,start_post)] = string
    return strings_posishion

file_name = 'test.txt'
strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
posishion = custom_write(file_name, strings)
print(posishion)

