"""Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом. 
Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции). 
Ввод данных из файла с контролем правильности ввода. 
Базы данных не использовать. При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами. 
Для GUI и визуализации использовать библиотеку tkinter.
Вариант 21:
Объекты – отрезки
Функции:	
сегментация
визуализация
раскраска
перемещение на плоскости
"""


import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
class Point:
    def __init__(self,x,y):
        self.point = [x, y]

class Otrezki:
    def __init__(self,point1,point2,color="black",count_segments=1):
        self.point1 = point1
        self.point2 = point2
        self.color = color
        self.count_segments = count_segments
    def get_color(self,color):
        self.color = color
    def move(self,point1,point2):
        self.point1 = point1
        self.point2 = point2
    def change_segmentation(self,count_segments):
        self.count_segments = count_segments
    def vizualization(self,number):
        if self.count_segments <= 0:
            raise ValueError("Число сегментов должно быть больше 0.")

        x_coords = np.linspace(self.point1.point[0], self.point2.point[0], self.count_segments + 1)
        y_coords = np.linspace(self.point1.point[1], self.point2.point[1], self.count_segments + 1)

        plt.plot([self.point1.point[0], self.point2.point[0]], [self.point1.point[1], self.point2.point[1]], linewidth=1, label=f'Отрезок №{number}', color=self.color) 

        plt.plot(x_coords, y_coords, 'ro', markersize=5, label='Разделительные точки')

        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title(f"Визульное представление отрезка/отрезков")
        plt.legend()
        plt.grid(True)
        plt.show()
    def view(self):
        return [self.point1,self.point2,self.color,self.count_segments]
    
def create_new_file(otrezki,filename):
    with open(filename, 'w') as file:
        for info in range(len(otrezki)):
            get_info=otrezki[info].view()
            file.write(f"{get_info[0].point[0]},{get_info[0].point[1]},{get_info[1].point[0]},{get_info[1].point[1]},{get_info[2]},{get_info[3]}\n")
    file.close()

def load_segments_from_file(filename):
    try:
        with open(filename, 'r',encoding='utf-8') as file:
            lines = file.readlines()
        otrezki = []
        count=0
        for line in lines:
            parts = line.strip().split(',')  # Разделитель запятая
            count+=1
            if len(parts) == 6:
                try:
                    x1, y1, x2, y2, color,segments = map(str, parts)
                    mcolors.to_rgba(color)
                    otrezki.append(Otrezki(Point(float(x1),float(y1)), Point(float(x2),float(y2)), color, int(segments))) # добавить проверку на введенный цвет
                except ValueError:
                    messagebox.showwarning(f"Ошибка в формате строки:" ,f"Строка №{count}: {line}\nПример формирования: x1,y1,x2,y2,цвет на английском,количество сегментов > 0\n(10,15,20,25,black,1)")
            else:
                messagebox.showwarning(f"Ошибка в формировании данных в файле.", f"Пример формирования: x1,y1,x2,y2,цвет на английском,количество сегментов > 0\n (10,15,20,25,black,1)\n Строка №{count}: {line}")
            file.close()
        return otrezki
    except FileNotFoundError:
        print(f"Файл test.txt не найден.")
        messagebox.showwarning(f"Файл test.txt не найден.")
        return []

def click_button_back1(window,filename):
    window.destroy()
    menu_GUI(filename)

def view_otrezki_GUI(otrezki):
    view = tk.Tk()
    view.title("Список отрезков")
    view.geometry("900x600")
    view.resizable(width=False,height=False)

    frame = tk.Frame (view,bg="gray")
    frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

    label1=tk.Label(frame,text="Список отрезков",font=("Time",20))
    label1.place(x=325,y=10,width=250,height=50)

    text_view = tk.Text(frame,wrap=tk.WORD,font=("Time",16))
    text_view.place(x=100,y=80,width=700,height=400)
    view_otrezki_fuc(text_view,otrezki)
    button= tk.Button(frame,text="Назад",foreground="white",font=("Time",20),bg="red", command=lambda: click_button_back1(view,filename))
    button.place(x=400,y=510,width=100,height=50)

def view_otrezki_fuc(text_view,otrezki):
    text_view.delete(1.0,tk.END)
    for otrezok in range(len(otrezki)):
        text_view.insert(tk.END,f"Отрезок №{otrezok+1}")
        info=otrezki[otrezok].view()
        text_view.insert(tk.END,f"\nКоординаты первой точки отрезка: {info[0].point[0]} ; {info[0].point[1]} ")
        text_view.insert(tk.END,f"\nКоординаты второй точки отрезка: {info[1].point[0]} ; {info[1].point[1]} ")
        text_view.insert(tk.END,f"\nЦвет отрезка: {info[2]}")
        text_view.insert(tk.END,f"\nКоличество сегментов: {info[3]}")
        text_view.insert(tk.END,"\n"+"="*58+"\n")
    
