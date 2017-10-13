
class Term(object):
    def __init__(self):
        self.cachedStopWords = {"stop": [
            "a", "an", "are", "as", "at", "be", "but",
            "for", "if", "in", "into", "is", "it",
            "no", "not", "of", "on", "such",
            "that", "the", "their", "then", "there", "these", "from",
            "they", "this", "to", "was", "will", "with", "and", "or", "rs", "price", "gender", "color"]}
        pass

    def finding_term(self, query, val):
        val['term'] = []
        val['shitty_words'] = []
        list_tokens = query.split(' ')
        list_tokens = [' '.join([word for word in text.split() if word not in self.cachedStopWords['stop'
                                                                                                   '']]) for text in
                       list_tokens]
        for token in list_tokens:
            if token:
                if token:
                    val['term'].append(token)
        val['query'] = " ".join(val['term'])
        return val
