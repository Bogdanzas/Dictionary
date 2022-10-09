from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.ttk import *
from tkinter import scrolledtext,messagebox
import json
def btn_write():
    with open('words.json') as file:
        words = json.load(file)
    word_eng=text_1.get().lower().replace(' ','')
    word_rus=text_2.get().lower().replace(' ','')
    meaning_eng=text_3.get()
    meaning_rus=text_4.get()
    words[word_rus]={"word_rus":word_rus,"word_eng":word_eng,"meaning_rus":meaning_rus,"meaning_eng":meaning_eng}
    words[word_eng]={"word_rus":word_rus,"word_eng":word_eng,"meaning_rus":meaning_rus,"meaning_eng":meaning_eng}
    with open('words.json', 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=True, indent=4)
    messagebox.showinfo('Измения сохранены','Изменения сохранены')
def delete_all():
    data = {"": ""}
    with open('words.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=True, indent=4)
    #print(data)
    messagebox.showinfo('Измения сохранены','Изменения сохранены')
def give_all_data():
    with open('words.json') as file:
        words = json.load(file)
        print(words)
window = Tk() 
window.title("Редактор словаря")
window.geometry('450x250')
photo = PhotoImage(file = "1.gif")
w = Label(window, image=photo)
w.pack()

lbl1 = Label(window, text="Слово на английском")
lbl1.place(x=20, y=10)
text_1 = Entry(window,width=10)
text_1.place(x=230, y=10)

lbl2 = Label(window, text="Слово на русском")
lbl2.place(x=20, y=60)
text_2 = Entry(window,width=10)
text_2.place(x=230, y=60)

lbl3 = Label(window, text="Определение на английском")
lbl3.place(x=20, y=110)
text_3 = Entry(window,width=10)
text_3.place(x=230, y=110)

lbl4 = Label(window, text="Определение на русском")
lbl4.place(x=20, y=155)
text_4 = Entry(window,width=10)
text_4.place(x=230, y=155)

btn_write = Button(window, text="Записать:", command=btn_write)
btn_write.place(x=175, y=200)

btn3 = Button(window, text="Очистить словарь",command=delete_all)
btn3.place(x=300, y=200)


btn51 = Button(window, text="Вывести словарь:", command=give_all_data)
btn51.place(x=15, y=200)

window.mainloop()
