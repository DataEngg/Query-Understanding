import os

import re
import collections
import jellyfish
import operator
from fuzzywuzzy import fuzz
from nltk.metrics.distance import edit_distance


class SpellCheck:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        self.data_path = os.path.abspath(os.path.join("query_understanding","dataset"))
        self.csv_path = os.path.join(self.data_path)
        self.txt_path = os.path.join(self.data_path)
        self.lWords = self.initialize_dictionary()
        self.lWords = self.train(self.lWords)

    # Returning the words in a list as lower case and defining a word as a list of alphabetic character
    # Works because the singular version of a word is more probably than the possessive notation (dog, dog's)
    def words(self, text):
        return re.findall('[a-z]+', text.lower())

    # Returning dictionary = {'a':{abbey:1, abbreviated:2}, 'b':{},...,'z':{}}
    # Instead of iterating through the whole dictionary, iteration happens based on first letter
    def train(self, words):
        occurences = {}
        for l in self.alphabet:
            occurences[l] = collections.defaultdict(
                lambda: 1)  # Sets default values in a dictionary, less iteration to check if element is a part of the dictionary
        for w in words:
            if w[0] in occurences and w in occurences[w[0]]:
                occurences[w[0]][w] += 1  # Incrementing occurence of word
            elif w[0] in occurences and w not in occurences[w[0]]:
                occurences[w[0]][w] = 1
            else:
                occurences[w[0]] = {}
                occurences[w[0]][w] = 1
        return occurences

    # Edits can be deletion (deletes), swapping adajent letters (transposes), alteration (replaces), or inserting a letter (inserts)
    # Returns a set of of all words one edit away from correct word
    def edits1(self, word):
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
        replaces = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
        inserts = [a + c + b for a, b in splits for c in self.alphabet]
        return list(deletes + transposes + replaces + inserts)

    # Returns a set of words with the possible edits
    def known_edits2(self, word, wDict):
        return list(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in wDict)

    # A known word is most likely to be a word that has a vowel mistyped rather than 2 consonants, probable correct first letter, edit distances of around 1 or 2
    def known(self, word, wDict):
        return list(w for w in word if w in wDict)

    # Highest Level Method
    # Returns the possible word
    def correct(self, word, wDict):
        candidates = self.known([word], wDict[word[0]]) or self.known(self.edits1(word),
                                                                      wDict[word[0]]) or self.known_edits2(word, wDict[
            word[0]]) or [word]  # gets a set of words with the shortest edit distance from the typed word.
        # print(candidates)
        return self.get_max_candidates(candidates, word, wDict)

    def get_max_candidates(self, candidates, word, wDict):
        if len(candidates) == 1:
            return max(candidates,
                       key=wDict.get)
        elif len(candidates) == 0:
            return 'NO SUGGESTION'
        else:
            matched = 0
            synonyms = None
            old_word = None
            mapped = dict()
            list_value = list()
            for value in candidates:
                ratio = fuzz.token_set_ratio(word.lower().strip(), value.lower().strip())
                mapped[value] = ratio
                list_value.append(ratio)
            max_key = max(mapped.items(), key=operator.itemgetter(1))[0]
            max_ratio = max(mapped.items(), key=operator.itemgetter(1))[1]
            if list_value.count(max_ratio) > 1:
                for value, ratio in mapped.items():
                    if matched <= ratio:
                        # print(old_word, synonyms, matched)
                        if old_word is not None:
                            synonyms = self.get_soundex(word.lower().strip(), value.lower().strip(), old_word)
                            old_word = synonyms
                        else:
                            synonyms = value.lower().strip()
                            old_word = synonyms
                        matched = ratio
            else:
                synonyms = max_key
            return synonyms

    def get_soundex(self, word1, word2, old_word):
        if jellyfish.soundex(word1) == jellyfish.soundex(word2):
            return word2
        elif jellyfish.soundex(word1) == jellyfish.soundex(old_word):
            return old_word
        else:
            return word1

    def initialize_dictionary(self):
        """
        Returns a set of words contained in a large list of English words
        """
        word_set = set()
        #filename = os.path.join(self.csv_path, "words.csv")
        nltk_words = os.path.join(self.csv_path, "nltk_words.csv")
        #if os.path.isfile(filename):
        #    with open(filename, 'r') as f:
        #        for line in iter(f):
        #            word_set.add(line.strip().replace("'s", "").lower())
        if os.path.isfile(nltk_words):
            with open(nltk_words, 'r') as f:
                for line in iter(f):
                    word_set.add(line.strip().lower())
        else:
            print(
                "There's seems to be a problem loading in the word list, ensure availability of nltk_words.csv in dataset directory")
        return word_set

    def run(self, token):
        try:
            spellchk = self.correct(token.lower(), self.lWords)
            if spellchk == token and spellchk not in self.lWords[token[0]]:
                return "#" + token
            else:
                if edit_distance(token, spellchk) <= 2:
                    return spellchk
                else:
                    return "#" + token
        except:
            return "#" + token

    def spelling(self, product_title):
        product_list = list()
        for data in product_title.split():
            if '#' in data:
                value = self.run(data.split("#")[1].strip())
                # if '#' not in value:
                product_list.append(value)
            else:
                product_list.append(data.strip())
        return " ".join(product_list)

    def spellCheck(self, token):
        spellcheck = self.run(token)
        if '#' in spellcheck:
            return False
        else:
            return spellcheck

    def last_spelling(self, product_title):
        product_list = list()
        for data in product_title.split():
            if '#' in data:
                value = self.run(data.split("#")[1].strip())
                if '#' not in value:
                    product_list.append(value)
            else:
                product_list.append(data.strip())
        return " ".join(product_list)

#if __name__ == '__main__':
#    print(SpellCheck().run("womenr"))
