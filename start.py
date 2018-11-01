"""设置启动程序的简单方式"""
from scrapy import cmdline

cmdline.execute("scrapy crawl bmw5".split())
