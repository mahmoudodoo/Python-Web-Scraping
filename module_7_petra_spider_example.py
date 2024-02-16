
import scrapy
from scrapy.crawler import CrawlerProcess

class PetraSpider(scrapy.Spider):
    name = 'petra_spider'
    start_urls = ['https://en.wikipedia.org/wiki/Petra']

    def parse(self, response):
        # Extracting the title of the page
        page_title = response.css('h1::text').get()
        # Extracting the first paragraph
        description = response.css('p:nth-of-type(3)::text').get()

        yield {
            'page_title': page_title,
            'description': description,
        }

# Running the spider
process = CrawlerProcess(settings={
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'module_7_petra_info.csv',
})

process.crawl(PetraSpider)
process.start()
