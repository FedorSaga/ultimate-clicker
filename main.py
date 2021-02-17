from tkinter import*
from random import*
import time

def buy(x):
    global boost, points, shop_points, point_lbl
    if x == 2:
        if points < 300:
            for i in range(7):
                shop_points.config(fg='red')
                time.sleep(0.2)
                shop_points.update()
                shop_points.config(fg='white')
                time.sleep(0.2)
                shop_points.update()
            
        else:
            points -= 300
            boost *= 2
            shop_points.update()
    shop_points.config(fg='black', text='You have '+str(points)+' points.')
    point_lbl.config(text='You have '+str(points)+' points.')

def open_shop():
    global boost, points, shop_points, shop_open
    
    shop = Tk()
    shop.geometry('400x400')
    shop.resizable(False, False)
    shop.title('Ultimate Clicker Shop')
    shop.config(bg='white')
    
    shop_points = Label(shop, text='You have '+str(points)+' points.', bg='white', fg='black')
    shop_points.place(anchor=NW)
    
    double_lfrm = LabelFrame(shop, text='2x boost', bg='white')
    double_lfrm.pack(pady=50)
    
    double_lbl = Label(double_lfrm, text='cost: 300P', bg='white')
    double_lbl.pack(pady=5, padx=5)
    
    double_btn = Button(double_lfrm, text='Buy', bg='white', command=lambda: buy(2))
    double_btn.pack(pady=5, padx=5)
    
    shop_open = True
    
def click():
    global clicks, colors, points, boost, shop_open
    rand_color = choice(colors)
    main_btn.config(bg=rand_color, activebackground=rand_color)
    clicks += 1
    points += boost * 1
    
    if shop_open == True:
        shop_points.config(fg='black', text='You have '+str(points)+' points.')
        
    allclicks_lbl.config(text='You clicked '+str(clicks)+' times.')
    point_lbl.config(text='You have '+str(points)+' points.')
    

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
point_lbl = Label(root, text='You have '+str(points)+' points.', bg='white')
point_lbl.place(relx=0.29, rely=0.25, relwidth=0.4, relheight=0.05)

shop_open = False
shop_btn = Button(text='shop', command=open_shop, bg='white', activebackground='#fcfcfc')
shop_btn.place(relx=0.001, rely=0.001, relwidth=0.2, relheight=0.09)

root.mainloop()