import customtkinter as ctk

main_window = ctk.CTk(fg_color= "#5DA7B1")

WIDTH = 1200
HEIGTH = 800

screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

x = screen_width/2 - WIDTH/2
y = screen_height/2 - HEIGTH/2

main_window.geometry(f"{WIDTH}x{HEIGTH}+{x}+{y}")