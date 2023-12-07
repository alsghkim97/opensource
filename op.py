from tkinter import*
import tkinter as tk

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

f1.pack(fill="both",expand=True)

resultLabel1 = Label(f1,text="결과:",bg="#E0E0E0")
resultLabel1.place(x=260,y=270)
resultLabel2 = Label(f1,text="      ",bg="#E0E0E0")
resultLabel2.place(x=290,y=270)

guessField = Entry(f1,width=38)
guessField.place(x=102,y=303)
guessField.insert(0, "1에서 100까지의 숫자중 하나를 입력하세요")

window.mainloop()