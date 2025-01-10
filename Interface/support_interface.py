from customtkinter import *
from PIL import Image
from Interface.login_progressive import LoginProgressive
from Interface.login_geico import LoginGeico

class SupportInterface:
    def __init__(self):
        self.geico_img = Image.open("Interface/images/geico.jpg")
        self.progressive_img = Image.open("Interface/images/progressive.jpeg")
        self.allstate_img = Image.open("Interface/images/allstate.png")


    def support_page(self):
        self.window = CTk()
        self.window.geometry("660x400")
        set_appearance_mode("dark")
        self.window.config(padx=30, pady=30)

        main_frame = CTkFrame(self.window, border_color="white", border_width=2, corner_radius=20)
        main_frame.pack(fill=BOTH, expand=True)


        question_label = CTkLabel(main_frame, text="Which Company?", font=("Arial", 20, "bold"), text_color="white")
        question_label.pack(side=TOP, pady=20)

        options_frame = CTkFrame(main_frame)
        geico_button = CTkButton(options_frame, text="Geico", command=self.geico_button, corner_radius=30, image=CTkImage(dark_image=self.geico_img, light_image=self.geico_img))
        progressive_button = CTkButton(options_frame, text="Progressive", command=self.progressive_button, corner_radius=30, image=CTkImage(dark_image=self.progressive_img, light_image=self.progressive_img))
        allstate_button = CTkButton(options_frame, text="Allstate", command=lambda: print("Chat"), corner_radius=30, image=CTkImage(dark_image=self.allstate_img, light_image=self.allstate_img))


        options_frame.pack(side=BOTTOM, pady=60)
        geico_button.pack(side=LEFT, padx=10)
        progressive_button.pack(side=LEFT, padx=10)
        allstate_button.pack(side=LEFT, padx=10)
        self.window.mainloop()

    def progressive_button(self):
        LoginProgressive().login()

    def geico_button(self):
        LoginGeico().login()
