import customtkinter as ctk
from CTkListbox import CTkListbox

def get_tab(tab):
    ip_scan_frame = ctk.CTkFrame(tab)
    ip_scan_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    listbox = CTkListbox(ip_scan_frame, height=100)
    listbox.pack(padx=10, pady=(10, 5), fill="both", expand=True)

    scan_btn = ctk.CTkButton(ip_scan_frame, text="Scan Network")
    scan_btn.pack(padx=10, pady=(5, 10), fill="x")

    ip_get_frame = ctk.CTkFrame(tab)
    ip_get_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    ip_entry = ctk.CTkEntry(ip_get_frame, placeholder_text="Enter ip...")
    ip_entry.pack(padx=10, pady=(50, 10), fill="x")

    get_btn = ctk.CTkButton(ip_get_frame, text="Get file", state="disabled")
    get_btn.pack(padx=10, pady=10, fill="x")