from nltk.corpus import stopwords


class Term(object):
    def __init__(self):
        self.cachedStopWords = set(stopwords.words("english"))
        pass

    def finding_term(self, query, val):
        val['term'] = []
        list_tokens = query.split(' ')
        list_tokens = [' '.join([word for word in text.split() if word not in self.cachedStopWords]) for text in list_tokens]
        for token in list_tokens:
            if token:
                val['term'].append(token)
        return val
