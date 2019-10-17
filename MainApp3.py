from selenium import webdriver
import requests
from bs4 import BeautifulSoup


path = 'E:\Bigdata\webdriver\chromedriver.exe'
# chrome webdiver 생성
driver = webdriver.Chrome(path)

driver.get('http://cpbpoint.mbcplus.com/stats/player_rank/?mode=hitter&sortValue=ASC&sortKey=PA&tab_margin=0&htype=ALL&t_code=&position=')

num = 0
while True :
    num +=1
    ranking = driver.find_element_by_xpath('//*[@id="scRank"]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{}]/td[1]'.format(num)).text  # 순위1
    name = driver.find_element_by_xpath('//*[@id="scRank"]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{}]/td[2]'.format(num)).text  # 이름
    team = driver.find_element_by_xpath('//*[@id="scRank"]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{}]/td[3]'.format(num)).text  # 팀
    position = driver.find_element_by_xpath('//*[@id="scRank"]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{}]/td[4]'.format(num)).text  # 포지션
    war = driver.find_element_by_xpath('//*[@id="scRank"]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{}]/td[5]'.format(num)).text  # 총점
    batting_Average = driver.find_element_by_xpath('//*[@id="scRank"]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{}]/td[6]'.format(num)).text  # 타율
    games = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[1]'.format(num)).text  # 경기수
    babip = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[2]'.format(num)).text  # 타구안타비율
    allPlate = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[3]'.format(num)).text  # 타석
    intPlate = int(allPlate)
    at_Bats = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[4]'.format(num)).text  # 타수
    hits = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[5]'.format(num)).text  # 안타
    intHits = int(hits)
    doubles = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[6]'.format(num)).text  # 2루타
    triples = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[7]'.format(num)).text  # 3루타
    home_Runs = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[8]'.format(num)).text  # 홈련
    total_Bases = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[9]'.format(num)).text  #  루타
    runs_Scored = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[10]'.format(num)).text  # 득점수
    runs_Batted = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[12]'.format(num)).text  # 타점
    stolen_Bases = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[13]'.format(num)).text  # 도루성공
    caught_Stealing = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[14]'.format(num)).text  # 도루실패
    desc =driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[15]'.format(num)).text  # 성공률
    sacrifice_Hit = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[16]'.format(num)).text  # 회생 타율
    sacrifice_Fly = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[17]'.format(num)).text  # 회생 플라이
    bases_on_Balls = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[18]'.format(num)).text  # 볼넷
    if intPlate < 446:
        break

    # hit_By_Pitch = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[18]'.format(num)).text  # 사구
    # stolen_Bases = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[15]'.format(i)).text  # 도루성공
    # intentional = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[19]'.format(i)).text  # 고의 사구
    # strike_Outs = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[20]'.format(i)).text  # 삼진
    # sickness = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[21]'.format(i)).text  # 삼진
    # sacrifice_Hit = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[22]'.format(i)).text  # 회생 번트
    # sacrifice_Fly = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[23]'.format(i)).text  # 회생 플라이
    # base_Percentage = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[25]'.format(i)).text  # 출루율
    # slugging_Percentage = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[26]'.format(i)).text  # 장타율
    # ops = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[27]'.format(i)).text  # ops(출루율 + 장타율)
    # wOBA = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[28]'.format(i)).text  # wOBS(출루율 스케일)
    # wRC= driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[29]'.format(i)).text  # ops+ 스타일
    # wpa = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[30]'.format(i)).text  # 추가한 승리 확율
    print(ranking, name ,team, position,war,batting_Average,games,babip, intPlate,at_Bats,intHits,doubles,triples,  home_Runs,
          total_Bases,runs_Scored,runs_Batted, stolen_Bases, caught_Stealing,desc,sacrifice_Hit,sacrifice_Fly,bases_on_Balls )

# while True:
#     num += 1
#     allPlate = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[3]'.format(num)).text  # 타석
#     intPlate = int(allPlate)
#     hits = driver.find_element_by_xpath('//*[@id="slideDataplayer"]/tbody/tr[{}]/td[5]'.format(num)).text  # 안타
#     listHits = list(map(int,hits))
#     if intPlate < 446:
#         break
# print(hits)