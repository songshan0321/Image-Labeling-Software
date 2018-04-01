# coding=utf-8
import os
import tkFileDialog
import Tkinter as Tk
import ttk
from PIL import Image, ImageTk
import sqlite3 	#Import the SQLite3 module

class MainApplication(Tk.Tk):
	image = photo = []

	def __init__(self):
		Tk.Tk.__init__(self)
		self.path = Tk.StringVar()

		self.cb_ls = []	# checkbox list: [(<Tkinter.Checkbutton instance>,<Tkinter.IntVar instance>),......]
		self.cb_data_ls = []	# checkbox data list: [(<Tkinter.Checkbutton instance>,1),......]
		self.file_ls = []	# image list: [(<Tkinter.Checkbutton instance>,<Tkinter.IntVar instance>),......]
		self.file_chosen_ls = []	# image data list: [<Tkinter.Checkbutton instance>,......]
		self.lbl_dict={"Person":"person",
						"Home":"home",
						"Playground/Fitness corner (outdoor)":"playground",
						"Void deck":"void_deck",
						"Park":"park",
						"Open public space":"public_space",
						"Supermarket":"supermarket",
						"Dry/wet market":"market",
						"Restaurant/Food court/Coffee shop/Hawker center":"food_court",
						"Shop":"shop",
						"Mall/Shopping center":"mall",
						"Hospital":"hospital",
						"Polyclinic/Pharmacy":"clinic",
						"Community center/club":"community_center",
						"Senior activity/Daycare center":"senior",
						"Religious venue":"religious",
						"Transaction services (e.g. bank, post office)":"transaction_ser",
						"Indoor fitness facility (e.g. sports hall, gym, swimming pool)":"fitness",
						"Bus Stop/Interchange":"bus_stop",
						"MRT/LRT station":"mrt",
						"Covered walkway":"walkway",
						"Pedestrian crossing":"pedestrian_crossing",
						"Cycling path (seperated from footpath)":"cycling_path",
						"Street lights":"street_lights",
						"Traffic lights":"traffic_lights",
						"Street signs":"street_signs",
						"Trees/Grass":"trees",
						"Public furniture (e.g. benches, tables, places related to to sitting/resting)":"furniture",
						"Stairs and level changes":"stairs",
						"Ramps":"ramps",
						"Walking":"walk",
						"Cycling":"cycle",
						"On a bus":"bus",
						"On a train":"train",
						"On a car (as a passenger)":"car",
						"Driving a car/vehicle":"drive",
						"Sitting":"sit",
						"Chatting":"chat",
						"Eating":"eat",
						"Shopping":"shopping",
						"Running":"run",
						"Other exercising activity":"exercise",
						"Not Useful":"not_useful"}

		self.title("Photo Labelling Software")
		# self.geometry("1000x800")
		# self.master.attributes('-zoom', True)
		self.attributes('-fullscreen', True)
		self.grid_rowconfigure(1, weight = 1)
		self.grid_columnconfigure(0, weight = 1)

		# image_frame holds the images and is within left_frame
		self.left_frame = Tk.Frame(self.master)
		self.image_frame = Tk.Frame(self.master)
		self.left_frame.grid(row = 0, sticky = "ew")
		self.image_frame.grid(row = 1, sticky = "nsew")

		self.canvas = Tk.Canvas(self.image_frame)
		self.frame_in2 = Tk.Frame(self.canvas)
		self.my_scrollbar = Tk.Scrollbar(self.image_frame, orient = "vertical", command = self.canvas.yview)
		self.canvas.configure(yscrollcommand = self.my_scrollbar.set)
		self.my_scrollbar.pack(side = "right", fill = "y")
		self.canvas.pack(side = "left")

		self.canvas.create_window((0, 0), window = self.frame_in2, anchor = 'nw')

		self.frame_in2.bind("<Configure>", self.my_canvas)

		self.path_label = Tk.Label(self.left_frame, text = "  Path  :   ").grid(row = 0, column = 0)
		self.entry = Tk.Entry(self.left_frame, textvariable = self.path, width = 50).grid(row = 0, column = 1)
		self.b1 = Tk.Button(self.left_frame, text = "Select", command = self.open_photo).grid(row = 0, column = 2)
		self.b2 = Tk.Button(self.left_frame, text = "Update", command = self.update).grid(row = 0, column = 3)

		# right_frame is the frame that displays the tags
		self.right_frame = Tk.Frame(self.master)
		self.right_frame.grid(sticky= "ne", row = 1, column = 1)
		self.tag_labels = ttk.Notebook(self.right_frame)
		self.tag_labels.grid(sticky = "n")
		self.gen_tag_labels()



	def gen_tag_labels(self):
		general_tab = ttk.Frame(self.tag_labels)
		location_tab = ttk.Frame(self.tag_labels)
		activity_tab = ttk.Frame(self.tag_labels)
		others_tab = ttk.Frame(self.tag_labels)

		self.tag_labels.add(general_tab, text = "General")
		self.tag_labels.add(location_tab, text = "Location/Built Environment Features")
		self.tag_labels.add(activity_tab, text = "Activity")
		self.tag_labels.add(others_tab, text = "Others")

		# General Tab
		var = Tk.IntVar()
		person = Tk.Checkbutton(general_tab, text = "Person", variable = var)
		self.cb_ls.append((person,var))

		# Location Tab
		var = Tk.IntVar()
		home = Tk.Checkbutton(location_tab, text = "Home", variable = var)
		self.cb_ls.append((home,var))
		var = Tk.IntVar()
		playground = Tk.Checkbutton(location_tab, text = "Playground/Fitness corner (outdoor)", variable = var)
		self.cb_ls.append((playground,var))
		var = Tk.IntVar()
		voiddeck = Tk.Checkbutton(location_tab, text = "Void deck", variable = var)
		self.cb_ls.append((voiddeck,var))
		var = Tk.IntVar()
		park = Tk.Checkbutton(location_tab, text = "Park", variable = var)
		self.cb_ls.append((park,var))
		var = Tk.IntVar()
		publicspace = Tk.Checkbutton(location_tab, text = "Open public space", variable = var)
		self.cb_ls.append((publicspace,var))
		var = Tk.IntVar()
		supermarket = Tk.Checkbutton(location_tab, text = "Supermarket", variable = var)
		self.cb_ls.append((supermarket,var))
		var = Tk.IntVar()
		market = Tk.Checkbutton(location_tab, text = "Dry/wet market", variable = var)
		self.cb_ls.append((market,var))
		var = Tk.IntVar()
		foodplace = Tk.Checkbutton(location_tab, text = "Restaurant/Food court/Coffee shop/Hawker center", variable = var)
		self.cb_ls.append((foodplace,var))
		var = Tk.IntVar()
		shop = Tk.Checkbutton(location_tab, text = "Shop", variable = var)
		self.cb_ls.append((shop,var))
		var = Tk.IntVar()
		mall = Tk.Checkbutton(location_tab, text = "Mall/Shopping center", variable = var)
		self.cb_ls.append((mall,var))
		var = Tk.IntVar()
		hospital = Tk.Checkbutton(location_tab, text = "Hospital", variable = var)
		self.cb_ls.append((hospital,var))
		var = Tk.IntVar()
		clinic = Tk.Checkbutton(location_tab, text = "Polyclinic/Pharmacy", variable = var)
		self.cb_ls.append((clinic,var))
		var = Tk.IntVar()
		community = Tk.Checkbutton(location_tab, text = "Community center/club", variable = var)
		self.cb_ls.append((community,var))
		var = Tk.IntVar()
		seniorcenter = Tk.Checkbutton(location_tab, text = "Senior activity/Daycare center", variable = var)
		self.cb_ls.append((seniorcenter,var))
		var = Tk.IntVar()
		religion = Tk.Checkbutton(location_tab, text = "Religious venue", variable = var)
		self.cb_ls.append((religion,var))
		var = Tk.IntVar()
		services = Tk.Checkbutton(location_tab, text = "Transaction services (e.g. bank, post office)", variable = var)
		self.cb_ls.append((services,var))
		var = Tk.IntVar()
		indoors = Tk.Checkbutton(location_tab, text = "Indoor fitness facility (e.g. sports hall, gym, swimming pool)", variable = var)
		self.cb_ls.append((hospital,var))
		var = Tk.IntVar()
		bus_stop = Tk.Checkbutton(location_tab, text = "Bus Stop/Interchange", variable = var)
		self.cb_ls.append((bus_stop,var))
		var = Tk.IntVar()
		train_station = Tk.Checkbutton(location_tab, text = "MRT/LRT station", variable = var)
		self.cb_ls.append((train_station,var))
		var = Tk.IntVar()
		road = Tk.Checkbutton(location_tab, text = "Covered walkway", variable = var)
		self.cb_ls.append((road,var))
		var = Tk.IntVar()
		crossroad = Tk.Checkbutton(location_tab, text = "Pedestrian crossing", variable = var)
		self.cb_ls.append((crossroad,var))
		var = Tk.IntVar()
		cyclepath = Tk.Checkbutton(location_tab, text = "Cycling path (seperated from footpath)", variable = var)
		self.cb_ls.append((cyclepath,var))
		var = Tk.IntVar()
		streetlight = Tk.Checkbutton(location_tab, text = "Street lights", variable = var)
		self.cb_ls.append((streetlight,var))
		var = Tk.IntVar()
		trafficlight = Tk.Checkbutton(location_tab, text = "Traffic lights", variable = var)
		self.cb_ls.append((trafficlight,var))
		var = Tk.IntVar()
		streetsign = Tk.Checkbutton(location_tab, text = "Street signs", variable = var)
		self.cb_ls.append((streetsign,var))
		var = Tk.IntVar()
		trees = Tk.Checkbutton(location_tab, text = "Trees/Grass", variable = var)
		self.cb_ls.append((trees,var))
		var = Tk.IntVar()
		publicgoods = Tk.Checkbutton(location_tab, text = "Public furniture (e.g. benches, tables, places related to to sitting/resting)", variable = var)
		self.cb_ls.append((publicgoods,var))
		var = Tk.IntVar()
		stairs = Tk.Checkbutton(location_tab, text = "Stairs and level changes", variable = var)
		self.cb_ls.append((stairs,var))
		var = Tk.IntVar()
		ramps = Tk.Checkbutton(location_tab, text = "Ramps", variable = var)
		self.cb_ls.append((ramps,var))

		# Activity Tab
		var = Tk.IntVar()
		walk = Tk.Checkbutton(activity_tab, text = "Walking", variable = var)
		self.cb_ls.append((walk,var))
		var = Tk.IntVar()
		cycle = Tk.Checkbutton(activity_tab, text = "Cycling", variable = var)
		self.cb_ls.append((cycle,var))
		var = Tk.IntVar()
		on_bus = Tk.Checkbutton(activity_tab, text = "On a bus", variable = var)
		self.cb_ls.append((on_bus,var))
		var = Tk.IntVar()
		on_train = Tk.Checkbutton(activity_tab, text = "On a train", variable = var)
		self.cb_ls.append((on_train,var))
		var = Tk.IntVar()
		on_car = Tk.Checkbutton(activity_tab, text = "On a car (as a passenger)", variable = var)
		self.cb_ls.append((on_car,var))
		var = Tk.IntVar()
		drive = Tk.Checkbutton(activity_tab, text = "Driving a car/vehicle", variable = var)
		self.cb_ls.append((drive,var))
		var = Tk.IntVar()
		sit = Tk.Checkbutton(activity_tab, text = "Sitting", variable = var)
		self.cb_ls.append((sit,var))
		var = Tk.IntVar()
		talk = Tk.Checkbutton(activity_tab, text = "Chatting", variable = var)
		self.cb_ls.append((talk,var))
		var = Tk.IntVar()
		eat = Tk.Checkbutton(activity_tab, text = "Eating", variable = var)
		self.cb_ls.append((eat,var))
		var = Tk.IntVar()
		shop = Tk.Checkbutton(activity_tab, text = "Shopping", variable = var)
		self.cb_ls.append((shop,var))
		var = Tk.IntVar()
		run = Tk.Checkbutton(activity_tab, text = "Running", variable = var)
		self.cb_ls.append((run,var))
		var = Tk.IntVar()
		others = Tk.Checkbutton(activity_tab, text = "Other exercising activity", variable = var)
		self.cb_ls.append((others,var))

		#Others_tab
		var = Tk.IntVar()
		useless = Tk.Checkbutton(others_tab, text = "Not Useful", variable = var)
		self.cb_ls.append((useless,var))

		for cb in self.cb_ls:
			cb[0].grid(sticky = "w")

	def my_canvas(self, event):
		self.canvas.configure(scrollregion = self.canvas.bbox("all"), width = 1000, height = 700)

	def open_photo(self):
		path_ = tkFileDialog.askdirectory()
		self.path.set(path_)
		col = 1
		row = 1
		self.file_ls = []
		for file_name in os.listdir(self.path.get()):
			global image, photo
			if file_name.endswith(".jpg"):
				self.image.insert(0, Image.open(os.path.join(self.path.get(), file_name)).resize((300, 200), Image.ANTIALIAS))
				self.photo.insert(0, ImageTk.PhotoImage(self.image[0]))
				var = Tk.IntVar()
				if col == 1:
					c1 = Tk.Checkbutton(self.frame_in2, text = file_name, image = self.photo[0], compound = 'top',
					                    variable = var, onvalue = 1, offvalue = 0)
					c1.grid(row = row, column = 0, sticky = Tk.W)
					# c1.pack()
					col += 1
				elif col == 2:
					c1 = Tk.Checkbutton(self.frame_in2, text = file_name, image = self.photo[0], compound = 'top',
					                    variable = var, onvalue = 1, offvalue = 0)
					c1.grid(row = row, column = 1, sticky = Tk.W)
					# c1.pack()
					col += 1
				else:
					c1 = Tk.Checkbutton(self.frame_in2, text = file_name, image = self.photo[0], compound = 'top',
					                    variable = var, onvalue = 1, offvalue = 0)
					c1.grid(row = row, column = 2, sticky = Tk.W)
					# c1.pack()
					col -= 2
					row += 1
				self.file_ls.append((c1,var))

	def update(self):
		# Take file_ls input and insert into file_chosen_ls
		self.file_chosen_ls=[]
		for x in self.file_ls:
			f = x[0]
			var = x[1]
			if var.get() == 1:
				self.file_chosen_ls.append(f)
				f.configure(state="disabled")
		#print self.file_chosen_ls

		# Take cb_data input and insert into cb_data_ls
		self.cb_data_ls=[]
		for y in self.cb_ls:
			cb = y[0]
			var = y[1]
			if var.get() == 1:
				self.cb_data_ls.append((cb,1))
			else:
				self.cb_data_ls.append((cb,0))
		# print self.cb_data_ls

		# update data to database
		try: # if file not exist in database, add new row
			self.run_query("INSERT INTO attributes(file) VALUES (?)", (self.file_chosen_ls[0].cget("text"),))
		except: # if file exist in database, update it to all 0 first
			self.run_query("UPDATE attributes SET date=NULL,person=0,home=0,playground=0,void_deck=0,park=0,public_space=0,supermarket=0,market=0,food_court=0,shop=0,mall=0,hospital=0,clinic=0,community_center=0,senior=0,religious=0,transaction=0,fitness=0,bus_stop=0,mrt=0,walkway=0,pedestrian_crossing=0,cycling_path=0,street_lights=0,traffic_lights=0,street_signs=0,trees=0,furniture=0,stairs=0,ramps=0,walk=0,cycle=0,bus=0,train=0,car=0,drive=0,sit=0,chat=0,eat=0,shop=0,run=0,exercise=0,not_useful=0 WHERE file = (?)", (self.file_chosen_ls[0].cget("text"),))

		self.insert_row_data(self.cb_data_ls,0)

		# Run if more than 1 picture being chosen
		if len(self.file_chosen_ls) >= 2:
			for j in range(1,len(self.file_chosen_ls)):
				try: # if file not exist in database, add new row
					self.run_query("INSERT INTO attributes(file) VALUES (?)", (self.file_chosen_ls[j].cget("text"),))
				except: # if file exist in database, update it to all 0 first
					self.run_query("UPDATE attributes SET date=NULL,person=0,not_useful=0,home=0,park=0,supermarket=0,food_court=0,hospital=0,playground=0,place_of_worship=0,street=0,bus_stop=0,mrt_station=0,walking=0,cycling=0,sitting=0,chatting=0,eating=0,shopping=0,resting=0,others=0 = 0 WHERE file = (?)", (self.file_chosen_ls[j].cget("text"),))

				self.insert_row_data(self.cb_data_ls,j)

	def insert_row_data(self,ls,n):
		# get data from data_ls and insert into SQL table
		for data in ls:
			label = self.lbl_dict[data[0].cget("text")]
			k = data[1] # k is a boolean
			if k == 1:
				db = sqlite3.connect('D:\GitHub\Labeling-Backend\Application\lkydata.db')
				cur = db.cursor()
				query_result = cur.execute("UPDATE attributes SET " + label + " = (?) WHERE file = (?)", (1,self.file_chosen_ls[n].cget("text"),))
				db.commit()

	def run_query(self,query,parameters=()):
		with sqlite3.connect('D:\GitHub\Labeling-Backend\Application\lkydata.db') as db:
			cur = db.cursor()
			query_result = cur.execute(query,parameters)
			db.commit()
		return query_result

root = MainApplication()
root.mainloop()