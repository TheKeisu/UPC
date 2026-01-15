def compute_example(a, b):
    try:
        from electrodynamics import calculations as ed_calc
        # prefer a known adapter function if present
        if hasattr(ed_calc, "compute_example"):
            return ed_calc.compute_example(a, b)
        # fallback: return a simple summary
        return f"electrodynamics: a={a}, b={b}"
    except Exception as e:
        return f"error importing electrodynamics: {e}"
