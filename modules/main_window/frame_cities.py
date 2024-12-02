import customtkinter 
from .window import main_window, HEIGTH

scrollabel_frame = customtkinter.CTkScrollableFrame(
    master = main_window,
    width= 275,
    height= HEIGTH,
    fg_color="#096C82"
)
scrollabel_frame.grid(row = 0,column = 0)