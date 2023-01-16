from datetime import *
from tkinter import *
from functools import partial
import json
import re
import webbrowser
import converter
import requests
# pip install win10toast
import win10toast


clicks = 0

ICO_NAME = "icons\\planner_0.ico"
BG_COLOR = "#e6e6e6"
BT_COLOR = "#555"
TT_COLOR = "#bfbfbf"
DATE_TMP = date.today()


class Calendar(object):
    buttons = []
    day_week_names = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    next_month_btn = None
    prev_month_btn = None
    title = None

    selected_btn = None
    selected = False

    def __init__(self, tasks):
        global BG_COLOR
        self.tasks = tasks
        notification("Планировщик", self.tasks.getTaskStr(), 5)
        self.title = Label(text=f"{self.getDateTitle(DATE_TMP)}", compound="c", padx=5, bg=BG_COLOR, image=pixelVirtual,
                           font=("Verdana", 16))

        self.next_month_btn = Button(text="→", compound="c", height=15, width=30, padx=5, pady=5, bg=BG_COLOR, bd=1,
                                     image=pixelVirtual, borderwidth=0, font=("Verdana", 16),
                                     command=self.getNextMonth)

        self.prev_month_btn = Button(text="←", compound="c", height=15, width=30, padx=5, pady=5, bg=BG_COLOR, bd=1,
                                     image=pixelVirtual, borderwidth=0, font=("Verdana", 16),
                                     command=self.getPrevMonth)

        prem = DATE_TMP.month - 1
        counter = 1
        if prem < 1:
            prem = 12 - prem

        pre_d_number = self.getDaysNumber(date(DATE_TMP.year, prem, DATE_TMP.day))
        d_number = self.getDaysNumber(DATE_TMP)
        start_point = self.getMonthWeekday(DATE_TMP)
        for i in range(6):
            self.buttons.append([])
            for j in range(7):
                if (j in range(0, start_point) and i == 0):
                    self.buttons[i].append(Button(text=f"{pre_d_number - (start_point - j - 1)}", image=pixelVirtual,
                                                  compound="c", height=40, width=50, padx=5, pady=5, bg="#696969", bd=1,
                                                  highlightcolor="#ccc", fg="#a8a8a8", font=("Verdana", 10),
                                                  relief=GROOVE, activebackground="#999999", activeforeground="#000",
                                                  command=self.getPrevMonth))
                elif counter <= d_number:
                    self.buttons[i].append(Button(text=f"{counter}", image=pixelVirtual,
                                                  compound="c", height=40, width=50, padx=5, pady=5, bg=BT_COLOR, bd=1,
                                                  highlightcolor="#ccc", fg="#f5f5f5", font=("Verdana", 10),
                                                  relief=GROOVE, activebackground="#ccc", activeforeground="#000"))
                    self.buttons[i][j].config(command=partial(self.select, self.buttons[i][j]))
                    counter += 1
                else:
                    self.buttons[i].append(Button(text=f"{counter - d_number}", image=pixelVirtual,
                                                  compound="c", height=40, width=50, padx=5, pady=5, bg="#696969", bd=1,
                                                  highlightcolor="#ccc", fg="#a8a8a8", font=("Verdana", 10),
                                                  relief=GROOVE, activebackground="#999999", activeforeground="#000",
                                                  command=self.getNextMonth))
                    counter += 1
                self.display()

    def setMap(self):
        prem = DATE_TMP.month - 1
        counter = 1
        if prem < 1:
            prem = 12 - prem

        pre_d_number = self.getDaysNumber(date(DATE_TMP.year, prem, DATE_TMP.day))
        d_number = self.getDaysNumber(DATE_TMP)
        start_point = self.getMonthWeekday(DATE_TMP)

        for i in range(6):
            for j in range(7):
                if (j in range(0, start_point) and i == 0):
                    self.buttons[i][j].config(text=f"{pre_d_number - (start_point - j - 1)}", image=pixelVirtual,
                                              compound="c", bg="#696969", bd=1,
                                              highlightcolor="#ccc", fg="#a8a8a8",
                                              relief=GROOVE, activebackground="#999999", activeforeground="#000",
                                              command=self.getPrevMonth)
                elif counter <= d_number:
                    self.buttons[i][j].config(text=f"{counter}", image=pixelVirtual,
                                              compound="c", bg=BT_COLOR, bd=1,
                                              highlightcolor="#ccc", fg="#f5f5f5",
                                              relief=GROOVE, activebackground="#ccc", activeforeground="#000",
                                              command=partial(self.select, self.buttons[i][j]))
                    counter += 1
                else:
                    self.buttons[i][j].config(text=f"{counter - d_number}", image=pixelVirtual,
                                              compound="c", bg="#696969", bd=1,
                                              highlightcolor="#ccc", fg="#a8a8a8",
                                              relief=GROOVE, activebackground="#999999", activeforeground="#000",
                                              command=self.getNextMonth)
                    counter += 1

        self.title.config(text=f"{self.getDateTitle(DATE_TMP)}")

    def getNextMonth(self):
        global DATE_TMP
        if DATE_TMP.month < 12:
            DATE_TMP = date(DATE_TMP.year, DATE_TMP.month + 1, 1)
        else:
            DATE_TMP = date(DATE_TMP.year + 1, 1, 1)
        self.setMap()

    def getPrevMonth(self):
        global DATE_TMP
        if DATE_TMP.month > 1:
            DATE_TMP = date(DATE_TMP.year, DATE_TMP.month - 1, 1)
        else:
            DATE_TMP = date(DATE_TMP.year - 1, 12, 1)
        self.setMap()

    def display(self):
        global BG_COLOR
        Label(width=20, height=50, bg=BG_COLOR, image=pixelVirtual).grid(row=0, column=0)

        self.title.grid(row=0, column=1, columnspan=7, sticky=W + S)

        self.next_month_btn.grid(row=0, column=5, columnspan=2, sticky=W+S, pady=5)
        self.prev_month_btn.grid(row=0, column=3, columnspan=2, sticky=E+S, pady=5)

        for i in range(len(self.buttons[0])):
            Label(text=self.day_week_names[i], width=3, height=1, bg=BG_COLOR, font=("Verdana", 10)).grid\
                (row=1, column=i + 1, padx=1, pady=1, sticky=S)

        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                self.buttons[i][len(self.buttons[i]) - 1].grid(row=i + 2, column=j + 1, padx=1, pady=1)
                self.buttons[i][j].bind('<Enter>', partial(self.select, self.buttons[i][j]))  # Событие наведения на ячейку календаря
                self.buttons[i][j].bind('<Leave>', partial(self.select, self.buttons[i][j]))  # Событие при выводе мыши из ячейки календаря

    def select(self, button, event=None):
        global DATE_TMP
        try:
            if (event == None):  # На кнопку нажали...
                if self.selected == False:  # ..и она не выбрана
                    button.config(bg="#fff555", fg="#000")

                    self.selected_btn = button
                    self.selected = True
                    DATE_TMP = date(DATE_TMP.year, DATE_TMP.month, int(button["text"]))
                    self.tasks.setTaskList(DATE_TMP)

                elif button == self.selected_btn and self.selected == True:  # ..и нажали на ту же самую (выбранную) кнопку
                    button.config(bg=BT_COLOR, fg="#f5f5f5")
                    self.selected = False
                    DATE_TMP = date(DATE_TMP.year, DATE_TMP.month, 1)
                    self.tasks.setTaskList(DATE_TMP)
                elif button != self.selected_btn and self.selected == True:  # ..и она еще не выбрана, хоть и выбрана какая-то другая ячейка
                    self.selected_btn.config(bg=BT_COLOR, fg="#f5f5f5")
                    button.config(bg="#fff555", fg="#000")
                    self.selected_btn = button
                    DATE_TMP = date(DATE_TMP.year, DATE_TMP.month, int(button["text"]))
                    self.tasks.setTaskList(DATE_TMP)

            elif event.type == '7' and self.selected == False and button.cget('bg') != "#696969":
                DATE_TMP = date(DATE_TMP.year, DATE_TMP.month, int(button["text"]))
                self.tasks.setTaskList(DATE_TMP)
                button.config(bg="#fff555", fg="#000")
                self.selected_btn = button
            elif event.type == '8' and self.selected == False and button.cget('bg') != "#696969":
                DATE_TMP = date(DATE_TMP.year, DATE_TMP.month, 1)
                self.tasks.setTaskList(DATE_TMP)
                self.selected_btn.config(bg=BT_COLOR, fg="#f5f5f5")
                self.selected_btn = None
        except:
            pass

    def getDateTitle(self, p_date):
        months = {
            1: "Январь",
            2: "Февраль",
            3: "Март",
            4: "Апрель",
            5: "Май",
            6: "Июнь",
            7: "Июль",
            8: "Август",
            9: "Сентябрь",
            10: "Октябрь",
            11: "Ноябрь",
            12: "Декабрь"}
        return f"{months[p_date.month]}, {p_date.year}"

    def getDaysNumber(self, p_date):  # Возвращает кол-во дней в месяце
        num_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if num_days[p_date.month - 1] == 28 and p_date.year % 4 == 0:
            return 29
        else:
            return num_days[p_date.month - 1]

    def getMonthWeekday(self, p_date):  # Возвращает номер дня недели первого дня месяца
        return date(p_date.year, p_date.month, 1).weekday()


