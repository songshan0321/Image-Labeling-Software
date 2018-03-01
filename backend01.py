# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 23:15:28 2018

@author: Windows 10
"""
from Tkinter import *
import sqlite3 #Import the SQLite3 module

    

def load_data():
    # Load data from activity table and return a list of label
    cur.execute("SELECT * FROM labels")
    rows = cur.fetchall()
    
    global lbl_ls
    lbl_ls = []
    for row in rows: 
        lbl = row[1]
        lbl_ls.append(lbl)
    #print "lbl_ls =",
    #print lbl_ls

def get_pic_list(n):
    pic_ls=[]
    for x in range(1,n+1):
        pic = "pic_field{0}".format(x)
        pic_ls.append(pic)
    return pic_ls
    print pic_ls


def import_GUI():
    global pic_field1
    global pic_field2
    pic_field1 = Entry(master, text="name1")
    pic_field1.pack()
    pic_field2 = Entry(master, text="name2")
    pic_field2.pack()
    
    global btn_ls
    btn_ls=[] # [('walk': num)]
    # Generate multiple buttons from lbl_ls
    for label in lbl_ls:
        num = IntVar()
        c= Checkbutton(master, text=label, variable=num)
        c.pack()
        btn_ls.append((label,num))
        
    #print "btn_ls =",
    #print btn_ls
    
    b = Button(master, text="Update", command=update)
    b.pack()
    
def update():
    global name_ls
    name_ls = []
    if pic_field1.get() != '':
        name_ls.append(pic_field1.get())
    else:
        print "Error! There is no image selected."
        
    if pic_field2.get() != '':
        name_ls.append(pic_field2.get())
    #print name_ls

    # Take checkboxes input and insert into data_ls
    data_ls=[]
    for btn in btn_ls:
        label = btn[0]
        Int = btn[1]
        if Int.get() == 1:
            data_ls.append((label,1))
        else:
            data_ls.append((label,0))     
    #print data_ls
            
    try:
        cur.execute("INSERT INTO result(image) VALUES (?)", (name_ls[0],))
        db.commit()
    except:
        cur.execute("UPDATE result SET date = NULL, person = 0, not_useful = 0, house = 0, park = 0, market = 0, food_center = 0, hospital = 0, playground = 0, religous = 0, road = 0, bus_stop = 0, mrt = 0, walk = 0, cycle = 0, sit = 0, chat = 0, eat = 0, shopping = 0, rest = 0, other_activity = 0 WHERE image = (?)", (name_ls[0],))
        db.commit()
            
    insert_row_data(data_ls,0)
            
    # Check if more than 1 picture being chosen
    if len(name_ls) >= 2:        
        for j in range(1,len(name_ls)):
            try:
                cur.execute("INSERT INTO result(image) VALUES (?)", (name_ls[j],))
                db.commit()
            except:
                cur.execute("UPDATE result SET date = NULL, person = 0, not_useful = 0, house = 0, park = 0, market = 0, food_center = 0, hospital = 0, playground = 0, religous = 0, road = 0, bus_stop = 0, mrt = 0, walk = 0, cycle = 0, sit = 0, chat = 0, eat = 0, shopping = 0, rest = 0, other_activity = 0 WHERE image = (?)", (name_ls[j],))
                db.commit()
                
            insert_row_data(data_ls,j)
        
            
    print 'Inserted ' + str(name_ls)

def insert_row_data(ls,n):
    # get data from data_ls and insert into SQL table
    for data in ls:
        label = data[0]
        k = data[1] # k is a boolean
        if k == 1:
            cur.execute("UPDATE result SET " + label + " = (?) WHERE image = (?)", (1,name_ls[n],))
            db.commit()
            
            
db = sqlite3.connect('Labelling.db')
cur = db.cursor()

# Create GUI
master = Tk()
master.title("My APP")
master.geometry('600x600')
    
load_data()
import_GUI()


mainloop()