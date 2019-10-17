from selenium import webdriver
import requests
from bs4 import BeautifulSoup


path = 'E:\Bigdata\webdriver\chromedriver.exe'
# chrome webdiver 생성
url ='http://cpbpoint.mbcplus.com/stats/player_rank/?mode=hitter&sortValue=ASC&sortKey=PA&tab_margin=0&htype=ALL&t_code=&position='
driver = requests.get(url)

driver.get(url)
soup = BeautifulSoup(url, 'html.parser')
num = 1
count = soup.select(td ) # 카운터
#print(len(count))
print(count)
filterKbo = soup.find_all('#scRank > div > div > div.body_hieh > div > div.table_t_b_l_w.stat2_brd > div > table > tbody > tr'.format(num))
print(filterKbo)