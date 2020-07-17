from tkinter import *

w = Tk()
w.title("Calc")
w.geometry("400x600+500+100")
li = [1, 2, 3, '+', 4, 5, 6, '-', 7, 8, 9, '*', 'C', 0, '=', '/']


def assign(event):
    global e
    global r
    global input_text
    t = event.widget.cget("text")
    if t != "C":
        if r == "":
            if t == "=":
                try:
                    r = str(eval(l1.get()))
                    input_text.set(r)
                except Exception as b:
                    e = "Error"
                    print(b)
                    input_text.set(e)
                    e = ""
            else:
                e = e + str(t)
                input_text.set(e)
        else:
            if t == "+" or t == "-" or t == "*" or t == "/":
                e = r
                e = e + str(t)
                input_text.set(e)
            else:
                e = ""
                e = e + str(t)
                input_text.set(e)
            r = ""
    else:
        e = ""
        input_text.set("")


r = ""
e = ""
input_text = StringVar()

# label
l1 = Entry(w, bg="white", fg="black", font=("Times New Roman", 40, "bold"), textvariable=input_text)
l1.pack(expand=True, fill="both")

for i in range(4):
    i = Frame(w, bg="grey")
    i.pack(expand=True, fill="both")
    for j in range(4):
        j = Button(i, text=li[j], font=("Verdana", 25, "bold"), relief=GROOVE, border=0)
        j.pack(side="left", expand=True, fill="both")
        j.bind("<Button-1>", assign)
    del li[:4]


w.mainloop()
