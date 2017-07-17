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
        self.less = ['below', 'under', 'cheap', 'less', 'lesser']
        self.greater = ['above', 'greater']
        self.between = ['between']

    def pricing(self):
        with open(os.path.join(self.csv_path, "price.csv")) as fout:
            for data in fout.readlines():
                self.p.add(data.strip().lower())

    def finding_price(self, string, val):
        val['price'] = dict()
        for word in self.p:
            if word in self.less:
                if word in string:
                    number = re.findall('\d+', string)[0]
                    val['price']['less than'] = number
                    string = self.remove_word(query=string, word=word, number=number)
            elif word in self.greater:
                if word in string:
                    number = re.findall('\d+', string)[0]
                    val['price']['greater than'] = number
                    string = self.remove_word(query=string, word=word, number=number)
            elif word in self.between:
                if word in string:
                    print(word)
                    number = re.findall('\d+', string)
                    print(number)
                    if len(number) == 2:
                        val['price']['greater than'] = number[0]
                        val['price']['less than'] = number[1]
                        string = self.remove_word(query=string, word=word, number=number)

        return string, val

    def remove_word(self, query, word, number):
        list_token = [item.lower().strip() for item in query.lower().split(word)][0]
        if not isinstance(number, list):
            list_token_number = query.split(number)[1]
            list_value = list_token + list_token_number
        else:
            list_token_number = query.split(number[1])[1]
            list_value = list_token + list_token_number
        return list_value
