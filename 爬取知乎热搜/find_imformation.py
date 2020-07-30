import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/hot'
headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Cookie':'_zap=86faf9fb-208a-4d03-ad24-c29ca36f1dbb; d_c0="AHCUPPI4KBGPTp8e9pi9rudpBMxLvCQ37FI=|1587537058"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1595509556,1595512248,1595512291,1595517511; _ga=GA1.2.239098809.1587537058; _xsrf=17153EIBGeKkGAZT31AgXpzqAhrWzOic; z_c0="2|1:0|10:1587987441|4:z_c0|92:Mi4xWkYyVUJRQUFBQUFBY0pRODhqZ29FU1lBQUFCZ0FsVk44QkdVWHdCM0pIUDFkSGNRYkFFYnlrdTdmT0dyaFRhYlF3|131d364e05295749aeb2665f328ff49834d7ece7e8879aaa8cfbdb2f06d95be1"; tst=h; q_c1=282ecb2ad41c489fb9f89bc4a95e1e83|1594379324000|1588402898000; tshl=; _gid=GA1.2.1544347816.1595493543; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1595517511; KLBRSID=3d7feb8a094c905a519e532f6843365f|1595517514|1595509557; _gat_gtag_UA_149949619_1=1; SESSIONID=vJoq9UCUxU01pbFnqLYMG9OSNuU6d3uQ7ZQ2XTs3ZkU; JOID=Ul4QAUtsy48Oam2ETW69FnUSLhBZHILnfVM-xB8UmLw4GA_EICNlk1NsaIBIxxuMvZDJKB6SQ85q5YjjIZe6uek=; osd=WlgXBU5kzYgKb2WCSmq4HnMVKhVRGoXjeFs4wxsRkLo_HArMJiRhlltqb4RNzx2LuZXBLhmWRsZs4ozmKZG9vew=',
    'Referer':'https://www.baidu.com/link?url=RbuiMtE5e3yigT_f9L2Jc-iOQnLPdoJ9rvzs3vcobsO&wd=&eqid=fcd1deca0000a7fb000000045f19aa45',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
r = requests.get(url,headers = headers,verify = False)
html = r.text
titles = []
urls = []
hots = []
soup = BeautifulSoup(html,'html.parser')
url = soup.find_all('div',class_='HotItem-content')
for i in url:
    url = i.a.attrs['href']
    urls.append(url)
title = soup.find_all('h2',class_='HotItem-title')
for i in title:
    titles.append(i.get_text())
for title in soup.find_all(attrs={'class':'HotItem-content'}):
    a = re.findall('</svg>(.*?)<span class="HotItem-action">',str(title))
    hots.append(a[0][:-2])
dt = {'rank':range(1,51),'url':urls,'title':titles,'hot':hots}
d = pd.DataFrame(dt)

d.to_csv('zihu.csv',index=False,sep=',')
