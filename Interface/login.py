from customtkinter import *
from PIL import Image
from Automatizacao._funcoes import suporte_geico, suporte_progressive

class Login:
## Interface para login na geico e logica do botao de login
    def geico(self):
        self.window = CTk()
        self.window.geometry("660x500")
        set_appearance_mode("dark")
        self.window.config(padx=30, pady=30)

        main_frame = CTkFrame(self.window, border_color="white", border_width=2, corner_radius=20)
        main_frame.pack(fill=BOTH, expand=True)


        question_label = CTkLabel(main_frame, text="Login to Geico", font=("Arial", 20, "bold"), text_color="white")
        question_label.pack(side=TOP, pady=20)
        self.nome_entry = CTkEntry(main_frame, placeholder_text="Nome", corner_radius=30)
        self.username_entry = CTkEntry(main_frame, placeholder_text="Username", corner_radius=30)
        self.password_entry = CTkEntry(main_frame, placeholder_text="Password", corner_radius=30, show="*")
        self.message_entry = CTkEntry(main_frame, placeholder_text="Message", corner_radius=30)
        login_button = CTkButton(main_frame, text="Login", command=self.login_geico, corner_radius=30)

        self.nome_entry.pack(side=TOP, pady=20)
        self.username_entry.pack(side=TOP, pady=20)
        self.password_entry.pack(side=TOP, pady=20)
        self.message_entry.pack(side=TOP, pady=20)
        login_button.pack(side=BOTTOM, pady=20)
        self.window.mainloop()


    def login_geico(self):
        suporte_geico(self.username_entry.get(), self.password_entry.get(), self.message_entry.get(), nome=self.nome_entry.get())
        self.window.destroy()



### Interface para login na progressive e logica do botao de login
    def progressive(self):
        self.window = CTk()
        self.window.geometry("660x400")
        set_appearance_mode("dark")
        self.window.config(padx=30, pady=30)

        main_frame = CTkFrame(self.window, border_color="white", border_width=2, corner_radius=20)
        main_frame.pack(fill=BOTH, expand=True)


        question_label = CTkLabel(main_frame, text="Login to Progressive", font=("Arial", 20, "bold"), text_color="white")
        question_label.pack(side=TOP, pady=20)
        
        self.username_entry = CTkEntry(main_frame, placeholder_text="Username", corner_radius=30)
        self.password_entry = CTkEntry(main_frame, placeholder_text="Password", corner_radius=30, show="*")
        self.message_entry = CTkEntry(main_frame, placeholder_text="Message", corner_radius=30)
        login_button = CTkButton(main_frame, text="Login", command=self.login_progessive, corner_radius=30)


        self.username_entry.pack(side=TOP, pady=20)
        self.password_entry.pack(side=TOP, pady=20)
        self.message_entry.pack(side=TOP, pady=20)
        login_button.pack(side=TOP, pady=20)
        self.window.mainloop()

    def login_progessive(self):
        suporte_progressive(self.username_entry.get(), self.password_entry.get(), self.message_entry.get())

        self.window.destroy()






