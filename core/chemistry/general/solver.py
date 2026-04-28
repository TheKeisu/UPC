from __future__ import annotations

import chemparse
import sympy as sp

import core.chemistry.general.calculations as calcs
import core.chemistry.general.enum as enum
import core.chemistry.periodic_table as ptbl


COMMON_OXIDATION_STATES: dict[str, int] = {
    "H": 1,
    "O": -2,
    "F": -1,
    "Cl": -1,
    "Br": -1,
    "I": -1,
    "S": -2,
    "N": -3,
    "P": -3,
    "C": 4,
    "Na": 1,
    "K": 1,
    "Li": 1,
    "Mg": 2,
    "Ca": 2,
    "Ba": 2,
    "Al": 3,
    "Zn": 2,
    "Fe": 3,
    "Cu": 2,
    "Ag": 1,
    "Pb": 2,
}


def _build_case_prompt(input_text, enum_formula):
    cases = enum.get_formula_cases(enum_formula)
    if not cases:
        return input_text

    formula_key = enum.get_formula_key(enum_formula)
    formula_title = enum.FORMULAS.get(formula_key, {}).get("title", "Формула")
    lines = [f"{input_text}\n{formula_title}:"]
    for number, case in cases.items():
        lines.append(f"{number}. {case['name']}")
    lines.append("Номер варианта: ")
    return "\n".join(lines)


