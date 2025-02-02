from bs4 import BeautifulSoup
import requests

from tkinter import * # 불러오는 두가지 방법
from tkinter import messagebox
import random

root = Tk()
root.title("로또 당첨 확인")
root.geometry("640x480")

def show_text():
    #entry
    entried = entry.get()
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={entried}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8"
    res = requests.get(url)
    # print(type(entried))
    soup = BeautifulSoup(res.text, "html.parser")
    
    w_numbers = soup.select(".winning_number span")
    
    available_rounds = [tag["data-kgs-option"] for tag in soup.select("li[data-kgs-option]")]
    
    # 입력한 회차가 존재x면 예외 처리
    if entried not in available_rounds:
        text.delete("1.0", END)
        text.insert(END, f"{entried}회 로또 당첨 번호는 존재하지 않습니다.")
        return
    
    w_n_list = [int(i.text) for i in w_numbers]
    bonus_number = soup.select_one(".bonus_number span").text
    #text에 번호 출력
    text.delete("1.0", END)  # 텍스트에 있는 문자열 삭제
    text.insert(END, f"{entried}회 로또 당첨번호:\n{w_n_list}\n\n보너스 번호: {bonus_number}")

# 입력을 위해서는 레이아웃은 메서드체인을 사용할 수 없음
label = Label(root, text="당첨 회차 입력")
label.pack() # 잘 안되면 pack 내려보자

# Entry는 한줄 입력
entry = Entry(root, width=30)
entry.pack() # 같이 연결해서 쓰면 안돼. entry에 있는 레이아웃만 원하기 때문.
# 버튼
button = Button(root, text="당첨 번호 확인", command=show_text).pack()
# Text: 당첨 번호 출력
text = Text(root, width=40, height=10)
text.pack()

root.mainloop()

    # entry.delete(0, END)  # 엔트리에 있는 문자열 삭제
    # text
    # print(text.get("1.0", END)) # 전체 텍스트를 다 가져옴


    # # 응답이 정상인지 확인 (HTTP 상태 코드가 200인지 체크)
    # if res.status_code != 200:
    #     text.delete("1.0", END)
    #     text.insert(END, f"{entried}회 로또 당첨 번호는 존재하지 않습니다.")
    #     return  # 함수 종료


    # # url은 유효 but 회차가 존재하지 않는 경우
    # if not w_numbers:  # ([] 또는 None)
    #     text.delete("1.0", END)
    #     text.insert(END, f"{entried}회 로또 당첨 번호는 존재하지 않습니다.")
    #     return  # 함수 종료