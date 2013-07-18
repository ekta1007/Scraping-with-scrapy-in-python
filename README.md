Scraping-with-scrapy-in-python
==============================

A baby problem in scraping in python 

For an overview on scrapy - see the official documentation at -  http://doc.scrapy.org/en/latest/intro/tutorial.html

I have tried to keep the "baby_scaping.py" as basic/bare-bones as possible(I have not even used the lxml) - will add more files to this repo on pagination & intelligent crawling, mainly the bits on recursive scraping, also called a crawlspider.
With an optimally designed Crawlspider - you can navigate the pages in a website and only extract the elements of interest. An optimial crawlspider will also keep a memory tab on what is already crawled - so that the crawler does not get stuck in an infinite loop. 
Note also that crwling with approprite rules, can get a very memory intensive activity - no wonder there are ways to run bots on your personal machine, as a proxy to someone else's use case .



For now, all you need to understand this is 3 broad things -:
1. What a scraper really does and the overview of offcial Tutorial 
2. Building Xpaths and trying it out with XPath checker plugin in modzilla
3. Writing your spider to extract the items of interest from the webpage.


for suggestions, comments, collaboration, rech out to me at ekta1007@gmail.com 

