import scrapy
from scrapy.loader import ItemLoader
from cbf_cloud.items import JogoItem


class CbfSpider(scrapy.Spider):
    f = open(
        "D:\Caio\Projetos-Python\scrapy-cloud-cbf\cbf_cloud\jogos.json", "w"
    ).close()
    name = "cbf"
    allowed_domains = ["cbf.com.br"]
    start_urls = [
        f"https://www.cbf.com.br/amp/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022/{i+1}"
        for i in range(380)
    ]

    def parse(self, response):
        jogo = ItemLoader(item=JogoItem(), response=response)

        # Pega o local no formato ["Estádio", "Cidade", "Estado"]
        # Se o local ainda não foi definido, retorna ["A definir", "A definir", "A definir"]
        local = self.get_local(response)

        # Pega a data no formato "dd/mm/yyyy"
        # Se a data ainda não foi definida, retorna '00/00/0000'
        data = self.get_data(response)

        # Pega a hora no formato "00:00"
        # Se a hora ainda não foi definida, retorna '00:00'
        hora = self.get_hora(response)

        jogo.add_value("numero", int(response.url.split("/")[-1]))
        jogo.add_css("time_mandante", ".jogo-equipe-nome-completo::text")
        jogo.add_css("time_visitante", ".jogo-equipe-nome-completo::text")
        jogo.add_value("data", data)
        jogo.add_value("hora", hora)
        jogo.add_value("estadio", local[0])
        jogo.add_value("cidade", local[1])
        jogo.add_value("estado", local[2])

        return jogo.load_item()

    def get_hora(self, response):
        hora = response.css(".m-t-15 .text-6::text").get()
        if not hora:
            hora = "00:00"
        return hora

    def get_data(self, response):
        data = response.css(".col-xs-6 span::text").get()
        if not data:
            data = "00/00/0000"
        return data

    def get_local(self, response):
        local = response.css(".col-xs-12 span::text").get().split(" - ")
        if "a definir" in local[0].lower():
            local = ["A definir"] * 3
        return local
