# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
from requests.auth import HTTPBasicAuth
from itemadapter import ItemAdapter


class CbfCloudPipeline:
    def process_item(self, item, spider):

        # Atualizando API no HEROKU
        r = requests.post(url="https://cbf-jogos.herokuapp.com/jogos/",
                          auth=HTTPBasicAuth("caio", "HarperLee"), data=item)

        if not r.ok:
            url=f"https://cbf-jogos.herokuapp.com/jogos/{item['numero']}/"
            requests.put(url, auth=HTTPBasicAuth("caio", "HarperLee"), data=item)
        
        return item
