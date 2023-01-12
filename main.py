#Name: Sophia Wojcik
#Date: January 11 2023
#The Weeknd's albums database 

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import colorchooser
from tabulate import tabulate
from PIL import ImageTk,Image



root = Tk()
root.title('The Weeknd- Album Database')
root.geometry("1000x500")



def primary_color():
  primary_color = colorchooser.askcolor()[1]

  #Update Treeview color
  if primary_color:
    # Pick color of striped rows
    my_tree.tag_configure('evenrow', background=primary_color)

def secondary_color ():
  secondary_color = colorchooser.askcolor()[1]

  #update Treeview color
  if secondary_color: 
    # Pick color of striped rows
    my_tree.tag_configure('oddrow', background=secondary_color)
    
def highlight_color ():
  highlight_color = colorchooser.askcolor()[1]

  #Update Treeview color
  if highlight_color: 
   # Change Selected Color Treeview
    style.map('Treeview', 
              background=[('selected', highlight_color)])

#Add Menu 
my_menu = Menu(root)
root.config(menu=my_menu)

#Configure Menu
option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=option_menu)

#Drop down Menu
option_menu.add_command(label="Primary Color",command=primary_color)
option_menu.add_command(label="Secondary Color",command=secondary_color)
option_menu.add_command(label="Highlight Color",command=highlight_color)

option_menu.add_command(label="Exit",command=root.quit)


# Insert data into database [year, album name, num of songs, sales, release year]
data = [
	["2011", "House of Balloons", 9, "100,000", 477],
	["2011", "Thursday",9 , "95,000", 192],
	["2011", "Echoes of Silence", 9, "95,000", 110],
  ["2012", "Trilogy", 30, "1 015,000", 40],
  ["2013", "Kiss Land", 12, "515,000", 86],
  ["2015", "Beauty Behind the Madness", 14, "2 315,000", 37 ],
  ["2016", "Starboy", 18, "1 440,000", 45],
  ["2018", "My Dear Melancholy", 6, "270,000", 397], 
  ["2020", "After Hours", 14, "1 005,000", 5],
  ["2022", "Dawn FM", 24, "285,000", 15]
  
]




#database
#create a database or connect to one that exists 
conn = sqlite3.connect ('Weeknd_Album.db')

#Create cursor instance: able to execute sqlite statements
cursor = conn.cursor ()

#Create a table 
cursor.execute("""CREATE TABLE if not exists albums ( 
  release_year integer, 
  album_name text,
  numof_songs integer, 
  sales integer, 
  releaseYear_ranking integer)
  """)

#add fake data into table 
for record in data: 
  cursor.execute ("INSERT INTO albums VALUES (:release_year, :album_name, :numof_songs, :sales, :releaseYear_ranking)",
#create a python dictionary:
             {
              'release_year': record[0],
              'album_name': record[1],
              'numof_songs': record[2],
              'sales': record[3],
              'releaseYear_ranking': record[4]
             }
            ) 


  
#Commit changes 
conn.commit()

#Close connection to database
conn.close ()


def query_database ():
#database
#create a database or connect to one that exists 
  conn = sqlite3.connect ('Weeknd_Album.db')

#Create cursor instance: able to execute sqlite statements
  cursor = conn.cursor ()

  #print database table
  cursor.execute ("SELECT * FROM albums")
  records = cursor.fetchall()
  
  print(tabulate(records, tablefmt = 'fancy_grid',headers= ["Album Release Year", "Album Name", "Number of Songs", "Sales", "Release Year Ranking"]))
  
  #Commit changes 
  conn.commit()

#Close connection to database
  conn.close ()


# Style format
style = ttk.Style()

# Table theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="white",
	foreground="black",
	rowheight=25,
	fieldbackground="#718194")

# Change Selected Color Treeview
style.map('Treeview',
#Python list with tuple inside. 
	background=[('selected', "347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define database Columns
my_tree['columns'] = ("Album Release Year", "Album Name", "Number of Songs", "Sales", "Release year Ranking")

# Format Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Album Release Year", anchor=W, width=150)
my_tree.column("Album Name", anchor=W, width=180)
my_tree.column("Number of Songs", anchor=CENTER, width=140)
my_tree.column("Sales", anchor=CENTER, width=140)
my_tree.column("Release year Ranking", anchor=CENTER, width=170)


# Create database headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Album Release Year", text="Album Release Year", anchor=W)
my_tree.heading("Album Name", text="Album Name", anchor=W)
my_tree.heading("Number of Songs", text="Number of Songs", anchor=CENTER)
my_tree.heading("Sales", text="Sales", anchor=CENTER)
my_tree.heading("Release year Ranking", text="Release year Ranking", anchor=CENTER)




# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="light green")

# Add our data to the screen
global count
count = 0

#Number of records inserted into database (even and odd)
for record in data:
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]),tags=('oddrow',))
	# increment counter
	count += 1

#Display album cover image when selecting a record 

  
img = Image.open("starboy.webp")
img = img.resize((100,100))

my = ImageTk.PhotoImage (img)
label = Label (image = my)
label.pack()







  
# Add Display Record Entry Boxes (after selecting a record)
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

#ary_label = Label(data_frame, text="Album Release Year")
#ary_label.grid(row=0, column=0, padx=10, pady=10)
#ary_entry = Entry(data_frame)
#ary_entry.grid(row=0, column=1, padx=10, pady=10)

#an_label = Label(data_frame, text="Album Name")
#an_label.grid(row=0, column=2, padx=10, pady=10)
#an_entry = Entry(data_frame)
#an_entry.grid(row=0, column=3, padx=10, pady=10)

#ns_label = Label(data_frame, text="Number of Songs")
#ns_label.grid(row=0, column=4, padx=10, pady=10)
#ns_entry = Entry(data_frame)
#ns_entry.grid(row=0, column=5, padx=10, pady=10)

#sales_label = Label(data_frame, text="Sales")
#sales_label.grid(row=1, column=0, padx=10, pady=10)
#sales_entry = Entry(data_frame)
#sales_entry.grid(row=1, column=1, padx=10, pady=10)

#ryr_label = Label(data_frame, text="Release year Ranking")
#ryr_label.grid(row=1, column=2, padx=10, pady=10)
#ryr_entry = Entry(data_frame)
#ryr_entry.grid(row=1, column=3, padx=10, pady=10)



# Add Command Buttons
#button_frame = LabelFrame(root, text="Commands")
#button_frame.pack(fill="x", expand="yes", padx=50)

#update_button = Button(button_frame, text="Update Record")
#update_button.grid(row=0, column=0, padx=10, pady=10)










query_database ()

root.mainloop()
