# # selenium
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# # driver = webdriver.Chrome()
# # driver.get("https://naver.com")

# # input("대기")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome()

# driver.get("https://naver.com")

# input("")
# 여기까지 webdriver 설정
# ----------------------------------------------------------------------beaurifulsoup보단 어려움. 메서드 많아서

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # By 사용
from selenium.webdriver.common.keys import Keys # Key 사용
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# 옵션 객체 생성
chrome_option = Options()
# 옵션 추가
chrome_option.add_argument("--start-maximized") # 최대 크기로 열기
# chrome_option.add_argument("--headless") # GUI 창 안열기


service = Service()
driver = webdriver.Chrome(service=service, options=chrome_option)

#브라우저 제어

# driver.get("https://google.com")
# print(driver.title) # Google
# print(driver.current_url) #https://www.google.com/
# driver.maximize_window()
# time.sleep(2) #2초 멈춤
# driver.get("https://www.wikipedia.org") # 위키피디아로 이동
# time.sleep(2) #2초 멈춤
# driver.back()
# time.sleep(2) #2초 멈춤
# driver.forward()
# time.sleep(2) #2초 멈춤
# driver.refresh()
# time.sleep(2) #2초 멈춤
# driver.quit()

# input("")

########################
# # 웹 상호작용
# driver.get("https://google.com")
# time.sleep(2)
# search_input = driver.find_element(By.NAME, "q")
# # search_input = driver.find_element(By.ID, "#input") 이렇게 해도됨. 태그네임으로도 가능
# time.sleep(2)
# # print(search_input)
# search_input.send_keys("selenium1")
# time.sleep(2)
# search_input.send_keys(Keys.BACKSPACE)
# # search_input.send_keys(Keys.ENTER)


# input("")

##########################
# # 스크롤과 창옵션
# driver.get("https://naver.com")
# time.sleep(2)
# driver.execute_script("alert('hello, selenium')") # 자바스크립트 안의 문자열
# alert = driver.switch_to.alert
# print(alert.text)
# time.sleep(2)
# alert.accept() # 확인버튼 누름

# # element 창 찾기
# search_input = driver.find_element(By.XPATH, '//*[@id="query"]') # copy xpath로 간편하게 찾기
# search_input.send_keys("selenium")
# search_input.send_keys(Keys.ENTER)

# input("")

##################
# # 무한 스크롤
# driver.get("https://www.google.com/imghp?hl=ko&authuser=0&ogbl")
# search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
# search_input.send_keys("토끼")
# search_input.send_keys(Keys.ENTER)


# for i in range(3):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 자바 스크립트 코드(스크롤하는 코드). 그냥 외우는게 나아
#     # driver.implicitly_wait(5) # 모든 요소를 찾기 전에 지정된 시간만큼 암시적으로 대기
#     time.sleep(2)

# input("")

####################################3
# # 대기

# driver.get("https://google.com")
# driver.implicitly_wait(10)

# '''
# EC메서드 (대기조건을 말함)
# EC.title_is(문자열) : 현재 페이지 제목이 지정된 문자열과 일치할 때 (까지 대기)
# EC.title_contains(문자열) : 현재 페이지 제목에 문자열이 포함될 때 (까지 대기)
# EC.presence_of_element_located((By.ID, "아이디값")) # DOM(자바스크립트 페이지 동적으로 열리는거)이 존재할 때(화면에 표시 안돼도 됨). 꼭 id 말고도 by 뒤에 다 옴
# EC.visibility_of_element_located((By.CSS_SELECTOR, "선택자)) # DOM이 존재할 때(화면에 표시)
# EC.presence_of_all_elements_located((By.CSS_SELECTOR, "선택자)) # DOM에 모든 요소가 존재할 때(화면에 표시 안돼도 됨)
# EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "선택자)) # DOM에 모든 요소가 존재할 때 (화면에 표시)
# EC.element_to_be_clickable((By.CSS_SELECTOR, "선택자)) # 요소가 화면에 표시되고 클릭이 가능할 때
# EC.element_to_be_selected((By.CSS_SELECTOR, "선택자)) # 요소가 선택된 상태가 될 때
# '''

# 검색 입력 필드 대기
# search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q"))) # 구글 검색 창이 열릴때까지 대기
# search_input.send_keys("python")
# search_input.send_keys(Keys.ENTER)

