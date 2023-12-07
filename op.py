from tkinter import*
import tkinter as tk
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
    

resultLabel1 = Label(f1,text="결과:",bg="#E0E0E0")
resultLabel1.place(x=260,y=270)
resultLabel2 = Label(f1,text="      ",bg="#E0E0E0")
resultLabel2.place(x=290,y=270)

guessField = Entry(f1,width=38)
guessField.place(x=102,y=303)
guessField.insert(0, "1에서 100까지의 숫자중 하나를 입력하세요")


tryButton = Button(f1,text="시도",fg="green",bg="white",command=guessing)
tryButton.place(x=377,y=300)

resetButton = Button(f1,text="초기화",fg="red",bg="white")
resetButton.place(x=413,y=300)

hintButton = Button(f1,text="힌트",fg="blue",bg="white")
hintButton.place(x=461,y=300)

histogram_button = tk.Button(window, text="통계",fg="orange",bg="white")
histogram_button.place(x=497, y=300)

f1.pack(fill="both",expand=True)

window.mainloop()