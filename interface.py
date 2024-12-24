from tkinter import *

from Cotacao_automatica.cotacao_funcoes import *
from Suporte_automatico.suporte_funcoes import *



### PAGINA PRINCIPAL
def main():
    global main_window 
    main_window = Tk()
    main_window.minsize(500,200)
    main_window.title("AutoWork")
    main_window.config(padx=30, pady=30)

    welcome_label = Label(text="Welcome to the AutoWork App", font=("Arial", 16, "bold"))
    welcome_label.grid(row=0, column=1)



    quote_button = Button(text="Get Quote",command=get_quote)
    quote_button.grid(row=1, column=0)

    support_button = Button(text="Get Support", command=get_support)
    support_button.grid(row=1, column=1)

    quit_button = Button(text="Quit", command=main_window.destroy)
    quit_button.grid(row=1, column=2)


    main_window.mainloop()


### PAGINA PRA COTACAO
def get_quote():
    def quote_geico():
        opcao = "geico"
        if checked_state.get() == 1:
            card_and_cotacao(opcao)
            
        else:
            fazer_cotacao_only(opcao)
        quote_window.destroy()

    def quote_progressive():
        opcao = "progressive"
        if checked_state.get() == 1:
            card_and_cotacao(opcao)
        else:
            fazer_cotacao_only(opcao)
        quote_window.destroy()

    main_window.destroy()
    quote_window = Tk()
    quote_window.minsize(500,200)
    quote_window.title("AutoWork")
    quote_window.config(padx=50, pady=30)
    select_label = Label(text="Select an Option", font=("Arial", 14, "bold"), pady=10)
    select_label.grid(column=1,row=0)

    trello_only = Button(text="Trello Card", pady=10, command= card_only)
    trello_only.grid(column=1,row=1)

    checked_state= IntVar()
    checkbutton = Checkbutton(text="Trello", variable=checked_state)
    checkbutton.grid(column=0, row=1)


    geico = Button(text="Geico Quote", pady=10, command=quote_geico)
    geico.grid(column=0,row=2)

    progressive = Button(text="Progressive Quote", pady=10, command=quote_progressive)
    progressive.grid(column=2,row=2)

    delete = Button(text="Delete", pady=10, command=data.delete_excel)
    delete.grid(column=1,row=4)




    quote_window.mainloop()


### PAGINA DO SUPORTE
def get_support():

    def get_input():
        user = user_entry.get()
        password = password_entry.get()
        mensagem = mensagem_entry.get()
        support_progressive (user=user, password=password, mensagem=mensagem)
    main_window.destroy()
    support_window = Tk()
    support_window.title("AutoWork")
    support_window.config(padx=50, pady=30)

    user_label = Label(text="Username")
    user_label.grid(row=0, column=0)
    user_entry = Entry(support_window, text="User")
    user_entry.grid(row=0, column=1)

    password_label = Label(text="Password")
    password_label.grid(row=1, column=0)
    password_entry = Entry(support_window, text="Password")
    password_entry.grid(row=1, column=1)


    mensagem_label = Label(text="Mensagem")
    mensagem_label.grid(row=2, column=0)
    mensagem_entry = Entry(support_window, text="Your message")
    mensagem_entry.grid(row=2,column=1)

    button = Button(text="Enter", command=get_input, width=15)
    button.grid(row=3, column=1)
    support_window.mainloop()


if __name__ == "__main__":
    main() 