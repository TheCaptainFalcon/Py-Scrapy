import scrapy


class BooksSeleniumSpider(scrapy.Spider):
    name = 'books_selenium_'
    allowed_domains = ['books.toscrape.com/']
    start_urls = ['http://books.toscrape.com//']

    def parse(self, response):
        pass
