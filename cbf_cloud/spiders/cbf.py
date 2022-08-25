import scrapy


class CbfSpider(scrapy.Spider):
    name = 'cbf'
    allowed_domains = ['cbf.com.br']
    start_urls = [f"https://www.cbf.com.br/amp/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022/{i}" for i in range(10)]

    def parse(self, response):
        numero_jogo = int(response.url.split('/')[-1].split('?')[0])
        data_jogo = response.css('.col-xs-6 span::text').get()
        return {'data_jogo': data_jogo, 'numero_jogo': numero_jogo}
