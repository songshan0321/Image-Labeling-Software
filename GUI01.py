# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 22:57:18 2018

@author: Windows 10
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 09:24:55 2018
@author: doanthanh
"""

from Tkinter import *
import Tkinter as tk
import ttk
from PIL import ImageTk, Image
import sqlite3 #Import the SQLite3 module


class Application:
    def __init__(self, master):
        
        db = sqlite3.connect('Labelling.db')
        cur = db.cursor()
        
        # Load data from activity table and return a list of label
        cur.execute("SELECT * FROM labels")
        rows = cur.fetchall()
        
        lbl_ls = []
        for row in rows: 
            lbl = row[1]
            lbl_ls.append(lbl)
        #print "lbl_ls =",
        #print lbl_ls
        
        #create regions for the main frame
        leftFrame = Frame(master, width=1000)
        leftFrame.grid(sticky=W, row=0, column=0, rowspan=500, columnspan=300)
        rightFrame = Frame(master)
        rightFrame.grid(sticky=E, row=0, column=301, rowspan=500)
        
        ToolBar = Frame(leftFrame, bg="grey", width=1000, height=900)
        ToolBar.grid(sticky=N, columnspan=300)
        
        ImageHolder = Frame(leftFrame, width=900, height=800)
        ImageHolder.grid(sticky=S)
        
        PrevNext = Frame(leftFrame)
        PrevNext.grid(sticky=S)
        
        TagLabels = ttk.Notebook(rightFrame)
        TagLabels.grid(sticky=N)
        
        
        
        #Toolbar, #insert your functions in command to for events
        self.openFile = Button(ToolBar, text="Open File", height=2, width=7, command=self.doNothing) 
        self.openFile.grid(sticky=W, row=1, rowspan=2, column=0, columnspan=3)
        
        
        self.saveImgs = Button(ToolBar, text="Save", height=2, width=7, command=self.update)
        self.saveImgs.grid(sticky=E, row=1, rowspan=2, column=7, columnspan=3)
        
        #ImgHolders
        
        #tempPhoto = PhotoImage(file="/Users/doanthanh/CodingProjects/LKYCIC Image Labeling/Dog1.png")
        #showPhoto = Label(ImageHolder, image=tempPhoto)
        #showPhoto.grid()
        imgHolder = Label(ImageHolder, text="View images here")
        imgHolder.grid(padx=100, pady=100)
        pic_field = Entry(ImageHolder, text="Image Name")
        pic_field.pack()
        
        #PrevNext 
        prev = Button(PrevNext, text="<", width=4)
        prev.grid(sticky=W, padx=20, row = 497, rowspan=2, column=10, columnspan=2)
        nxt= Button(PrevNext, text=">", width=4)
        nxt.grid(sticky=E, row = 497, rowspan=2, column=18, columnspan=2)
        
        #TagLabels
        generalTab = ttk.Frame(TagLabels)
        envTab =  ttk.Frame(TagLabels)
        activityTab =  ttk.Frame(TagLabels)
        thingTab =  ttk.Frame(TagLabels)
        addTab = ttk.Frame(TagLabels)
        
        TagLabels.add(generalTab, text="General")
        TagLabels.add(envTab, text="Location")
        TagLabels.add(activityTab, text="Activity")
        TagLabels.add(thingTab, text="Things")
        TagLabels.add(addTab, text="+")
        
        btn_ls=[]
        #General Tab
        
        # Generate multiple buttons from lbl_ls
        for label in lbl_ls[0:2]:
            num = IntVar()
            c= Checkbutton(generalTab, text=label, variable=num)
            c.grid(sticky=W)
            btn_ls.append((label,num))
        
        #Locations tab
        
        for label in lbl_ls[2:12]:
            num = IntVar()
            c= Checkbutton(envTab, text=label, variable=num)
            c.grid(sticky=W)
            btn_ls.append((label,num))
        
        #activity tab
        
        for label in lbl_ls[12:20]:
            num = IntVar()
            c= Checkbutton(activityTab, text=label, variable=num)
            c.grid(sticky=W)
            btn_ls.append((label,num))
        
    def doNothing(self):
        print("Huat Ah!")
        
    def update(self):
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
        
        

root = tk.Tk()
app = Application(root)
root.title("Image Labeling Software")
root.mainloop()