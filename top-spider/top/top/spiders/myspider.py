import scrapy
class DmozSpider(scrapy.Spider):
    name = "demoz"
    allowed_domains = ["weibo.com"]
    start_urls = [
        "https://s.weibo.com/top/summary"
    ]
    def parse(self, response):
        print('hahah')
        titles = response.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr[2]/td[2]/a').extract()
        for title in titles:
            print(title.strip())
    # def parse(self, response):
    #     for line in response.xpath('//*[@id="pl_top_realtimehot"]/table/tbody'):
    #         # 初始化item对象保存爬取的信息
    #         item = TopItem()
    #         # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
    #         item['title'] = line.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr[1]/td[2]/a').extract()
    #         yield item

