# Step 1: Import tkinter module
import tkinter as tk
from tkinter import messagebox

# Step 2: Create the main window (root window)
root = tk.Tk()

# Set window title and size
root.title("My First GUI")
root.geometry("300x200")

# Step 3: Add widgets
# Create a label widget
label = tk.Label(root, text="Hello, World!", font=("Helvetica", 16))
label.pack(pady=20)  # Add the label to the window

# Function for the button
def on_button_click():
    messagebox.showinfo("Button Clicked", "You clicked the button!")

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Step 4: Start the main event loop
root.mainloop()
