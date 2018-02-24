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


class Application:
    def __init__(self, master):
        
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
        
        
        self.saveImgs = Button(ToolBar, text="Save", height=2, width=7, command=self.doNothing)
        self.saveImgs.grid(sticky=E, row=1, rowspan=2, column=7, columnspan=3)
        
        #ImgHolders
        
        #tempPhoto = PhotoImage(file="/Users/doanthanh/CodingProjects/LKYCIC Image Labeling/Dog1.png")
        #showPhoto = Label(ImageHolder, image=tempPhoto)
        #showPhoto.grid()
        imgHolder = Label(ImageHolder, text="View images here")
        imgHolder.grid(padx=100, pady=100)
        
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
        
        #General Tab
        person = Checkbutton(generalTab, text="Person")
        person.grid(sticky=W)
        useless = Checkbutton(generalTab, text="Not useful")
        useless.grid(sticky=W)
        
        #Locations tab
        home = Checkbutton(envTab, text="House")
        park = Checkbutton(envTab, text="Park")
        market = Checkbutton(envTab, text="Supermarket/Wet market")
        foodstore = Checkbutton(envTab, text="Food center/Coffeeshop")
        hospital = Checkbutton(envTab, text="Hospital")
        common = Checkbutton(envTab, text="Playground/Void Deck")
        religion = Checkbutton(envTab, text="Religious Venue")
        road = Checkbutton(envTab, text="On Road/Street")
        busstop = Checkbutton(envTab, text="Bus Stop")
        mrtstation = Checkbutton(envTab, text="MRT station")
        
        home.grid(sticky=W)
        park.grid(sticky=W)
        market.grid(sticky=W)
        foodstore.grid(sticky=W)
        hospital.grid(sticky=W)
        common.grid(sticky=W)
        religion.grid(sticky=W)
        road.grid(sticky=W)
        busstop.grid(sticky=W)
        mrtstation.grid(sticky=W)
        
        #activity
        
        walk = Checkbutton(activityTab, text="Walking")
        cycle = Checkbutton(activityTab, text="Cycling")
        sit = Checkbutton(activityTab, text="Sitting")
        talk = Checkbutton(activityTab, text="Chatting")
        eat = Checkbutton(activityTab, text="Eating")
        shop = Checkbutton(activityTab, text="Shopping")
        rest = Checkbutton(activityTab, text="Resting")
        others = Checkbutton(activityTab, text="Others")
        
        walk.grid(sticky=W)
        cycle.grid(sticky=W)
        sit.grid(sticky=W)
        talk.grid(sticky=W)
        eat.grid(sticky=W)
        shop.grid(sticky=W)
        rest.grid(sticky=W)
        others.grid(sticky=W)
        
    def doNothing(self):
        print("Huat Ah!")
        
        

root = tk.Tk()
app = Application(root)
root.title("Image Labeling Software")
root.mainloop()