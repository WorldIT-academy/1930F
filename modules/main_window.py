import customtkinter

main_window = customtkinter.CTk()

main_window.title("project")
WIDTH = 1000
HEIGHT = 500
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
screen_x = screen_width // 2 - WIDTH// 2
screen_y = screen_height // 2 - HEIGHT// 2
print(screen_width, screen_height)
main_window.geometry(f"{WIDTH}x{HEIGHT}+{screen_x}+{screen_y}")

