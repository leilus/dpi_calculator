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

    def on_select(e):
        csNum = float(3.18)
        forNum = float(12.6)
        selected_option = combo_var.get()
        second_selected_option = combo_varSecond.get()
        if (selected_option == "Valorant" and second_selected_option == "CS-GO"):
            print("esa")

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

    dpi_text = Label(root, text="Your DPI", bg="grey")
    your_dpi = Entry(root, width=20)

    sens_text.pack()
    your_sens.pack()
    dpi_text.pack()
    your_dpi.pack()

    def cs_convert():
        sens_num = float(your_sens.get())
        dpi_num = int(your_dpi.get())
        result.config(text=(round(sens_num * dpi_num)))

    result = Label(root, text="", bg="grey")
    result.pack()

    conv_result = Button(root, text="Convert", command=cs_convert)
    conv_result.pack()

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
