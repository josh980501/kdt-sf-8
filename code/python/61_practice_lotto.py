# import tkinter as tk
from tkinter import * # 불러오는 두가지 방법

from tkinter import messagebox
import random

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

driver.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=1154%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8")

def show_text():
    #entry
    entried = entry.get()
    print(entried)
    label.config(text=f"입력된 문자는 : {entried}")
    entry.delete(0, END)  # 엔트리에 있는 문자열 삭제
    # text
    print(text.get("1.0", END)) # 전체 텍스트를 다 가져옴
    entry.delete(1, END)  # 엔트리에 있는 문자열 삭제

# 입력을 위해서는 레이아웃은 메서드체인을 사용할 수 없음
# Entry는 한줄 입력
entry = Entry(root, width=30)
entry.pack() # 같이 연결해서 쓰면 안돼. entry에 있는 레이아웃만 원하기 때문.

# Text 여러줄 입력
text = Text(root, width=40, height=10)
text.pack()

button = Button(root, text="버튼클릭", command=show_text).pack()

label = Label(root, text="")
label.pack() # 잘 안되면 pack 내려보자
root.mainloop()