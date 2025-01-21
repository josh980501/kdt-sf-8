

########################## [ 기본 세팅 ] ##############################
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By #By 사용하기 위한 모듈
from selenium.webdriver.common.keys import Keys #Keys 사용하기 위한 모듈 (엔터, 리턴 등)
from selenium.webdriver.support.ui import WebDriverWait #webdriverwait를 사용하0기 위한 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options #옵션
import requests, time
chrome_option = Options()
#옵션추가
# chrome_option.add_argument("--start-maximized") #최대크기로 열기
# chrome_option.add_argument("--headless") #GUI창 안열고 백그라운드 실행(리소스절약)
##########################[ 쇼핑몰 크롤링 ]#############################
service=Service() #생략 귀찮으면 대소문과 구분 후 괄호 다 치면 됨.
driver = webdriver.Chrome(service=Service(), options=chrome_option)
driver.get("https://www.vans.co.kr/")
search_shoe= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/header/div[1]/div[1]/div[1]/nav/ul[1]/li[2]/a/span')))
search_shoe.click()
# search_cost=[WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="wrapper"]/main/section/div[4]/section/ul/li[1]/div/div[2]/p[2]/span')))]
# value1=search_cost[0].text.replace(" 원","")
# value=value1.replace(",","")
# print(value)
# if int(value)>50000:


for i in range(1,10):
    search_name=[WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="wrapper"]/main/section/div[4]/section/ul/li[{i}]/div/div[2]/p[1]/a')))]
    search_cost=[WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="wrapper"]/main/section/div[4]/section/ul/li[{i}]/div/div[2]/p[2]/span')))]
    value1=search_cost[0].text.replace(" 원","")
    name=search_name[0].text
    value=value1.replace(",","")
    if int(value) > 50000:
        print(i,"번째 상품 이름 :",name, "| 가격 :",value)



# //*[@id="wrapper"]/main/section/div[4]/section/ul/li[1]/div/div[2]/p[2]/span
# //*[@id="wrapper"]/main/section/div[4]/section/ul/li[2]/div/div[2]/p[2]/span
# //*[@id="wrapper"]/main/section/div[4]/section/ul/li[3]/div/div[2]/p[2]/span