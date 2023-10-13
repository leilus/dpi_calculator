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
total_sens = 0


def first_chose():
    clear_widgets()

    dpi_text = Label(root, text="Your DPI", font=20, bg="gray")
    dpi_text.pack(padx=5, pady=5)
    your_dpi = Entry(root, width=20)
    your_dpi.pack(padx=5, pady=5)

    val_text = Label(root, text="Your Valorant sens", font=20, bg="gray")
    val_text.pack(padx=5, pady=5)
    val_sens = Entry(root, width=20)
    val_sens.pack(padx=5, pady=5)

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
    global total_sens
    clear_widgets()
    selected_option = None
    second_selected_option = None

    def on_select(e):
        nonlocal selected_option, second_selected_option
        selected_option = combo_var.get()
        second_selected_option = combo_varSecond.get()

    def keyHandler(e):
        if selected_option == second_selected_option:
            total_sens_conv = same_option()
        elif selected_option and second_selected_option:
            total_sens_conv = conversion_functions.get((selected_option, second_selected_option), lambda: 1)()
        result.config(text=total_sens_conv)

    def same_option():
        sens_num = float(your_sens.get())
        return round((sens_num), 3)
    def cs_convert():
        cs_num = 3.18
        sens_num = float(your_sens.get())
        return round((cs_num * sens_num), 3)

    def cs_reserve_convert():
        cs_num = 3.18
        sens_num = float(your_sens.get())
        return round((sens_num / cs_num), 3)

    def fort_convert():
        fort_num = 12.6
        sens_num = float(your_sens.get())
        return round((sens_num * fort_num), 3)

    def fort_reserve_convert():
        fort_num = 12.6
        sens_num = float(your_sens.get())
        return round((sens_num / fort_num), 3)

    def fort_to_cs():
        fort_num = 3.96
        sens_num = float(your_sens.get())
        return round((sens_num / fort_num), 3)

    def cs_to_fort():
        cs_num = 3.96
        sens_num = float(your_sens.get())
        return round((sens_num * cs_num), 3)

    conversion_functions = {
        ("Valorant", "CS-GO"): cs_convert,
        ("Valorant", "Fortnite"): fort_convert,
        ("CS-GO", "Valorant"): cs_reserve_convert,
        ("Fortnite", "Valorant"): fort_reserve_convert,
        ("CS-GO", "Fortnite"): cs_to_fort,
        ("Fortnite", "CS-GO"): fort_to_cs
    }

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

    sens_text.pack()
    your_sens.pack()

    root.bind('<KeyRelease>', keyHandler)

    def dpi_show():
        if checkbox_var.get():
            first_label.pack()
            first_entry.pack()
            second_label.pack()
            second_entry.pack()
            button.pack(padx=10, pady=10)
        else:
            first_label.pack_forget()
            first_entry.pack_forget()
            second_label.pack_forget()
            second_entry.pack_forget()
            button.pack_forget()

    def compare_dpi():
        entry_dpi = int(first_entry.get())
        second_entry_dpi = int(second_entry.get())
        if selected_option and second_selected_option:
            total_sens_conv = conversion_functions.get((selected_option, second_selected_option), lambda: 1)()
            total_dpi = round(((entry_dpi / second_entry_dpi) * total_sens_conv), 3)
            result.config(text=total_dpi)

    checkbox_var = BooleanVar()
    checkbox = Checkbutton(root, text="Change DPI", bg="gray", variable=checkbox_var, onvalue=1, offvalue=0,
                           command=dpi_show)
    checkbox.pack(padx=10, pady=10)

    first_label = Label(root, text="Your DPI", bg="gray")
    second_label = Label(root, text="DPI to Convert", bg="gray")
    first_entry = Entry(root, width=20)
    second_entry = Entry(root, width=20)

    reset_button = Button(root, text="Go back", command=reset)
    reset_button.pack(side="bottom")

    button = Button(root, text="compare", command=compare_dpi)

    result = Label(root, text="", bg="grey", font=20)
    result.pack(side="bottom", padx=20, pady=20)


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
