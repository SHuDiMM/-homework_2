class WordsFinder():

    def __init__(self, *args):
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, "r", encoding="utf-8") as file:
                content = file.read().lower()

                for symbol in punctuation:
                    content = content.replace(symbol, "")

                words = content.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        result = {}

        for name, words in self.get_all_words().items():
            position = words.index(word) + 1
            result[name] = position

        return result

    def count(self, word):
        word = word.lower()
        result = {}

        for name, words in self.get_all_words().items():
            result[name] = words.count(word)

        return result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
