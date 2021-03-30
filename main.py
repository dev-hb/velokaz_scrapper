from velokaz_scrapper import VelokazScrapper
import json
from helpers import Helpers

# get scrapping schema
helps = Helpers("schema.json")
schema = json.loads(helps.readFile())

# fetch all the processes and get data
result = None
for page in schema['schema']:
    # create a scrapper instance
    scrapper = VelokazScrapper(page['url'])
    for process in page['process']:
        if process['is_dynamic']:
            result = scrapper.get(process, result)
        else:
            result = scrapper.paginate(process, result)

print(result)