def move_otrezok(otrezki):
    view = tk.Tk()
    view.title("Список отрезков")
    view.geometry("900x900")
    view.resizable(width=False,height=False)

    frame = tk.Frame (view,bg="gray")
    frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

    label1=tk.Label(frame,text="Список отрезков",font=("Time",20))
    label1.place(x=325,y=10,width=250,height=50)

    text_view = tk.Text(frame,wrap=tk.WORD,font=("Time",16))
    text_view.place(x=100,y=80,width=700,height=200)
    view_otrezki_fuc(text_view,otrezki)

    label2=tk.Label(frame,text="Для перемещения отрезка: \n1) выберите и введите номер отрезка\n2) введите новые координаты точек",font=("Time",16))
    label2.place(x=200,y=300,width=500,height=100)

    label3=tk.Label(frame,text="Номер отрезка",font=("Time",16))
    label3.place(x=360,y=430,width=180,height=50)
    
    text_box_number_change = tk.Entry(frame,font=("Time",20))
    text_box_number_change.place(x=425,y=490,width=50,height=50)

    label4=tk.Label(frame,text="Первая точка",font=("Time",16))
    label4.place(x=20,y=550,width=180,height=50)

    label5=tk.Label(frame,text="Вторая точка",font=("Time",16))
    label5.place(x=680,y=550,width=180,height=50)

    labelX=tk.Label(frame,text="X",font=("Time",16))
    labelX.place(x=20,y=610,width=50,height=50)
    labelX2=tk.Label(frame,text="X",font=("Time",16))
    labelX2.place(x=680,y=610,width=50,height=50)

    labelY=tk.Label(frame,text="Y",font=("Time",16))
    labelY.place(x=20,y=670,width=50,height=50)
    labelY2=tk.Label(frame,text="Y",font=("Time",16))
    labelY2.place(x=680,y=670,width=50,height=50)

    text_box_X1 = tk.Entry(frame,font=("Time",16))
    text_box_X1.place(x=80,y=610,width=120,height=50)

    text_box_X2 = tk.Entry(frame,font=("Time",16))
    text_box_X2.place(x=740,y=610,width=120,height=50)

    text_box_Y1 = tk.Entry(frame,font=("Time",16))
    text_box_Y1.place(x=80,y=670,width=120,height=50)

    text_box_Y2 = tk.Entry(frame,font=("Time",16))
    text_box_Y2.place(x=740,y=670,width=120,height=50)    

    button= tk.Button(frame,text="Ввести",foreground="white",font=("Time",20),bg="green",command=lambda: move_otrezok_fuc(otrezki,text_box_number_change.get(),text_box_X1.get(),text_box_Y1.get(),text_box_X2.get(),text_box_Y2.get(),text_view,filename))
    button.place(x=400,y=730,width=100,height=50)

    button= tk.Button(frame,text="Назад",foreground="white",font=("Time",20),bg="red",command=lambda:click_button_back1(view,filename))
    button.place(x=100,y=730,width=100,height=50)

def move_otrezok_fuc(otrezki,choice,x1,y1,x2,y2,text_view,filename):
    if choice != "" and x1 != "" and x2 != "" and y1 != "" and y2 != "": 
        try: 
            choice,x1,y1,x2,y2 = int(choice),float(x1),float(y1),float(x2),float(y2)
            try:
                otrezki[choice-1].move(Point(x1,y1),Point(x2,y2))
                create_new_file(otrezki,filename)
                new_otrezki = load_segments_from_file(filename)
                view_otrezki_fuc(text_view,new_otrezki)
                messagebox.showinfo(f"Успех","Отрезок успешно перемещён")
            except:
                messagebox.showwarning(f"Ошибка","Отрезка с таким номером нет, попробуйте снова")
        except:
            messagebox.showwarning(f"Ошибка","Неверный тип данных")
    else:
        messagebox.showwarning(f"Ошибка","Некоторые поля не заполнены")

