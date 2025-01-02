from customtkinter import *
from PIL import Image
from Suporte_automatico.suporte_funcoes import support_progressive

class LoginProgressive:
    def login(self):
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
        login_button = CTkButton(main_frame, text="Login", command=self.login_button, corner_radius=30)


        self.username_entry.pack(side=TOP, pady=20)
        self.password_entry.pack(side=TOP, pady=20)
        self.message_entry.pack(side=TOP, pady=20)
        login_button.pack(side=TOP, pady=20)
        self.window.mainloop()


    def login_button(self):
        support_progressive(self.username_entry.get(), self.password_entry.get(), self.message_entry.get())

        self.window.destroy()


