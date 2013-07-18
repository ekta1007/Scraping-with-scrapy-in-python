
# A baby problem in scraping in python  - will keep this file seperate and add more files in the repository

# For an overview on scrapy - see the official documentation at - 
# http://doc.scrapy.org/en/latest/intro/tutorial.html

# To start a new scrapy project 
scrapy startproject ebay

# This will create the folder structures - ebay-> ebay-> spiders - of this we will modify the items.py file to add the fields that you wnat to extract

# items.py file in ebay/ebay
from scrapy.item import Item, Field

class EbayItem(Item):
    # define the fields for your item here like:
    # name = Field()
    allurls = Field()
    price2 = Field()
    name=Field()
    pass


# My_Basic_spider.py in ebay->ebay->spiders 
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from ebay.items import EbayItem
# Note that EbayItem is a class of the file in the items.py in the ebay->ebay directory and defines the fields that we want to extract from #the web pages in scope/allowed_domains .

# Note that for now, we use only the "BaseSpider" class with just one start url - and will use Crawlspider class that extends 
class MySpider(BaseSpider):
    name = "ebay"
    allowed_domains = ["ebay.com"]
    start_urls = ["http://www.ebay.com/rpp/marketingcampaign/under-armour-sport-essentials/shop-all/for-her?_trkparms=clkid%3D9132820885905073443"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        allurls=hxs.select("id('e4')/div/a/@href").extract()
        #=hxs.select("id('e4')/div/a") 
        price2=hxs.select("id('e4')/div/div/span[1]/text()").extract() 
        name= hxs.select("id('e4')/div/a/text()").extract() 
        print allurls
        print '--------'
        print price2
        print '----'
        print name
  	# writing to a csv file 
	    mywriter = csv.writer(open("ebaytest.csv", "wb"))
		head = ("Name", "Price", "urls")
		mywriter.writerow(head)
		for i in range(0,len(price2)):
			mywriter.writerow(name[i],price2[i],allurls[i])
        print ' My first baby scraping was a success!! '
		
		

# To call the crawler, go to the top most directory structure and..
# Note that "ebay" is the name of the spider in Myspider class and this is the one that is used to refer to the spider 
scrapy crawl ebay
# This begins crawling, prints the output to the screen (of course, because you asked for it!) and also genates the csv file, that you can see 
