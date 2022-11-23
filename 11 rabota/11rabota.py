import requests
from tkinter import * 
from tkinter import ttk
from pprint import pprint 
import json



    
window = Tk()
window.title('Озеров Сергей Сергеевич')
window.geometry('900x600')


txt = Entry(window, width=10)
txt.grid(column=0, row=0)
txt.insert(0,'evanphx')

def new_file(filename, text):
    filename = open('/home/zloy/Рабочий стол/Progromice/Учёба/Практические работы  (Языки программирования)/11rabota.txt','w')
    filename.write(text)

def clicked():
    try:
        json = requests.get(f'https://api.github.com/users/{txt.get()}').json()
    except:
        json=requests.get(f'https://api.github.com/users/evanphx').json()
    try:     
        company = json['company']
    except:
        company = 'None'
    try:
        created_at = json['created-at']
    except:
        created_at = 'None'
    try:
        email = json['email']
    except:
        email = 'None'
    try:
        id = json['id']
    except:
        id = 'None'
    try:
        name = json['name']
    except:
        name='None'
    try:
        url = json['url']
    except:
        url = 'None'
    new_file('/home/zloy/Рабочий стол/Progromice/Учёба/Практические работы  (Языки программирования)/11rabota.txt', f"'company': {company}\n'created_at': {created_at}\n'email':{email}\n'id':{id}\n'name':{name}\n'url':{url}")

    
btn=Button(window,text='Click', fg='black', bg='white', command= clicked)
btn.grid(column=2, row=0)



window.mainloop()
