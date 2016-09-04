import scrapy


class WageSpider(scrapy.Spider):
    name = 'blsgov'
    allowed_domains = ['example.com']
    start_urls = ['http://www.bls.gov/oes/current/oes111011.htm']

    def parse(self, response):
        for desc in response.xpath('//*[@id="bodytext"]/p[1]/text()').extract():
            yield {"description": desc}

        for job_id in response.xpath('//*[@id="bodytext"]/h2/text()').extract():
            yield {"job_id": job_id}