def change_color(otrezki):
    view = tk.Tk()
    view.title("Список отрезков")
    view.geometry("900x750")
    view.resizable(width=False,height=False)

    frame = tk.Frame (view,bg="gray")
    frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

    label1=tk.Label(frame,text="Список отрезков",font=("Time",20))
    label1.place(x=325,y=10,width=250,height=50)

    text_view = tk.Text(frame,wrap=tk.WORD,font=("Time",16))
    text_view.place(x=100,y=80,width=700,height=200)
    view_otrezki_fuc(text_view,otrezki)

    label2=tk.Label(frame,text="Для изменения цвета отрезка: \n1) выберите и введите номер отрезка\n2) введите цвет отрезка на английском",font=("Time",16))
    label2.place(x=200,y=300,width=500,height=100)

    label3=tk.Label(frame,text="Номер отрезка",font=("Time",16))
    label3.place(x=360,y=430,width=180,height=50)

    text_box_number_change = tk.Entry(frame,font=("Time",20))
    text_box_number_change.place(x=425,y=490,width=50,height=50)

    label4=tk.Label(frame,text="Новый цвет отрезка",font=("Time",16))
    label4.place(x=325,y=550,width=250,height=50)

    text_box_color = tk.Entry(frame,font=("Time",16))
    text_box_color.place(x=375,y=610,width=150,height=50)

    button= tk.Button(frame,text="Ввести",foreground="white",font=("Time",20),bg="green",command=lambda: change_color_fuc(otrezki,text_box_number_change.get(),text_box_color.get(),text_view,filename))
    button.place(x=500,y=670,width=100,height=50)

    button= tk.Button(frame,text="Назад",foreground="white",font=("Time",20),bg="red",command=lambda:click_button_back1(view,filename))
    button.place(x=300,y=670,width=100,height=50)

def change_color_fuc(otrezki,number_otrezka,color,text_view,filename):
    if number_otrezka != "" or color != "": 
        try:
            number_otrezka=int(number_otrezka)
            try:
                mcolors.to_rgba(color)
                color = str(color)
                try:
                    otrezki[number_otrezka-1].get_color(color)
                    create_new_file(otrezki,filename)
                    new_otrezki = load_segments_from_file(filename)
                    view_otrezki_fuc(text_view,new_otrezki)
                    messagebox.showinfo(f"Успех","Отрезок успешно перекрашен")
                except: 
                    messagebox.showwarning(f"Ошибка","Отрезка с таким номером нет, попробуйте снова")
            except:
                messagebox.showwarning("Ошибка!","Проверьте данные в поле \"Новый цвет отрезка\"")
        except:
            messagebox.showwarning("Ошибка!","Проверьте данные в поле \"Номер отрезка\"")
    else:
        messagebox.showwarning(f"Ошибка","Некоторые поля не заполнены")

def segmentation(otrezki):
    view = tk.Tk()
    view.title("Список отрезков")
    view.geometry("900x750")
    view.resizable(width=False,height=False)

    frame = tk.Frame (view,bg="gray")
    frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

    label1=tk.Label(frame,text="Список отрезков",font=("Time",20))
    label1.place(x=325,y=10,width=250,height=50)

    text_view = tk.Text(frame,wrap=tk.WORD,font=("Time",16))
    text_view.place(x=100,y=80,width=700,height=200)
    view_otrezki_fuc(text_view,otrezki)

    label2=tk.Label(frame,text="Для сегментирования отрезка: \n1) выберите и введите номер отрезка\n2) введите количество сегментов отрезка",font=("Time",16))
    label2.place(x=200,y=300,width=500,height=100)

    label3=tk.Label(frame,text="Номер отрезка",font=("Time",16))
    label3.place(x=360,y=430,width=180,height=50)

    text_box_number_change = tk.Entry(frame,font=("Time",20))
    text_box_number_change.place(x=425,y=490,width=50,height=50)

    label4=tk.Label(frame,text="Количество сегментов",font=("Time",16))
    label4.place(x=325,y=550,width=250,height=50)

    text_box_segments = tk.Entry(frame,font=("Time",16))
    text_box_segments.place(x=375,y=610,width=150,height=50)

    button= tk.Button(frame,text="Ввести",foreground="white",font=("Time",20),bg="green",command=lambda: segmentation_fuc(otrezki,text_box_number_change.get(),text_box_segments.get(),text_view,filename))
    button.place(x=500,y=670,width=100,height=50)

    button= tk.Button(frame,text="Назад",foreground="white",font=("Time",20),bg="red",command=lambda:click_button_back1(view,filename))
    button.place(x=300,y=670,width=100,height=50)
