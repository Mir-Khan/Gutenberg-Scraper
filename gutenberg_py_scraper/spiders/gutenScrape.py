import scrapy

# basically the tutorial class with a couple of private methods I made
# also the crawl delay was modified in settings.py to comply with robots.txt

# this will hold the necessary fields used by scrapy to download files
class TextFileItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()

class TextSpider(scrapy.Spider):
    name = "text"
    
    def __create_base_url(self, num):
        # the base url format used by gutenberg
        return "https://www.gutenberg.org/files/"+ str(num) + "/" + str(num) +"-0.txt"

    def __create_url_list(self):
        retList = []
        # this just gets texts 10-1500, note some numbers don't exist with the url format in create_base_url
        for textNum in range(10, 1501):
            url = self.__create_base_url(textNum);
            retList.append(url);
        return retList;
    
    def start_requests(self):
        urls = self.__create_url_list()
        for url in urls: 
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        file_url = response.url
        item = TextFileItem(file_urls=[file_url])
        yield item