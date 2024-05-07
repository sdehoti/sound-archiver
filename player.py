import customtkinter

class Player:
    def __init__(self, master):
        self.frame = customtkinter.CTkFrame(master)
        self.frame.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.frame_label = customtkinter.CTkLabel(self.frame, text="Player Controls", font= ("Arial", 16))
        self.frame_label.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)