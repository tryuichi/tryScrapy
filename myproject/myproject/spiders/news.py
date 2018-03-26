import scrapy

class NewsSpider(scrapy.Spider):
    name = 'news'   # 実行時するSpiderの名前。実行場所はscrapy.cfgのいるところで、scrapy crawl news
    # クロール対象とするドメインのリスト
    allowed_domains = ['news.yahoo.co.jp']
    # クロールを開始するURLのリスト
    start_urls = ['http://news.yahoo.co.jp/']

    def parse(self, response):
        """
        トップページのトピックス一覧から個々のトピックスへのリンクを抜き出して表示する。
        """
        for url in response.css('ul.topics a::attr("href")').re(r'/pickup/\d+$'):
            yield scrapy.Request(response.urljoin(url), self.parse_topics)
        
    def parse_topics(self, response):
        pass
