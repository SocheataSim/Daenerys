import tkinter as tk
import math

def calculate_area():
    try:
        radius = float(radius_entry.get())
        area = radius ** 2 * math.pi
        result_label.config(text=f"Area size: {area:.3f}")
    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Area Calculation")
root.geometry("300x100")

prompt_label = tk.Label(root, text="Enter Radius Value")
prompt_label.pack()

radius_entry = tk.Entry(root)
radius_entry.pack()

calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
