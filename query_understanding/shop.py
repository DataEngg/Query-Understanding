import os


class Shop(object):
    def __init__(self):
        self.data_path = os.path.abspath(os.path.join("query_understanding", "dataset"))
        self.csv_path = os.path.join(self.data_path)
        self.s = set()
        self.shop()

    def shop(self):
        with open(os.path.join(self.csv_path, "shop_name.csv")) as fout:
            for data in fout.readlines():
                for d in data.strip().lower().split(' '):
                    self.s.add(d)

    def finding_shop(self, query, val):
        val['shop'] = []
        list_tokens = query.split('by')
        if len(list_tokens) == 2:
            if list_tokens[1].strip().lower() in self.s:
                val['shop'].append(list_tokens[1].strip().lower())
                return list_tokens[0], val
            list_tokens.append(list_tokens[1])
            list_tokens[1] = 'by'
            return " ".join(list_tokens), val
        elif len(list_tokens) == 1:
            return " ".join(list_tokens), val
        return '', val

