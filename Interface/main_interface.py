from customtkinter import *
from Interface.typeins_interface import TypeinsInterface
from Interface.support_interface import SupportInterface
from PIL import Image



class MainInterface:
    def __init__(self):
        self.car_img = Image.open("Interface/images/car_logo.png")
        self.chat_img = Image.open("Interface/images/chat.png")
        self.shield_img = Image.open("Interface/images/shield.png")
        self.exit_img = Image.open("Interface/images/exit.png")


        
    def main_page(self):
        self.window = CTk()
        self.window.geometry("660x400")
        set_appearance_mode("dark")

        self.window.config(padx=30, pady=30)
        car_icon = CTkImage(dark_image=self.car_img, light_image=self.car_img, size= (120,120))

        main_frame = CTkFrame(self.window, border_color="white", border_width=2, corner_radius=20)
        main_frame.pack(fill=BOTH, expand=True)

        ##Text + Image for the Gui part.
        logo_frame = CTkFrame(main_frame)
        image_label = CTkLabel(logo_frame, text="", image=car_icon)
        welcome_label = CTkLabel(logo_frame, text="Autowork Cars", text_color="White", font=("Arial", 30, "bold"), padx=20)
        logo_frame.pack(side=TOP, pady=30)
        welcome_label.pack(side=LEFT)
        image_label.pack(side=LEFT)


        options_frame = CTkFrame(main_frame)
        support_button = CTkButton(options_frame, text="Support", command=self.support_func, corner_radius=30 , image=CTkImage(dark_image=self.chat_img, light_image=self.chat_img))
        quote_button = CTkButton(options_frame, text="Get a Quote", command=self.quote_func, corner_radius=30, image=CTkImage(dark_image=self.shield_img, light_image=self.shield_img))
        exit_button = CTkButton(options_frame, text="Exit", command=self.window.quit, corner_radius=30, image=CTkImage(dark_image=self.exit_img, light_image=self.exit_img))

        options_frame.pack(side=BOTTOM, pady=60)

        quote_button.pack(side=LEFT,padx=10)
        support_button.pack(side=LEFT, padx=10)
        exit_button.pack(side=LEFT, padx=10)
        self.window.mainloop()
        

    def quote_func(self):
            self.window.destroy()
            self.quote = TypeinsInterface()
            self.quote.typeins_page()
            
    def support_func(self):
            self.window.destroy()
            self.support = SupportInterface()
            self.support.support_page()


