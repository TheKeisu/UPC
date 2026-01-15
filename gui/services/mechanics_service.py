def compute_example(a, b):
    try:
        from mechanics import calculations as m_calc
        if hasattr(m_calc, "compute_example"):
            return m_calc.compute_example(a, b)
        return f"mechanics: a={a}, b={b}"
    except Exception as e:
        return f"error importing mechanics: {e}"
