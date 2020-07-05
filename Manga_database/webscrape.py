import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

#req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()

url = 'https://mangakakalot.com/manga_list?type=topview&category=all&state=all&page=1'
uclient = ureq(url)
urlre = uclient.read()
uclient.close()

ps = soup(urlre, "html.parser")

containers = ps.findAll('div',{'class' : 'list-truyen-item-wrap'})
container = containers[0]
print(len(containers))
#for container in containers : 
#	print(container.a.href) 

'''import csv
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

list500=[]

url='https://www.imdb.com/list/ls063540474/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'

uclient = ureq(url)
urlre=uclient.read()
uclient.close()

ps=soup(urlre,"html.parser")

containers=ps.findAll('div',{'class':'lister-item-content'})
container=containers[0]
for container in containers:
	list500.append(container.h3.a.text)'''
