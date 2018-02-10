# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:37:30 2018

@author: Songshan
"""

# BACKEND TRIAL

from Tkinter import *
import sqlite3 #Import the SQLite3 module


def update():
    name = pic_field.get()
    try:
        print "Go into try"
        cur.execute("INSERT INTO main(pic_name) VALUES (?)", (name,))
        db.commit()
    except:
        cur.execute("UPDATE main SET walk=0,train=0,rest=0 WHERE pic_name = (?)", (name,))
        db.commit()

    # Take checkboxes input and inser into table one by one
    for act, num in btn_dic.iteritems(): # {'walk': num}
        if num.get() == 1:
            cur.execute("UPDATE main SET " + act + " = (?) WHERE pic_name = (?)", (1,name))
            db.commit()
            
    
    print 'Inserted ' + name
    
    
db = sqlite3.connect('activity.db')

cur = db.cursor()

master = Tk()
master.title("My APP")
master.geometry('400x200')


# Load data from activity table and return a dict
cur.execute("SELECT * FROM activity")
rows = cur.fetchall()

act_dic = {}
for row in rows: 
    act = row[1]
    num = "var" + str(row[0])
    act_dic[act] = num
#print "act_dic =",
#print act_dic


# GUI Part

pic_field = Entry(master, text="Pic Name")
pic_field.pack()

btn_dic={} # {'walk': num}
# Generate multiple buttons from act_dic
for act, num in act_dic.iteritems():
    num = IntVar()
    c= Checkbutton(master, text=act, variable=num)
    btn_dic[act] = num
    c.pack()

b = Button(master, text="Save", command=update)
b.pack()


mainloop()













