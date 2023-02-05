from tkinter import * #Импортируем нашу библиотеку


parent = Tk() #создаем окно, которое будет родительским для наших элементов
redbutton = Button(parent, text = "Red", fg = "red") #Создаем 1 кнопку и параметром (parent) привязываем её к родительскому окну
redbutton.pack( side = LEFT) #Устанавливаем расположение кнопки отностительно центра окна
bluebutton = Button(parent, text = "Blue", fg = "blue") #Параметром (text) указываем текст, который будет написан на кнопке
bluebutton.pack( side = RIGHT ) 
greenbutton = Button(parent, text = "Green", fg = "green") #параметром (fg) устанавливаем цвет текста
greenbutton.pack( side = TOP) 
parent.mainloop() #и зацикливаем наше окно, чтобы оно не закрывалось само