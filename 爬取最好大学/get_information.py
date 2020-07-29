import requests
import bs4
import xlwings as xw
from bs4 import BeautifulSoup


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('failure')


def getimformation(html, lst):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            lst.append([td1.string for td1 in tds])

def gettitle(html,title_lst):
    soup = BeautifulSoup(html,'html.parser')
    tr = soup.find('thead')
    b = tr.find('tr')
    a = b.find_all('th')
    title_lst.append(i.get_text() for i in a[:-1])
    c = b.find_all('option')
    title_lst.append(d.get_text() for d in c
                     )

years = ['2016','2017','2018','2019','2020']

app = xw.App(visible=True,add_book=False)
wb = app.books.add()
wb.save(r'D://imformation.xlsx')

for i in range(len(years)):
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming'+years[i]+'.html'
    lst = []
    title_list = []
    html = getHtmlText(url)
    gettitle(html,title_list)
    getimformation(html,lst)
    if int(years[i]) == 2017:
        num = 1
        while num <= len(lst):
            lst[num - 1][0] = str(num)
            num += 1
    else:
        pass
    lst.insert(0,title_list)
    wb.sheets.add(years[i])
    wb.sheets[years[i]].range('A1').options(expand='table').value = lst

wb.save()
wb.close()
app.quit()