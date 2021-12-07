# Scrapy settings for pinwheel project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'irs_forms'

SPIDER_MODULES = ['irs_forms.spiders']
NEWSPIDER_MODULE = 'irs_forms.spiders'

ROBOTSTXT_OBEY = True

