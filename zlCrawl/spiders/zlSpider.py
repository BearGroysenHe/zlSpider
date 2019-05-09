# -*- coding: utf-8 -*-
import scrapy
import json
import sys
sys.path.append(__file__)
from ..items import ZlcrawlItem
import re


class ZlspiderSpider(scrapy.Spider):
    name = 'zlSpider'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?start=1&pageSize=100&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.20504341&x-zp-page-request-id=db316ddc5ff0471da99c44475cc166c8-1557389657650-25108']
    start = 101
    def parse(self, response):
        results =  json.loads(response.body.decode('utf-8'))['data']['results']
        for result in results:
            item = ZlcrawlItem(job_name = result['jobName'],degree_requirement = result['eduLevel']['name'],
                               work_experence_requirement = result['workingExp']['name'],location = result['city']['display'],
                               welfare = result['welfare'],company_name = result['company']['name'],url = result['company']['url'],
                               salary = result['salary'])
            yield item
        if ZlspiderSpider.start < 1000:
            new_url = re.sub(r'start=\d*','start=%d'%(ZlspiderSpider.start),ZlspiderSpider.start_urls[0],1)
            ZlspiderSpider.start += 100
            yield scrapy.Request(url = new_url,callback=self.parse)

