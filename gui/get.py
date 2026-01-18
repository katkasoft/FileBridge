import customtkinter as ctk
from CTkListbox import CTkListbox

class GetTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.configure(fg_color="transparent")

        self.setup_ui()

    def setup_ui(self):
        self.ip_scan_frame = ctk.CTkFrame(self)
        self.ip_scan_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.listbox = CTkListbox(self.ip_scan_frame, height=100)
        self.listbox.pack(padx=10, pady=(10, 5), fill="both", expand=True)

        self.scan_btn = ctk.CTkButton(self.ip_scan_frame, text="Scan Network")
        self.scan_btn.pack(padx=10, pady=(5, 10), fill="x")

        self.ip_get_frame = ctk.CTkFrame(self)
        self.ip_get_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.ip_entry = ctk.CTkEntry(self.ip_get_frame, placeholder_text="Enter ip...")
        self.ip_entry.pack(padx=10, pady=(50, 10), fill="x")

        self.get_btn = ctk.CTkButton(self.ip_get_frame, text="Get file", state="disabled")
        self.get_btn.pack(padx=10, pady=10, fill="x")