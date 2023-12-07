from tkinter import*
import tkinter as tk
from tkinter import ttk
import random

answer=random.randint(1,100)
#answer=random.randint(1,100)
count=0 #시도횟수

window = Tk()
window.geometry('600x700')

window.configure(bg="white")
window.title("숫자를 맟줘보세요")

f1=Frame(window,relief="solid")
canvas1 = Canvas(f1,width=450,height=150, bg="#afeeee")
canvas1.create_text(225,75,fill="darkblue",font="Times 30 italic bold",
                   text=" 20160814\n  김민호") 
canvas1.place(x=75,y=50) #학번 이름 칸

canvas2 = Canvas(f1,width=450,height=50, bg="#afeeee")
canvas2.create_text(225,30,fill="darkblue",font="Times 15 italic bold",
                   text="숫자 게임에 오신 것을 환영합니다.") 
canvas2.place(x=75,y=200)

def update_ranking():
    tree.delete(*tree.get_children())  # 기존 트리뷰의 아이템 삭제

    # 데이터 정렬
    sorted_data = sorted(player_data, key=lambda x: x[1])

    # 데이터 추가
    for idx, (name, tries) in enumerate(sorted_data, start=1):
        rank_format = f"{idx}위" if idx >= 10 else f"{idx}위 "
        tree.insert("", "end", values=(rank_format, name, tries))  


def guessing():
    try:
        guess = int(guessField.get())
    except ValueError:
        resultLabel2["text"] = "숫자로 입력하세요"
        guessField.delete(0, 'end')  # 입력 위젯을 지우기
        return                 # 문자열 입력시 오류없이 다시 입력하게 만들기
    
    global count
    

    if guess>answer:
        msg="높음"
        count+=1
    elif guess<answer:
        msg="낮음"
        count+=1
    else:
        msg="정답"
        
        get_user_input()
        count=0    #초기화 따로 안눌러도 정답맞추면 시도횟수 초기화


    resultLabel2["text"]=msg
    guessField.delete(0,5)

def reset():
    global answer
    global count
    answer=random.randint(1,100)
    count=0
    resultLabel2["text"]="다시한번하세요!"
#초기화 함수
    
def hint():
    
    hint1=answer-10
    if(hint1<0):
        hint1=0
     
    hint2=answer+10
    if(hint2>100):
        hint2=100
        
    messagebox.showinfo("힌트",f"{hint1} ~ {hint2} 사이의 숫자")
    
    
def on_entry_click(event):
    if guessField.get() == "1에서 100까지의 숫자중 하나를 입력하세요":
        guessField.delete(0, END)
        guessField.config(fg="black")  
# 클릭하면 엔트리 텍스트 사라지게 하는 함수 정의

resultLabel1 = Label(f1,text="결과:",bg="#E0E0E0")
resultLabel1.place(x=260,y=270)
resultLabel2 = Label(f1,text="      ",bg="#E0E0E0")
resultLabel2.place(x=290,y=270)

guessField = Entry(f1,width=38)
guessField.place(x=102,y=303)
guessField.insert(0, "1에서 100까지의 숫자중 하나를 입력하세요")
guessField.bind("<FocusIn>", on_entry_click)

tryButton = Button(f1,text="시도",fg="green",bg="white",command=guessing)
tryButton.place(x=377,y=300)

resetButton = Button(f1,text="초기화",fg="red",bg="white",command=reset)
resetButton.place(x=413,y=300)

hintButton = Button(f1,text="힌트",fg="blue",bg="white",command=hint)
hintButton.place(x=461,y=300)

histogram_button = tk.Button(window, text="통계",fg="orange",bg="white")
histogram_button.place(x=497, y=300)

f1.pack(fill="both",expand=True)

canvas3 = Canvas(window,width=452,height=50, bg="#afeeee")
canvas3.create_text(225,30,fill="darkblue",font="Times 15 italic bold",
                   text="순위표") 
canvas3.place(x=75,y=365)

tree = ttk.Treeview(window, columns=("Rank", "Name", "Tries"), show="headings")

# 각 열의 제목 지정
tree.heading("Rank", text="순위")
tree.heading("Name", text="이름")
tree.heading("Tries", text="시도횟수")

# 각 열의 너비 지정
tree.column("Rank", width=116,anchor=tk.CENTER) #anchor=tk.CENTER 가운데정렬
tree.column("Name", width=216,anchor=tk.CENTER)
tree.column("Tries", width=116,anchor=tk.CENTER)

# Treeview 배치
tree.place(x=77,y=420)

window.mainloop()