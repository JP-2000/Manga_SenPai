import scrapy

links_list = []

for i in range (1, 5):
    links_list.append("https://manganelo.com/genre-all/%d?type=topview"%(i))

print(links_list)
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://manganelo.com/chapter/read_one_punch_man_manga_online_free3/chapter_1"]

    def parse(self, response):
        #panel = response.css('div.container-chapter-reader')
        #images = panel.css('img::attr(src)').getall()
        chapter = response.css('div.panel-chapter-info-top h1::text').get()
        #chapter = details[len(details) - 1]
        #for img in images: 
        yield {
            "chapter" : chapter
        }
        next_chapter = response.css('div.navi-change-chapter-btn a.navi-change-chapter-btn-next.a-h::attr(href)').get()
        if next_chapter is not None:
            yield response.follow(next_chapter, callback=self.parse)














    '''    #for container in response.css('div.genres-item-info'): 
        #yield {
         #   'title' : response.css('div.panel-story-info-description h3::text').get()
        #}

        next_pages = response.css('div.content-genres-item div.genres-item-info h3 a::attr(href)').getall()
        for next_page in next_pages:
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse_manga)
        
    def parse_manga(self, response):
        chap_box = response.css('div.panel-story-chapter-list')
        chap_list = chap_box.css('ul li a::attr(href)').getall()
        for chap in chap_list:
            #yield {
             #   'title': chap
            #}
            if chap is not None:
                yield response.follow(chap, callback=self.parse_chap)
    
    def parse_chap(self, response):
        page_box = response.css('div.container-chapter-reader')
        page_list = page_box.css('img::attr(src)').getall()
        for i in range(0, 100):
            yield {
                'text' : page_list[i]
            }''' 
