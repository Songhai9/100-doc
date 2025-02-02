import tkinter as tk

window = tk.Tk()
window.title('Distance converter')

def calculate():
    km_result.config(text=f'{float(miles_input.get()) * 1.60934}')

miles_input = tk.Entry()
miles_label = tk.Label(text='Miles')
is_equal_label = tk.Label(text='is equal to')
km_result = tk.Label(text='0')
km_label = tk.Label(text='Km')
calculate_btn = tk.Button(text='Calculate', command=calculate)

miles_input.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
is_equal_label.grid(row=1, column=0)
km_result.grid(row=1, column=1)
km_label.grid(row=1, column=2)
calculate_btn.grid(row=2, column=1)



window.mainloop()