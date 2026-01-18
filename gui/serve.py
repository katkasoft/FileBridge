import customtkinter as ctk
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = 'Error happened'
    finally:
        s.close()
    return ip

def serve_tab(tab):
    ip_title = ctk.CTkLabel(tab, text="Your IP Address:", font=("Roboto", 14, "bold"))
    ip_title.pack(padx=10, pady=(20, 5))

    ip_addr = ctk.CTkLabel(
        tab, 
        text=get_local_ip(), 
        font=("Consolas", 24, "bold"),
        text_color="#1f6aa5"
    )
    ip_addr.pack(padx=10, pady=10)

    file_frame = ctk.CTkFrame(tab)
    file_frame.pack(padx=10, pady=10)

    file_entry = ctk.CTkEntry(file_frame, placeholder_text="Path to file...", width=200)
    file_entry.grid(row=0, column=0, padx=10, pady=10)

    file_btn = ctk.CTkButton(file_frame, text="Open", width=80)
    file_btn.grid(row=0, column=1, padx=10, pady=10)

    serve_btn = ctk.CTkButton(tab, text="Serve", width=300, state="disabled")
    serve_btn.pack(padx=10, pady=20)