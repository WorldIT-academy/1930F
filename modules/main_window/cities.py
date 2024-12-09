import customtkinter
from .frame_cities import scrollabel_frame


class City(customtkinter.CTkFrame):
    def __init__(self, master):
        customtkinter.CTkFrame.__init__(
            self = self,
            master = master,
            width = 236,
            height = 100,
            border_color =  "#FFFFFF",
            fg_color = "#096C82",
            border_width = 2,
            corner_radius = 20
        )
        self.pack(pady= 30)
        self.city_name = customtkinter.CTkLabel(
            master = self,
            text = "Dnipro",
            font = ("Roboto Slab", 16, "bold"),
            text_color= "#FFFFFF"
        )
        self.city_time = customtkinter.CTkLabel(  master = self,
            text = "20:56",
            font = ("Roboto Slab", 12, "bold"),
            text_color= "#FFFFFF"
        )
        self.weather_description = customtkinter.CTkLabel(  master = self,
            text = "Хмарно",
            font = ("Roboto Slab", 12, "bold"),
            text_color= "#b5d3d9"
        )
        self.city_temperature = customtkinter.CTkLabel( master = self,
            text = "25°",
            font =("Roboto Slab", 48, "bold"),
            text_color = "#FFFFFF",                                      
        )
        self.city_min_max_temperature = customtkinter.CTkLabel(master = self,                                             
            text = "макс.: 11 , мін.: 4 ",
            font = ("Roboto Slab", 12, "bold"),
            text_color= "#b5d3d9"                             
        )
        self.weather_description.place(x = 14, y = 66)
        self.city_time.place(x = 14, y = 28)
        self.city_name.place(x = 14, y = 8 )
        self.city_temperature.place(x = 154, y = 6)
        self.city_min_max_temperature.place(x = 122, y = 66)
        
        
for i in range(6):
    city = City(scrollabel_frame)