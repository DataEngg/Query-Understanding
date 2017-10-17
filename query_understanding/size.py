class Size(object):
    def __init__(self):
        self.size = ['m', 'l', 's', 'xl', 'xxl', 'xxxl', 'xxxxl', 'medium', 'small', 'large', 'extra large']
        self.match_size = ['xl', 'xxl', 'xxxl', 'xxxxl', 'medium', 'small', 'large', 'extra large']
        pass

    def finding_size(self, query, val):
        val['size'] = []
        if 'size' in query:
            list_tokens = query.split('size')
            if list_tokens[0] and len(list_tokens[0].strip().split(' ')) > 1:
                first_word = list_tokens[0].strip().split(' ')[-1]
            else:
                first_word = list_tokens[0].strip()
            if list_tokens[1] and len(list_tokens[1].strip().split(' ')) > 1:
                second_word = list_tokens[1].strip().split()[0]
            else:
                second_word = list_tokens[1].strip()
            if first_word in self.size or first_word.isdigit():
                val['size'].append(first_word)
                list_tokens_new = list_tokens[0].split(first_word)[0]
                query = list_tokens_new + list_tokens[1]
                return query, val
            elif second_word in self.size or second_word.isdigit():
                val['size'].append(second_word)
                list_tokens_new = list_tokens[1].split(second_word)[1]
                query = list_tokens[0] + list_tokens_new
                return query, val
        else:
            list_tokens = query.split()
            for size in self.match_size:
                if size in list_tokens:
                    val['size'].append(size)
                    list_tokens.remove(size)
            query = ' '.join(list_tokens)

        return query, val
