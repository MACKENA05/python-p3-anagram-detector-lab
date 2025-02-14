class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list_anagrams):
        sorted_word = sorted(self.word)
        return [word for word in list_anagrams if sorted(word) == sorted_word]



anagram_checker = Anagram('listen')

result = anagram_checker.match(['enlists', 'google', 'inlets', 'banana'])
print(result)