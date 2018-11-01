import os

BOT_NAME = 'bmw'

SPIDER_MODULES = ['bmw.spiders']
NEWSPIDER_MODULE = 'bmw.spiders'

# True为从网站根目录开始爬取，爬取不到直接暂停。改为False
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1     # 下载延迟(设置爬取数据的间隔)

# 请求头信息
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36'
}
# 可以选择的文件存储方式
ITEM_PIPELINES = {
   # 'bmw.pipelines.BmwPipeline': 300,      # 传统
   'bmw.pipelines.BMWImagesPipeline': 99,   # 重写后的异步下载
}

# 设置图片下载的路径，供images piplines使用
IMAGES_STORE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")