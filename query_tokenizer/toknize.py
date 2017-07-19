import os

from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from color import Colors
from price import Price
from gender import Gender
from term import  Term


class Tokize(object):
    """
    Split the raw query into set of tokens via help of tokenizer.
    """

    def __init__(self):
        """
        Initialize variable for tokenizing
        """
        self.data_path = os.path.join(os.path.abspath(os.path.join("..", os.path.abspath('..'))), 'dataset')
        self.csv_path = os.path.join(self.data_path)

    def tokens(self):
        """
        Tokenize the sentence.
        """

        while (True):
            print("Enter the query for test")
            query = input()
            if query:
                list_token = [item.lower().strip() for item in query.lower().split(' ')]
                value, list_token = Colors().finding_colors(list_tokens=list_token)
                query = " ".join(list_token)
                new_query, val = Price().finding_price(string=query, val=value)
                new_query, val = Gender().finding_gender(new_query, val=val)
                val = Term().finding_term(new_query, val=val)
                print(new_query)
                print(val)


if __name__ == '__main__':
    Tokize().tokens()
