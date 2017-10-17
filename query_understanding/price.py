import os
import re


class Price(object):
    """

    """

    def __init__(self):
        self.data_path = os.path.abspath(os.path.join("query_understanding", "dataset"))
        self.csv_path = os.path.join(self.data_path)
        self.p = set()
        self.pricing()
        self.less = ['below', 'under', 'less', 'lesser', 'to']
        self.greater = ['above', 'greater', 'from']
        self.between = ['between']
        self.word = ['cheap', 'cheapest']
        self.equal = ['of', 'for']

    def pricing(self):
        with open(os.path.join(self.csv_path, "price.csv")) as fout:
            for data in fout.readlines():
                self.p.add(data.strip().lower())

    def finding_price(self, string, val):
        val['price'] = dict()
        list_of_words = string.split()
        for word in self.p:
            number = ''
            string = string.lower()
            if word in self.less:
                if word in string:
                    # number = re.findall('\d+', string.split(word)[1])
                    number = list_of_words[list_of_words.index(word) + 1]
                    if number.isdigit():
                        val['price']['lt'] = number
                        string = self.remove_word(query=string, word=word, number=number)
            elif word in self.greater:
                if word in string:
                    # number = re.findall('\d+', string.split(word)[1])
                    number = list_of_words[list_of_words.index(word) + 1]
                    if number.isdigit():
                        val['price']['gte'] = number
                        string = self.remove_word(query=string, word=word, number=number)
            elif word in self.between:
                if word in string:
                    number = re.findall('\d+', string.split(word)[1])
                    if len(number) == 2:
                        val['price']['gte'] = number[0]
                        val['price']['lt'] = number[1]
                        string = self.remove_word(query=string, word=word, number=number)
            elif word in self.equal:
                if word in string:
                    occur = self.occurences(list_of_words, word)
                    for value in occur:
                        number = list_of_words[value + 1]
                        if number.isdigit():
                            val['price']['eq'] = number
                            string = self.remove_word(query=string, word=word, number=number)

        return string, val

    def occurences(self, string, word):
        occur = []
        try:
            old = 0
            for x in range(0, 50):
                new = string.index(word, x)
                if new != old:
                    old = new
                    occur.append(new)
                else:
                    pass
        except:
            pass
        return occur

    def remove_word(self, query, word, number):
        list_token = query.lower().split(" " + word + " ")
        if list_token:
            if not isinstance(number, list):
                list_token_number = " ".join(list_token).split(" " + number + " ")
                if len(list_token_number) >= 2:
                    list_value = " ".join(list_token_number)
                elif len(list_token_number) == 1:
                    list_value = list_token_number[0]
                else:
                    list_value = ''
            else:
                list_token_number = query.split(" " + number[1] + " ")
                if len(list_token_number) == 2 and len(list_token) == 2:
                    list_value = list_token[0] + list_token_number[1]
                elif len(list_token) == 2:
                    list_value = list_token[0]
                else:
                    list_value = ''
        else:
            list_value = ''
        return list_value
