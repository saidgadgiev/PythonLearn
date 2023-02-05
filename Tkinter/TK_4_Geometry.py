# Метод Python Tkinter place()
# Менеджер place() упорядочивает виджеты по определенным координатам x и y.

# Синтаксис:

# widget.place(options)
# Список возможных вариантов приведен ниже:

# Anchor: он представляет собой точное положение виджета в контейнере. 
# Значение по умолчанию (direction) – NW (левый верхний угол).
# bordermode: значение по умолчанию для типа границы – INSIDE, что 
# означает игнорирование родительского элемента внутри границы. Другой вариант – OUTSIDE.
# height, width: это высота и ширина в пикселях.
# relheight, relwidth: представлен как число с плавающей запятой между 0,0 и 1,0, 
# указывающее долю высоты и ширины родительского элемента.
# relx, rely: представлен в виде числа с плавающей запятой между 0,0 и 1,0, которое 
# представляет собой смещение в горизонтальном и вертикальном направлениях.
# x, y: это относится к горизонтальному и вертикальному смещению в пикселях.

from tkinter import*
top = Tk()
top.geometry("300x250")
name = Label(top, text="Name").place(x=30, y=50)
email = Label(top, text="Email").place(x=30, y=90)
password = Label(top, text="Password").place(x=20, y=130)
e1 = Entry(top).place(x=80, y=50)
e2 = Entry(top).place(x=80, y=90)
e3 = Entry(top).place(x=80, y=130)
top.mainloop()