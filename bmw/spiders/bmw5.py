import scrapy
from bmw.items import BmwItem


class Bmw5Spider(scrapy.Spider):
    # start启动时需要用到，名字必须是唯一的
    name = 'bmw5'
    # 允许的域名，限制爬虫的范围
    allowed_domains = ['car.autohome.com.cn']
    # 开始的url，可传递多个
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454438']

    def parse(self, response):
        # response是scrapy自己帮我们传回的响应数据，直接拿来用
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            # 获取类别名称
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            # 获取图片下载路径
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # map需要一个函数和list，lambda匿名函数使用urljoin方法补齐urls列表传递过来的每一个url参数
            urls = list(map(lambda url: response.urljoin(url), urls))
            # 引用BmwItem，传递必须的参数
            item = BmwItem(category=category, image_urls=urls)
            yield item