def segmentation_fuc(otrezki,number_otrezka,segments,text_view,filename):
    if number_otrezka != "" or segments != "": 
        try:
            number_otrezka=int(number_otrezka)
            try:
                segments = int(segments)
                if segments>0:
                    try: 
                        otrezki[number_otrezka-1].change_segmentation(segments)
                        create_new_file(otrezki,filename)
                        new_otrezki = load_segments_from_file(filename)
                        view_otrezki_fuc(text_view,new_otrezki)
                        messagebox.showinfo(f"Успех","Количество сегментов у отрезка изменено")
                    except:
                        messagebox.showwarning(f"Ошибка","Отрезка с таким номером нет, попробуйте снова")
                else:
                    messagebox.showwarning(f"Ошибка","Количество сегментов должно быть более 0")
            except:
                messagebox.showwarning("Ошибка!","Проверьте данные в поле \"Количество сегментов\"")
        except:
            messagebox.showwarning("Ошибка!","Проверьте данные в поле \"Номер отрезка\"")
    else:
        messagebox.showwarning(f"Ошибка","Некоторые поля не заполнены")

def vizual(otrezki):
    view = tk.Tk()
    view.title("Список отрезков")
    view.geometry("900x550")
    view.resizable(width=False,height=False)

    frame = tk.Frame (view,bg="gray")
    frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

    label1=tk.Label(frame,text="Список отрезков",font=("Time",20))
    label1.place(x=325,y=10,width=250,height=50)

    text_view = tk.Text(frame,wrap=tk.WORD,font=("Time",16))
    text_view.place(x=100,y=80,width=700,height=200)
    view_otrezki_fuc(text_view,otrezki)

    label2=tk.Label(frame,text="Для визуализации отрезка: выберите и введите номер отрезка",font=("Time",16))
    label2.place(x=140,y=300,width=620,height=50)

    label3=tk.Label(frame,text="Номер отрезка",font=("Time",16))
    label3.place(x=360,y=360,width=180,height=50)

    text_box_number_change = tk.Entry(frame,font=("Time",20))
    text_box_number_change.place(x=425,y=420,width=50,height=50)

    button= tk.Button(frame,text="Ввести",foreground="white",font=("Time",20),bg="green",command=lambda: vizual_fuc(otrezki,text_box_number_change.get()))
    button.place(x=500,y=480,width=100,height=50)

    button= tk.Button(frame,text="Назад",foreground="white",font=("Time",20),bg="red",command=lambda:click_button_back1(view,filename))
    button.place(x=300,y=480,width=100,height=50)

def vizual_fuc(otrezki,number_otrezka):
    if number_otrezka != "":
        try:
            number_otrezka=int(number_otrezka)
            try:
                otrezki[number_otrezka-1].vizualization(number_otrezka)
            except:
                messagebox.showwarning(f"Ошибка","Отрезка с таким номером нет, попробуйте снова")
        except:
            messagebox.showwarning("Ошибка!","Проверьте данные в поле \"Номер отрезка\"")
    else:
        messagebox.showwarning(f"Ошибка","Некоторые поля не заполнены")
def menu_GUI(filename):
    menu = tk.Tk()
    menu.title("Меню")
    menu.geometry("900x400")
    menu.resizable(width=False,height=False)

    frame = tk.Frame (menu,bg="gray")
    frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

    label1=tk.Label(frame,text="Меню",font=("Time",20))
    label1.place(x=400,y=10,width=100,height=50)

    text_menu = tk.Canvas(frame)
    text_menu.place(x=250,y=70,width=400,height=100)
    text_menu.create_text(200,50,text="1 - Вывести информацию об отрезках\n2 - Переместить отрезок\n3 - Поменять цвет отрезка\n4 - Поменять количество сегментов\n5 - Отобразить отрезок графически", font=("Time",13))
    
    label2=tk.Label(frame,text="Выберите действие и введите число",font=("Time",13))
    label2.place(x=300,y=200,width=300,height=50)

    text_box = tk.Entry(frame,font=("Time",20))
    text_box.place(x=425,y=260,width=50,height=50)

    button= tk.Button(frame,text="Ввести",foreground="white",font=("Time",20),bg="green",command=lambda: menu_fac(menu,text_box,filename))
    button.place(x=400,y=330,width=100,height=50)

    menu.mainloop()
def menu_fac(menu,text_box,filename):
    otrezki = load_segments_from_file(filename)
    try:
        choice = int(text_box.get())
        if choice == 1:
            view_otrezki_GUI(otrezki)
            menu.destroy()
        elif choice == 2:
            move_otrezok(otrezki)
            menu.destroy()
        elif choice == 3:
            change_color(otrezki)
            menu.destroy()
        elif choice == 4:
            segmentation(otrezki)
            menu.destroy()
        elif choice ==5:
            vizual(otrezki)
            menu.destroy()
        elif choice > 5 or choice < 1:
            messagebox.showwarning("Ошибка!","Действия под введенным числом не существует")
    except:
        messagebox.showwarning("Ошибка!","Проверьте введенные данные")
           
filename="test.txt"
menu_GUI(filename)