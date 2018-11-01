"""可以选择的保存数据方式和路径"""
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from bmw import settings


class BmwPipeline(object):
    """传统下载和分类方法"""
    def __init__(self):
        # 实例化一个images的文件并获取这个文件的路径
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")
        # 当前目录下没有就创建一个
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        # 获取爬取的数据结果
        category = item["category"]
        urls = item["urls"]
        # 拼接路径
        category_path = os.path.join(self.path, category)
        # 没有这个类别的目录就创建一个
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            # 获取图片的名字并存储到对应的目录
            image_name = url.split("_")[-1]
            request.urlretrieve(url, os.path.join(category_path, image_name))
        return item


class BMWImagesPipeline(ImagesPipeline):
    """重写文件存储路径异步下载方法"""
    def get_media_requests(self, item, info):
        # 发送下载请求之前被调用，然后去发送下载请求
        request_objs = super(BMWImagesPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            # 重新赋值item,并返回修改后的结果
            request_obj.item = item
        # 重写后必须return返回给下一个函数处理
        return request_objs

    def file_path(self, request, response=None, info=None):
        # 在图片将要被存储的时候调用，来获取这个图片的存储路径
        path = super(BMWImagesPipeline, self).file_path(request, response, info)
        # 获取传递的类别名称
        category = request.item.get("category")
        # 设置图片下载的路径
        images_store = settings.IMAGES_STORE
        # 拼接存储路径
        category_path = os.path.join(images_store, category)
        # 没有这个类别路径就创建
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        # 替换源码本身的图片名
        image_name = path.replace("full/", "")
        # 设置对应图片的路径下载地址
        image_path = os.path.join(category_path, image_name)
        return image_path