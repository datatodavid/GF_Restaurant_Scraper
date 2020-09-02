from findmegf_long.items import FindMeGFItem
from scrapy import Spider, Request
import re
import math

class FindMeGFSpider(Spider):
    name = 'findmegf_long_spider'
    allowed_urls = ['https://www.findmeglutenfree.com']
    start_urls = ['https://www.findmeglutenfree.com']
    # start_urls = [f'https://www.zillow.com/denver-co/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22denver%2C%20co%22%2C%22mapBounds%22%3A%7B%22west%22%3A-105.96514707223652%2C%22east%22%3A-103.80633359567402%2C%22south%22%3A39.05600865335748%2C%22north%22%3A40.29683428039092%7D%2C%22customRegionId%22%3A%22c5a0f5f4c2X1-CR1otvrmlx1lnr2_uv3g4%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A11093%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D']
    # start_urls = ['https://www.zillow.com/denver-co/?searchQueryState=%7B%22usersSearchTerm%22%3A%22denver%2C%20co%22%2C%22mapBounds%22%3A%7B%22west%22%3A-105.37737851754902%2C%22east%22%3A-104.29797177926777%2C%22south%22%3A39.486579388443936%2C%22north%22%3A40.10593600620436%7D%2C%22customRegionId%22%3A%22c5a0f5f4c2X1-CR1otvrmlx1lnr2_uv3g4%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A11093%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%7D%2C%22isListVisible%22%3Atrue%7D']

    def parse(self, response):
        us_city_urls = [i for i in response.xpath('//footer[@class="container py-5"]/div//@href').extract() if '/us/' in i]
        us_city_urls = ['https://www.findmeglutenfree.com' + url for url in us_city_urls]

        # print('='*55)
        # print(len(us_city_urls))
        # print('='*55)

        # for url in us_city_urls[:2]: # WHEN TESTING USE THIS TO LIMIT
        for url in us_city_urls:
            yield Request(url=url, callback=self.parse_neighborhood_page)

    def parse_neighborhood_page(self, response):
        current_url = ['https://www.findmeglutenfree.com' + response.xpath('//ul[@class="list-unstyled mt-2 p-2 tags-list"]//@href').extract_first()]
        try:
            city_neighborhood_urls = response.xpath('//ul[@class="list-unstyled mt-2 p-2"]//@href').extract()
            city_neighborhood_urls = ['https://www.findmeglutenfree.com' + url for url in city_neighborhood_urls]
            city_neighborhood_urls = current_url + city_neighborhood_urls
        except:
            city_neighborhood_urls = current_url

        for url in city_neighborhood_urls: # WHEN TESTING USE THIS TO LIMIT
        # for url in city_neighborhood_urls:
            yield Request(url=url, callback=self.parse_results_page)

    def parse_results_page(self, response):
        rest_urls = response.xpath('//div[@class="sl-title"]//@href').extract()
        rest_urls = ['https://www.findmeglutenfree.com' + url for url in rest_urls]

        # print('='*55)
        # print(len(rest_urls))
        # print('='*55)
        
        # for url in rest_urls[:2]: # WHEN TESTING USE THIS TO LIMIT
        for url in rest_urls:
            yield Request(url=url, callback=self.parse_listing_page)

    def parse_listing_page(self, response):
        rev = response.xpath('//div[@class="col-lg-8 mb-2"]')
        

        page_url = response.request.url
        try:
            name = rev.xpath('.//h1/text()').extract_first()
        except:
            name = None
        try:
            avg_rating = float(rev.xpath('.//span[@class="rating-stars align-baseline"]/@title').extract_first()[0:3])
        except:
            avg_rating = None
        try:
            num_ratings = int(rev.xpath('.//span[@class="rating-num align-middle ml-2"]/text()').extract_first().split(" ")[0])
        except:
            num_ratings = None
        try:
            num_reviews = len(rev.xpath('.//div[@class="rev-username rev-overflow-e"]//text()').extract())  
        except:
            num_reviews = None
        try:
            how_expensive = rev.xpath('.//span[@class="ml-2 align-middle"]/text()').extract_first()
        except:
            how_expensive = None
        # perc_celiac_friendly = int(rev.xpath('.//div/div/text()').extract()[17].split("%")[0])
        # total_celiac_freindly = int(rev.xpath('.//div/div/text()').extract()[17].split(" votes")[0].split('of ')[1])
        try:
            total_celiac_friendly = len([i for i in rev.xpath('.//p/text()').extract() if 'Yes\n' in i])
        except:
            total_celiac_friendly = None
        try:
            total_not_celiac_friendly = len([i for i in rev.xpath('.//p/text()').extract() if 'No\n' in i])
        except:
            total_not_celiac_friendly = None
        try:
            total_reviewers_celiac = len([i for i in rev.xpath('//div[@class="rev-ul rev-overflow-e"]//text()').extract() if 'Celiac' in i])
        except:
            total_reviewers_celiac = None
        try:
            address = rev.xpath('.//span[@class="mr-3"]/text()').extract_first().split(', ')[0]
        except:
            address = None
        try:
            city = rev.xpath('.//span[@class="mr-3"]/text()').extract_first().split(', ')[-2]
        except:
            city = None
        try:
            state = rev.xpath('.//span[@class="mr-3"]/text()').extract_first().split(', ')[-1][0:2]
        except:
            state = None
        try:
            zipcode = rev.xpath('.//span[@class="mr-3"]/text()').extract_first().split(', ')[-1][3:]
        except:
            zipcode = None
        try:
            phone = rev.xpath('.//div[@class="mt-3 font-weight-bold"]//text()').extract_first()
        except:
            phone = None
        try:
            business_url = rev.xpath('.//div[@class="mt-3 mr-3"]//text()').extract()[1]
        except:
            business_url = None
        try:
            gf_features = rev.xpath('.//div[@class="row mt-4 biz-tags-c p-4"]/div[1]/ul/li/text()').extract()
        except:
            gf_features = None
        try:
            dedicated_gf = bool([i for i in rev.xpath('.//div[@class="row mt-4 biz-tags-c p-4"]/div[1]/ul/li/text()').extract() if 'Dedicated Gluten Free Facility' in i])
        except:
            dedicated_gf = None
        try:
            dedicated_fryer = bool([i for i in rev.xpath('.//div[@class="row mt-4 biz-tags-c p-4"]/div[1]/ul/li/text()').extract() if 'Dedicated Fryer' in i])
        except:
            dedicated_fryer = None
        try:
            gf_menu = bool([i for i in rev.xpath('.//div[@class="row mt-4 biz-tags-c p-4"]/div[1]/ul/li/text()').extract() if 'Gluten Free Menu' in i])
        except:
            gf_menu = None
        try:
            categories = rev.xpath('.//div[@class="row mt-4 biz-tags-c p-4"]/div[2]/ul/li/text()').extract()
        except:
            categories = None
        try:
            reviewer_name = rev.xpath('.//div[@class="rev-username rev-overflow-e"]//text()').extract()
        except:
            reviewer_name = None
        try:
            review_rating = rev.xpath('.//span[@class="rating-stars align-baseline"]/@title').extract()[1:]
        except:
            review_rating = None
        try: 
            nolist = ['Yes\n', 'No\n', '— Very\n', '— Very confident\n', '— Not very\n', 'Not Much\n', '— Gluten-free items are marked on the main menu\n', '— No gluten-free information on the menu\n', '— Separate gluten-free menu\n',  '— Most\n',  '— Some\n', '— Not at all\n', '— None\n', '— Excellent\n', '— Somewhat\n', '— Below Average\n', '— Good\n', '— Average\n', '— Poor\n']  
            newlistrev = [str for str in rev.xpath('.//p/text()').extract() if all(no_str not in str for no_str in nolist)]
            newlistrev2 = [str + "..." for str in newlistrev] 
            newlistclean = ' '.join(newlistrev2).split('\n...')
            review_text = newlistclean[:-1]
        except:
            review_text = None
        
            


        item = FindMeGFItem()
        item['page_url'] =  page_url
        item['name'] = name
        item['avg_rating'] = avg_rating
        item['num_ratings'] = num_ratings
        item['num_reviews'] = num_reviews
        item['how_expensive'] = how_expensive
        # item['perc_celiac_friendly'] = perc_celiac_friendly
        item['total_celiac_friendly'] = total_celiac_friendly
        item['total_not_celiac_friendly'] = total_not_celiac_friendly
        item['total_reviewers_celiac'] = total_reviewers_celiac
        item['address'] = address
        item['city'] = city
        item['state'] = state
        item['zipcode'] = zipcode
        item['phone'] = phone
        item['business_url'] = business_url
        item['gf_features'] = gf_features
        item['dedicated_gf'] = dedicated_gf
        item['dedicated_fryer'] = dedicated_fryer
        item['gf_menu'] = gf_menu
        item['categories'] = categories
        item['reviewer_name'] = reviewer_name
        item['review_rating'] = review_rating
        item['review_text'] = review_text
       
        yield item
