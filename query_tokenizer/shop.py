import os


class Shop(object):
    def __init__(self):
        self.data_path = os.path.join("dataset")
        self.csv_path = os.path.join(self.data_path)
        self.s = set()
        self.shop()

    def shop(self):
        with open(os.path.join(self.csv_path, "shop_name.csv")) as fout:
            for data in fout.readlines():
                self.s.add(data.strip().lower())

    def finding_shop(self, query, val):
        val['shop'] = []
        list_tokens = query.split('by')
        if len(list_tokens) == 2:
            if list_tokens[1].lower() in self.s:
                val['shop'].append(list_tokens[1].lower())
            return list_tokens[0], val
        elif len(list_tokens) == 1:
            return list_tokens[0], val
        return '', val
