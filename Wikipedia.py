import wikipedia as w
from  tkinter import *

search = Tk()
search.geometry("528x528")
search.iconbitmap("icon.ico")
search.config(border=0, bg="black")
search.title('Brief Search')
search.resizable(0, 0)
Label(search, text="Enter The Word Here : ", bg='black', fg='white', font=('times', 15,'bold', 'italic')).place(x=20, y=50)
word = Entry(search, width=28, fg='white', bg='black', font=('times', 15,'bold', 'italic'), border=1)
word.place(x=230, y=54)
scrapped_box = Text(search, height=15, width=55, bg='black', fg='white', font=('times', 12, 'bold', 'italic'), border=0)
scrapped_box.place(x=38, y=150)


def close():
    search.destroy()


def clear_fields():
    word.delete(0, END)
    scrapped_box.delete(0.0, END)


def extract():
    sc = word.get()
    scrapped = str(sc)
    scrape = w.summary(scrapped, sentences=4)
    summary = scrape
    scrapped_box.insert(0.0, summary)


Button(search, text="Search", border=0, command=extract, font=('times', 12,'bold', 'italic'), bg='black', fg='white', activebackground='gray', activeforeground='white')\
    .place(x=340, y=90)
Button(search, text="Clear All", border=0, command=clear_fields, font=('times', 12,'bold', 'italic'), bg='black', fg='white', activebackground='gray', activeforeground='white')\
    .place(x=420, y=90)
Button(search, text="Close", width=52, border=0, command=close, font=('times', 12,'bold', 'italic'), bg='black', fg='white', activebackground='black', activeforeground='white')\
    .place(x=20, y=450)

search.mainloop()