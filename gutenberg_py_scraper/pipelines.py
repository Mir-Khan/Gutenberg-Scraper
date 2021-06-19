# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import itemadapter
from scrapy.pipelines.files import FilesPipeline

class GutenbergPyScraperPipeline:
    def process_item(self, item, spider):
        return item

class ModifiedFilePipeline(FilesPipeline):
    pass
    def file_path(self, request, response=None, info=None):
        file_name: str = request.url.split("/")[-1]
        return file_name