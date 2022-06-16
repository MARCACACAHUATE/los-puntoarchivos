from scrapy.http import TextResponse
import scrapy

class NoticiasSpider(scrapy.Spider):
    name = "noticias"
    start_urls = [

    ]


    def parse(self, response: TextResponse):
        response.xpath()