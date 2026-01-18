import customtkinter as ctk
from CTkListbox import CTkListbox
import socket
from gui.get import *
from gui.serve import *

app = ctk.CTk()
app.title("FileBridge")

app.geometry("425x300") 
app.resizable(False, False)

tabview = ctk.CTkTabview(app, width=480, height=400)
tabview.pack(padx=10, pady=5)

tabview.add("Get")
tabview.add("Serve")

tabview.tab("Get").grid_columnconfigure(0, weight=1)
tabview.tab("Get").grid_columnconfigure(1, weight=1)

get_tab(tabview.tab("Get"))
serve_tab(tabview.tab("Serve"))

app.mainloop()