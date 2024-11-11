import customtkinter as ctk

main_window = ctk.CTk(fg_color= "#5DA7B1" )
main_window.title("Project")
width = 1200
height = 800
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
x = screen_width//2 - width//2
y = screen_height//2 - height//2

main_window.geometry(f"{width}x{height}+{x}+{y}")