from bs4 import BeautifulSoup
import requests

# # 전자 신문 메인 기사 크롤링
# html_url = "https://www.donga.com/news/Society/article/all/20250116/130875667/1"
# res = requests.get(html_url)

# soup = BeautifulSoup(res.text, "html.parser")
# title = soup.select_one("header.view_head > div.inner > section.head_group > h1")
# print("제목: ", title.text)

# date = soup.select_one("ul.news_info span.is_blind")
# print("발행일: ", date.text)

# content = soup.select_one("section.news_view ")
# print("내용: ", content.text.strip())


# # 환율 정보 크롤링
# html_url = "https://finance.naver.com/marketindex/"
# res = requests.get(html_url)

# soup = BeautifulSoup(res.text, "html.parser")

# title = soup.select("#exchangeList h3.h_lst")
# name = [i.text for i in title]
# exchange = soup.select("#exchangeList span.value")
# number = [i.text for i in exchange]
# # print(number)
# zipped = list(zip(name, number))
# # print(zipped)
# for country, exchange in zipped:
#     print(f"{country} {exchange}")


# 주식 정보 크롤링
html_url = "https://finance.naver.com/item/main.naver?code=000270"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")

#종목명, 코드, 기준 시간, 가격
company = soup.select_one(".wrap_company > h2 > a")
code = soup.select_one(".wrap_company span.code")
time = soup.select_one("#time > em.date")
price = soup.select_one(".today > .no_today > .no_up > .blind")
print(price)

# 전일대비 상승/감소
price_updown = soup.select("p.no_exday > em.no_up > span.blind")
price_updown_list = [i.text for i in price_updown]
won_percent = ["원", "%"]
updown = soup.select("p.no_exday > em.no_up > span.ico")
updown_list = [i.text for i in updown]
zipped = zip(price_updown_list, won_percent, updown_list)
#전일가, 시가
end_start = ["전일", "시가"]
price_end_start = soup.select(".rate_info td.first > em > .blind")
price_end_start_list = [i.text for i in price_end_start]
zipped2 = zip(end_start, price_end_start)

# 주식 정보 출력
print("<오늘의 주식 정보>")
print(f"관심 종목: {company.text}")
print(f"코드: {code.text}")
print(f"{time.text}")
print(f"\n현재가: {price.text}")
print("===============================")

for price, unit, up_down in zipped:
    print(f"전일 대비 {price}{unit} {up_down}")
print()

for endstart, priceendstart in zipped2:
    print(f"{endstart}: {priceendstart.text}원")