import customtkinter
from .frame_cities import scrollabel_frame
from ..json_folder.read_json import *
from ..weather import *

list_cities = ["Дніпро", "Київ", "Рим", "Лондон", "Варшава", "Прага", "Париж"]

class City(customtkinter.CTkFrame):
    def __init__(self, master, city_name):
        customtkinter.CTkFrame.__init__(
            self = self,
            master = master,
            width = 236,
            height = 100,
            border_color = "#FFFFFF",
            fg_color = "#096C82",
            border_width = 2,
            corner_radius = 20
        )
        self.pack(pady= 30)
        update_weather(city_name)

        self.data = read("weather_data.json")

        self.city_name = customtkinter.CTkLabel(
            master = self,
            text = city_name,
            font = ("Roboto Slab", 16, "bold"),
            text_color= "#FFFFFF"
        )
        self.city_time = customtkinter.CTkLabel(  master = self,
            text = "00:00",
            font = ("Roboto Slab", 12, "bold"),
            text_color= "#FFFFFF"
        )
        self.weather_description = customtkinter.CTkLabel(  master = self,
            text = self.data["weather"][0]["description"],
            font = ("Roboto Slab", 12, "bold"),
            text_color= "#b5d3d9"
        )

        self.city_temperature = customtkinter.CTkLabel( master = self,
            text = str(int(self.data["main"]["temp"]))+ "°",
            font =("Roboto Slab", 48, "bold"),
            text_color = "#FFFFFF",                                      
        )
        max_temp = int(self.data["main"]["temp_max"])
        min_temp = int(self.data["main"]["temp_min"])
        self.city_min_max_temperature = customtkinter.CTkLabel(master = self,                                             
            text = f"макс.: {max_temp} , мін.: {min_temp} ",
            font = ("Roboto Slab", 12, "bold"),
            text_color= "#b5d3d9"                             
        )
        self.weather_description.place(x = 14, y = 66)
        self.city_time.place(x = 14, y = 28)
        self.city_name.place(x = 14, y = 8 )
        self.city_temperature.place(x = 152, y = 6)
        self.city_min_max_temperature.place(x = 122, y = 66) 
        
for city_name in list_cities:
    city = City(scrollabel_frame, city_name)