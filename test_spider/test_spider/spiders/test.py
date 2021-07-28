import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
    
        quotes = response.xpath("//*[@class='quote']")
        for quote in quotes:
            text = quote.xpath(".//*[@class='text']").extract_first()
            author = quote.xpath(".//*[@itemprop='author']").extract()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            print('\n')
            print(text)
            print(author)
            print(tags)
            print('\n')

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)