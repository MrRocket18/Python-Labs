""" Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса. 
Допускается использовать любую графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter."""
from tkinter import *
from tkinter import messagebox
from itertools import combinations
def find_max_fraction(fractions):
  max_fraction = (0, 1)
  max_value = 0
  for fraction in fractions:
    if  fraction[0] + fraction[1] < 40:
      value = fraction[0] / fraction[1]
      if value > max_value:
        max_value = value
        max_fraction = (fraction[0], fraction[1])
  return max_fraction
def find_fractions(mas,window):
  if len(mas)==0:
    messagebox.showwarning('Ошибка!', 'Вы ничего не ввели! Попробуйте снова')
    window.destroy()
    enter_window()
  fractions=[]
  for numerator, denominator in combinations(mas,2):
    if numerator < denominator:
      fractions.append((numerator,denominator))
  return fractions

def display_fractions(fractions,out_text_fractions):
    result_text = " ".join([f"{fraction[0]}/{fraction[1]}," for fraction in fractions])  
    out_text_fractions.delete("1.0", END)
    out_text_fractions.insert(END, result_text)

def click_button_back(window2):
  window2.destroy()
  enter_window()

def center_window(window,width,height):
  window.update_idletasks()
  screen_width = window.winfo_screenwidth()
  screen_height = window.winfo_screenheight()
  x = (screen_width - width) // 2
  y = (screen_height - height) // 2
  window.geometry(f"{width}x{height}+{x}+{y}")

def enter_window():
  window = Tk()
  window.title("Окно ввода")
  center_window(window,900,400)
  window.resizable(width=False,height=False)

  frame = Frame (window,bg="gray")
  frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

  Name_Text=Label(frame,text="Введите в нижнем поле числа, из которых хотите найти максимальныю правильную дробь, через пробел",font=("Time",13))
  Name_Text.place(x=1,y=1,width=888,height=50)

  numbers_for_fractions=Text(frame,font=("Time",30))
  numbers_for_fractions.place(x=100,y=70,width=700,height=200)
  
  enter=Button(frame,text="Ввести",foreground="white",font=("Time",20),bg="green", command=lambda: click_button_enter(window,numbers_for_fractions))
  enter.place(x=400,y=300,width=100,height=50)
  window.mainloop()

def click_button_enter(window,numbers_str):
  if numbers_str=="":
    messagebox.showwarning('Ошибка!', 'Вы ничего не ввели! Попробуйте снова')
    window.destroy()
    enter_window()
  try:
    numbers =list(map(int,numbers_str.get("1.0","end-1c").split()))
  except (UnboundLocalError,ValueError):
    print(f"Ошибка ! Проверьте введенные данные и попробуйтьте снова.")
    messagebox.showwarning('Ошибка!', 'Ошибка! Проверьте введенные данные и попробуйтьте снова.')
  true_fractions = find_fractions(numbers,window)
  numerator, denominator=find_max_fraction(true_fractions)

  window.destroy()
  window2= Tk()
  window2.title("Окно вывода")
  center_window(window2,900,900)
  window2.resizable(width=False,height=False)

  frame = Frame (window2,bg="gray")
  frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

  max_fraction_text=Label(frame,text="Максимальная правильная дробь, учитывая условия",font=("Time",20))
  max_fraction_text.place(x=100,y=2,width=700,height=50)

  result_out = Canvas(frame)
  result_out.place(x=350,y=70, width=200,height=200)
  result_out.create_text(100,50,text=numerator,font=("Time",50))
  result_out.create_text(100,60,text="_",font=("Time",50))
  result_out.create_text(100,140,text=denominator,font=("Time",50))
  back=Button(frame,text="Назад",foreground="white",font=("Time",20),bg="green", command=lambda: click_button_back(window2))
  back.place(x=100,y=800,width=100,height=50)

  fractions_text=Label(frame,text="Правильные дроби, которые можно составить из введеных чисел",font=("Time",20))
  fractions_text.place(x=25,y=290,width=850,height=50)

  result_out_fractions = Text(frame,wrap=WORD,font=("Time",20))
  result_out_fractions.place(x=100,y=350,width=700,height=400)
  scrollbar = Scrollbar(result_out_fractions, command=result_out_fractions.yview)
  scrollbar.pack(side=RIGHT, fill="y")
  result_out_fractions.config(yscrollcommand=scrollbar.set)
  display_fractions(true_fractions,result_out_fractions)

  exit=Button(frame,text="Выйти из программы",foreground="white",font=("Time",20),bg="red", command=lambda: window2.destroy())
  exit.place(x=500,y=800,width=300,height=50)
  
  window2.mainloop()

enter_window()
print("Программа завершила работу")