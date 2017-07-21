import os
import re


class Price(object):
    """

    """

    def __init__(self):
        self.data_path = os.path.join("dataset")
        self.csv_path = os.path.join(self.data_path)
        self.p = set()
        self.pricing()
        self.less = ['below', 'under', 'less', 'lesser']
        self.greater = ['above', 'greater']
        self.between = ['between']
        self.word = ['cheap', 'cheapest']

    def pricing(self):
        with open(os.path.join(self.csv_path, "price.csv")) as fout:
            for data in fout.readlines():
                self.p.add(data.strip().lower())

    def finding_price(self, string, val):
        val['price'] = dict()
        for word in self.p:
            number = ''
            if word in self.less:
                if word in string:
                    number = re.findall('\d+', string.split(word)[1])
                    if number:
                        val['price']['less than'] = number[0]
                        string = self.remove_word(query=string, word=word, number=number[0])
            elif word in self.greater:
                if word in string:
                    number = re.findall('\d+', string.split(word)[1])
                    if number:
                        val['price']['greater than'] = number[0]
                        string = self.remove_word(query=string, word=word, number=number[0])
            elif word in self.between:
                if word in string:
                    number = re.findall('\d+', string.split(word)[1])
                    if len(number) == 2:
                        val['price']['greater than'] = number[0]
                        val['price']['less than'] = number[1]
                        string = self.remove_word(query=string, word=word, number=number)

        return string, val

    def remove_word(self, query, word, number):
        list_token = query.lower().split(word)
        if list_token:
            if not isinstance(number, list):
                list_token_number = " ".join(list_token).split(number)
                if len(list_token_number) == 2:
                    list_value = " ".join(list_token_number)
                elif len(list_token_number) == 1:
                    list_value = list_token_number[0]
                else:
                    list_value = ''
            else:
                list_token_number = query.split(number[1])
                if len(list_token_number) == 2 and len(list_token) == 2:
                    list_value = list_token[0] + list_token_number[1]
                elif len(list_token) == 2:
                    list_value = list_token[0]
                else:
                    list_value = ''
        else:
            list_value = ''
        return list_value
