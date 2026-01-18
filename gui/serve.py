import customtkinter as ctk
import socket
import os

class ServeTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.selected_file = ""

        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="transparent")

        self.setup_ui()

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = 'Error happened'
        finally:
            s.close()
        return ip

    def setup_ui(self):
        self.ip_title = ctk.CTkLabel(self, text="Your IP Address:", font=("Roboto", 14, "bold"))
        self.ip_title.pack(padx=10, pady=(20, 5))

        self.ip_addr = ctk.CTkLabel(
            self, 
            text=self.get_local_ip(), 
            font=("Consolas", 24, "bold"),
            text_color="#1f6aa5"
        )
        self.ip_addr.pack(padx=10, pady=10)

        self.file_frame = ctk.CTkFrame(self)
        self.file_frame.pack(padx=10, pady=10)

        self.file_entry = ctk.CTkEntry(self.file_frame, placeholder_text="Path to file...", width=200)
        self.file_entry.grid(row=0, column=0, padx=10, pady=10)
        self.file_entry.bind("<KeyRelease>", self.file_input_handler)

        self.file_btn = ctk.CTkButton(self.file_frame, text="Open", width=80, command=self.open_file)
        self.file_btn.grid(row=0, column=1, padx=10, pady=10)

        self.serve_btn = ctk.CTkButton(self, text="Serve", width=300, state="disabled", command=self.serve)
        self.serve_btn.pack(padx=10, pady=20)

    def open_file(self):
        path = ctk.filedialog.askopenfilename()
        if path:
            self.selected_file = path
            self.sync_entry_with_file()
            self.validate_serve_button()

    def file_input_handler(self, event):
        current_input = self.file_entry.get()
        if os.path.exists(current_input) and os.path.isfile(current_input):
            self.selected_file = current_input
            self.validate_serve_button()
        else:
            self.serve_btn.configure(state="disabled")

    def sync_entry_with_file(self):
        if self.file_entry.get() != self.selected_file:
            self.file_entry.delete(0, 'end')
            self.file_entry.insert(0, self.selected_file)

    def validate_serve_button(self):
        if self.selected_file and os.path.isfile(self.selected_file):
            self.serve_btn.configure(state="normal")
        else:
            self.serve_btn.configure(state="disabled")

    def serve(self):
        print(f"Starting server for: {self.selected_file}")
