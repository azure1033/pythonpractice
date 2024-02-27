
from urllib.parse import urljoin
import  requests
import re
import logging



base_url = 'https://b.faloo.com/1279070.html'
headers = {
     'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
chapters = 47
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')


def parse_content(html):
    pattern_content = re.compile('<div class="noveContent">(.*?)</div>', re.S)
    contents = re.search(pattern_content, html).group().strip() if re.search(pattern_content, html).group().strip() else None
    content = re.sub('<p>|</p>|<div class="noveContent">|', '', contents)
    return content


def parse_title(html):
    pattern_title = re.compile('<head>.*?<title>(.*?)</title>', re.S)
    title = re.search(pattern_title, html).group(1).strip()
    return title
def newurl(base_url,item):
        url = urljoin(base_url ,item)
        return url

def main():
    for chapter in range(1, chapters + 1):
        item = f'/1279070_{chapter}.html'
        response = requests.get(url=newurl(base_url,item), headers=headers)
        html = response.text
        with open('原神：邀请纳西妲，MC造净善宫.txt', 'a', encoding='utf-8') as f:
            f.write(parse_title(html))
            f.write(parse_content(html))
        logging.info(f'the {chapter} chpater is completed')

    


if __name__ == '__main__':
    main()
    print('over')


