import scrapy
import requests


class CbfSpider(scrapy.Spider):
    name = 'cbf'
    allowed_domains = ['cbf.com.br']
    start_urls = [
        f"https://www.cbf.com.br/amp/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022/{i+1}" for i in range(3)]

    def parse(self, response):
        numero_jogo = int(response.url.split('/')[-1].split('?')[0])
        data_jogo = response.css('.col-xs-6 span::text').get()
        jogo = {'numero_jogo': numero_jogo, "time_mandante": "Flamengo",
                "time_visitante": "Vasco",
                "estadio": "São Januário",
                "cidade": "Rio de Janeiro",
                "estado": "RJ"}
        response = requests.post('https://cbf-jogos.herokuapp.com/jogos/', jogo)
        if not response.ok:
            requests.put(f'https://cbf-jogos.herokuapp.com/jogos/{numero_jogo}/', jogo)
        return jogo
