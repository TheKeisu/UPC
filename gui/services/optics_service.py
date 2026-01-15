import math
from optics import calculations as optics_calc

def calc_n21_from_angles_deg(alpha_deg, gamma_deg):
    sin_alpha = math.sin(math.radians(alpha_deg))
    sin_gamma = math.sin(math.radians(gamma_deg))
    return optics_calc.calc_n21_from_sin_alpha_sin_gamma(sin_alpha, sin_gamma)

def compute_example(a, b):
    return calc_n21_from_angles_deg(a, b)
