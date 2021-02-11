from tkinter import*
from random import*

def open_shop():
    global boost, points
    
    shop = Tk()
    shop.geometry('700x600')
    shop.title('Ultimate clicker shop')
    shop.config(bg='white')
    
    double_lfrm = LabelFrame(shop, text='2x boost')
    double_lfrm.place(relx=0.4, relwidth=0.2)
    
    double_lbl = Label(double_lfrm, text='cost: 100P', bg='black')
    double_lfrm.pack()
    
def click():
    global clicks, colors, points, boost
    rand_color = choice(colors)
    main_btn.config(bg=rand_color, activebackground=rand_color)
    clicks += 1
    points += boost * 1
    allclicks_lbl.config(text='You clicked '+str(clicks)+' times.')
    point_lbl.config(text='You have '+str(clicks)+' points.')
    

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

points = 0
boost = 1
point_lbl = Label(text='You have '+str(points)+' points.', bg='white')
point_lbl.place(relx=0.29, rely=0.25, relwidth=0.4, relheight=0.05)

shop_btn = Button(text='shop', command=open_shop)
shop_btn.place(relx=0.001, rely=0.001, relwidth=0.2, relheight=0.09)

root.mainloop()