from bs4 import BeautifulSoup
import requests



url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=1157%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
w_numbers = soup.select(".winning_number span")
# print(w_numbers)

w_n_list = [i.text for i in w_numbers]
bonus_number = soup.select_one(".bonus_number span").text
real_round = soup.select_one("a._select_trigger").text
# 모든 'data-kgs-option' 속성 값을 가져오기
available_rounds = [int(tag["data-kgs-option"]) for tag in soup.select("li[data-kgs-option]")]
print(w_n_list)
print(bonus_number)
print(real_round)
print(available_rounds)