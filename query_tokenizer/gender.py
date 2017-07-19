class Gender(object):
    def __init__(self):
        self.male = ['men', 'mens', 'boy', 'boys', 'male', 'males']
        self.female = ['female', 'females', 'girl', 'girls', 'women', 'womens']

    def finding_gender(self, query, val):
        val['gender'] = []
        list_tokens = query.split(' ')
        for token in list_tokens:
            if token in self.male:
                val['gender'].append(token)
                list_tokens.remove(token)
            elif token in self.female:
                val['gender'].append(token)
                list_tokens.remove(token)
            else:
                pass
        return " ".join(list_tokens), val
