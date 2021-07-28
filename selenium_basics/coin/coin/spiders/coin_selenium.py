import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which



class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.binance.us/en/markets']
    start_urls = [
        "https://www.binance.us/en/markets"
    ]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriver")

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get("https://www.binance.us/en/markets")

        # btc_tab = driver.find_element_by_class_name("ReactVirtualized__Table__rowColumn")
        
        self.html = driver.page_source
        driver.close

    def parse(self, response):
        resp = Selector(text=self.html)
        # for currency in response.xpath("//div[contains(@class, 'sc-62mpio-0 fIHIZl')]//text()"):
        # for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__rowColumn')]"):
            # remove .// ?? not sure if needed
        classShort = ".//div[contains(@class, 'ReactVirtualized__Table__rowColumn')]"
        yield {
            "coin" : resp.xpath(classShort + "[3]/text()".get()),
            "last price" : resp.xpath(classShort + "[4]/div/span/text()".get()),
            "24hr Change" : resp.xpath(classShort + "[5]/span/text()".get()),
            "volume 24h" : resp.xpath(classShort + "[9]/text()".get())
        }


# //div[contains(@class, 'showPrice')]/text()