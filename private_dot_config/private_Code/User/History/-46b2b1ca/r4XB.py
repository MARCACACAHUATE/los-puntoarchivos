from scrapy.http import TextResponse
import scrapy

class NoticiasSpider(scrapy.Spider):
    name = "noticias"
    start_urls = [
        "www.elfinanciero.com.mx",
        "www.larepublica.co",
        "www.eluniversal.com.mx",
        "www.jornada.com.mx",
        "www.milenio.com"
    ]


    def parse(self, response: TextResponse):
        response.xpath()