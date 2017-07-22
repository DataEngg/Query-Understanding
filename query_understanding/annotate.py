import os

from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from color import Colors
from price import Price
from gender import Gender
from shop import Shop
from term import Term


class Annotater(object):
    """
    Split the raw query into set of tokens via help of tokenizer.
    """

    def __init__(self):
        """
        Initialize variable for tokenizing
        """
        self.data_path = os.path.join("test_dataset")
        self.csv_path = os.path.join(self.data_path)

    def annotate(self, color=True, price=True, gender=True, shop=True):
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
                    if shop:
                        query, value = Shop().finding_shop(query, val=value)
                    val = Term().finding_term(query, val=value)
                    print(query)
                    print(val)
                except Exception as e:
                    import traceback
                    print(traceback.format_exc())
                    print("No Mapping")

    def test_annotate(self, color=True, price=True, gender=True, shop=True):
        """
        Tokenize the sentence.
        """
        file_open = open(os.path.join(self.csv_path, "answer.csv"),'w')
        with open(os.path.join(self.csv_path, "by.csv")) as fout:
            for query in fout.readlines():
                if query:
                    file_open.write(query + "--->>")
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
                        if shop:
                            query, value = Shop().finding_shop(query, val=value)
                        val = Term().finding_term(query, val=value)
                        # print(query)
                        file_open.write(str(val) + "\n")
                    except Exception as e:
                        import traceback
                        print(traceback.format_exc())
                        print("No Mapping")


if __name__ == '__main__':
    # Annotater().annotate(color=True,gender=True,price=True,shop=True)
    Annotater().test_annotate(color=True, gender=True, price=True, shop=True)
