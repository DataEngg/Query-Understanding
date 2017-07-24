class Size(object):
    def __init__(self):
        self.size = ['m', 'l', 's', 'xl', 'xxl', 'xxxl', 'xxxxl', 'medium', 'small', 'large', 'extra large']
        pass

    def finding_size(self, query, val):
        val['size'] = []
        if 'size' in query:
            list_tokens = query.split('size')
            print(list_tokens)
            if len(list_tokens[0].strip().split(' ')) > 1:
                first_word = list_tokens[0].strip().split(' ')[-1]
            else:
                first_word = list_tokens[0].strip()
            if len(list_tokens[1].strip().split(' ')) > 1:
                second_word = list_tokens[1].strip().split()[0]
            else:
                second_word = list_tokens[1].strip()
            print(first_word, second_word)
            if first_word in self.size:
                val['size'].append(first_word)
                list_tokens_new = list_tokens[0].split(first_word)[0]
                query = list_tokens_new + list_tokens[1]
                return query, val
            elif second_word in self.size:
                val['size'].append(second_word)
                list_tokens_new = list_tokens[1].split(first_word)[1]
                query = list_tokens_new + list_tokens[1]
                return query, val
        return query, val
