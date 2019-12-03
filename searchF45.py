import scrapy
from scrapy.crawler import CrawlerProcess

exercises = None

class F45Crawler(scrapy.Spider):
    name = "f45_spider"

    def start_requests(self):
        urls = ["https://f45training.sg/rivervalley/schedule/"]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
    
    def parse(self, response):
        
        exercises = response.css('div.sm-ptb > ul > li > h6::text').extract()
        days = response.css('div.sm-ptb > ul > li > p::text').extract()
        print(days)
        filepath = 'sports.csv'
        with open(filepath, 'w') as f:
            f.write("URL: " + response.url + "\n")
            f.write("River Valley F45\n")
            f.write("---------------------------")
            for i in range(len(exercises)):
                f.write(exercises[i])
                f.write(days[i])
        

process = CrawlerProcess()

process.crawl(F45Crawler)

process.start()

print(exercises)
