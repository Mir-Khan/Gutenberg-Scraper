# Gutenberg-Scraper
A Python scraper to grab files from the Gutenberg project for use in another project. This was created using the crawl template for scrapy.

Uploads to a Google Cloud Project with proper setup, has a custom FilesPipeline to grab the proper filename instead of a generated hash.

Files missing that would need a set up:
* spiders/\_\_init\_\_.py
* spiders/settings.py
* spiders/pipelines.py

__Why are they missing?__ They have sensitive information relating to Google Cloud Services, but the initial setup for each file is as follows:

#### spiders/\_\_init\_\_.py
```
import os
import json
import pkgutil
import logging

path = "{}/google-cloud-storage-credentials.json".format(os.getcwd())
# this is where you put the storage credentials content with escaped text
credentials_content = 'ESCAPED CLOUD JSON'

with open(path, "w") as text_file:
    text_file.write(credentials_content)

logging.warning("Path to credentials: %s" % path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
```

### spiders/settings.py
Only the relevant parts that were changed are included below.

```
# this complies with the crawl delay as detailed by the Gutenberg Project robots.txt
DOWNLOAD_DELAY = 5

# the pipelines are outlined here with the relevant info
ITEM_PIPELINES = {
    'gutenberg_py_scraper.pipelines.GutenbergPyScraperPipeline': 300,
    'gutenberg_py_scraper.pipelines.ModifiedFilePipeline': 1
}
FILES_STORE = 'DIRECTORY IN CLOUD WHERE YOU WANT FILES SAVED'
GCS_PROJECT_ID = 'PROJECT ID IN GOOGLE CLOUD'
```

### spiders/pipelines.py
This just has a custom file pipeline that doesn't name the files a hashed name but instead what the file extension is at the webpage.
```
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
```