# email_text = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')
# href = email_text.get_attribute("href") # get_attribute: 속성값 가져옴
# print(href)

# input("")

#################################################
# 스크린샷
# driver.get("https://www.youtube.com/")
# time.sleep(2)
# driver.save_screenshot("youtube.png")

# input("")


# driver.get("https://www.nate.com/")
# time.sleep(2)
# search_input = driver.find_element(By.XPATH, '//*[@id="q"]')
# search_input.send_keys("파이썬")
# search_input.send_keys(Keys.ENTER)
# time.sleep(2)
# driver.save_screenshot("python.png")

# github 크롤링
# driver.get("https://github.com/")
# time.sleep(2)
# sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/header/div/div[2]/div/div/div/a')
# sign_in.click()
# # ID, PW 입력
# idpw_input = driver.find_element(By.XPATH, '//*[@id="login_field"]')
# idpw_input.send_keys("ch032kr@gmail.com")
# idpw_input = driver.find_element(By.XPATH, '//*[@id="password"]')
# idpw_input.send_keys("krcho0872030496@")
# idpw_input.send_keys(Keys.ENTER)
# time.sleep(2)
# # 우측 상단 프로필 클릭
# profile = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[4]/deferred-side-panel/include-fragment/react-partial-anchor/button/span/span/img')
# profile.click()
# time.sleep(2)
# profile = driver.find_element(By.XPATH, '//*[@id="__primerPortalRoot__"]/div/div/div/div[2]/div/ul/li[3]')
# profile.click()
# time.sleep(2)
# # 이름 가져오기
# id_text = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/div/div/div[1]/div/div/div[1]/div[2]/h1/span[2]')
# id_profile = id_text.text
# print(f"나의 이름: {id_profile}")


# 쇼핑몰 크롤링 하기(200만원 이상 tv 상품 출력)
driver.get("https://www.11st.co.kr/")
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="tSearch"]/form/fieldset/input')))
search_input.send_keys("tv") #tv 검색
search_input.send_keys(Keys.ENTER)
driver.implicitly_wait(10)

div_pattern_name = [4, 2]  # div 값을 번갈아 적용할 패턴
div_pattern_cost = [5, 3]  # div 값을 번갈아 적용할 패턴

print("<200만원 이상인 상품>\n")

for i in range(1, 5):  # li[1] ~ li[4]

    div_index_name = div_pattern_name[(i - 1) % 2]  # 4와 2를 교대로 선택
    xpath_name = f'//*[@id="section_list"]/div/ul/li[{i}]/div/div[2]/div[1]/dl/div[{div_index_name}]/dd'
    
    div_index_cost = div_pattern_cost[(i - 1) % 2] # 5와 3을 교대로 선택
    xpath_cost = f'//*[@id="section_list"]/div/ul/li[{i}]/div/div[2]/div[1]/dl/div[{div_index_cost}]/dd[2]/span'

    name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_name)))
    # print(name.text)
    cost = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_cost)))
    # print(cost.text)
    if cost.text > "2,000,000":
        print(f"제품명: {name.text}")
        print(f"가격: {cost.text}원\n")
        




# prices = driver.find_element(By.TAG_NAME, 'dd.c-card-item__price')
# print(prices.text)

# 상품명
# //*[@id="section_list"]/div/ul/li[1]/div/div[2]/div[1]/dl/div[4]/dd
# //*[@id="section_list"]/div/ul/li[2]/div/div[2]/div[1]/dl/div[2]/dd
# //*[@id="section_list"]/div/ul/li[3]/div/div[2]/div[1]/dl/div[4]/dd
# //*[@id="section_list"]/div/ul/li[4]/div/div[2]/div[1]/dl/div[2]/dd

# 가격
# //*[@id="section_list"]/div/ul/li[1]/div/div[2]/div[1]/dl/div[5]/dd[2]/span
# //*[@id="section_list"]/div/ul/li[2]/div/div[2]/div[1]/dl/div[3]/dd[2]/span
# //*[@id="section_list"]/div/ul/li[3]/div/div[2]/div[1]/dl/div[5]/dd[2]/span
# //*[@id="section_list"]/div/ul/li[4]/div/div[2]/div[1]/dl/div[3]/dd[2]/span
    
# input("")


