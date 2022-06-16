from ast import match_case
from email import utils
from scrapy.http import TextResponse
import scrapy
from .xpath import * 

class NoticiasSpider(scrapy.Spider):
    name = "noticias"
    start_urls = [
        "https://www.elfinanciero.com.mx",
        "https://www.larepublica.co",
       #"https://www.eluniversal.com.mx",
       #"https://www.jornada.com.mx",
       #"https://www.milenio.com"
    ]

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)


    def parse(self, response: TextResponse):
        
        # Inicializa los xpath y categorias de cada pagina
        match response.url:
            case "https://www.elfinanciero.com.mx":
                xpath = xpath_paginas["elfinanciero"] 
                links_categorias = categorias["elfinanciero"]
            
            case "https://www.larepublica.co":
                xpath = "Cosas de laRepublica"
                links_categorias = categorias["larepublica"]

            case "https://www.eluniversal.com.mx":
                xpath = xpath_paginas["eluniversal"]
                links_categorias = ["eluniversal"]


        # scrapeamos la pagina principal de la pagina
        for key, value in xpath.items():
            noticias = response.xpath(value).getall()

        # scrapeamos cada categoria de la pagina
        

        noticias_links = list(set(noticias))
        self.log(f"los links de las noticias son: {noticias}")
        # Noticias


    def parse_noticias(self, resposne: TextResponse):
        pass