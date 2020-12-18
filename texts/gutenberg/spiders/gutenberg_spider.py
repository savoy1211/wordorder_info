import scrapy
from scrapy.http import Request
from requests import get
from bs4 import BeautifulSoup as BS


class MySpider(scrapy.Spider):
    name = 'gutenberg'
    allowed_domains = ['gutenberg.org']

    def start_requests(self):
        yield scrapy.Request('https://www.gutenberg.org/browse/authors/a', self.parse)

    def parse(self, response):
        i = 0
        main_url = 'https://www.gutenberg.org'
        check_lang = response.xpath('//li[@class="pgdbetext"]/text()').getall()
        hrefs = response.xpath('//li[@class="pgdbetext"]/a/@href').getall()
        print(check_lang)
        print(hrefs)
        hrefs_lang_filtered = []
        p = 0
        for href in hrefs:
            if 'English' in check_lang[p]:
                hrefs_lang_filtered.append(href)
        
        for href in hrefs_lang_filtered:
            yield scrapy.Request(main_url+href, self.parse_individual)
            # i += 1
            # if i > 15:
            #     break


    # def parse_individual(self, response):
    #     # print(response.xpath('//a[@class="link"]/@href').getall())
    #     main_url = 'https://www.gutenberg.org'
    #     try:
    #         utf = [href for href in response.xpath('//a[@class="link"]/@href').getall() if href[-5:] == 'utf-8'][0]
    #     except Exception:
    #         return
    #     final_url = main_url+utf
    #     response = get(final_url)
    #     soup = BS(response.content, "html.parser")
    #     with open('english/a/'+final_url[final_url.rindex('/')+1:len(final_url)-6], 'w') as f:
    #         f.write(soup.__str__())


    def parse_individual(self, response):
        # print(response.xpath('//a[@class="link"]/@href').getall())
        main_url = 'https://www.gutenberg.org'
        try:
            utf = [href for href in response.xpath('//a[@class="link"]/@href').getall() if href[-5:] == 'utf-8'][0]
        except Exception:
            return
        final_url = main_url+utf
        response = get(final_url)
        soup = BS(response.content, "html.parser")
        with open('english/a/'+final_url[final_url.rindex('/')+1:len(final_url)-6], 'w') as f:
            f.write(soup.__str__())