class TasksManager():
    path = ""
    data = {}

    def __init__(self, path):
        self.path = path
        with open(self.path, "r", encoding="utf8") as read_file:
            try:
                self.data = json.load(read_file)
            except:
                pass

    def getTasks(self):
        pass

    def saveChanges(self):
        with open(self.path, "w", encoding="utf8") as write_file:
            json.dump(self.data, write_file, ensure_ascii=False)

    def addTask(self, note, start_date, end_date):
        date_tmp = start_date
        while date_tmp + timedelta(days=1) <= end_date + timedelta(days=1):
            try:
                self.data[str(date_tmp.year)][str(date_tmp.month)][str(date_tmp.day)].append(note)
            except:
                try:
                    self.data[str(date_tmp.year)][str(date_tmp.month)] |= {str(date_tmp.day): [note]}
                except:
                    try:
                        self.data[str(date_tmp.year)] |= {str(date_tmp.month): {str(date_tmp.day): [note]}}
                    except:
                        self.data[str(date_tmp.year)] = {str(date_tmp.month): {str(date_tmp.day): [note]}}
            date_tmp += timedelta(days=1)
        self.saveChanges()

    def getTaskList(self, p_date):
        try:
            return self.data[str(p_date.year)][str(p_date.month)][str(p_date.day)]
        except:
            return []

    def printTasks(self):
        print(self.data)

    def deleteTask(self, p_date, index=0):
        self.data[str(p_date.year)][str(p_date.month)][str(p_date.day)].pop(index)
        self.saveChanges()


