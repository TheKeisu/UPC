import tkinter as tk
from tkinter import ttk
from ..services import mechanics_service

class MechanicsView(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.columnconfigure(1, weight=1)

        ttk.Label(self, text="Mechanics - example adapter").grid(row=0, column=0, columnspan=2, sticky="w")
        ttk.Label(self, text="a:").grid(row=1, column=0, sticky="w")
        self.a_var = tk.DoubleVar(value=1.0)
        ttk.Entry(self, textvariable=self.a_var).grid(row=1, column=1, sticky="ew")
        ttk.Label(self, text="b:").grid(row=2, column=0, sticky="w")
        self.b_var = tk.DoubleVar(value=1.0)
        ttk.Entry(self, textvariable=self.b_var).grid(row=2, column=1, sticky="ew")
        self.result_var = tk.StringVar()
        ttk.Button(self, text="Compute", command=self.on_compute).grid(row=3, column=0, columnspan=2, pady=6)
        ttk.Label(self, textvariable=self.result_var, foreground="blue").grid(row=4, column=0, columnspan=2, sticky="w")

    def on_compute(self):
        a = self.a_var.get()
        b = self.b_var.get()
        try:
            res = mechanics_service.compute_example(a, b)
            self.result_var.set(f"{res}")
        except Exception as e:
            self.result_var.set(f"Error: {e}")
