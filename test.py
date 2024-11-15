from tkinter import *


def get_quote():
    def quote_geico():
        if checked_state.get() == 1:
            print("trello + geico")
        else:
            print("only geico")
        quote_window.destroy()

    def quote_progressive():
        if checked_state.get() == 1:
            print("trello + progressive")
        else:
            print("only progressive")
        quote_window.destroy()

    main_window.destroy()
    quote_window = Tk()
    quote_window.minsize(500,200)
    quote_window.title("AutoWork")
    quote_window.config(padx=50, pady=30)
    select_label = Label(text="Select an Option", font=("Arial", 14, "bold"), pady=10)
    select_label.grid(column=1,row=0)

    trello_only = Button(text="Trello Card", pady=10)
    trello_only.grid(column=1,row=1)

    checked_state= IntVar()
    checkbutton = Checkbutton(text="Trello", variable=checked_state)
    checkbutton.grid(column=0, row=1)


    geico = Button(text="Geico Quote", pady=10, command=quote_geico)
    geico.grid(column=0,row=2)

    progressive = Button(text="Progressive Quote", pady=10, command=quote_progressive)
    progressive.grid(column=2,row=2)

    delete = Button(text="Delete", pady=10)
    delete.grid(column=1,row=4)




    quote_window.mainloop()













main_window = Tk()
main_window.minsize(500,200)
main_window.title("AutoWork")
main_window.config(padx=30, pady=30)

welcome_label = Label(text="Welcome to the AutoWork App", font=("Arial", 16, "bold"))
welcome_label.grid(row=0, column=1)



quote_button = Button(text="Get Quote",command=get_quote)
quote_button.grid(row=1, column=0)

support_button = Button(text="Get Support")
support_button.grid(row=1, column=1)

quit_button = Button(text="Quit", command=main_window.destroy)
quit_button.grid(row=1, column=2)


main_window.mainloop()