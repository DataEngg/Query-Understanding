import os

from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from color import Colors
from price import Price
from gender import Gender
from term import Term


class Annotater(object):
    """
    Split the raw query into set of tokens via help of tokenizer.
    """

    def __init__(self):
        """
        Initialize variable for tokenizing
        """
        self.data_path = os.path.join(os.path.abspath(os.path.join("..", os.path.abspath('..'))), 'dataset')
        self.csv_path = os.path.join(self.data_path)

    def annotate(self, color=True, price=True, gender=True):
        """
        Tokenize the sentence.
        """

        while (True):
            print("Enter the query for test")
            query = input()
            if query:
                try:
                    value = {}
                    list_token = [item.lower().strip() for item in query.lower().split(' ')]
                    if color:
                        value, list_token = Colors().finding_colors(list_tokens=list_token)
                    query = " ".join(list_token)
                    if price:
                        query, value = Price().finding_price(string=query, val=value)
                    if gender:
                        query, value = Gender().finding_gender(query, val=value)
                    val = Term().finding_term(query, val=value)
                    print(query)
                    print(val)
                except Exception as e:
                    import traceback
                    print(traceback.format_exc())
                    print("No Mapping")


if __name__ == '__main__':
    Annotater().annotate(color=True,gender=True)
