import requests
from bs4 import BeautifulSoup


class VelokazScrapper:

    def __init__(self, url):
        self.root = url
        self.data = requests.get(url).content
        self.parser = BeautifulSoup(self.data, "lxml")

    def getNewRoor(self, child):
        if child == None:
            prs = self.parser
        else:
            prs = child
        return prs

    def handleClass(self, schema, child=None):
        prs = self.getNewRoor(child)
        args = {"class", schema['target']}
        if schema['method'] == "one":
            return prs.find(schema['element'], args)
        else:
            pr = prs.find_all(schema['element'], args)
            return BeautifulSoup(''.join([str(x) for x in pr]), "lxml")
        return None

    def handleNormal(self, schema, child=None):
        prs = self.getNewRoor(child)
        if schema['method'] == "one":
            return prs.find(schema['element'])
        else:
            pr = prs.find_all(schema['element'])
            return BeautifulSoup(''.join([str(x) for x in pr]), "lxml")
        return None

    def get(self, schema, child=None):
        type = schema['type']
        if type == "class":
            return self.handleClass(schema, child)
        elif type == "id":
            return self.handleId(schema, child)
        elif type == "normal":
            return self.handleNormal(schema, child)
        return None
