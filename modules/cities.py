import customtkinter as ctk
from .city_frame import cities


class CityFrame(ctk.CTkFrame):
    def __init___(self):
        ctk.CTkFrame.__init__(
            self = self,
            master = cities,
            width = 236,
            height= 101,
            border_width= 2,
            border_color= 'white',
            fg_color = '#096C82'
        )
        
        self.pack(pady = 30) 
         
cityframe1 = CityFrame(cities)