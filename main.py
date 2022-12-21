from tkinter import *
from tkinter import ttk


root = Tk()
root.title('The Weeknd- Album Database')
root.geometry("500x500")

# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color

style.map('Treeview',
#Python list with tuple inside. 
	background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Album Release Year", "Album Name", "Number of Songs", "Sales", "Release year Ranking")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Album Release Year", anchor=W, width=150)
my_tree.column("Album Name", anchor=W, width=140)
my_tree.column("Number of Songs", anchor=CENTER, width=140)
my_tree.column("Sales", anchor=CENTER, width=140)
my_tree.column("Release year Ranking", anchor=CENTER, width=170)




# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Album Release Year", text="Album Release Year", anchor=W)
my_tree.heading("Album Name", text="Album Name", anchor=W)
my_tree.heading("Number of Songs", text="Number of Songs", anchor=CENTER)
my_tree.heading("Sales", text="Sales", anchor=CENTER)
my_tree.heading("Release year Ranking", text="Release year Ranking", anchor=CENTER)



# Add Fake Data
data = [
	["John", "Elder", 1, "123 Elder St.", "Las Vegas"],
	["Mary", "Smith", 2, "435 West Lookout", "Chicago"],
	["Tim", "Tanaka", 3, "246 Main St.", "New York"]
	
]

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightgreen")

# Add our data to the screen
global count
count = 0


for record in data:
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]),tags=('oddrow',))
	# increment counter
	count += 1


# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label = Label(data_frame, text="Album Release Year")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Album Name")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="Number of Songs")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = Label(data_frame, text="Sales")
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = Label(data_frame, text="Release year Ranking")
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)

state_label = Label(data_frame, text="Album Release Year")
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)




# Add Command Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record")
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records")
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected")
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected")
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up")
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down")
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Select Record")
select_record_button.grid(row=0, column=7, padx=10, pady=10)





root.mainloop()
