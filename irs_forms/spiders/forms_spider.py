import scrapy
from scrapy.crawler import CrawlerProcess
from ..items import IrsFormsItem
import json


class FormsSpider(scrapy.Spider):
    name = "forms"

    custom_settings = {"FEEDS": {"forms_data.csv": {"format": "csv"}}}

    def __init__(self, search=None, *args, **kwargs):
        super(FormsSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value={search}&criteria=formNumber&submitSearch=Find']
    
    def parse(self, response):
        for listItem in response.css('table.picklist-dataTable tr'):
            form_number = listItem.css('td.LeftCellSpacer a::text').get()
            form_title = listItem.css('td.MiddleCellSpacer::text').get()
            year = listItem.css('td.EndCellSpacer::text').get()
            form_link = listItem.css('td.LeftCellSpacer a::attr(href)').get()

            forms = IrsFormsItem()
            forms['form_number'] = form_number
            forms['form_title'] = form_title
            forms['year'] = year
            forms['link'] = form_link
            yield forms

        pageLinks = response.xpath('//div[@class="paginationBottom"]/a/text()').getall()
        index = pageLinks.index('Next »')
        if index:
            links = response.xpath('//div[@class="paginationBottom"]/a/@href').getall()
            next_page = response.urljoin(links[index])
            yield scrapy.Request(next_page, callback=self.parse)
