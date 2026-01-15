def compute_example(a, b):
    try:
        from thermodynamics import calculations as t_calc
        if hasattr(t_calc, "compute_example"):
            return t_calc.compute_example(a, b)
        return f"thermodynamics: a={a}, b={b}"
    except Exception as e:
        return f"error importing thermodynamics: {e}"
