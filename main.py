from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("DPI Calculator")
root.geometry("600x400")
root.config(bg="gray")
label = Label(root, text="E-DPI Calculator", font="30", fg="white", bg="gray")
label.pack(padx=5, pady=5)

current_function = None
def first_chose():
    clear_widgets()
    val_text = Label(root, text="Your valorant sens", font=20, bg="gray")
    val_text.pack(padx=5, pady=5)
    val_sens = Entry(root, width=20)
    val_sens.pack(padx=5, pady=5)

    dpi_text = Label(root, text="Your dpi", font=20, bg="gray")
    dpi_text.pack(padx=5, pady=5)
    your_dpi = Entry(root, width=20)
    your_dpi.pack(padx=5, pady=5)

    root.bind('<KeyRelease>', lambda event=None: calculate(val_sens, your_dpi))

    text = Label(root, text="Your eDPI: ", font=18, bg="gray")
    text.pack()
    result = Label(root, text="", font=20, bg="gray")
    result.pack()
    reset_button = Button(root, text="Go back", command=reset)
    reset_button.pack()

    def calculate(sens_entry, dpi_entry):
        sens_num = float(sens_entry.get())
        dpi_num = int(dpi_entry.get())
        result.config(text=round((sens_num * dpi_num), 1))


def second_chose():
    clear_widgets()

    selected_option = None
    second_selected_option = None

    def on_select(e):
        nonlocal selected_option, second_selected_option
        selected_option = combo_var.get()
        second_selected_option = combo_varSecond.get()

    def keyHandler(e):
        nonlocal selected_option, second_selected_option
        key = (selected_option, second_selected_option)
        if key in conversion_functions:
            conversion_functions[key]()


    def cs_convert():
        cs_num = 3.18
        sens_num = float(your_sens.get())
        # dpi_num = int(your_dpi.get())
        cs_sens = cs_num * sens_num
        result.config(text=round((cs_sens), 3))

    def cs_reserve_convert():
        cs_num = 3.18
        sens_num = float(your_sens.get())
        cs_sens = sens_num / cs_num
        result.config(text=round((cs_sens), 3))

    def fort_convert():
        fort_num = 12.6
        sens_num = float(your_sens.get())
        fort_sens = sens_num * fort_num
        result.config(text=round((fort_sens), 3))

    def fort_reserve_convert():
        fort_num = 12.6
        sens_num = float(your_sens.get())
        fort_sens = sens_num / fort_num
        result.config(text=round((fort_sens), 3))

    def fort_to_cs():
        fort_num = 3.96
        sens_num = float(your_sens.get())
        cs_sens = sens_num / fort_num
        result.config(text=round((cs_sens), 3))

    def cs_to_fort():
        cs_num = 3.96
        sens_num = float(your_sens.get())
        fort_sens = sens_num * cs_num
        result.config(text=round((fort_sens), 3))

    conversion_functions = {
        ("Valorant", "CS-GO"): cs_convert,
        ("Valorant", "Fortnite"): fort_convert,
        ("CS-GO", "Valorant"): cs_reserve_convert,
        ("Fortnite", "Valorant"): fort_reserve_convert,
        ("CS-GO", "Fortnite"): cs_to_fort,
        ("Fortnite", "CS-GO"): fort_to_cs
    }

    #option menu
    from_text = Label(root, text="Convert from: ", bg="grey")
    combo_var = tk.StringVar()
    combo = ttk.Combobox(root, textvariable=combo_var)
    combo['values'] = ('Valorant', 'CS-GO', 'Fortnite')
    from_text.pack()
    combo.pack()

    to_text = Label(root, text="Convert to: ", bg="grey")
    combo_varSecond = tk.StringVar()
    comboSecond = ttk.Combobox(root, textvariable=combo_varSecond)
    comboSecond['values'] = ('Valorant', 'CS-GO', 'Fortnite')
    to_text.pack()
    comboSecond.pack()

    combo.bind('<<ComboboxSelected>>', on_select)
    comboSecond.bind('<<ComboboxSelected>>', on_select)
    sens_text = Label(root, text="Your sens", bg="grey")
    your_sens = Entry(root, width=20)

    # dpi_text = Label(root, text="Your DPI", bg="grey")
    # your_dpi = Entry(root, width=20)

    # change_sensText = Label(root, text="To sens", bg="grey")
    # change_sens = Entry(root, width=20)

    sens_text.pack()
    your_sens.pack()
    # dpi_text.pack()
    # your_dpi.pack()

    root.bind('<KeyRelease>', keyHandler)

    result = Label(root, text="", bg="grey")
    result.pack()
    reset_button = Button(root, text="Go back", command=reset)
    reset_button.pack()
def reset():
    clear_widgets()
    first_button = Button(root, text="eDPI Calculator", command=first_chose)
    first_button.pack()

    second_button = Button(root, text="Convert your sens", command=second_chose)
    second_button.pack()
def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

first_button = Button(root, text="eDPI Calculator", command=first_chose)
first_button.pack()

second_button = Button(root, text="Convert your sens", command=second_chose)
second_button.pack()

root.mainloop()
