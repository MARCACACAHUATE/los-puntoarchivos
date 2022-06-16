from ast import match_case
from scrapy.http import TextResponse
import scrapy

class NoticiasSpider(scrapy.Spider):
    name = "noticias"
    start_urls = [
        "https://www.elfinanciero.com.mx",
       #"https://www.larepublica.co",
       #"https://www.eluniversal.com.mx",
       #"https://www.jornada.com.mx",
       #"https://www.milenio.com"
    ]

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.categorias = {
            "elfinanciero": [
                "https://www.elfinanciero.com.mx/tv/",
                "https://www.elfinanciero.com.mx/economia/",
                "https://www.elfinanciero.com.mx/empresas/",
                "https://www.elfinanciero.com.mx/nacional/",
                "https://www.elfinanciero.com.mx/FoxSports/",
                "https://www.elfinanciero.com.mx/bloomberg-businessweek/",
                "https://www.elfinanciero.com.mx/salud/",
                "https://www.elfinanciero.com.mx/suplementos/",
                "https://www.elfinanciero.com.mx/mundo-empresa/",
                "https://www.elfinanciero.com.mx/mundo/",
                "https://www.elfinanciero.com.mx/tech/",
            ]
        }
        self.xpath = {
            "elfinanciero": {
                ""
            }
        }

    def parse(self, response: TextResponse):
        # Links a todas las categorias
        links = []

        # Noticias
        noticias_populares = response.xpath('//section[@id="main"]//section[2]//a[contains(@class, "headline")]/@href').getall()
        noticias_principal = list(set(response.xpath("//section[@id='main']//section[1]//a/@href").getall()))
        self.log(noticias_populares)
        self.log(noticias_principal)


    def parse_noticias(self, resposne: TextResponse):
        pass