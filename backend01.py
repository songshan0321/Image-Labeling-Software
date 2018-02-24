# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 23:15:28 2018

@author: Windows 10
"""
from Tkinter import *
import sqlite3 #Import the SQLite3 module


def update():
    name = pic_field.get()
    
    try:
        print "Go into 'try'"
        cur.execute("INSERT INTO result(image) VALUES (?)", (name,))
        db.commit()
    except:
        cur.execute("UPDATE result SET date = NULL, person = 0, not_useful = 0, house = 0, park = 0, market = 0, food_center = 0, hospital = 0, playground = 0, religous = 0, road = 0, bus_stop = 0, mrt = 0, walk = 0, cycle = 0, sit = 0, chat = 0, eat = 0, shopping = 0, rest = 0, other_activity = 0 WHERE image = (?)", (name,))
        db.commit()

            
    # Take checkboxes input and insert into table one by one
    for lbl in btn_ls:
        label = lbl[0]
        num = lbl[1]
        if num.get() == 1:
            cur.execute("UPDATE result SET " + label + " = (?) WHERE image = (?)", (1,name))
            db.commit()
            
    
    print 'Inserted ' + name
    
db = sqlite3.connect('Labelling.db')
cur = db.cursor()

master = Tk()
master.title("My APP")
master.geometry('600x600')
    
# Load data from activity table and return a list of label
cur.execute("SELECT * FROM labels")
rows = cur.fetchall()

lbl_ls = []
for row in rows: 
    lbl = row[1]
    lbl_ls.append(lbl)
#print "lbl_ls =",
print lbl_ls

# GUI Part

pic_field = Entry(master, text="Image Name")
pic_field.pack()

btn_ls=[] # [('walk': num)]
# Generate multiple buttons from lbl_ls
for label in lbl_ls:
    num = IntVar()
    c= Checkbutton(master, text=label, variable=num)
    btn_ls.append((label,num))
    c.pack()
    
#print "btn_ls =",
print btn_ls

b = Button(master, text="Save", command=update)
b.pack()


mainloop()












