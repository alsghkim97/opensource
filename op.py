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


f1.pack(fill="both",expand=True)



window.mainloop()