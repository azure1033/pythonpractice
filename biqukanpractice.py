
from lxml import etree
import requests
from requests.packages import urllib3
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s : %(message)s')
BASE_URL = 'https://www.biqukan8.cc/1_1094/'
headers = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
chapters = 100


def scrape_page(url):
    logging.info('scrape %s', url)
    urllib3.disable_warnings()
    response = requests.get(url,headers)
    print(response.status_code)
    if response.status_code == 200:
        return response.text
    else:
        logging.warning('dont find %s',response.status_code)
def parse_url(url):
    html = etree.HTML(scrape_page(url))
    details = html.xpath('//div[@class="listmain"]//a/@href')
    return details
    
def main():
    part_urls = parse_url(BASE_URL)
    for detail in part_urls[range(1, chapters +1)]:
        detail_url = urljoin(BASE_URL, detail)
        html = scrape_page(detail_url)
        dic = parse_details(html)
        with open('biqukan.txt', 'a', encoding='utf-8') as f:
            f.write(dic['title'], dic['content'], sep='\n')


def parse_details(html):
    detail_html = etree.HTML(html)
    title = detail_html.xpath('//div[@class="content"]//h1/text()')
    content = detail_html.xpath('//div[@id="content" and @class="showtxt"]//br/text()')
    return {
        'title':title,
        'content':content
    }


if __name__ == '__main__':
    main()
    logging.info('over')
