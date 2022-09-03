import scrapy
from itemloaders.processors import TakeFirst, Compose


def tratar_nome_time(time):
    # A função apenas deixa o nome do time no padrão desejado

    nome_time, estado_time = time.split(' - ')

    nomes_times = {"AMÉRICA FC SAF": "América", "CUIABÁ SAF": 'Cuiabá',
                   "ATLÉTICO MINEIRO": "Atlético", "ATHLETICO PARANAENSE": "Athletico"}

    if nome_time.upper() in nomes_times:
        return nomes_times[nome_time.upper()] + ' - ' + estado_time

    return nome_time + ' - ' + estado_time


class JogoItem(scrapy.Item):
    # define the fields for your item here like:
    numero = scrapy.Field(output_processor=TakeFirst())
    time_mandante = scrapy.Field(
        output_processor=Compose(TakeFirst(), tratar_nome_time))
    time_visitante = scrapy.Field(
        output_processor=Compose(TakeFirst(), tratar_nome_time))
    data = scrapy.Field(output_processor=TakeFirst())
    hora = scrapy.Field(output_processor=TakeFirst())
    estadio = scrapy.Field(output_processor=TakeFirst())
    cidade = scrapy.Field(output_processor=TakeFirst())
    estado = scrapy.Field(output_processor=TakeFirst())
