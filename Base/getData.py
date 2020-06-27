import os

import yaml


class GetData:
    @classmethod
    def load_yaml(self, name):
        with open("./Data" + os.sep + name, "r", encoding="utf-8")as f:
            data = yaml.safe_load(f)
        return data
