import customtkinter as ctk
from .window import main_window
from ..weather import update_weather

class Forecast(ctk.CTkScrollableFrame):
    def __init__(self, master):
        ctk.CTkScrollableFrame.__init__(
           self,
           master = master,
           width = 820,
           height = 240,
           border_width= 5,
           border_color= "#FFFFFF",
           corner_radius= 20,
           fg_color= '#5DA7B1',
           orientation= 'horizontal'
        )
        self.place(x=375 , y=429)
        update_weather("Dnipro", "forecast_data.json",  "forecast", 10)
    
forecast = Forecast(master = main_window)