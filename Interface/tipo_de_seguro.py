from customtkinter import *
from PIL import Image
from Interface.cotacao import QuoteInterface

class TypeinsInterface:
    def __init__(self):
        self.car = Image.open("Interface/images/car_icon.png")
        self.ap = Image.open("Interface/images/apartment.png")
        self.truck = Image.open("Interface/images/truck.png")


    def typeins_page(self):
        self.window = CTk()
        self.window.geometry("660x400")
        set_appearance_mode("dark")
        self.window.config(padx=30, pady=30)


        main_frame = CTkFrame(self.window, border_color="white", border_width=2, corner_radius=20)
        main_frame.pack(fill=BOTH, expand=True)


        question_label = CTkLabel(main_frame, text="Type of insurance would you like to get a quote for?", font=("Arial", 20, "bold"), text_color="white")
        question_label.pack(side=TOP, pady=20)

        options_frame = CTkFrame(main_frame)
        car_button = CTkButton(options_frame, text="Car", command=self.quote_button, corner_radius=30, image=CTkImage(dark_image=self.car, light_image=self.car))
        ap_button = CTkButton(options_frame, text="Apartment", command=lambda: print("Not yet"), corner_radius=30, image=CTkImage(dark_image=self.ap, light_image=self.ap))
        truck_button = CTkButton(options_frame, text="Commercial", command=lambda: print("Not Yet"), corner_radius=30, image=CTkImage(dark_image=self.truck, light_image=self.truck))


        options_frame.pack(side=BOTTOM, pady=60)
        car_button.pack(side=LEFT, padx=10)
        ap_button.pack(side=LEFT, padx=10)
        truck_button.pack(side=LEFT, padx=10)
        self.window.mainloop()
     
    def quote_button(self):
        self.window.destroy()
        self.quote = QuoteInterface()
        self.quote.company_quote()