def formula_selection(input_text, enum_formula):
    option = int(input(_build_case_prompt(input_text, enum_formula)))

    match enum_formula:
        case enum.SUBSTANCE_AMOUNT:
            match option:
                case 1:
                    mass = float(input("Введите массу: "))
                    molar_mass = float(input("Введите молярную массу: "))
                    print(f"Количество вещества = {calcs.calc_substance_amount(mass, molar_mass)}")
                case 2:
                    substance_amount = float(input("Введите количество вещества: "))
                    molar_mass = float(input("Введите молярную массу: "))
                    print(f"Масса = {calcs.calc_mass_substance_amount(substance_amount, molar_mass)}")

        case enum.MOLAR_MASS:
            mass = float(input("Введите массу: "))
            substance_amount = float(input("Введите количество вещества: "))
            print(f"Молярная масса = {calcs.calc_molar_mass(mass, substance_amount)}")

        case enum.PARTICLES_COUNT:
            match option:
                case 1:
                    substance_amount = float(input("Введите количество вещества: "))
                    print(f"Число частиц = {calcs.calc_particles_count(substance_amount)}")
                case 2:
                    particles_count = float(input("Введите число частиц: "))
                    print(f"Количество вещества = {calcs.calc_substance_amount_particles_count(particles_count)}")

        case enum.IDEAL_GAS_LAW:
            match option:
                case 1:
                    substance_amount = float(input("Введите количество вещества: "))
                    temperature = float(input("Введите температуру (K): "))
                    volume = float(input("Введите объем (м³): "))
                    print(f"Давление = {calcs.calc_ideal_gas_pressure(substance_amount, temperature, volume)}")
                case 2:
                    substance_amount = float(input("Введите количество вещества: "))
                    temperature = float(input("Введите температуру (K): "))
                    pressure = float(input("Введите давление (Па): "))
                    print(f"Объем = {calcs.calc_ideal_gas_volume(substance_amount, temperature, pressure)}")
                case 3:
                    pressure = float(input("Введите давление (Па): "))
                    volume = float(input("Введите объем (м³): "))
                    temperature = float(input("Введите температуру (K): "))
                    print(f"Количество вещества = {calcs.calc_ideal_gas_substance_amount(pressure, volume, temperature)}")
                case 4:
                    pressure = float(input("Введите давление (Па): "))
                    volume = float(input("Введите объем (м³): "))
                    substance_amount = float(input("Введите количество вещества: "))
                    print(f"Температура = {calcs.calc_ideal_gas_temperature(pressure, volume, substance_amount)}")

        case enum.GAS_VOLUME_BY_SUBSTANCE:
            match option:
                case 1:
                    substance_amount = float(input("Введите количество вещества: "))
                    print(f"Объем = {calcs.calc_gas_volume_by_substance(substance_amount)}")
                case 2:
                    volume = float(input("Введите объем газа: "))
                    print(f"Количество вещества = {calcs.calc_substance_amount_gas_volume(volume)}")

        case enum.GAS_DENSITY:
            match option:
                case 1:
                    molar_mass = float(input("Введите молярную массу: "))
                    molar_volume = float(input("Введите молярный объем: "))
                    print(f"Плотность = {calcs.calc_gas_density(molar_mass, molar_volume)}")
                case 2:
                    gas_density = float(input("Введите плотность газа: "))
                    molar_volume = float(input("Введите молярный объем: "))
                    print(f"Молярная масса = {calcs.calc_molar_mass_gas_density(gas_density, molar_volume)}")

        case enum.MASS_FRACTION:
            match option:
                case 1:
                    substance_mass = float(input("Введите массу вещества: "))
                    solution_mass = float(input("Введите массу раствора: "))
                    print(f"Массовая доля = {calcs.calc_mass_fraction(substance_mass, solution_mass)}")
                case 2:
                    mass_fraction = float(input("Введите массовую долю: "))
                    solution_mass = float(input("Введите массу раствора: "))
                    print(f"Масса вещества = {calcs.calc_substance_mass_mass_fraction(mass_fraction, solution_mass)}")
                case 3:
                    substance_mass = float(input("Введите массу вещества: "))
                    mass_fraction = float(input("Введите массовую долю: "))
                    print(f"Масса раствора = {calcs.calc_solution_mass_mass_fraction(substance_mass, mass_fraction)}")

        case enum.MOLAR_CONCENTRATION:
            match option:
                case 1:
                    substance_amount = float(input("Введите количество вещества: "))
                    volume = float(input("Введите объем: "))
                    print(f"Концентрация = {calcs.calc_molar_concentration(substance_amount, volume)}")
                case 2:
                    concentration = float(input("Введите концентрацию: "))
                    volume = float(input("Введите объем: "))
                    print(f"Количество вещества = {calcs.calc_substance_amount_molar_concentration(concentration, volume)}")
                case 3:
                    substance_amount = float(input("Введите количество вещества: "))
                    concentration = float(input("Введите концентрацию: "))
                    print(f"Объем = {calcs.calc_volume_molar_concentration(substance_amount, concentration)}")

        case enum.SOLUTION_MASS:
            match option:
                case 1:
                    substance_mass = float(input("Введите массу вещества: "))
                    solvent_mass = float(input("Введите массу растворителя: "))
                    print(f"Масса раствора = {calcs.calc_solution_mass(substance_mass, solvent_mass)}")
                case 2:
                    solution_mass = float(input("Введите массу раствора: "))
                    solvent_mass = float(input("Введите массу растворителя: "))
                    print(f"Масса вещества = {calcs.calc_substance_mass_solution_mass(solution_mass, solvent_mass)}")
                case 3:
                    solution_mass = float(input("Введите массу раствора: "))
                    substance_mass = float(input("Введите массу вещества: "))
                    print(f"Масса растворителя = {calcs.calc_solvent_mass_solution_mass(solution_mass, substance_mass)}")

        case enum.MASS_CONSERVATION:
            match option:
                case 1:
                    reactants_mass = float(input("Введите массу реагентов: "))
                    print(f"Масса продуктов = {calcs.calc_mass_conservation(reactants_mass)}")
                case 2:
                    products_mass = float(input("Введите массу продуктов: "))
                    print(f"Масса реагентов = {calcs.calc_reactants_mass_conservation(products_mass)}")

        case enum.REACTION_YIELD:
            match option:
                case 1:
                    practical_mass = float(input("Введите практическую массу: "))
                    theoretical_mass = float(input("Введите теоретическую массу: "))
                    print(f"Выход реакции = {calcs.calc_reaction_yield(practical_mass, theoretical_mass)}")
                case 2:
                    reaction_yield = float(input("Введите выход реакции (%): "))
                    theoretical_mass = float(input("Введите теоретическую массу: "))
                    print(f"Практическая масса = {calcs.calc_practical_mass_reaction_yield(reaction_yield, theoretical_mass)}")
                case 3:
                    practical_mass = float(input("Введите практическую массу: "))
                    reaction_yield = float(input("Введите выход реакции (%): "))
                    print(f"Теоретическая масса = {calcs.calc_theoretical_mass_reaction_yield(practical_mass, reaction_yield)}")

        case enum.HEAT_AMOUNT:
            match option:
                case 1:
                    heat_capacity = float(input("Введите удельную теплоемкость: "))
                    mass = float(input("Введите массу: "))
                    delta_temperature = float(input("Введите изменение температуры: "))
                    print(f"Количество теплоты = {calcs.calc_heat_amount(heat_capacity, mass, delta_temperature)}")
                case 2:
                    heat_amount = float(input("Введите количество теплоты: "))
                    mass = float(input("Введите массу: "))
                    delta_temperature = float(input("Введите изменение температуры: "))
                    print(f"Удельная теплоемкость = {calcs.calc_heat_capacity_heat_amount(heat_amount, mass, delta_temperature)}")

        case enum.REACTION_HEAT_EFFECT:
            match option:
                case 1:
                    substance_amount = float(input("Введите количество вещества: "))
                    enthalpy_change = float(input("Введите изменение энтальпии: "))
                    print(f"Тепловой эффект = {calcs.calc_reaction_heat_effect(substance_amount, enthalpy_change)}")
                case 2:
                    heat_amount = float(input("Введите тепловой эффект: "))
                    enthalpy_change = float(input("Введите изменение энтальпии: "))
                    print(f"Количество вещества = {calcs.calc_substance_amount_reaction_heat_effect(heat_amount, enthalpy_change)}")

        case enum.FARADAY_LAW:
            match option:
                case 1:
                    molar_mass = float(input("Введите молярную массу: "))
                    current = float(input("Введите силу тока: "))
                    time = float(input("Введите время: "))
                    electrons_count = float(input("Введите число электронов: "))
                    print(f"Масса вещества = {calcs.calc_faraday_law(molar_mass, current, time, electrons_count)}")
                case 2:
                    deposited_mass = float(input("Введите массу вещества: "))
                    molar_mass = float(input("Введите молярную массу: "))
                    time = float(input("Введите время: "))
                    electrons_count = float(input("Введите число электронов: "))
                    print(f"Сила тока = {calcs.calc_current_faraday_law(deposited_mass, molar_mass, time, electrons_count)}")
                case 3:
                    deposited_mass = float(input("Введите массу вещества: "))
                    molar_mass = float(input("Введите молярную массу: "))
                    current = float(input("Введите силу тока: "))
                    electrons_count = float(input("Введите число электронов: "))
                    print(f"Время = {calcs.calc_time_faraday_law(deposited_mass, molar_mass, current, electrons_count)}")

        case enum.EQUILIBRIUM_CONSTANT:
            match option:
                case 1:
                    products_concentration = float(input("Введите концентрацию продуктов: "))
                    reactants_concentration = float(input("Введите концентрацию реагентов: "))
                    print(f"Константа равновесия = {calcs.calc_equilibrium_constant(products_concentration, reactants_concentration)}")
                case 2:
                    products_concentration = float(input("Введите концентрацию продуктов: "))
                    products_coefficient = float(input("Введите степень у продуктов: "))
                    reactants_concentration = float(input("Введите концентрацию реагентов: "))
                    reactants_coefficient = float(input("Введите степень у реагентов: "))
                    print(
                        "Константа равновесия = "
                        f"{calcs.calc_equilibrium_constant_with_coefficients(products_concentration, products_coefficient, reactants_concentration, reactants_coefficient)}"
                    )

        case enum.REACTION_RATE:
            match option:
                case 1:
                    delta_concentration = float(input("Введите изменение концентрации: "))
                    delta_time = float(input("Введите промежуток времени: "))
                    print(f"Скорость реакции = {calcs.calc_reaction_rate(delta_concentration, delta_time)}")
                case 2:
                    rate = float(input("Введите скорость реакции: "))
                    delta_time = float(input("Введите промежуток времени: "))
                    print(f"Изменение концентрации = {calcs.calc_delta_concentration_reaction_rate(rate, delta_time)}")

        case enum.RATE_LAW:
            match option:
                case 1:
                    rate_constant = float(input("Введите константу скорости: "))
                    concentration_a = float(input("Введите концентрацию A: "))
                    order_a = float(input("Введите порядок по A: "))
                    concentration_b = float(input("Введите концентрацию B: "))
                    order_b = float(input("Введите порядок по B: "))
                    print(
                        f"Скорость реакции = {calcs.calc_reaction_rate_law(rate_constant, concentration_a, order_a, concentration_b, order_b)}"
                    )
                case 2:
                    rate = float(input("Введите скорость реакции: "))
                    concentration_a = float(input("Введите концентрацию A: "))
                    order_a = float(input("Введите порядок по A: "))
                    concentration_b = float(input("Введите концентрацию B: "))
                    order_b = float(input("Введите порядок по B: "))
                    print(
                        f"Константа скорости = {calcs.calc_rate_constant_reaction_rate(rate, concentration_a, order_a, concentration_b, order_b)}"
                    )

        case enum.PH:
            match option:
                case 1:
                    hydrogen_ion_concentration = float(input("Введите концентрацию H+: "))
                    print(f"pH = {calcs.calc_ph(hydrogen_ion_concentration)}")
                case 2:
                    ph = float(input("Введите pH: "))
                    print(f"Концентрация H+ = {calcs.calc_hydrogen_ion_concentration(ph)}")

        case enum.POH:
            match option:
                case 1:
                    hydroxide_ion_concentration = float(input("Введите концентрацию OH-: "))
                    print(f"pOH = {calcs.calc_poh(hydroxide_ion_concentration)}")
                case 2:
                    poh = float(input("Введите pOH: "))
                    print(f"Концентрация OH- = {calcs.calc_hydroxide_ion_concentration(poh)}")

        case enum.PH_POH_RELATION:
            match option:
                case 1:
                    ph = float(input("Введите pH: "))
                    print(f"pOH = {calcs.calc_poh_from_ph(ph)}")
                case 2:
                    poh = float(input("Введите pOH: "))
                    print(f"pH = {calcs.calc_ph_from_poh(poh)}")

        case enum.FREEZING_POINT_DEPRESSION:
            match option:
                case 1:
                    cryoscopic_constant = float(input("Введите Kf: "))
                    molality = float(input("Введите моляльность: "))
                    print(f"ΔT = {calcs.calc_freezing_point_depression(cryoscopic_constant, molality)}")
                case 2:
                    freezing_point_depression = float(input("Введите ΔT: "))
                    molality = float(input("Введите моляльность: "))
                    print(f"Kf = {calcs.calc_cryoscopic_constant(freezing_point_depression, molality)}")

        case enum.BOILING_POINT_ELEVATION:
            match option:
                case 1:
                    ebullioscopic_constant = float(input("Введите Kb: "))
                    molality = float(input("Введите моляльность: "))
                    print(f"ΔT = {calcs.calc_boiling_point_elevation(ebullioscopic_constant, molality)}")
                case 2:
                    boiling_point_elevation = float(input("Введите ΔT: "))
                    molality = float(input("Введите моляльность: "))
                    print(f"Kb = {calcs.calc_ebullioscopic_constant(boiling_point_elevation, molality)}")

        case enum.PHOTON_ENERGY:
            match option:
                case 1:
                    frequency = float(input("Введите частоту: "))
                    print(f"Энергия фотона = {calcs.calc_photon_energy(frequency)}")
                case 2:
                    energy = float(input("Введите энергию: "))
                    print(f"Частота = {calcs.calc_frequency_photon_energy(energy)}")

        case enum.REACTION_STOICHIOMETRY:
            match option:
                case 1:
                    run_console_reaction_equation()


