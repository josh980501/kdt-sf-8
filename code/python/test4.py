from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# 크롬 옵션 설정
chrome_option = Options()
chrome_option.add_argument("--start-maximized")  # 최대화된 창으로 열기
# chrome_option.add_argument("--headless") # GUI 창 안열기

# 웹드라이버 설정
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_option)


# 네이버 쇼핑 페이지 열기
driver.get("https://shopping.naver.com/ns/home")

# 검색창에 "tv" 입력 및 검색
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div[1]/form/div/div/div/div/input'))
)
search_input.send_keys("tv")
search_input.send_keys(Keys.ENTER)

for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 자바 스크립트 코드(스크롤하는 코드). 그냥 외우는게 나아
    # driver.implicitly_wait(5) # 모든 요소를 찾기 전에 지정된 시간만큼 암시적으로 대기
    time.sleep(2)

# 가격 정보를 기다리며 가져오기
prices = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'priceTag_inner_price__TctbK'))
)
names = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'basicProductCardInformation_title__Bc_Ng'))
)
# price_list = [i.text for i in prices]
# name_list = [j.text for j in names]
# print(price_list)
# print(name_list)
# input("")
# 텍스트 추출 및 출력
for price in prices:
    price_text = price.text
    real_price = price_text.replace("원","").strip()
    price_number = int(real_price.replace(",", ""))
    if price_number > 500000:
        print(real_price)










# texts = [i.text for i in prices]
# print(texts)
# for text in texts:
#     print(text)

