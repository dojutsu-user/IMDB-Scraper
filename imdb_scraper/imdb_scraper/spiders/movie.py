# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

SEARCH_QUERY = (
    'https://www.imdb.com/search/title?'
    'title_type=feature&'
    'user_rating=1.0,10.0&'
    'countries=us&'
    'languages=en&'
    'count=250&'
    'view=simple'
)


class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['imdb.com']
    start_urls = [SEARCH_QUERY]

    rules = (Rule(
        LinkExtractor(restrict_css=('div.desc a')),
        follow=True,
        callback='parse_query_page',
    ),)

    def parse_query_page(self, response):
        links = response.css('span.lister-item-header a::attr(href)').extract()
        for link in links:
            yield response.follow(link, callback=self.parse_movie_detail_page)

    def parse_movie_detail_page(self, response):
        data = {}
        data['title'] = response.css('h1::text').extract_first().strip()
        data['rating'] = response.css(
            '.subtext::text').extract_first().strip() or None
        data['year'] = response.css('#titleYear a::text').extract_first()
        data['users_rating'] = response.xpath(
            '//span[contains(@itemprop, "ratingValue")]/text()').extract_first()
        data['votes'] = response.xpath(
            '//span[contains(@itemprop, "ratingCount")]/text()').extract_first()
        data['metascore'] = response.xpath(
            '//div[contains(@class, "metacriticScore")]/span/text()').extract_first()
        data['img_url'] = response.xpath(
            '//div[contains(@class, "poster")]/a/img/@src').extract_first()
        countries = response.xpath(
            '//div[contains(@class, "txt-block") and contains(.//h4, "Country")]/a/text()').extract()
        data['countries'] = [country.strip() for country in countries]
        languages = response.xpath(
            '//div[contains(@class, "txt-block") and contains(.//h4, "Language")]/a/text()').extract()
        data['languages'] = [language.strip() for language in languages]
        actors = response.xpath('//td[not(@class)]/a/text()').extract()
        data['actors'] = [actor.strip() for actor in actors]
        genres = response.xpath(
            "//div[contains(.//h4, 'Genres')]/a/text()").extract()
        data['genre'] = [genre.strip() for genre in genres]
        tagline = response.xpath(
            '//div[contains(string(), "Tagline")]/text()').extract()
        data['tagline'] = ''.join(tagline).strip() or None
        data['description'] = response.xpath(
            '//div[contains(@class, "summary_text")]/text()').extract_first().strip() or None
        directors = response.xpath(
            "//div[contains(@class, 'credit_summary_item') and contains(.//h4, 'Director')]/a/text()").extract() or None
        if directors:
            data['directors'] = [director.strip() for director in directors]
        data['runtime'] = response.xpath(
            "//div[contains(@class, 'txt-block') and contains(.//h4, 'Runtime')]/time/text()").extract_first() or None
        data['imdb_url'] = response.url.replace('?ref_=adv_li_tt', '')

        yield data
