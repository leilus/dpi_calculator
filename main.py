from tkinter import *

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
    sens_choice = Label(root, text="siema")
    sens_choice.pack()
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
