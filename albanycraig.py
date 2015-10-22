from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scraper.items import CraigslistItem


class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://albany.craigslist.org/search/jjj?query=tech"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//span[@class='pl']")
	items = []
        for titles in titles:
           item = CraigslistItem()
           item["title"] = titles.select("a/text()").extract()
           item["link"] = titles.select("a/@href").extract()
           items.append(item)
        return items
