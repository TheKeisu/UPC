import tkinter as tk
from tkinter import ttk
from ..services import optics_service

class OpticsView(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.columnconfigure(1, weight=1)

        ttk.Label(self, text="Optics — n21 = sin(alpha) / sin(gamma)").grid(row=0, column=0, columnspan=2, sticky="w")

        ttk.Label(self, text="alpha (deg):").grid(row=1, column=0, sticky="w")
        self.alpha_var = tk.DoubleVar(value=30.0)
        ttk.Entry(self, textvariable=self.alpha_var).grid(row=1, column=1, sticky="ew")

        ttk.Label(self, text="gamma (deg):").grid(row=2, column=0, sticky="w")
        self.gamma_var = tk.DoubleVar(value=20.0)
        ttk.Entry(self, textvariable=self.gamma_var).grid(row=2, column=1, sticky="ew")

        self.result_var = tk.StringVar()
        ttk.Button(self, text="Compute n21", command=self.on_compute).grid(row=3, column=0, columnspan=2, pady=6)
        ttk.Label(self, textvariable=self.result_var, foreground="blue").grid(row=4, column=0, columnspan=2, sticky="w")

    def on_compute(self):
        a = self.alpha_var.get()
        g = self.gamma_var.get()
        try:
            n21 = optics_service.calc_n21_from_angles_deg(a, g)
            self.result_var.set(f"n21 = {n21:.6f}")
        except Exception as e:
            self.result_var.set(f"Error: {e}")
