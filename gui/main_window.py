import tkinter as tk
from tkinter import ttk
import importlib

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Physics Toolkit")
        self.geometry("800x480")

        left = ttk.Frame(self, padding=8)
        left.pack(side="left", fill="y")
        self.modules = ["optics", "electrodynamics", "mechanics", "thermodynamics", "sections"]
        for name in self.modules:
            btn = ttk.Button(left, text=name.capitalize(), command=lambda n=name: self.show_module(n))
            btn.pack(fill="x", pady=2)

        self.container = ttk.Frame(self, padding=8)
        self.container.pack(side="right", fill="both", expand=True)
        self.current_view = None
        self.show_module("optics")

    def show_module(self, module_name):
        if self.current_view:
            self.current_view.destroy()
            self.current_view = None
        try:
            mod = importlib.import_module(f"gui.views.{module_name}_view")
            ViewClass = getattr(mod, f"{module_name.capitalize()}View")
            self.current_view = ViewClass(self.container)
        except Exception:
            mod = importlib.import_module("gui.views.module_view")
            ModuleView = getattr(mod, "ModuleView")
            self.current_view = ModuleView(self.container, module_name)
        self.current_view.pack(fill="both", expand=True)
