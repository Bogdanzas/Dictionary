from tkinter import * 
from tkinter.ttk import *
from tkinter.colorchooser import askcolor
from tkinter import scrolledtext,messagebox
import json
with open('words.json') as file:
    words = json.load(file)
def button_convert():
    txt2.delete(1.0,END)
    entered=txt.get(1.0, END)
    entered_word=str(entered.splitlines()[0]).lower().replace(' ','')
    if entered_word in words:
        try:
            language=language_1.get()
            if language=="Русский":
                word=words[entered_word]['meaning_rus']
                txt2.insert(INSERT,'%s'%word)
            elif language=="English":
                word=words[entered_word]['meaning_eng']
                txt2.insert(INSERT,'%s'%word)
        except:
            messagebox.showinfo('Ошибка', 'Данного слова нет в словаре')
    else:
        messagebox.showinfo('Ошибка','Данного слова нет в словаре')
window = Tk() 
window.title("Биологический словарь") 
window.geometry('525x270')
photo = PhotoImage(file = "1.gif")
w = Label(window, image=photo)
w.pack()

txt = scrolledtext.ScrolledText(window,width=20,height=5)
txt.place(x=25, y=70)

btn_convert = Button(window, text="Перевести", command=button_convert)
btn_convert.place(x=225, y=200)


txt2 = scrolledtext.ScrolledText(window,width=20,height=5)
txt2.place(x=275, y=70)

language_1 = Combobox(window,width=10)
language_1['values']= ("Русский","English")
language_1.current(0) #Элемент выбранный по умолчанию
language_1.place(x=200, y=20)


lbl1 = Label(window, text="Определение")
lbl1.place(x=70, y=20)


lbl1 = Label(window, text="Значение")
lbl1.place(x=375, y=20)


window.mainloop()
