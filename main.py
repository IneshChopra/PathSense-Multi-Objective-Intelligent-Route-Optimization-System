import customtkinter as ctk
from tkinter import messagebox
from map_utils import find_and_show_route

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def on_click():
    loading_label.configure(text="Finding best route 🚗💨")
    app.update()

    source = source_entry.get()
    dest = dest_entry.get()
    mode = mode_menu.get()

    result = find_and_show_route(source, dest, mode)

    loading_label.configure(text="")

    if result != "Success":
        messagebox.showerror("Error", result)

app = ctk.CTk()
app.title("PathSense 🚗")
app.geometry("500x500")

ctk.CTkLabel(app, text="Path", font=("Arial", 32, "bold")).pack(pady=20)

source_entry = ctk.CTkEntry(app, placeholder_text="Enter Source", width=320)
source_entry.pack(pady=10)

dest_entry = ctk.CTkEntry(app, placeholder_text="Enter Destination", width=320)
dest_entry.pack(pady=10)

mode_menu = ctk.CTkOptionMenu(app, values=["Shortest", "Fastest", "Emergency"])
mode_menu.pack(pady=15)

ctk.CTkButton(app, text="Find Route", command=on_click, width=220).pack(pady=25)

loading_label = ctk.CTkLabel(app, text="")
loading_label.pack()

ctk.CTkLabel(app, text="Powered by PathSense 🚗", font=("Arial", 12)).pack(side="bottom", pady=10)

app.mainloop()