import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ultimate Physics Calculator")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.setup_ui()
        
    def setup_ui(self):
        label = tk.Label(self, text="Welcome to the Ultimate Physics Calculator")
        label.pack()
        
        button = tk.Button(self, text="Click Me")
        button.pack()