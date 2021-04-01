import requests
from bs4 import BeautifulSoup


def getVariableTypeValue(variable, it):
    if variable['type'] == "limit":
        return "-" + (str(variable['step'] * it))
    return None


class VelokazScrapper:

    def __init__(self, url):
        self.root = url
        self.data = requests.get(url).content
        self.parser = BeautifulSoup(self.data, "lxml")

    def getNewRoot(self, child):
        if child == None:
            prs = self.parser
        else:
            prs = child
        return prs

    def handleClass(self, schema, child=None, as_list=False):
        prs = self.getNewRoot(child)
        args = {"class": schema['target']}
        if schema['occurs'] == "one":
            return prs.find(schema['element'], args)
        else:
            pr = prs.find_all(schema['element'], args)
            return BeautifulSoup(''.join([str(x) for x in pr]), "lxml")
        return None

    def handleId(self, schema, child=None, as_list=False):
        prs = self.getNewRoot(child)
        args = {"id": schema['target']}
        if schema['occurs'] == "one":
            return prs.find(schema['element'], args)
        else:
            pr = prs.find_all(schema['element'], args)
            return BeautifulSoup(''.join([str(x) for x in pr]), "lxml")
        return None

    def handleNormal(self, schema, child=None, as_list=False):
        prs = self.getNewRoot(child)
        if schema['occurs'] == "one":
            return prs.find(schema['element'])
        else:
            pr = prs.find_all(schema['element'])
            if as_list: return pr
            else: return BeautifulSoup(''.join([str(x) for x in pr]), "lxml")
        return None

    def getPaginationURL(self, schema):
        mini_scrapper = VelokazScrapper(schema['url'])
        inner_schema_process = schema['paginate']['process']
        result = None
        for process in inner_schema_process:
            result = mini_scrapper.get(process, result)
        return result[0]

    def handleText(self, schema, child=None, as_list=False):
        prs = self.getNewRoot(child)
        if schema['occurs'] == "one":
            return prs.find(schema['element']).text
        else:
            pr = prs.find_all(schema['element'])
            result = [p.text for p in pr]
            if as_list: return result
            else: return BeautifulSoup(' '.join([str(x) for x in result]), "lxml")
        return None

    def handleAttribute(self, schema, child=None, as_list=False):
        prs = self.getNewRoot(child)
        pr = prs.find_all(schema['element'])
        result = [p[schema['target']] for p in pr]
        if as_list:
            return result
        else:
            return BeautifulSoup(' '.join([str(x) for x in result]), "lxml")
        return None

    def handleFetch(self, schema, child, as_list):
        prs = self.getNewRoot(child)
        results = []
        for target in schema['targets']:
            if target['occurs'] == "one":
                return prs.find(target['element']).text
            else:
                pr = prs.find_all(target['element'])
                result = [p.text for p in pr]
                if not as_list:
                    result = BeautifulSoup(' '.join([str(x) for x in result]), "lxml")
            results.append({
                target['name']: result
            })
        return results

    def get(self, schema, child=None, as_list=False):
        type = schema['type']
        if schema['as_list']: as_list = True
        if type == "class":
            return self.handleClass(schema, child, as_list)
        elif type == "id":
            return self.handleId(schema, child, as_list)
        elif type == "normal":
            return self.handleNormal(schema, child, as_list)
        elif type == "text":
            return self.handleText(schema, child, as_list)
        elif type == "attribute":
            return self.handleAttribute(schema, child, as_list)
        elif type == "fetch":
            return self.handleFetch(schema, child, as_list)
        return None

    def getDynamic(self, schema, child=None, as_list=False, variables=[]):
        pass

    def paginate(self, schema, child=None, as_list=False):
        if schema['has_paginate']:
            next_page_url = self.getPaginationURL(schema)
        else:
            result = None
        pass
