import requests
from bs4 import BeautifulSoup


def getHtml(url,header):
    try:
        r = requests.get(url,headers = header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("sorry")

def getimformation(html,title,imformation,score):
    soup = BeautifulSoup(html,'html.parser')
    one = soup.find('ul',class_='subject-list')
    lis = one.find_all('li',class_='subject-item')
    print(lis)
    for li in lis:
        title.append(li.find_all('a')[1]['title'].strip())
        imformation.append(li.find('div',class_='pub').string.strip())
        score.append(li.find('span',class_='rating_nums').string.strip())

def main(title,imformation,score):
    url = 'https://book.douban.com/tag/%E7%BB%8F%E6%B5%8E%E5%AD%A6?type=S'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
    html = getHtml(url,header)
    getimformation(html,title,imformation,score)


title = []
imformation = []
score = []
main(title,imformation,score)