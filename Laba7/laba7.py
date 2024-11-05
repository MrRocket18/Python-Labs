""" Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса. 
Допускается использовать любую графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter."""

from tkinter import *
from itertools import combinations
def find_max_fraction(numbers):
  max_fraction = (0, 1)
  max_value = 0
  for pair in combinations(numbers, 2):
    numerator, denominator = pair
    if numerator < denominator and numerator + denominator < 20:
      value = numerator / denominator
      if value > max_value:
        max_value = value
        max_fraction = (numerator, denominator)
  return max_fraction

def click_button_back(window2):
  window2.destroy()
  enter_window()

def enter_window():
  window = Tk()
  window.title("Окно ввода")
  window.geometry("900x400")
  window.resizable(width=False,height=False)

  frame = Frame (window,bg="light blue")
  frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

  Name_Text=Label(frame,text="Введите в нижнем поле числа, из которых хотите найти максимальныю правильную дробь, через запятую",font=("Time",13))
  Name_Text.place(x=1,y=1,width=888,height=50)

  numbers_for_fractions=Text(frame,font=("Time",30))
  numbers_for_fractions.place(x=100,y=70,width=700,height=200)
  

  enter=Button(frame,text="Ввести",foreground="white",font=("Time",20),bg="green", command=lambda: click_button_enter(window,numbers_for_fractions))
  enter.place(x=400,y=300,width=100,height=50)
  window.mainloop()

def click_button_enter(window,numbers_str):
  numbers =list(map(int,numbers_str.get("1.0","end-1c").split(",")))
  numerator, denominator=find_max_fraction(numbers)

  window.destroy()
  window2= Tk()
  window2.title("Окно вывода")
  window2.geometry("900x400")
  window2.resizable(width=False,height=False)

  frame = Frame (window2,bg="light blue")
  frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

  result_out = Canvas(frame,width=200,height=200)
  result_out.pack()
  result_out.create_text(100,50,text=numerator,font=("Time",50))
  result_out.create_text(100,60,text="_",font=("Time",50))
  result_out.create_text(100,140,text=denominator,font=("Time",50))
  back=Button(frame,text="Назад",foreground="white",font=("Time",20),bg="green", command=lambda: click_button_back(window2))
  back.place(x=100,y=300,width=100,height=50)

  exit=Button(frame,text="Выйти из программы",foreground="white",font=("Time",20),bg="red", command=lambda: window2.destroy())
  exit.place(x=500,y=300,width=300,height=50)
  
  window2.mainloop()

enter_window()
print("Программа завершила работу")