
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

base_url = 'https://www.xbiquge.bz/book/45525/'



def scrape_url(url):
    response = requests.get(url)
    return response.text

def B_S(html):
    soup = BeautifulSoup(html,'lxml')
    return soup

def detail_html():
    soup = B_S(scrape_url(base_url))
    for part in (soup.find_all(name='dd')):
        part_url = part.a.attrs['href']
        wholeurl = urljoin(base_url, part_url)
        yield scrape_url(wholeurl)
###
def parse_title_content(html):
    soup = B_S(html)
    for content in soup.find_all(attrs={'id':'content', 'name':'content'}):
        contents = content.get_text()
    title = soup.find(name='h1').string
    return  {
            'title': title,
            'content': contents
        }
         
    
def main():
    for html in detail_html():
        p = parse_title_content(html)
        title = p['title']
        content = p['content']
        with open('神印王座.txt', 'a', encoding='utf-8') as f:
            f.write(title)
            f.write(content)

if __name__ == '__main__':
    main()
    print('over')
     