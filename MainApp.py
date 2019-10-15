from selenium import webdriver
import requests
from bs4 import BeautifulSoup


path = 'E:\Bigdata\webdriver\chromedriver.exe'
# chrome webdiver 생성
driver = webdriver.Chrome(path)

driver.get('http://www.statiz.co.kr/stat.php')

num = list(range(3,13))
notd = list(range(1,31))
for i in num:
    for j in notd:
        find = driver.find_element_by_xpath('//*[@id="mytable"]/tbody/tr[{}]/td[{}]'.format(i,j))
        print(find.text)

    if i > 14:
        break
    i +=i
