class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the original word to lowercase

    def match(self, words):
        # Sort the characters of the original word
        sorted_word = sorted(self.word)
        matches = []

        for word in words:
            # Sort the characters of the current word (converted to lowercase) and compare with the sorted original word
            if sorted(word.lower()) == sorted_word:
                matches.append(word)

        return matches