def _format_number(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return f"{value:.6f}".rstrip("0").rstrip(".")


def _resolve_element_query(query: str):
    text = query.strip()
    if not text:
        return None

    if text.isdigit():
        return ptbl.ELEMENTS_BY_NUMBER.get(int(text))

    normalized_symbol = text[0].upper() + text[1:].lower() if len(text) > 1 else text.upper()
    element = ptbl.ELEMENTS_BY_SYMBOL.get(normalized_symbol)
    if element is not None:
        return element

    element = ptbl.ELEMENTS_BY_ENGLISH_NAME.get(text.lower())
    if element is not None:
        return element

    symbol = ptbl.RUSSIAN_TO_SYMBOL.get(text.lower())
    if symbol is not None:
        return ptbl.ELEMENTS_BY_SYMBOL.get(symbol)

    return None


def _parse_formula_composition(formula: str) -> dict[str, float]:
    composition = chemparse.parse_formula(formula)

    if not composition:
        raise ValueError(f"Не удалось разобрать формулу: {formula}")

    normalized: dict[str, float] = {}
    for symbol, count in composition.items():
        if ptbl.ELEMENTS_BY_SYMBOL.get(symbol) is None:
            raise ValueError(f"Неизвестный элемент в формуле: {symbol}")
        normalized[symbol] = float(count)

    return normalized


def _format_composition(composition: dict[str, float]) -> str:
    parts: list[str] = []
    for symbol, count in composition.items():
        element = ptbl.ELEMENTS_BY_SYMBOL[symbol]
        russian_name = ptbl.RUSSIAN_NAMES_BY_SYMBOL.get(symbol, element.name.title())
        parts.append(f"{symbol} ({russian_name}) × {_format_number(float(count))}")
    return ", ".join(parts)


def _format_reaction_side(items: list[dict[str, object]]) -> str:
    parts: list[str] = []
    for item in items:
        coefficient = int(item["coefficient"])
        prefix = "" if coefficient == 1 else str(coefficient)
        parts.append(f"{prefix}{item['formula']}")
    return " + ".join(parts)


def _balance_reaction(reactants: list[dict[str, object]], products: list[dict[str, object]]) -> None:
    species = reactants + products
    elements: list[str] = []
    for item in species:
        for symbol in item["composition"]:
            if symbol not in elements:
                elements.append(symbol)

    matrix_rows: list[list[sp.Rational]] = []
    for symbol in elements:
        row: list[sp.Rational] = []
        for item in reactants:
            row.append(-sp.Rational(int(item["composition"].get(symbol, 0))))
        for item in products:
            row.append(sp.Rational(int(item["composition"].get(symbol, 0))))
        matrix_rows.append(row)

    matrix = sp.Matrix(matrix_rows)
    nullspace = matrix.nullspace()
    if not nullspace:
        raise ValueError("Не удалось уравнять реакцию. Проверь формулы веществ.")

    vector = nullspace[0]
    denominators = [term.as_numer_denom()[1] for term in vector]
    common_multiple = sp.lcm(denominators) if denominators else 1
    coefficients = [sp.Integer(term * common_multiple) for term in vector]

    sign = 1
    for value in coefficients:
        if value != 0:
            sign = -1 if value < 0 else 1
            break
    coefficients = [int(value * sign) for value in coefficients]

    if any(value <= 0 for value in coefficients):
        raise ValueError("Не удалось получить положительные коэффициенты реакции.")

    common_divisor = int(sp.gcd(coefficients))
    if common_divisor > 1:
        coefficients = [value // common_divisor for value in coefficients]

    for item, coefficient in zip(species, coefficients, strict=True):
        item["coefficient"] = coefficient


def _prompt_quantity(name: str, molar_mass: float) -> float:
    while True:
        unit = input(f"Единица для {name} (1 - моль, 2 - г): ").strip()
        if unit not in {"1", "2"}:
            print("Нужно выбрать 1 или 2")
            continue

        try:
            value = float(input(f"Введите количество для {name}: "))
        except ValueError:
            print("Нужно ввести число")
            continue

        return value if unit == "1" else value / molar_mass


def _count_atoms(items: list[dict[str, object]]) -> dict[str, int]:
    totals: dict[str, int] = {}
    for item in items:
        coefficient = int(item["coefficient"])
        composition = item["composition"]
        for symbol, count in composition.items():
            totals[symbol] = totals.get(symbol, 0) + int(count) * coefficient
    return totals


def _format_atom_counts(counts: dict[str, int]) -> str:
    if not counts:
        return "—"

    parts: list[str] = []
    for symbol in sorted(counts):
        name = ptbl.RUSSIAN_NAMES_BY_SYMBOL.get(symbol, ptbl.ELEMENTS_BY_SYMBOL[symbol].name.title())
        parts.append(f"{symbol} ({name}) = {counts[symbol]}")
    return ", ".join(parts)


def _prompt_species(side_name: str, index: int) -> dict[str, object]:
    while True:
        raw = input(
            f"Введите {side_name} {index} (символ/название элемента или формулу вещества): "
        ).strip()
        if not raw:
            print("Вещество не может быть пустым")
            continue

        element = _resolve_element_query(raw)
        if element is not None:
            formula = element.symbol
            display_name = ptbl.RUSSIAN_NAMES_BY_SYMBOL.get(element.symbol, element.name.title())
            composition = {element.symbol: 1}
            break

        try:
            composition = _parse_formula_composition(raw)
        except ValueError as exc:
            print(exc)
            continue

        formula = raw
        display_name = raw
        break

    molar_mass = calcs.calc_molar_mass_by_formula(formula)
    return {
        "formula": formula,
        "display_name": display_name,
        "composition": composition,
        "molar_mass": molar_mass,
    }


def _extract_single_element_symbol(species: dict[str, object]) -> str | None:
    composition = species["composition"]
    if len(composition) != 1:
        return None
    return next(iter(composition))


def _formula_from_ions(cation_symbol: str, cation_charge: int, anion_symbol: str, anion_charge: int) -> str:
    cation_index = abs(anion_charge)
    anion_index = abs(cation_charge)

    divisor = int(sp.gcd([cation_index, anion_index]))
    cation_index //= divisor
    anion_index //= divisor

    cation_part = cation_symbol if cation_index == 1 else f"{cation_symbol}{cation_index}"
    anion_part = anion_symbol if anion_index == 1 else f"{anion_symbol}{anion_index}"
    return f"{cation_part}{anion_part}"


def _infer_products_from_reactants(reactants: list[dict[str, object]]) -> list[dict[str, object]]:
    if len(reactants) != 2:
        raise ValueError("Авто-расчёт продукта сейчас поддерживает ровно 2 реагента")

    symbol_a = _extract_single_element_symbol(reactants[0])
    symbol_b = _extract_single_element_symbol(reactants[1])
    if symbol_a is None or symbol_b is None:
        raise ValueError("Авто-расчёт продукта поддерживает реагенты-элементы (например Fe и O2)")

    if symbol_a == symbol_b:
        raise ValueError("Реагенты должны быть разными элементами")

    charge_a = COMMON_OXIDATION_STATES.get(symbol_a)
    charge_b = COMMON_OXIDATION_STATES.get(symbol_b)
    if charge_a is None or charge_b is None:
        raise ValueError("Для одного из элементов нет правила степени окисления в текущем справочнике")

    if charge_a * charge_b >= 0:
        raise ValueError("Элементы должны иметь противоположные степени окисления для бинарного соединения")

    if charge_a > 0:
        product_formula = _formula_from_ions(symbol_a, charge_a, symbol_b, charge_b)
    else:
        product_formula = _formula_from_ions(symbol_b, charge_b, symbol_a, charge_a)

    composition = _parse_formula_composition(product_formula)
    molar_mass = calcs.calc_molar_mass_by_formula(product_formula)
    return [
        {
            "formula": product_formula,
            "display_name": product_formula,
            "composition": composition,
            "molar_mass": molar_mass,
        }
    ]


def run_console_reaction_equation() -> None:
    reactants_count = int(input("Количество реагентов: "))
    if reactants_count <= 0:
        print("Количество веществ должно быть положительным")
        return

    reactants = [_prompt_species("реагент", index) for index in range(1, reactants_count + 1)]

    try:
        products = _infer_products_from_reactants(reactants)
    except ValueError as exc:
        print(exc)
        return

    try:
        _balance_reaction(reactants, products)
    except ValueError as exc:
        print(exc)
        return

    substances = [
        {**item, "side": "реагент"} for item in reactants
    ] + [
        {**item, "side": "продукт"} for item in products
    ]

    print("\nСобранное уравнение:")
    print(f"{_format_reaction_side(reactants)} -> {_format_reaction_side(products)}")

    print("\nВещества и состав:")
    for index, item in enumerate(substances, start=1):
        print(
            f"{index}. {item['formula']} ({item['side']}), "
            f"коэффициент {item['coefficient']}, "
            f"M = {_format_number(float(item['molar_mass']))} г/моль"
        )
        print(f"   Состав: {_format_composition(item['composition'])}")

    print("\nУравнение сбалансировано.")

    print("\nВведите количество каждого реагента, чтобы вычислить продукты.")
    reactant_amounts: list[float] = []
    for item in reactants:
        reactant_amounts.append(_prompt_quantity(item["formula"], float(item["molar_mass"])))

    limiting_values = [amount / int(item["coefficient"]) for amount, item in zip(reactant_amounts, reactants, strict=True)]
    reaction_extent = min(limiting_values)
    limiting_index = limiting_values.index(reaction_extent)
    limiting_item = reactants[limiting_index]

    print(f"\nЛимитирующий реагент: {limiting_item['formula']}")
    print(f"Количество лимитирующего реагента: {_format_number(reactant_amounts[limiting_index])} моль")
    print("\nРезультаты реакции:")

    for item in reactants:
        coefficient = int(item["coefficient"])
        required_amount = coefficient * reaction_extent
        remaining = reactant_amounts[reactants.index(item)] - required_amount
        print(
            f"- {item['formula']} (реагент): израсходовано {_format_number(required_amount)} моль, "
            f"остаток {_format_number(max(remaining, 0.0))} моль"
        )

    for item in products:
        coefficient = int(item["coefficient"])
        amount = coefficient * reaction_extent
        mass = amount * float(item["molar_mass"])
        print(
            f"- {item['formula']} (продукт): n = {_format_number(amount)} моль, "
            f"m = {_format_number(mass)} г"
        )
