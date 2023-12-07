from tkinter import*
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

plt.rcParams['font.family'] = 'Malgun Gothic'
answer=random.randint(1,100)
#answer=random.randint(1,100)
count=0 #시도횟수
name_window = None
player_data = []

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

def get_user_input():
    global name_window 
      #위에 none으로 초기화하였음
      
    if name_window is None: 
        user_input = simpledialog.askstring("입력", "값을 입력하세요:")
        #simpledialog.askstring 메서드: 
         #사용자가 입력을 완료=> 입력값을 반환하고, 
         #사용자가 "취소" 버튼을 => None을 반환
        if user_input is not None:  #즉 취소없이 입력값 제공한 경우
           
            
            existing_names = [str(tree.item(item)["values"][1]) for item in tree.get_children()]
            # 사용자 이름이 이미 트리뷰에 있는지 확인
            #tree.item(item)["values"][1]를 사용하면 해당 행의 열(NAME) 데이터에 접근
            #이제 모든 자식 항목에 대해 위의 과정을 반복하고, 그 결과를 리스트로 만듬
            
            if str(user_input) in existing_names: #사용자 이름이 이미 존재한다면
                messagebox.showinfo("경고", "이미 존재하는 사용자 이름입니다. 다른 이름을 입력하세요.")
                get_user_input()  # 경고후 다시 입력 받도록함
            else:#만약 이름이 고유한 경우
                print("사용자 입력:", user_input) 
                player_data.append((user_input, count)) #시도횟수와 사용자이름을 배열에 담음
                update_ranking() #update_ranking함수 호출
                
        name_window = None #입력창 닫음
        
def update_ranking():
    tree.delete(*tree.get_children())  # 기존 트리뷰의 아이템 삭제

    # 데이터 정렬
    sorted_data = sorted(player_data, key=lambda x: x[1])

    # 데이터 추가
    for idx, (name, tries) in enumerate(sorted_data, start=1):
        rank_format = f"{idx}위" if idx >= 10 else f"{idx}위 "
        tree.insert("", "end", values=(rank_format, name, tries))  


def plot_histogram():
    # 사용자 이름과 시도 횟수 추출
    user_names = [data[0] for data in player_data]
    tries = [data[1] for data in player_data]

    # 히스토그램 그리기
    plt.figure(figsize=(6, 4))
    plt.bar(user_names, tries, color='skyblue',width=0.2)
    plt.xlabel('사용자 이름')
    plt.ylabel('시도 횟수')
    plt.title('그래프')
    
    histogram_window = Toplevel(window)
    histogram_window.title("히스토그램")
    histogram_window.geometry('800x600')

    # Matplotlib 그림을 Tkinter 창에 삽입
    canvas = FigureCanvasTkAgg(plt.gcf(), master=histogram_window)
    canvas.draw()
    canvas.get_tk_widget().place(x=200, y=50)  # 필요한 경우 좌표를 조정하세요

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

histogram_button = tk.Button(window, text="통계",fg="orange",bg="white",command=plot_histogram)
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