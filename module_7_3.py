import re

class WordsFinder:

    file_names = []
    __symbols = '[,.=!?;:-]'

    def __init__(self, *args):
        for name in args:
            self.file_names.append(name)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                file_words = []
                for line in file:
                    low_str = line.lower()
                    low_str = re.sub(self.__symbols, '', low_str)
                    file_words += low_str.split()
                all_words[name] = file_words
        return all_words

    def find(self, word):
        find_words = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                find_words[key] = value.index(word.lower()) + 1
        return find_words

    def count(self, word):
        count_words = {}
        for key, value in self.get_all_words().items():
            count = [i for i in value if i == word.lower()]
            count_words[key] = len(count)
        return count_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего