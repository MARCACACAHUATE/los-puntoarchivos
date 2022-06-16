from scrapy.http import TextResponse
import scrapy

class NoticiasSpider(scrapy.Spider):
    name = "noticias"
    start_urls = [
        "https://www.elfinanciero.com.mx",
        "https://www.larepublica.co",
        "https://www.eluniversal.com.mx",
        "https://www.jornada.com.mx",
        "https://www.milenio.com"
    ]


    def parse(self, response: TextResponse):
        cuerpo = response.body()
        print(cuerpo.decode())