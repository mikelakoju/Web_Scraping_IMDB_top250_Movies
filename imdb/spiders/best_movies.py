# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//tbody[@class='lister-list']/tr"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt']/h1/text()").get(),
            'year': response.xpath("//div[@class='TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr']/ul/li[1]/span/text()").get(),
            'duration': response.xpath("//div[@class='TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr']/ul/li[3]/text()").get(),
            'genre': response.xpath("//a[@class='GenresAndPlot__GenreChip-cum89p-3 fzmeux ipc-chip ipc-chip--on-baseAlt']/span/text()").get(),
            'rating': response.xpath("//div[@class='AggregateRatingButton__ContentWrap-sc-1ll29m0-0 hmJkIS']/div/span[1]/text()").get(),
            'movie_url': response.url,
        }
