from customtkinter import *
from PIL import Image

from Automatizacao._funcoes import *


class QuoteInterface:
    def __init__(self):
        self.geico_img = Image.open("Interface/images/geico.jpg")
        self.progressive_img = Image.open("Interface/images/progressive.jpeg")
        self.allstate_img = Image.open("Interface/images/allstate.png")


    def company_quote(self):
        self.window = CTk()
        self.window.geometry("660x400")
        set_appearance_mode("dark")
        self.window.config(padx=30, pady=30)
        main_frame = CTkFrame(self.window, border_color="white", border_width=2, corner_radius=20)
        main_frame.pack(fill=BOTH, expand=True)

        question_label = CTkLabel(main_frame, text="Which company would you like to quote?", font=("Arial", 20, "bold"), text_color="white")
        question_label.pack(side=TOP, pady=20)



        

        options_frame = CTkFrame(main_frame)

        self.checked_state = IntVar()
        check_button = CTkCheckBox(options_frame, text="Trello", text_color="white", variable=self.checked_state, corner_radius=36)
        
        geico_button = CTkButton(options_frame, text="Geico", command= self.geico_button, corner_radius=30, image=CTkImage(dark_image=self.geico_img, light_image=self.geico_img))

        progressive_button = CTkButton(options_frame, text="Progressive", command= self.progressive_button, corner_radius=30, image=CTkImage(dark_image=self.progressive_img, light_image=self.progressive_img))

        allstate_button = CTkButton(options_frame, text="Allstate", command= self.allstate_button, corner_radius=30, image=CTkImage(dark_image=self.allstate_img, light_image=self.allstate_img))

        

        options_frame.pack(side=BOTTOM, pady=60)
        check_button.pack(side=LEFT)
        geico_button.pack(side=LEFT, padx=10)
        progressive_button.pack(side=LEFT, padx=10)
        allstate_button.pack(side=LEFT, padx=10)
        self.window.mainloop()
    

        
    
    def progressive_button(self):
        opcao = "progressive"
        if self.checked_state.get() == 1:
            card_and_cotacao(opcao)
        else:
            fazer_cotacao_only(opcao)
        self.window.destroy()
    
    def geico_button(self):
        opcao = "geico"
        if self.checked_state.get() == 1:
            card_and_cotacao(opcao)
            
        else:
            fazer_cotacao_only(opcao)
        self.window.destroy()

    def allstate_button(self):
        opcao = "allstate"
        if self.checked_state.get() == 1:
            card_and_cotacao(opcao)
        else:
            fazer_cotacao_only(opcao)
        self.window.destroy()
        
        

