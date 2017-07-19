from nltk.corpus import stopwords


class Term(object):
    def __init__(self):
        self.cachedStopWords = {"stop": [
            "a", "an", "and", "are", "as", "at", "be", "but", "by",
            "for", "if", "in", "into", "is", "it",
            "no", "not", "of", "on", "or", "such",
            "that", "the", "their", "then", "there", "these",
            "they", "this", "to", "was", "will", "with"]}
        pass

    def finding_term(self, query, val):
        val['term'] = []
        list_tokens = query.split(' ')
        list_tokens = [' '.join([word for word in text.split() if word not in self.cachedStopWords['stop'
                                                                                                   '']]) for text in
                       list_tokens]
        for token in list_tokens:
            if token:
                val['term'].append(token)
        val['query'] = " ".join(val['term'])
        return val
