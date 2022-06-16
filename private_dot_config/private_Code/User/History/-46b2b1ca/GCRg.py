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
        
        if response.url in self.start_urls:
            xpath = xpath_paginas

        # Links a todas las categorias
        links_categorias = categorias["elfinanciero"]

        # Noticias
        noticias_populares = response.xpath(xpath["noticias_populares"]).getall()
        noticias_principal = list(set(response.xpath(xpath["noticias_principal"]).getall()))
        self.log(noticias_populares)
        self.log(noticias_principal)


    def parse_noticias(self, resposne: TextResponse):
        pass