class Tasks():
    def __init__(self):
        self.manager = TasksManager("Tasks.json")
        self.task_list = None

        self.list_menu = None
        self.add_btn = None
        self.delete_btn = None
        self.task_window = None

        self.title_ll = None
        self.start_date_ll = None
        self.time_ll = None
        self.end_date_ll = None
        self.note_ll = None
        self.save_task_btn = None
        self.email_ll = None
        self.email_add_btn = None
        self.email_delete_btn = None
        self.link_ll = None

        self.title_en = None
        self.start_date_en = None
        self.start_time_en = None
        self.end_date_en = None
        self.end_time_en = None
        self.note_en = None
        self.email_lb = None
        self.email_en = None
        self.link_en = None

        """Настройки виджетов отображения задач"""
        self.gap = Label(width=5, height=1, bg=BG_COLOR)
        self.out_title_ll = Label(font=("Verdana", 16), width=20, height=1, bg=BG_COLOR)
        self.out_date_ll = Label(font=("Verdana", 10), width=20, height=1, bg=BG_COLOR)
        self.out_note_ll = Label(font=("Verdana", 11), width=400, compound="c", anchor="n",
                                 bg=BG_COLOR, justify=LEFT, image=pixelVirtual, wraplength=400, height=200)

        self.out_email_scroll_y = Scrollbar(orient=VERTICAL)
        self.out_email_ll = Listbox(font=("Verdana", 10), width=25, bg=BG_COLOR, borderwidth=0, height=4, yscrollcommand=self.out_email_scroll_y.set)
        self.out_email_scroll_y.config(command=self.out_email_ll.yview)

        self.out_link_ll = Label(font=("Verdana", 10, "underline"), width=40, bg=BG_COLOR, height=2, fg="#0000ff")


        """Настройки виджетов списка задач"""
        self.list_menu_ll = Label(text="", bg=BG_COLOR, width=20, height=1)
        self.list_menu = Listbox(width=20, height=6, relief=GROOVE, bg=TT_COLOR, font=("Verdana", 11))

        self.setTaskList(DATE_TMP)
        self.eventsManager(self.list_menu)

        self.add_btn = Button(text="+", compound="c", height=50, width=30, bg=BT_COLOR,
                              image=pixelVirtual,
                              highlightcolor="#ccc", fg="#f5f5f5", font=("Verdana", 10), relief=GROOVE,
                              activebackground="#ccc", activeforeground="#000",
                              command=self.getTaskPage)

        self.delete_btn = Button(text="-", compound="c", height=50, width=30, bg=BT_COLOR,
                                 image=pixelVirtual,
                                 highlightcolor="#ccc", fg="#f5f5f5", font=("Verdana", 10), relief=GROOVE,
                                 activebackground="#ccc", activeforeground="#000",
                                 command=self.deleteTask)

        """Расположение виджетов"""
        self.gap.grid(row=2, column=8)
        self.out_title_ll.grid(row=0, column=9, columnspan=3, rowspan=2, sticky=S)
        self.out_date_ll.grid(row=2, column=9, columnspan=2, sticky=N)
        self.out_note_ll.grid(row=3, column=9, columnspan=3, rowspan=6, sticky=N)


        self.out_link_ll.grid(row=11, column=9, columnspan=3, rowspan=1, sticky=N+W)
        self.out_link_ll.bind('<Button-1>', partial(self.eventsManager, self.out_link_ll))
        self.out_link_ll.bind('<Enter>', partial(self.eventsManager, self.out_link_ll))
        self.out_link_ll.bind('<Leave>', partial(self.eventsManager, self.out_link_ll))

        self.list_menu_ll.grid(row=9, column=2, columnspan=5, pady=0, sticky=S)
        self.list_menu.grid(row=10, column=2, columnspan=5, rowspan=3, padx=20, pady=10)
        self.list_menu.bind('<Double-Button-1>', partial(self.eventsManager, self.list_menu))
        self.add_btn.grid(row=10, column=6, sticky=S)
        self.delete_btn.grid(row=11, column=6)

    def eventsManager(self, obj, event=None):
        if event != None and event.type == '4':
            if (type(obj) == Listbox):
                select_note = list(self.list_menu.curselection())[0]
            elif (type(obj) == Label):
                select_note = list(self.list_menu.curselection())[0]
                webbrowser.open(self.manager.getTaskList(DATE_TMP)[select_note]['link'][1], new=0)
                return 0
        elif event != None and event.type == '7' and type(obj) == Label:
            obj.config(fg="#ff0000")
            return 0
        elif event != None and event.type == '8' and type(obj) == Label:
            obj.config(fg="#0000ff")
            return 0
        elif event != None:
            print(event.type)
            return 0
        else:
            if len(self.list_menu.get(0, END)) != 0:
                select_note = 0
            else:
                self.out_title_ll.config(text="Список задач пуст!", width=25, wraplength=400, height=1)
                return 0

        if len(self.manager.getTaskList(DATE_TMP)[select_note]['title']) > 20:
            w = 22
        else:
            w = len(self.manager.getTaskList(DATE_TMP)[select_note]['title'])

        self.out_title_ll.config(text=self.manager.getTaskList(DATE_TMP)[select_note]['title'],
                                 width=w, height=int(len(self.manager.getTaskList(DATE_TMP)[select_note]['title'])/20+0.99))

        if self.manager.getTaskList(DATE_TMP)[select_note]['end_date'] != '':
            self.out_date_ll.config(text=self.manager.getTaskList(DATE_TMP)[select_note]['start_date'] + ' ' +
                                         self.manager.getTaskList(DATE_TMP)[select_note]['start_time'] + ' - ' +
                                         self.manager.getTaskList(DATE_TMP)[select_note]['end_date'] + ' ' +
                                         self.manager.getTaskList(DATE_TMP)[select_note]['end_time'],
                                    width=len(self.manager.getTaskList(DATE_TMP)[select_note]['start_date'] + ' ' +
                                         self.manager.getTaskList(DATE_TMP)[select_note]['start_time'] + ' - ' +
                                         self.manager.getTaskList(DATE_TMP)[select_note]['end_date'] + ' ' +
                                         self.manager.getTaskList(DATE_TMP)[select_note]['end_time']))
        else:
            self.out_date_ll.config(text=self.manager.getTaskList(DATE_TMP)[select_note]['start_date'] + ' ' +
                                         self.manager.getTaskList(DATE_TMP)[select_note]['start_time'],
                                    width=len(self.manager.getTaskList(DATE_TMP)[select_note]['start_date'] + ' ' +
                                         self.manager.getTaskList(DATE_TMP)[select_note]['start_time']))


        self.out_note_ll.config(text=self.manager.getTaskList(DATE_TMP)[select_note]['note'])

        self.out_email_ll.delete(0, END)
        if len(self.manager.getTaskList(DATE_TMP)[select_note]['emails']) != 0:
            self.out_email_ll.grid(row=7, column=9, columnspan=3, rowspan=3, sticky=N + E)
            self.out_email_scroll_y.grid(row=7, column=12, rowspan=2)
        else:
            self.out_email_ll.grid_forget()
            self.out_email_scroll_y.grid_forget()


        for email in self.manager.getTaskList(DATE_TMP)[select_note]['emails']:
            self.out_email_ll.insert(END, email)


        self.out_link_ll.config(text=self.manager.getTaskList(DATE_TMP)[select_note]['link'][0])


    def setTaskList(self, p_date):
        self.task_list = self.manager.getTaskList(p_date)
        self.clearTaskList()
        for task in self.task_list:
            self.list_menu.insert(END, ' ' + task['title'])

    def clearTaskList(self):
        self.list_menu.delete(0, END)

    def getTaskPage(self):
        try:
            print(type(self.task_window))
            print(f"'{self.task_window.state()}'")
        except:
            pass
        if (self.task_window == None):
            self.createTaskWindow()
        else:
            try:
                self.task_window.state()
            except:
                self.createTaskWindow()

    def getTaskStr(self):
        str = ''
        if self.task_list != None and self.task_list != []:
            str += "Список задач на сегодня:"
            print(self.task_list)
            for task in self.task_list:
                str += '\n' + task['title']
        else:
            str = 'Список задач пуст 😞'

        return str

    def createTaskWindow(self):
        self.task_window = createWindow("Редактор задач", "top", "440x700+1200+200")

        self.title_ll = Label(self.task_window, width=12, text="Название", font=("Verdana", 8), bg=BG_COLOR)
        self.title_en = Entry(self.task_window, width=51, bg=TT_COLOR)

        self.start_date_ll = Label(self.task_window, width=10, text="Дата начала\n(dd.mm.yyyy)", font=("Verdana", 8),
                                   bg=BG_COLOR, wraplength=100)
        self.start_date_en = Entry(self.task_window, width=9, bg=TT_COLOR)
        self.time_ll = Label(self.task_window, width=14, text="Время (hh.mm):", font=("Verdana", 8),
                                   bg=BG_COLOR, wraplength=100)
        self.start_time_en = Entry(self.task_window, width=9, bg=TT_COLOR)
        self.start_date_en.insert(0, f'{DATE_TMP.day}.{DATE_TMP.month}.{DATE_TMP.year}')

        self.end_date_ll = Label(self.task_window, width=10, text="Окончание\n(dd.mm.yyyy)", font=("Verdana", 8),
                                 bg=BG_COLOR)
        self.end_date_en = Entry(self.task_window, width=9, bg=TT_COLOR)
        self.end_time_en = Entry(self.task_window, width=9, bg=TT_COLOR)
        self.save_task_btn = Button(self.task_window, text="Добавить запись", compound="c", height=30, width=150,
                                    bg=BT_COLOR,
                                    image=pixelVirtual,
                                    highlightcolor="#ccc", fg="#f5f5f5", font=("Verdana", 10), relief=GROOVE,
                                    activebackground="#ccc", activeforeground="#000",
                                    command=self.addTask)
        self.note_ll = Label(self.task_window, width=44, text="Место для заметок (описание)", font=("Verdana", 8),
                             bg=BG_COLOR)
        self.note_en = Text(self.task_window, width=44, height=13, bg=TT_COLOR)

        self.email_ll = Label(self.task_window, width=30, text="Электронная почта участников", font=("Verdana", 8),
                              bg=BG_COLOR)
        self.email_lb = Listbox(self.task_window, width=30, height=5, bg=TT_COLOR)
        self.email_add_btn = Button(self.task_window, text="+", compound="c", height=25, width=25, bg=BT_COLOR,
                                    image=pixelVirtual, pady=10,
                                    highlightcolor="#ccc", fg="#f5f5f5", font=("Verdana", 10), relief=GROOVE,
                                    activebackground="#ccc", activeforeground="#000",
                                    command=self.addEmail)
        self.email_delete_btn = Button(self.task_window, text="-", compound="c", height=25, width=25, bg=BT_COLOR,
                                       image=pixelVirtual, pady=10,
                                       highlightcolor="#ccc", fg="#f5f5f5", font=("Verdana", 10), relief=GROOVE,
                                       activebackground="#ccc", activeforeground="#000",
                                       command=self.deleteEmail)
        self.email_en = Entry(self.task_window, width=30, bg=TT_COLOR, relief=GROOVE)

        self.link_ll = Label(self.task_window, width=10, text="Место события:", bg=BG_COLOR, font=("Verdana", 8), wraplength=80)
        self.link_en = Entry(self.task_window, width=30, bg=TT_COLOR)

        self.title_ll.grid(column=0, row=0, columnspan=4, padx=0, pady=0, sticky=S + W)
        self.title_en.grid(column=0, row=1, columnspan=4, pady=0, sticky=N)
        self.start_date_ll.grid(column=0, row=2, padx=0, pady=15, sticky=S)
        self.start_date_en.grid(column=1, row=2, padx=0, pady=15, sticky=S)
        self.time_ll.grid(column=0, row=3, sticky=N)
        self.start_time_en.grid(column=1, row=3, sticky=N)
        self.end_date_ll.grid(column=2, row=2, padx=0, pady=15, sticky=S)
        self.end_date_en.grid(column=3, row=2, padx=0, pady=15, sticky=S)
        self.end_time_en.grid(column=3, row=3, sticky=N)
        self.note_ll.grid(column=0, columnspan=4, row=4, padx=20, sticky=S)
        self.note_en.grid(column=0, columnspan=4, row=5, padx=20, pady=5, sticky=S)

        self.email_ll.grid(column=0, columnspan=3, row=6, padx=20, pady=5, sticky=E + S)
        self.email_lb.grid(column=0, columnspan=3, rowspan=2, row=7, padx=20, sticky=E + S)
        self.email_add_btn.grid(column=3, row=7, sticky=W + N)
        self.email_delete_btn.grid(column=3, row=8, sticky=W + N)
        self.email_en.grid(column=0, row=9, columnspan=3, padx=20, sticky=N + E)

        self.link_ll.grid(column=0, row=10, columnspan=1, padx=20, pady=20, sticky=S + E)
        self.link_en.grid(column=1, row=10, columnspan=3, pady=20, sticky=W + S)

        self.save_task_btn.grid(column=2, row=12, columnspan=2, sticky=S)

    def addTask(self):
        if self.title_en.get() != '' and self.title_en.get() != '':
            start_date = re.compile("\d{1,2}[\./]\d{1,2}[\./]\d{4}").match(self.start_date_en.get())
            start_time = re.compile("[0-6]\d[\./][0-6]\d").match(self.start_time_en.get())
            end_date = re.compile("\d{1,2}[\./]\d{1,2}[\./]\d{4}").match(self.end_date_en.get())
            end_time = re.compile("[0-6]\d[\./][0-6]\d").match(self.end_time_en.get())
            if (start_date != None and end_date != None and self.start_date_en.get() < self.end_date_en.get()):
                start_date = start_date.group()
                end_date = end_date.group()
                start_time = start_time.group()
                end_time = end_time.group()

                place = converter.getLink(self.link_en.get())

                new_task = {"title": self.title_en.get(), "start_date": start_date, "start_time": start_time, "end_date": end_date, "end_time": end_time,
                            "note": self.note_en.get(1.0, END), "emails": self.email_lb.get(0, END), "link": [self.link_en.get(), place]}
                self.manager.addTask(new_task, date(int(re.search( r'\d{4}', start_date).group()),
                                                int(re.findall( r'\d{1,2}', start_date)[1]),
                                                int(re.findall( r'\d{1,2}', start_date)[0])),
                                            date(int(re.search( r'\d{4}', end_date).group()),
                                                int(re.findall( r'\d{1,2}', end_date)[1]),
                                                int(re.findall( r'\d{1,2}', end_date)[0])))
                print("Добавлена новая запись")
                self.setTaskList(DATE_TMP)
            elif (start_date != None):
                start_date = start_date.group()
                start_time = start_time.group()
                end_time = end_time.group()

                place = converter.getLink(self.link_en.get())

                new_task = {"title": self.title_en.get(), "start_date": start_date, "start_time": start_time, 'end_date': start_date, "end_time": end_time,
                            "note": self.note_en.get(1.0, END), "emails": self.email_lb.get(0, END), "link": [self.link_en.get(), place]}
                self.manager.addTask(new_task, date(int(re.search(r'\d{4}', start_date).group()),
                                                int(re.findall(r'\d{1,2}', start_date)[1]),
                                                int(re.findall(r'\d{1,2}', start_date)[0])),
                                             date(int(re.search(r'\d{4}', start_date).group()),
                                                  int(re.findall(r'\d{1,2}', start_date)[1]),
                                                  int(re.findall(r'\d{1,2}', start_date)[0])))
                print("Добавлена новая запись")
                self.setTaskList(DATE_TMP)
            else:
                print("Не указана начальная дата для задачи или конечная дата больше!")

    def addEmail(self):
        if ('@' in self.email_en.get()):
            self.email_lb.insert(0, self.email_en.get())

    def deleteEmail(self):
        select_note = list(self.email_lb.curselection())[0]
        if select_note != []:
            self.email_lb.delete(select_note)

    def deleteTask(self):
        try:
            select_note = list(self.list_menu.curselection())[0]
            print(select_note)
            if self.manager.data[str(DATE_TMP.year)][str(DATE_TMP.month)][str(DATE_TMP.day)][select_note]["title"] == self.out_title_ll["text"]:
                self.out_title_ll.config(text='')
                self.out_date_ll.config(text='')
                self.out_note_ll.config(text='')
                self.out_link_ll.config(text='')
                try:
                    self.out_email_ll.grid_forget()
                    self.out_email_scroll_y.grid_forget()
                except:
                    pass
            if select_note != []:
                self.manager.deleteTask(DATE_TMP, select_note)
                self.list_menu.delete(select_note)
        except:
            pass


def createWindow(text, type="tk", geometry="1000x650+250+200"):  # Создание главной панели
    global ICON_PAT
    if type == "tk":
        window = Tk()
    else:
        window = Toplevel()

    window.config(bg="#e6e6e6")  # Цвет и другие опции
    window.title(text)  # Название
    window.iconbitmap(ICO_NAME)  # Иконка
    window.geometry(geometry)  # Размеры и расположение

    return window

def notification(title, note, duration):
    icon_path = ICO_NAME
    win10toast.ToastNotifier().show_toast(title, note, icon_path=icon_path, duration=duration, threaded=True)

if __name__ == "__main__":
    window = createWindow("Планировщик")
    pixelVirtual = PhotoImage(width=1, height=1)
    l = Tasks()
    p = Calendar(l)
    window.mainloop()
