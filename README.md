O projeto tem por finalidade pegar informações dos jogos do Campeonato Brasileiro de Futebol Série A diretamente do site oficial da Confederação Brasileira de Futebol (CBF).

A CBF não possui API e portando dificulta o acesso e este spider visa facilitá-lo.

Inicialmente, o spider não pega informações do placar do jogo e nem é atualizado em tempo real.

O spider foi feito com Scrapy e Python e está vinculado ao ScrapingCloud. Futuramente, este spider será rodada de forma automática e atualizará uma API no Heroku, que também será disponibilizada.

EXEMPLO DE RESULTADO DO SPIDER:

{"numero": 6, "time_mandante": "Juventude - RS", "time_visitante": "Red Bull Bragantino - SP", "data": "11/04/2022", "hora": "20:00", "estadio": "Alfredo Jaconi", "cidade": "Caxias do Sul", "estado": "RS"}

INSTRUÇÕES

O projeto foi criado no Python 3.9.6, com o Scrapy 2.6.2

Clone o repositório no local desejado com git clone https://github.com/caioalves19/scrapy-cbf_cloud.git

Inicie um ambiente virtual com python -m venv env

Ative o ambiente virtual com env/Scripts/Activate.ps1

Digitar o comando "pip install -r requirements.txt" para instalar o Scrapy

Depois, entre na pasta do projeto com "cd cbf_cloud"

Para o spider basta digitar o comando "scrapy crawl cbf"

Se desejar gravar a saída em um arquivo JSON basta digitar "scrapy crawl cbf -o jogos.json"
