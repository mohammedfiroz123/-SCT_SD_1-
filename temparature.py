import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        
        if from_unit == to_unit:
            result = temp
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (temp * 9/5) + 32
            elif to_unit == "Kelvin":
                result = temp + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (temp - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (temp - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = temp - 273.15
            elif to_unit == "Fahrenheit":
                result = (temp - 273.15) * 9/5 + 32
                
        label_result.config(text=f"Converted: {result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid temperature.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x250")

# Create the input fields and labels
label_temp = tk.Label(root, text="Enter Temperature:")
label_temp.pack(pady=10)

entry_temp = tk.Entry(root, width=10)
entry_temp.pack(pady=5)

label_from = tk.Label(root, text="From:")
label_from.pack(pady=5)

combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_from.current(0)
combo_from.pack(pady=5)

label_to = tk.Label(root, text="To:")
label_to.pack(pady=5)

combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_to.current(1)
combo_to.pack(pady=5)

# Create the Convert button
button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=10)

# Label to display the result
label_result = tk.Label(root, text="Converted: ")
label_result.pack(pady=10)

# Run the main loop
root.mainloop()
