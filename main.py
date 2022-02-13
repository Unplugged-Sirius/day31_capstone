import json
import time
from tkinter import *
import pandas as pd
import random

#----data----------

data=pd.read_csv("Untitled spreadsheet - Sheet1.csv")
words=data.to_dict(orient="records")

#------constents-----------
green="#99CC99"
purp="#660033"
pink="#FF0080"
watever="#CA278C"
global lang
global word
global k
global lis


#--------------right-------------------
def wrong():
    pass
def right():
        lis = list(range(1, 95))

        overall()




#-------------UI-----------------------
windows = Tk()
canvas = Canvas(width=1000, height=500)
windows.title("i cant think of any!")
windows.minsize(width=1000, height=500)
bg = PhotoImage(file="823-8234296_grey-png-gray-pattern-background-png.png")
canvas.create_image(500, 250, image=bg)
canva = Canvas(width=650, height=350, bg=green)
lang = canva.create_text(350, 120, text="H I N D I", font="Helvetica 22 bold underline", fill=purp)
word = canva.create_text(350, 200, text="words", font="Helvetica 42 bold ", fill=pink)
time = canva.create_text(600, 25, text= 4, font="Helvetica 30 bold ", fill=watever)
canvas.pack()
canva.place(x=370, y=150)

lis = list(range(1,95))

def overall():
        k=random.choice(lis)







 #----------------english slide--------------------------------------#

        def eng_slide():
                canva.config( width=650, height=350, bg=purp)
                canva.itemconfig(lang, text="E N G L I S H", fill=green)
                canva.itemconfig(word, text=words[k]["english"], fill=pink)
                ok=Button(text="right", width=15, command=right )
                ok.place(x=450, y=450)
                not_ok = Button(text="wrong", width=15, command=wrong)
                not_ok.place(x=800, y=450)
                canvas.pack()
                canva.place(x=370, y=150)

                windows.mainloop()

                hindi_slide()

        def count_down(count):
                global a
                canva.itemconfig(time, text=f"{count}")
                if (count > 0):
                    a = windows.after(1000, count_down, count - 1)
                    windows.mainloop()
                elif(count==0):
                    eng_slide()
        def hindi_slide():
                # lis = list(range(1, 95))
                # k = random.choice(lis)
                canva.config(width=650, height=350, bg=green)
                canva.itemconfig(lang, text="H I N D I", fill=purp)
                canva.itemconfig(word, text=words[k]["hindi"], fill=pink)
                canva.itemconfig(time, text=count_down(4), fill=watever, font="Helvetica 30 bold ")
                canvas.pack()
                canva.place(x=370, y=150)
                # windows.mainloop()


        hindi_slide()
overall()
