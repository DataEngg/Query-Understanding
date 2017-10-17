import os

class Colors(object):
    def __init__(self):
        self.data_path = os.path.abspath(os.path.join("query_understanding", "dataset"))
        self.csv_path = os.path.join(self.data_path)
        self.c = set()
        self.color()

    def color(self):
        with open(os.path.join(self.csv_path, "colors.csv")) as fout:
            for data in fout.readlines():
                self.c.add(data.strip().lower())

    def finding_colors(self, list_tokens):
        val = dict()
        val['color'] = []
        for token in list_tokens:
            if token in self.c:
                val['color'].append(token)
                list_tokens.remove(token)
        return val, list_tokens
