class Gender(object):
    def __init__(self):
        self.gender = ['men', 'mens', 'boy', 'boys', 'male', 'males', 'female', 'females', 'girl', 'girls', 'women',
                       'womens']
        self.convert_gender = {"man": "men", "woman": "women"}

    def finding_gender(self, query, val):
        val['gender'] = []
        list_tokens = query.split(' ')
        for token in list_tokens:
            new_token = ""
            if token in self.convert_gender:
                new_token = self.convert_gender[token]
            if token in self.gender or new_token in self.gender:
                if new_token:
                    if new_token not in val['gender']:
                        val['gender'].append(new_token)
                else:
                    if token not in val['gender']:
                        val['gender'].append(token)
                list_tokens.remove(token)
            else:
                pass

        return " ".join(list_tokens), val
