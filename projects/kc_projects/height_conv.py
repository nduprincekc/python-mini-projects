import tkinter
from tkinter import Tk,Label,DoubleVar,Entry

window = Tk()
window.configure(background= 'yellow')
#print(window)
#window.size = 34,1112
window.geometry('323x222') # setting the width and the height of the app
window.title('kc app') # title of the app
window.resizable(width=False, height=False)
ft_lbl = Label(window,text= 'okk', bg ='black', fg = 'white', width = 12)
ft_lbl.grid(column=111,row=10,padx=15)


window.mainloop()
