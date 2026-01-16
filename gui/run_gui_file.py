from gui.windows.main_window import MainWindow
from tkinter import Tk

def run_gui():
    app = MainWindow()
    app.mainloop()
    
if __name__ == "__main__":
    run_gui()