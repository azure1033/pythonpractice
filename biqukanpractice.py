# the 21th practice

import re 
import requests

url = 'https://www.biqukan8.cc/1_1094/5403177.html'
headers = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
req = response.text
title = re.findall(r'<title>(.*?)</title>', req, re.S)
contents = re.findall(r'<div id="content" class="showtxt">(.*?)</div>', req, re.S)
content = re.sub(r'<script>|</script>|<br />|&nbsp|;|app2()|read2()', '', str(contents))
with open('一念永恒.txt', 'w',encoding='utf-8') as f:
    f.write(content)
