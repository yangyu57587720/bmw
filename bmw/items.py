"""定义传递数据的模型"""
import scrapy


class BmwItem(scrapy.Item):
    # 固定好需要传递什么参数
    category = scrapy.Field()
    image_urls = scrapy.Field()
    # 下载完成后会把下载的路径，url和图片校验码等存放在images
    images = scrapy.Field()
