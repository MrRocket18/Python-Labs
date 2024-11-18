import tkinter as tk
from tkinter import messagebox
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
    def segmentation(self):
        points_of_segments=[]
        points_of_segments.append(self.point1)
        x=self.point1.point1[0]
        y=x=self.point1.point1[1]
        for i in range(self.count_segments-1):
            x+=len/3
            y+=len/3
            points_of_segments.append(Point(x,y))
        points_of_segments.append(self.point2)
        return points_of_segments
   # def vizualization():
        """"""
    def view(self):
        return [self.point1,self.point2,self.color,self.count_segments]
        #print(f"Координаты первой точки отрезка: {self.point1.point[0]};{self.point1.point[1]}")
        #print(f"Координаты второй точки отрезка: {self.point2.point[0]};{self.point2.point[1]}")
        #print(f"Цвет отрезка: {self.color}")
        #print(f"Количество сегментов: {self.count_segments}")
def create_new_file(otrezki):
    with open("new_file.txt", 'w') as file:
        for info in range(len(otrezki)):
            get_info=otrezki[info].view()
            file.write(f"{get_info[0].point[0]},{get_info[0].point[1]},{get_info[1].point[0]},{get_info[1].point[1]},{get_info[2]},{get_info[3]}\n")
    file.close()

def load_segments_from_file():
    """Загружает отрезки из файла (CSV).""" # не читает файл
    try:
        with open("test.txt", 'r') as file:
            lines = file.readlines()
        otrezki = []
        for line in lines:
            parts = line.strip().split(',')  # Разделитель запятая
            if len(parts) == 6:
                try:
                    x1, y1, x2, y2, color,segments = map(str, parts)
                    otrezki.append(Otrezki(Point(float(x1),float(y1)), Point(float(x2),float(y2)), color, int(segments)))
                except ValueError:
                    print(f"Ошибка в формате строки: {line}")
                    messagebox.showwarning(f"Ошибка в формате строки: {line}")
            else:
                messagebox.showwarning(f"Ошибка в формировании данных в файле. Пример формирования: x1,y1,x2,y2,цвет на английском,количество сегментов (10,15,20,25,black,1) {line}")
        return otrezki
    except FileNotFoundError:
        print(f"Файл test.txt не найден.")
        messagebox.showwarning(f"Файл test.txt не найден.")
        return []

def click_button_back1(window):
    window.destroy()
    menu_GUI()

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
    button= tk.Button(frame,text="Назад",foreground="white",font=("Time",20),bg="red", command=lambda: click_button_back1(view))
    button.place(x=400,y=510,width=100,height=50)

def view_otrezki_fuc(text_view,otrezki):
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

    button= tk.Button(frame,text="Ввести",foreground="white",font=("Time",20),bg="green",command=lambda: move_otrezok_fuc(otrezki,text_box_number_change.get(),text_box_X1.get(),text_box_Y1.get(),text_box_X2.get(),text_box_Y2.get(),button))
    button.place(x=400,y=730,width=100,height=50)

def move_otrezok_fuc(otrezki,choice,x1,y1,x2,y2,button):
    if choice != "" or x1 != "" or x2 != "" or y1 != "" or y2 != "": 
        choice,x1,y1,x2,y2 = int(choice),float(x1),float(y1),float(x2),float(y2)
        otrezki[choice-1].move(Point(x1,y1),Point(x2,y2))
        new_info=otrezki[choice-1].view()
        print(new_info[0].point[0],new_info[0].point[1],new_info[1].point[0],new_info[1].point[1])
        #необходимо либо перезаписать файл, либо сделать новый файл с новыми данными
        create_new_file(otrezki)
    else:
        messagebox.showwarning(f"Некоторые поля не заполнены")

def change_color():
    """"""
def vizual():
    """"""

def menu_GUI():
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

    button= tk.Button(frame,text="Ввести",foreground="white",font=("Time",20),bg="green",command=lambda: menu_fac(menu,text_box))
    button.place(x=400,y=330,width=100,height=50)

    menu.mainloop()
def menu_fac(menu,text_box):
    otrezki = load_segments_from_file()
    choice = int(text_box.get())
    menu.destroy()
    if choice == 1:
        view_otrezki_GUI(otrezki)
    elif choice == 2:
        move_otrezok(otrezki)
    elif choice == 3:
        change_color()
    elif choice == 4:
        vizual()
           
menu_GUI()