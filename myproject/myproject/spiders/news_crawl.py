from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from myproject.items import Headline

class NewsCrawlSpider(CrawlSpider):
    name = 'news_crawl'   # 実行時するSpiderの名前。実行場所はscrapy.cfgのいるところで、scrapy crawl news_crawl
    # クロール対象とするドメインのリスト
    allowed_domains = ['news.yahoo.co.jp']
    # クロールを開始するURLのリスト
    start_urls = ['http://news.yahoo.co.jp/']

    # リンクをたどるためのルールのリスト
    rules = (
        # トピックスのページへのリンクを辿り、レスボンスをparse_topics()メソッドで処理する。
        Rule(LinkExtractor(allow='/pickup/\\d+$'), callback='parse_topics'),
    )

    def parse_topics(self, response):
        """
        トピックスのページからタイトルと本文を抜き出す。
        """
        item = Headline()   # Headlineオブジェクトの作成。
        item['title'] = response.css('.newsTitle ::text').extract_first() # タイトル
        item['body'] = response.css('.hbody').xpath('string()').extract_first() # 本文
        #item['body'] = ''.join(response.css('.hbody ::text').extract()) # 本文 CSSセレクターのみを使う場合
        yield item # Itemをyieldして、データを抽出する。
