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
# 호텔 이름, 가격
driver.get("https://www.booking.com/")
click_x_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="b2indexPage"]/div[45]/div/div/div/div[1]/div[1]/div'))
)
click_x_button.click()
search_city = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id=":rh:"]'))
)
search_city.send_keys("프랑크푸르트 중앙역")

search_date = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="indexsearch"]/div[2]/div/form/div/div[2]'))
)
search_date.click()

date_start = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[5]/td[1]/span'))
) # 1월 26일
date_start.click()

date_end = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[7]/span'))
) # 2월 1일
date_end.click()

time.sleep(2)
search_button = date_end.find_element(By.XPATH, '//*[@id="indexsearch"]/div[2]/div/form/div/div[4]')
search_button.click()

first_hotel = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="bodyconstraint-inner"]/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a/div[1]'))
)
# print(first_hotel.text)
hotel_price = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="bodyconstraint-inner"]/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/span/div/div/span[1]'))
)
# print(hotel_price.text)
print(f"호텔 이름: {first_hotel.text}\n가격: {hotel_price.text}")
input("")
