from ast import match_case
from email import utils
from urllib import response
from scrapy.http import TextResponse
import scrapy
from .xpath import * 

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
        self.xpath = None
        self.links_categorias = None


    def parse(self, response: TextResponse):
        
        # Inicializa los xpath y categorias de cada pagina
        match response.url:
            case "https://www.elfinanciero.com.mx":
                self.xpath = xpath_paginas["elfinanciero"] 
                self.links_categorias = categorias["elfinanciero"]
            
            case "https://www.larepublica.co":
                self.xpath = "Cosas de laRepublica"
                self.links_categorias = categorias["larepublica"]

            case "https://www.eluniversal.com.mx":
                self.xpath = xpath_paginas["eluniversal"]
                self.links_categorias = ["eluniversal"]


        # scrapeamos la pagina principal de la pagina
        for key, value in self.xpath["pagina_principal"].items():
            noticias = response.xpath(value).getall()

        # scrapeamos cada categoria de la pagina
        for item in self.links_categorias:
            yield scrapy.Request(item, callback = self.parse_categorias)
        
        noticias_links = list(set(noticias))


    def parse_categorias(self, response: TextResponse):
        for key, value in self.xpath["categorias"].items():
            noticias = response.xpath(value).getall() 
        
        for noticia in noticias:
            print("https://www.elfinanciero.com.mx" + noticia)
            yield scrapy.Request(url = noticia, callback = self.parse_noticias)


    def parse_noticias(self, response: TextResponse):
        self.log(response.body.decode())