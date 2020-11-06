# Import tkinter module for creating gui
import tkinter as tk

# creating the actual window
window = tk.Tk()

# Create grid for everything

window.columnconfigure([0, 1, 2, 3, 4, 5], minsize=150)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=50)

"""CM and Degree/Updates to each"""

# creating entry widgets and headers for cm and degrees
cm_label = tk.Label(text="Centimetres (20 - 500)")
cm_entry = tk.Entry()

degree_label = tk.Label(text="Degrees (1 - 360)")
degree_entry = tk.Entry()

cm_label.grid(row=0, column=0, sticky="w")
cm_entry.grid(row=1, column=0, sticky="n")
degree_label.grid(row=0, column=2)
degree_entry.grid(row=1, column=2, sticky="n")

# Create update buttons for the entry values of cm and degree (2 separate ones to look cleaner next to entries)
update1 = tk.Button(
    text="✓",
    width=1,
    height=1,
)

update2 = tk.Button(
    text="✓",
    width=1,
    height=1,
)
update1.grid(row=0, column=0, sticky="e")
update2.grid(row=0, column=2, sticky="e")


# Define the function to get the entry values when clicking the update button
# if cm is out of range, if statements are setup to push it back into the range
def entry(event):
    cm = cm_entry.get()
    degree = degree_entry.get()
    cm = float(cm)
    if cm < 20:
        cm = 20
        cm_entry.delete(0, tk.END)
        cm_entry.insert(0, cm)
    elif cm > 500:
        cm = 500
        cm_entry.delete(0, tk.END)
        cm_entry.insert(0, cm)
    degree = float(degree)
    if degree < 1:
        degree = 1
        degree_entry.delete(0, tk.END)
        degree_entry.insert(0, degree)
    elif degree > 360:
        degree = 360
        degree_entry.delete(0, tk.END)
        degree_entry.insert(0, degree)

    print(cm)
    print(degree)


# set button Presses for both entries
update1.bind("<Button-1>", entry)
update2.bind("<Button-1>", entry)

""" Start of Engine related """
# Create a take off button
takeoff = tk.Button(
    text="Take Off",
    width=10,
    height=2,
    bg="cyan",
)
takeoff.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

# Create a land button
land = tk.Button(
    text="Land",
    width=10,
    height=2,
    bg="#D2691E",
)
land.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

# Create a Cut Engine button button
cut_engine = tk.Button(
    text="PANIC",
    width=10,
    height=2,
    bg="red",
    fg="white"
)
cut_engine.grid(row=5, column=0, sticky="nsew", padx=2, pady=2)


# Define event handling for each button when clicked (Temporary Print to console for testing)
def button_takeoff(event):
    print("Take Off initiated")


takeoff.bind("<Button-1>", button_takeoff)


def button_land(event):
    print("Landing Initiated")


land.bind("<Button-1>", button_land)


def button_cut_engine(event):
    print("EMERGENCY! ENGINE HAS BEEN CUT")


cut_engine.bind("<Button-1>", button_cut_engine)

"""Start of Directional"""

# Create rotational buttons

button_rotate_cw = tk.Button(
    text="⟳",
    width=3,
    height=2
)
button_rotate_cw.grid(row=3, column=4, sticky="nesw", padx=2, pady=2)


def rotate_cw(event):
    print("Rotate clockwise")


button_rotate_cw.bind("<Button-1>", rotate_cw)

button_rotate_ccw = tk.Button(
    text="⟲",
    width=3,
    height=2
)
button_rotate_ccw.grid(row=3, column=2, sticky="nesw", padx=2, pady=2)


def rotate_ccw(event):
    print("Rotate counter-clockwise")


button_rotate_ccw.bind("<Button-1>", rotate_ccw)

# Create directional buttons
button_forward = tk.Button(
    text="⮉",
    width=3,
    height=2,
)
button_forward.grid(row=4, column=3, sticky="nesw", padx=2, pady=2)


def forward(event):
    print("move forward")


button_forward.bind("<Button-1>", forward)

button_back = tk.Button(
    text="⮋",
    width=3,
    height=2,
)
button_back.grid(row=5, column=3, sticky="nesw", padx=2, pady=2)


def back(event):
    print("move backward")


button_back.bind("<Button-1>", back)

button_up = tk.Button(
    text="🢁",
    width=3,
    height=2,
)
button_up.grid(row=3, column=3, sticky="nesw", padx=2, pady=2)


def up(event):
	print("move up")


button_up.bind("<Button-1>", up)

button_left = tk.Button(
    text="🢀",
    width=3,
    height=2,
)
button_left.grid(row=4, column=2, sticky="nesw", padx=2, pady=2)


def left(event):
    print("move left")


button_left.bind("<Button-1>", left)

button_right = tk.Button(
    text="🢂",
    width=3,
    height=2,
)
button_right.grid(row=4, column=4, sticky="nesw", padx=2, pady=2)


def right(event):
    print("move right")


button_right.bind("<Button-1>", right)

button_down = tk.Button(
    text="🢃",
    width=3,
    height=2,
)
button_down.grid(row=6, column=3, sticky="nesw", padx=2, pady=2)


def down(event):
    print("move down")


button_down.bind("<Button-1>", down)

# Running a loop of our window which will continuously look for inputs to execute until window is exited
window.mainloop()
