from selenium import webdriver
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)  # 아이피 주소, 포스트 주소
db = client['local'] # 로컬
collection = db.KBOBatter # Collection 선택
path = 'E:\Bigdata\webdriver\chromedriver.exe' #chromedriver 파일 주소

collection.remove() #클래스 삭제
# chrome webdiver 생성
driver = webdriver.Chrome(path)

driver.get('http://cpbpoint.mbcplus.com/stats/player_rank/?mode=hitter&sortValue=ASC&sortKey=PA&tab_margin=0&htype=ALL&t_code=&position=')
soup = BeautifulSoup(driver.page_source, 'html.parser')

num = 1
print(num)
count = soup.select('#scRank > div > div > div.body_hieh > div > div.table_t_b_l_w.stat2_brd > div > table > tbody >tr ') # 카운터
print(len(count))
while True:
    fielderKbo = driver.find_element_by_xpath('//*[@id="scRank"]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{}]'.format(num)).text + \
                 driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]'.format(num)).text
    driverkbo = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[1]'.format(num)).text

    if num == len(count) :
        break
    num += 1
    listKbo = fielderKbo.split()
    kbodata = {'순위': listKbo[0], '이름': listKbo[1], '구단':listKbo[2], '포지션': listKbo[3],
            'AVG': float(listKbo[5]), '경기수': int(driverkbo), '타석': int(listKbo[7]), '타수': int(listKbo[8]),
            '안타': int(listKbo[9]), '홈런': int(listKbo[12]), '득점': int(listKbo[14]), '타점': int(listKbo[15]),
            '도루': int(listKbo[16]), '4구': int(listKbo[21])}
    print(kbodata)

    collection.insert(kbodata)
driver.close()
client.close()