from selenium import webdriver
import requests
from bs4 import BeautifulSoup


path = 'E:\Bigdata\webdriver\chromedriver.exe'
# chrome webdiver 생성
driver = webdriver.Chrome(path)

driver.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2019&ye=2019&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR_ALL_ADJ&o2=TPA&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=0&si=&cn=')

num = list(range(0,36))
page = 0
count = len(num)
print(len(num))
while True:
    url = 'http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2019&ye=2019&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR_ALL_ADJ&o2=TPA&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa={}&si=&cn='.format(page)
    driver.get(url)
    for i in num:
        i += 1
        if i == 1or i==2:
            pass
        elif i == 13 or i == 14:
            pass
        elif i == 25 or i ==26:
            pass
        else:
            ranking = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[1]'.format(i)).text  # 순위1
            name = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[2]'.format(i)).text  # 이름
            team = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[3]'.format(i)).text  # 팀
            war = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[4]'.format(i)).text  # 총점
            games = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[5]'.format(i)).text  # 경기수
            allPlate = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[6]'.format(i)).text  # 타석
            at_Bats = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[7]'.format(i)).text  # 타수
            runs_Scored = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[8]'.format(i)).text  # 득점수
            hits = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[9]'.format(i)).text  # 안타
            doubles = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[10]'.format(i)).text  # 2루타
            triples = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[11]'.format(i)).text  # 3루타
            home_Runs = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[12]'.format(i)).text  # 홈련
            total_Bases = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[13]'.format(i)).text  # 총 루타
            runs_Batted = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[14]'.format(i)).text  # 타점
            stolen_Bases = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[15]'.format(i)).text  # 도루성공
            caught_Stealing = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[16]'.format(i)).text  # 도루실패
            bases_on_Balls = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[17]'.format(i)).text  # 볼넷
            hit_By_Pitch = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[18]'.format(i)).text  # 사구
            intentional = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[19]'.format(i)).text  # 고의 사구
            strike_Outs = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[20]'.format(i)).text  # 삼진
            sickness = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[21]'.format(i)).text  # 삼진
            sacrifice_Hit = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[22]'.format(i)).text  # 회생 번트
            sacrifice_Fly = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[23]'.format(i)).text  # 회생 플라이
            batting_Average = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[24]'.format(i)).text  # 타율
            base_Percentage = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[25]'.format(i)).text  # 출루율
            slugging_Percentage = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[26]'.format(i)).text  # 장타율
            ops = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[27]'.format(i)).text  # ops(출루율 + 장타율)
            wOBA = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[28]'.format(i)).text  # wOBS(출루율 스케일)
            wRC= driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[29]'.format(i)).text  # ops+ 스타일
            wpa = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[30]'.format(i)).text  # 추가한 승리 확율
            print(ranking, name, team, war, games, allPlate, at_Bats, runs_Scored, hits, doubles, triples,
                  home_Runs,total_Bases,runs_Scored,stolen_Bases,caught_Stealing, bases_on_Balls, hit_By_Pitch,
                  intentional, strike_Outs, sickness, sacrifice_Hit, sacrifice_Fly, batting_Average,
                  base_Percentage, slugging_Percentage, ops, wOBA, wRC, wpa)
        if i > count:
            break
    page += 30