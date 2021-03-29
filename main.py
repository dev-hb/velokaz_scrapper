from movies_scrapper import VelokazScrapper
import json
from helpers import Helpers

# create a scrapper instance
scrapper = VelokazScrapper("https://www.imdb.com/search/keyword/")
# get scrapping schema
helps = Helpers("schema.json")
schema = json.loads(helps.readFile())

l_list = scrapper.get(schema['schema'][0])
l_list = scrapper.get(schema['schema'][1], l_list)

print(scrapper.get(schema['schema'][2], l_list))
