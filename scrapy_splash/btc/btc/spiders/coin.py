import scrapy
from scrapy_splash import SplashRequest


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.binance.us/en/markets']

    script = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(0.5))
            btc_tab = assert(splash:select_all(".ReactVirtualized__Table__rowColumn"))
            splash:set_viewport_full()
            return {
                png = splash:png(),
                html = splash:html()
            }
        end   
    '''
            
    def start_requests(self):
        yield SplashRequest(url="https://www.binance.us/en/markets", callback=self.parse, endpoint="execute", args={
            'lua_source' :self.script
        })

    def parse(self, response):
        # for currency in response.xpath("//div[contains(@class, 'sc-62mpio-0 fIHIZl')]//text()"):
        for currency in response.xpath("//div[contains(@class, 'ReactVirtualized__Table__rowColumn')]"):
            # remove .// ?? not sure if needed
            yield {
                "coin" : currency.xpath(".//[3]/text()").get(),
                "last price" : currency.xpath(".//[4]/div/span/text()").get(),
                "24hr Change" : currency.xpath(".//[5]/span/text()").get(),
                "volume 24h" : currency.xpath(".//[9]/text()").get(),
            }


