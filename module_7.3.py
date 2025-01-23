# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов
# и записывать их в атрибут file_names в виде списка или кортежа.
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'],
# 'file3.txt': ['word5', 'word6', 'word7']}
# Где:'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

class WordsFinder:
    res = {}  # словарь для вывода результатов

    def __init__(self, *file_names):
        self.file_names = list(file_names)  # атрибут file_names в виде списка

    def get_all_words(self):
        all_words = {}  # Создайте пустой словарь all_words
        punctuation = ",.=!?;:-"  # Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.

        for filename in self.file_names:  # Переберите названия файлов и открывайте каждый из них, используя with.
            clear_line = ''  # обнуляем строки
            with open(filename, "r", encoding='utf-8') as file:
                for line in file:
                    line = line.lower()  # Для каждого файла считывайте единые строки, переводя их в нижний регистр
                    while line.find(' — ') != -1:  # Избавьтесь от пунктуации [' — '] в строке.
                        line = line.replace(' — ', " ")  # (тире обособлено пробелами, это не дефис в слове)
                        continue
                    for char in line:  # 4 Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':'] в строке.
                        if not char in punctuation:
                            clear_line += char
                words = clear_line.split()  # Разбейте эту строку на элементы списка методом split().
            all_words[filename] = words  # В словарь all_words запишите полученные данные,
            #   ключ - название файла, значение - список из слов этого файла.
            self.res.clear()
        return all_words

    def find(self, word):  # - метод, где word - искомое слово.
        for names, words in self.get_all_words().items():
            if word.lower() in words:
                place = words.index(word.lower()) + 1
                self.res[names] = place
        return self.res

    def count(self, word):  # count(self, word) - метод, где word - искомое слово.
        for names, words in self.get_all_words().items():
            if word.lower() in words:
                counter = words.count(word.lower())
                self.res[names] = counter
        return self.res


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
