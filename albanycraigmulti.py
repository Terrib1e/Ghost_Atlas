from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scraper.items import CraigslistItem

class MySpider(CrawlSpider):
    name = "craigs"
    allowed_domains = ["albany.craigslist.org"]
    start_urls = ["https://albany.craigslist.org/search/jjj?query=tech"]

    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items", follow= True),
    )
    def parse_start_url(self, response):
        return self.parse_items(response)

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//span[@class="pl"]')
        items = []
        for titles in titles:
            item = CraigslistItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return(items)
