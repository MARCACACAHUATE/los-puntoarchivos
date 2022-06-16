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