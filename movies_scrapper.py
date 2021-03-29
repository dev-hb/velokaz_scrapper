import requests
from bs4 import BeautifulSoup


class VelokazScrapper:

    def __init__(self, url):
        self.root = url
        self.data = requests.get(url).content
        self.parser = BeautifulSoup(self.data, "lxml")

    def handleClass(self, schema, child=None):
        if child == None:
            prs = self.parser
        else:
            prs = child
        if schema['method'] == "one":
            return prs.find(schema['element'], {"class", schema['target']})
        else:
            return prs.find_all(schema['element'], {"class", schema['target']})
        return None

    def get(self, schema, child=None):
        if schema['type'] == "class":
            return self.handleClass(schema, child)
        else:
            return self.handleId(schema, child)
        return None
