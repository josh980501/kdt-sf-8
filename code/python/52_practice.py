from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os # 폴더 만들어주려고 추가함
import requests
import numpy as np

# 크롬 옵션 설정
chrome_option = Options()
chrome_option.add_argument("--start-maximized")  # 최대화된 창으로 열기
# chrome_option.add_argument("--headless") # GUI 창 안열기
chrome_option.add_argument("--incognito")  # 시크릿 창으로 열기

# 웹드라이버 설정
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_option)

driver.get("https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx")
driver.implicitly_wait(10)

categories = np.array([[i.text for i in driver.find_elements(By.CSS_SELECTOR, "thead > tr > th")][:7]]) # 카테고리 7개까지만 불러오기
# print(categories)
records = []
rows = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")[:10]  # tbody의 첫 10개 행 가져오기

for row in rows:
    cells = [cell.text for cell in row.find_elements(By.CSS_SELECTOR, "td")[:7]]  # 각 행의 첫 7개 td만 가져오기
    records.append(cells)  # 리스트에 추가

records_arr = np.array(records)

total_info = np.vstack((categories, records_arr))
print(total_info)
os.makedirs("datas", exist_ok = True)

with open("datas/2024kbo.txt", "w", encoding="utf-8") as f:
    f.write("============= 2024 한국 프로야구 성적표 =============\n")  # 제목 추가
    for row in total_info:
        f.write("\t".join(row) + "\n")  # 각 행을 탭으로 구분하여 저장. "\t".join: 리스트를 문자열로 합쳐서 반환. 각 요소당 \t추가
with open("datas/2024kbo.txt", 'r', encoding="utf-8") as f:
    data = f.read()
    print(data)

# records = [i.text for i in driver.find_elements(By.CSS_SELECTOR, "tbody > tr ")][:10]
# print(records)
# print(infos)

# # infos = driver.find_elements(By.CSS_SELECTOR, "#cphContents_cphContents_cphContents_udpRecord table > tbody") # 모든 구단들의 정보 다 갖고옴
# # print(infos)
# for info in infos:
#     team_info = info.text
#     print(team_info)

# infos = driver.find_element(By.CSS_SELECTOR, "#cphContents_cphContents_cphContents_udpRecord table > tbody")

# infos = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located(
#         (By.CSS_SELECTOR, "#cphContents_cphContents_cphContents_udpRecord table > tbody")
#     )
# )