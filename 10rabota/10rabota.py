from tkinter import *
from tkinter import ttk
from tkinter.ttk import Checkbutton
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import Menu




window = Tk()
window.title("Озеров Сергей Сергеевич")
window.geometry('1200x600')



vkladka_control = ttk.Notebook(window)

tab1 = ttk.Frame(vkladka_control)

tab2 = ttk.Frame(vkladka_control)

tab3 = ttk.Frame(vkladka_control)

vkladka_control.add(tab1, text = '                                        Калькулятор                                        ')

vkladka_control.add(tab2, text = '                                           Чекбоксы                                           ')

vkladka_control.add(tab3, text = '                                              Текст                                         ')

vkladka_control.pack(fill=BOTH, expand=1)


combo = Combobox(tab1,width=5)
combo['values']=(NONE, "+", "-" , "*" , "/")
combo.grid(column=1,row=0)


def calc():
    get1=txt1.get()
    get2=txt2.get()
    
    if combo.get()=="+":
        value1=int(get1)+int(get2)
        calc_vivod.insert(0, value1)
    elif combo.get()=="-":
        value2=int(get1)-int(get2)
        calc_vivod.insert(0, value2)
    elif combo.get()=="*":
        value3=int(get1)*int(get2)
        calc_vivod.insert(0, value3)
    elif combo.get()=="/":
        value4=int(get1)/int(get2)
        calc_vivod.insert(0,value4)


        
def delete():
    txt1.delete(0,END)
    txt2.delete(0,END)
    calc_vivod.delete(0,END)


btn1 = Button(tab1,text='Remove all text in fields',bg='white', fg='black', command=delete)
btn1.grid(column=11,row=0)

txt1=Entry(tab1, width=7)
txt1.grid(row=0, column=0)

txt2=Entry(tab1, width=7)
txt2.grid(column=2, row=0)

btn_calc=Button(tab1,text="=", command=calc)
btn_calc.grid(column=3,row=0)

calc_vivod=Entry(tab1, width=10)
calc_vivod.grid(column=4, row=0)



chk1_state=BooleanVar()
chk2_state=BooleanVar()
chk3_state=BooleanVar()

chk1 = Checkbutton(tab2, text = 'Первый', var=chk1_state)

chk2 = Checkbutton(tab2, text = 'Второй', var=chk2_state)

chk3 = Checkbutton(tab2,text = 'Третий', var=chk3_state)

chk1.grid(column=1, row=0)
chk2.grid(column=1,row=1)
chk3.grid(column=1,row=2)


def clicked():
    if chk1.instate(['selected'])==True and chk2.instate(['selected'])==True and chk3.instate(['selected'])==True:
        messagebox.showinfo('Ответ', 'Вы выбрали все варианты.')
    elif chk1.instate(['selected'])==True and chk2.instate(['selected'])==True:
        messagebox.showinfo('Ответ', 'Вы выбрали первый и второй варианты.')
    elif chk1.instate(['selected'])==True and chk3.instate(['selected'])==True:
        messagebox.showinfo('Ответ', 'Вы выбрали первый и третий варианты.')
    elif chk2.instate(['selected'])==True and chk3.instate(['selected'])==True:
        messagebox.showinfo('Ответ', ' Вы выбрали второй и третий варианты.')
    elif chk1.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали первый вариант.')
    elif chk2.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали второй вариант.')
    elif chk3.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали третий вариант.')
    else:
        messagebox.showinfo("Ответ", "Вы ничего не выбрали :( ")

btn = Button(tab2,text = 'CLICK', bg='black', fg='white', command=clicked)
btn.grid(column=10,row=0)


    
text = Text(tab3, width=147, height=30)
text.pack(side=LEFT)
scroll = Scrollbar(command=text.xview)
scroll.pack(side=RIGHT,fill=X)
text.config(xscrollcommand=scroll.set)


def download():
    file = open('1.txt', 'r+', encoding='utf-8')
    line = file.read()
    text.insert('1.0',line)
    text.place(x=0,y=0) 


menu=Menu(window)
menu1_item = Menu(menu)
menu1_item.add_command(label='Загрузить текст', command=download)
menu.add_cascade(label='Загрузка', menu= menu1_item)
window.config(menu=menu)





window.mainloop()

