from tkinter import*
from random import*
    
def click():
    global clicks, colors
    rand_color = choice(colors)
    main_btn.config(bg=rand_color, activebackground=rand_color)
    clicks += 1
    allclicks_lbl.config(text='You clicked '+str(clicks)+' times.')    

root = Tk()
root.geometry('400x400')
root.title('Ultimate Clicker')
root.config(bg='white')

clicks = 0
colors = ['orange', 'yellow', 'purple', 'red', 'blue', 'pink']
rand_color = choice(colors)
main_btn = Button(text='Click me!', command=click, bg=rand_color, activebackground=rand_color)
main_btn.place(relx=0.27, rely=0.387, relheight=0.4, relwidth=0.452)

allclicks_lbl = Label(text='You clicked '+str(clicks)+' times.', bg='white')
allclicks_lbl.place(relx=0.29, rely=0.15, relheight=0.05, relwidth=0.4)

root.mainloop()