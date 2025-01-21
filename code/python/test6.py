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
chrome_option.add_argument("--headless") # GUI 창 안열기

# 웹드라이버 설정
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_option)

driver.get("https://images.google.com/?hl=ko")
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="APjFqb"]')))
search_input.send_keys("당나귀")
search_input.send_keys(Keys.ENTER)
driver.implicitly_wait(10)

for i in range(1,11):
    driver.implicitly_wait(5) # 모든 요소를 찾기 전에 지정된 시간만큼 암시적으로 대기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 자바 스크립트 코드(스크롤하는 코드). 그냥 외우는게 나아
    time.sleep(2)
    driver.save_screenshot(f"donkey{i}.png")
    print(f"{i}번째 사진 캡처완료")


# time.sleep(2)
# input("")