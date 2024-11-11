from .window import main_window
import customtkinter as ctk

# CTkScrollableFrame() - класс, с помощью которого можно создать элемент с прокруткой
cities = ctk.CTkScrollableFrame(
    master= main_window, 
    width= 275,
    height= 800,
    fg_color= "#096C82"
)
# grid - метод при помощи которого можно разместить елемент по сетке ( указав ряд и колонку )
cities.grid(row= 0, column= 0)

