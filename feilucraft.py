import requests
import logging
from lxml import etree
import time
from itertools import product

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')
baseurl = input('请输入你抓取的小说的URL:')
headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}


def scrape_url(url):
    logging.info('scrape...%s', url)
    response = requests.get(url,headers)
    time.sleep(1)
    try:
        return response.text
        
    except response.status_code != 200:
        logging.warning('mistake happening...')

def scrape_detail_url():
   urls = parse_url()
   htmls = []
   for url in urls:
       html = scrape_url(url)
       htmls.append(html)
   return htmls

def parse_url():
    basehtml = scrape_url(baseurl)
    target = etree.HTML(basehtml)
    part_urls = target.xpath('//*[@id="mulu"]/div[3]//@href')
    urls = ['https:' + part_url for part_url in part_urls]
    return urls

def parse_titlename(html):
    target = etree.HTML(html)
    title = target.xpath('//*[@id="center"]/div/div[1]/div[1]/h1/text()')
    content = target.xpath('//*[@id="center"]/div/div[1]/div[6]//text()')
    return {'title':title,
            'content':str(content).replace('\n','')}



def main():
        start = time.time()
        titles = [parse_titlename(html)['title']  for html in scrape_detail_url()]
        contents = [parse_titlename(html)['content'] for html in scrape_detail_url()]
        result = product(titles, contents)
        for title, content in result:
            print(title, content, sep='\n')
        end = time.time()
        print(end - start)
    

if __name__ == '__main__':
    main()
