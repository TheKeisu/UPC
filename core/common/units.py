_PREFIXES: dict[int, tuple[str, float]] = {
    1: ("", 1.0),
    2: ("Т", 1e12),
    3: ("Г", 1e9),
    4: ("М", 1e6),
    5: ("к", 1e3),
    6: ("м", 1e-3),
    7: ("мк", 1e-6),
    8: ("н", 1e-9),
    9: ("п", 1e-12),
}


def unit_transition(value=None, unit: str = "", output_unit: int | None = None):
    """Convert a numeric value to a different SI-prefixed unit.

    Supported choices:
    1 - base unit
    2 - тера
    3 - гига
    4 - мега
    5 - кило
    6 - милли
    7 - микро
    8 - нано
    9 - пико
    """

    if value is None:
        value = float(input("Введите значение: "))

    if output_unit is None:
        output_unit = int(
            input(
                "Выберите единицу измерения "
                "(без приставки - 1; тера - 2; гига - 3; мега - 4; кило - 5; "
                "милли - 6; микро - 7; нано - 8; пико - 9): "
            )
        )

    prefix, factor = _PREFIXES.get(output_unit, (None, None))
    if prefix is None or factor is None:
        raise ValueError("Неверный вариант единицы измерения")

    return float(value) / factor, f"{prefix}{unit}".strip()


def temp_transition(temperature=None, output_unit=None):

    if temperature is None:
        temperature = float(input("Введите температуру: "))

    if output_unit is None:
        output_unit = int(input("Выберите единицу температуры (К - 1; °C - 2): "))

    temperature = float(temperature)

    match output_unit:
        case 1:
            return temperature, "К"
        case 2:
            return temperature - 273.15, "°C"
        case _:
            raise ValueError("Неверный вариант единицы температуры")