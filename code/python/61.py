# import tkinter as tk
from tkinter import * # 불러오는 두가지 방법
from tkinter import messagebox
import random

root = Tk()
root.title("윈도우 프로그래밍 연습")
root.geometry("640x480")

# # 기본창 띄우기
# label = Label(root, text="안녕하세요")
# label.pack(side="left")
# root.mainloop()

# #레이아웃 pack() 방식
# label1 = Label(root, text="Top", bg="red", fg="white")
# label1.pack(side="top", fill="x", padx=10, pady=10)

# label2 = Label(root, text="BOTTOM", bg="blue", fg="white")
# label2.pack(side="bottom", fill="x", padx=10, pady=10)

# label3 = Label(root, text="left", bg="green", fg="white")
# label3.pack(side="left", fill="y", padx=10, pady=10)

# label4 = Label(root, text="RIGHT", bg="yellow", fg="black")
# label4.pack(side="right", fill="y", padx=10, pady=10)

# label5 = Label(root, text="CENTER", bg="purple", fg="white")
# label5.pack(side="top", fill="both", expand=True, padx=10, pady=10) # expand True이기 때문에 가운데 꽉참
# # root.mainloop()
# # --------------------------------------------------------------------
# # 레이아웃 Grid() 방식: 상대적으로 위치가 바뀜. 여기서 purple은 해당 열에 하나밖에 없기 때문에 위치 상대적으로 맞춰주려고 가운데 있음
# label1 = Label(root, text="label1", bg="red", fg="white")
# label1.grid(row=0, column=0, padx=10, pady=10)

# label2 = Label(root, text="label2", bg="blue", fg="white")
# label2.grid(row=0, column=1, padx=10, pady=10)

# label3 = Label(root, text="label3", bg="green", fg="white")
# label3.grid(row=1, column=0, padx=10, pady=10)

# label4 = Label(root, text="label4", bg="yellow", fg="black")
# label4.grid(row=1, column=1, padx=10, pady=10)

# label5 = Label(root, text="label5", bg="purple", fg="white")
# label5.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

# # root.mainloop()

# # 위젯
# # Label
# label = Label(root, text="Hello, tkinter!", font=("궁서체", 20), fg="blue")
# label.pack()
# # 버튼
# def on_click():
#     print("Button Click")

# button = Button(root, text="클릭", command=on_click).pack()
# root.mainloop()


'''
def show_text():
    #entry
    entried = entry.get()
    print(entried)
    label.config(text=f"입력된 문자는 : {entried}")
    entry.delete(0, END)  # 엔트리에 있는 문자열 삭제
    # text
    print(text.get("1.0", END)) # 전체 텍스트를 다 가져옴
    text.delete("1.0", END)  # 텍스트에 있는 문자열 삭제

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
'''

'''
#--------------------------------
# Frame

top_frame = Frame(root, bg="lightblue")
top_frame.pack(fill="x")
Label(top_frame, text="top frame").pack(pady=50)

bottom_frame = Frame(root, bg="lightgreen")
bottom_frame.pack(fill="both", expand=True)
Label(bottom_frame, text="bottom frame").pack(pady=50)

root.mainloop()
'''

#------------------------
'''
# checkbutton
def show_state():
    print(f"선택은 {var.get()}")

# checkbutton

# var = IntVar()
# checkbtn = Checkbutton(root, text="동의", variable=var, command=show_state).pack()

# radiobutton

var = StringVar(value="option1") # Radiobutton의 선택 상태를 저장하고 자동 업데이트하는 역할을 함
radio1 = Radiobutton(root, text="옵션1", variable=var, value="option1", command=show_state).pack(pady=10)
radio2 = Radiobutton(root, text="옵션2", variable=var, value="option2", command=show_state).pack(pady=10)

root.mainloop()
'''

#---------------------------------------------
'''
# listbox

def show_selected():
    selection = listbox.curselection() # 현재 선택된 항목의 인덱스를 가져옴
    print(selection) # 선택된 항목의 인덱스를 출력
    if selection: # 만약 아무 항목도 선택하지 않은 경우 selection은 ()이므로(빈 튜플,false), if selection: 조건문을 사용하여 오류를 방지
        print(f"선택된 과일은 : {listbox.get(selection[0])}") # 튜플의 1번째값이므로 selection[0]

listbox = Listbox(root)
listbox.pack(pady=10)
for item in ["사과", "바나나", "포도", "체리"]:
    listbox.insert(END, item) #End: 처음부터 넣는다는 뜻

button = Button(root, text="선택", command=show_selected)
button.pack(pady=10)

root.mainloop()
'''

#--------------------------------
'''
# messagebox
from tkinter import messagebox

def show_message():
    messagebox.showinfo("경고", "메세지창 띄우기 연습")

button = Button(root, text="클릭", command=show_message)
button.pack(pady=10)

root.mainloop()
'''

#-----------------
'''
from tkinter import messagebox
# 메뉴
def new_file():
    messagebox.showinfo("메뉴", "파일이 선택되었습니다")

def exit_app(): # 윈도우창 종료
    root.quit()

menubar = Menu(root)

filemenu = Menu(menubar,) # 메뉴바 자체를 메뉴에 넣음. tearoff = 0: 떼어내기 막음
filemenu.add_command(label="New", command=new_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_app)

menubar.add_cascade(label="파일", menu=filemenu)
root.config(menu=menubar) #옵션


root.mainloop()
'''

#----------------
# 쿠폰 추첨기
def on_click():
    name_list = ["김민경", "이동건", "최승우", "최영", "한수빈", "이채연", "조경록"]
    name = random.sample(name_list, 2)
    print(name)
    text.delete("1.0", END)
    text.insert(END, name)

window = Tk()
window.title("쿠폰 추첨기")
window.geometry("640x480")

# # 이미지 넣기
# label_img = Label(window)
# img = PhotoImage(file="./coupon.jpg")
# label_img.config(image=img)
# label_img.pack()

# 추첨버튼
Button(window, text="추첨", command=on_click).pack()

# 추첨된 사람 출력
text = Text(window, width=40, height=5, bg="green")
text.pack()

window.mainloop()
'''
'''