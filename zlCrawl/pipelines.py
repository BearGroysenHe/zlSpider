# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ZlcrawlPipeline(object):
    def process_item(self, item, spider):
        company_name = item['company_name']
        job_name = item['job_name']
        salary = item['salary']
        location = item['location']
        degree_requirement = item['degree_requirement']
        work_experence_requirement = item['work_experence_requirement']
        welfart = item['welfare']
        url = item['url']
        self.cursor.execute('''insert into PythonJob values('%s','%s','%s','%s','%s','%s',"%s",'%s');'''%(company_name,job_name,salary,location,degree_requirement,work_experence_requirement,welfart,url))
        self.db.commit()

    def open_spider(self,spider):
        self.db = pymysql.connect("localhost","root","123456","zlSpider" )
        self.cursor = self.db.cursor()

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()


