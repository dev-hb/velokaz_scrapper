from velokaz_scrapper import VelokazScrapper, getVariableTypeValue
import json
from helpers import Helpers
import time

# get scrapping schema
helps = Helpers("schema_list.json")
schema = json.loads(helps.readFile())

# fetch all the processes and get data
result = None
'''
for page in schema['schema']:
    # create a scrapper instance
    if not page['is_dynamic']:
        scrapper = VelokazScrapper(page['url'])
        for process in page['process']:
            result = scrapper.get(process, result)
    else:
        it = 0
        for i in range(142):
            result = None
            dynamic_url = page['url']
            for variable in page['variables']:
                if it > 0:
                    dynamic_url = dynamic_url.replace("{" + variable['name'] + "}", getVariableTypeValue(variable, it))
                else:
                    dynamic_url = dynamic_url.replace("{" + variable['name'] + "}", "")

            it += 1
            print("Processing iteration {}".format(it))
            for process in page['process']:
                scrapper = VelokazScrapper(dynamic_url)
                result = scrapper.get(process, result)

            for r in result:
                if str(r).find("http") == -1:
                    helps.save(r)
'''

url = "https://www.troc-velo.com/vetement-chaussures-northwawe-1-1-2931596.htm"
schema = json.loads(helps.readFile("schema_single.json"))
for page in schema['schema']:
    # create a scrapper instance
    scrapper = VelokazScrapper(url)
    for process in page['process']:
        result = scrapper.get(process, result)

print(result)
