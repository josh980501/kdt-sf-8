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
# 크롬 옵션 설정
chrome_option = Options()
chrome_option.add_argument("--start-maximized")  # 최대화된 창으로 열기
# chrome_option.add_argument("--headless") # GUI 창 안열기
chrome_option.add_argument("--incognito")  # 시크릿 창으로 열기

# 웹드라이버 설정
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_option)

'''
# 실습1. github 크롤링
driver.get("https://github.com/login")

driver.find_element(By.ID, "login_field").send_keys("") # 찾기 쉬울땐 걍 id로 하자
driver.find_element(By.ID, "password").send_keys("") # 찾기 쉬울땐 걍 id로 하자
driver.find_element(By.NAME, "commit").click()

name = driver.find_element(
    By.XPATH,
    '//*[@id="switch_dashboard_context_left_column-button"]/span[1]/span/span[2]',
)
print(f"사용자 이름은 : {name.text}")
input("")
'''


''''''
# 실습 2. 쇼핑몰
driver.get("https://www.11st.co.kr/")
find = driver.find_element(By.CSS_SELECTOR, ".search_text")
find.send_keys("노트북")
find.send_keys(Keys.ENTER)
time.sleep(5)

items = driver.find_elements(By.CSS_SELECTOR, "#section_commonPrd .c-search-list__item") # 일반 상품만 가져옴

for item in items:
    name = item.find_element(By.CSS_SELECTOR, ".c-card-item__name > dd").text

    price = item.find_element(By.CSS_SELECTOR, ".c-card-item__price > span").text
    print(price)

    price = int(price.replace(",", ""))
    if price >= 500000:
        print(f"상품명: {name}, 가격: {price}")

input("")



'''
# 실습 3. 여행 사이트
driver.get("https://www.agoda.com/ko-kr/")
time.sleep(2)

departure = driver.find_element(By.ID, "textInput").send_keys("도쿄")
search = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            '//*[@id="search-box-autocomplete-id"]/div/ul/li[1]'
        )
    )
)
search.find_element(By.CSS_SELECTOR, "li:first-child").click() # 첫번째거 클릭
# 시작 날짜
click_day = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="DatePicker__Accessible"]/div/div[2]/div[1]/div[3]/div[5]/div[4]'
        )
    )
)
click_day.click()

# 종료 날짜
driver.find_element(
    By.XPATH,
    '//*[@id="DatePicker__Accessible"]/div/div[2]/div[2]/div[3]/div[2]/div[2]'
).click()
# 인원 다시 클릭
driver.find_element(By.ID, "occupancy-box").click()
# people = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "occupancy-box"))
# )
# 검색하기 클릭
search_click = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="Tabs-Container"]/button'))
)
search_click.click()

# # 마지막으로 열린 탭으로 전환
# driver.switch_to.window(driver.window_handles[-1])

# 호텔명
hotel_name = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".hotel-list-container h3"))
)
price = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".hotel-list-container .PropertyCardPrice__Value")
    )
)
print(f"호텔명 : {hotel_name[0].text}, 가격 {price[0].text}")
input("")
'''

'''
# 실습4. 구글 이미지
driver.get("https://images.google.com/?hl=ko")
time.sleep(2)

search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search.send_keys("토끼")
search.send_keys(Keys.ENTER)
time.sleep(2)

# 무한 스크롤
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)


images = driver.find_elements(By.CSS_SELECTOR, "img.YQ4gaf")
# images = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "img.YQ4gaf"))
# )

os.makedirs("images", exist_ok = True) # 폴더 신규 생성. 존재하면 무시 

code = 1
for image in images[:6]:
    # print(image.get_attribute("src")) # 이건 이미지 주소만
    src = image.get_attribute("src")
    if "FAVICON" not in src and "https" in src: # 구글 모양 이런걸 파비콘이라고 함
        # print(src)
        res = requests.get(src) #src 서버에서 데이터 가져옴. src는 그냥 링크 담겨져 있는 텍스트
        # print(res) #<Response [200]>:잘 받았다는 뜻

        with open(f"images/img_{code}.png", "wb") as file: #images 폴더 안에 img어쩌고 파일
            file.write(res.content)
        code += 1

# input("")
'''
