##################################
#ЭЛЕКТРОСТАТИКА И ЭЛЕКТРОДИНАМИКА#
##################################

import electrodynamics.enum as enum
import electrodynamics.calculations as calcs

def formula_selection(input_text, enum_formula):
    option = int(input(input_text))

    match enum_formula:
        case enum.COULOMBS_LAW:
            match option:
                case 1:
                    electric_charge_1 = float(input("Введите электрический заряд №1: "))
                    electric_charge_2 = float(input("Введите электрический заряд №2: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Сила = {calcs.calc_coulombs_law(electric_charge_1, electric_charge_2, distance)}")
                case 2:
                    force = float(input("Введите силу: "))
                    electric_charge_2 = float(input("Введите электрический заряд №2: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Электрический заряд №1 = {calcs.calc_electric_charge_1_coulombs_law(force, electric_charge_2, distance)}")
                case 3:
                    force = float(input("Введите силу: "))
                    electric_charge_1 = float(input("Введите электрический заряд №1: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Электрический заряд №2 = {calcs.calc_electric_charge_2_coulombs_law(force, electric_charge_1, distance)}")
                case 4:
                    force = float(input("Введите силу: "))
                    electric_charge_1 = float(input("Введите электрический заряд №1: "))
                    electric_charge_2 = float(input("Введите электрический заряд №2: "))
                    print(f"Расстояние = {calcs.calc_distance_coulombs_law(force, electric_charge_1, electric_charge_2)}")

        case enum.EL_FIELD_INTENSITY:
            match option:
                case 1:
                    force = float(input("Введите силу: "))
                    electric_charge = float(input("Введите величину заряда: "))
                    print(f"Напряженность = {calcs.calc_el_field_intensity(force, electric_charge)}")
                case 2:
                    density = float(input("Введите напряженность: "))
                    electric_charge = float(input("Введите величину заряда: "))
                    print(f"Сила = {calcs.calc_force_el_field_intensity(density, electric_charge)}")
                case 3:
                    force = float(input("Введите силу: "))
                    density = float(input("Введите напряженность: "))
                    print(f"Величина заряда = {calcs.calc_electric_charge_el_field_intensity(force, density)}")

        case enum.POINT_CHARGE_EL_FIELD_INTENSITY:
            match option:
                case 1:
                    electric_charge = float(input("Введите величину заряда: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Напряженность = {calcs.calc_point_charge_el_field_intensity(electric_charge, distance)}")
                case 2:
                    intensity = float(input("Введите напряженность: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Величина заряда = {calcs.calc_electric_charge_point_charge_el_field_intensity(intensity, distance)}")
                case 3:
                    intensity = float(input("Введите напряженность: "))
                    electric_charge = float(input("Введите величину заряда: "))
                    print(f"Расстояние = {calcs.calc_distance_charge_point_charge_el_field_intensity(intensity, electric_charge)}")

        case enum.SURFACE_CHARGE_DENSITY:
            match option:
                case 1:
                    electric_charge = float(input("Введите величину заряда: "))
                    area = float(input("Введите площадь: "))
                    print(f"Поверхностная плотность зарядов = {calcs.calc_surface_charge_density(electric_charge, area)}")
                case 2:
                    density = float(input("Введите поверхностную плотность зарядов: "))
                    area = float(input("Введите площадь: "))
                    print(f"Электрический заряд = {calcs.calc_electric_charge_surface_charge_density(density, area)}")
                case 3:
                    density = float(input("Введите поверхностную плотность зарядов: "))
                    electric_charge = float(input("Введите величину заряда: "))
                    print(f"Площадь = {calcs.calc_area_surface_charge_density(density, electric_charge)}")

        case enum.INFINITY_SURFACE_EL_FIELD_INTENSITY:
            match option:
                case 1:
                    density = float(input("Введите поверхностную плотность зарядов: "))
                    print(f"Напряженность = {calcs.calc_infinity_surface_el_field_intensity(density)}")
                case 2:
                    intensity = float(input("Введите напряженность: "))
                    print(f"Поверхностная плотность зарядов = {calcs.calc_density_infinity_surface_el_field_intensity(intensity)}")

        case enum.DIELECTRIC_CONSTANT:
            match option:
                case 1:
                    intensity_1 = float(input("Введите напряженность эл. поля в вакууме: "))
                    intensity_2 = float(input("Введите напряженность эл. поля в диэлектрике: "))
                    print(f"Диэлектрическая проницаемость = {calcs.calc_dielectric_constant(intensity_1, intensity_2)}")
                case 2:
                    dielectric_constant = float(input("Введите диэлектрическую проницаемость: "))
                    intensity_2 = float(input("Введите напряженность эл. поля в диэлектрике: "))
                    print(f"Напряженность в вакууме = {calcs.calc_intensity_1_dielectric_constant(dielectric_constant, intensity_2)}")
                case 3:
                    dielectric_constant = float(input("Введите диэлектрическую проницаемость: "))
                    intensity_1 = float(input("Введите напряженность эл. поля в вакууме: "))
                    print(f"Напряженность в диэлектрике = {calcs.calc_intensity_2_dielectric_constant(dielectric_constant, intensity_1)}")

        case enum.INTERACTING_CHARGES_POTENTIAL_ENERGY:
            match option:
                case 1:
                    electric_charge_1 = float(input("Введите электрический заряд №1: "))
                    electric_charge_2 = float(input("Введите электрический заряд №2: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Потенциальная энергия = {calcs.calc_potential_energy(electric_charge_1, electric_charge_2, distance)}")
                case 2:
                    force = float(input("Введите потенциальную энергию: "))
                    electric_charge_2 = float(input("Введите электрический заряд №2: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Электрический заряд №1 = {calcs.calc_electric_charge_1_potential_energy(force, electric_charge_2, distance)}")
                case 3:
                    force = float(input("Введите потенциальную энергию: "))
                    electric_charge_1 = float(input("Введите электрический заряд №1: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Электрический заряд №2 = {calcs.calc_electric_charge_2_potential_energy(force, electric_charge_1, distance)}")
                case 4:
                    force = float(input("Введите потенциальную энергию: "))
                    electric_charge_1 = float(input("Введите электрический заряд №1: "))
                    electric_charge_2 = float(input("Введите электрический заряд №2: "))
                    print(f"Расстояние = {calcs.calc_distance_potential_energy(force, electric_charge_1, electric_charge_2)}")

        case enum.POTENTIAL:
            match option:
                case 1:
                    potential_energy = float(input("Введите потенциальную энергию: "))
                    electric_charge = float(input("Введите величину заряда: "))
                    print(f"Потенциал = {calcs.calc_potential(potential_energy, electric_charge)}")
                case 2:
                    potential = float(input("Введите потенциал: "))
                    electric_charge = float(input("Введите величину заряда: "))
                    print(f"Потенциальная энергия = {calcs.calc_potential_energy_potential(potential, electric_charge)}")
                case 3:
                    potential = float(input("Введите потенциал: "))
                    potential_energy = float(input("Введите потенциальную энергию: "))
                    print(f"Величина заряда = {calcs.calc_electric_charge_potential(potential, potential_energy)}")

        case enum.POINT_CHARGE_POTENTIAL:
            match option:
                case 1:
                    electric_charge = float(input("Введите величину заряда: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Потенциал = {calcs.calc_point_charge_potential(electric_charge, distance)}")
                case 2:
                    potential = float(input("Введите потенциал: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Величина заряда = {calcs.calc_electric_charge_point_charge_potential(potential, distance)}")
                case 3:
                    potential = float(input("Введите потенциал: "))
                    electric_charge = float(input("Введите величину заряда: "))
                    print(f"Расстояние = {calcs.calc_distance_point_charge_potential(potential, electric_charge)}")

        case enum.VOLTAGE:
            match option:
                case 1:
                    work = float(input("Введите работу: "))
                    electric_charge = float(input("Введите величину заряда: "))
                    print(f"Напряжение = {calcs.calc_voltage(work, electric_charge)}")
                case 2:
                    voltage = float(input("Введите напряжение: "))
                    electric_charge = float(input("Введите величину заряда: "))
                    print(f"Работа = {calcs.calc_work_voltage(voltage, electric_charge)}")
                case 3:
                    voltage = float(input("Введите напряжение: "))
                    work = float(input("Введите работу: "))
                    print(f"Величина заряда = {calcs.calc_electric_charge_voltage(voltage, work)}")

        case enum.EL_FIELD_VOLTAGE:
            match option:
                case 1:
                    intensity = float(input("Введите напряженность: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Напряжение = {calcs.calc_el_field_voltage(intensity, distance)}")
                case 2:
                    voltage = float(input("Введите напряжение: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Напряженность = {calcs.calc_intensity_el_field_voltage(voltage, distance)}")
                case 3:
                    voltage = float(input("Введите напряжение: "))
                    intensity = float(input("Введите напряженность: "))
                    print(f"Расстояние = {calcs.calc_distance_el_field_voltage(voltage, intensity)}")

        case enum.EL_CAPACITY:
            match option:
                case 1:
                    electric_charge = float(input("Введите величину заряда: "))
                    voltage = float(input("Введите напряжение: "))
                    print(f"Электроёмкость = {calcs.calc_el_capacity(electric_charge, voltage)}")
                case 2:
                    capacity = float(input("Введите электроёмкость: "))
                    voltage = float(input("Введите напряжение: "))
                    print(f"Величина заряда = {calcs.calc_charge_el_capacity(capacity, voltage)}")
                case 3:
                    capacity = float(input("Введите электроёмкость: "))
                    electric_charge = float(input("Введите величину заряда: "))
                    print(f"Напряжение = {calcs.calc_voltage_el_capacity(capacity, electric_charge)}")

        case enum.FLAT_CAPACITOR_EL_CAPACITY:
            match option:
                case 1:
                    area = float(input("Введите площадь пластин: "))
                    relative_perm = float(input("Введите относительную диэлектрическую проницаемость: "))
                    distance = float(input("Введите расстояние между пластинами: "))
                    print(f"Электроёмкость = {calcs.calc_flat_capacitor_capacity(area, relative_perm, distance)}")
                case 2:
                    capacity = float(input("Введите электроёмкость: "))
                    relative_perm = float(input("Введите относительную диэлектрическую проницаемость: "))
                    distance = float(input("Введите расстояние между пластинами: "))
                    print(f"Площадь пластин = {calcs.calc_area_flat_capacitor_capacity(capacity, relative_perm, distance)}")
                case 3:
                    capacity = float(input("Введите электроёмкость: "))
                    area = float(input("Введите площадь пластин: "))
                    distance = float(input("Введите расстояние между пластинами: "))
                    print(f"Относительная диэлектрическая проницаемость = {calcs.calc_relative_perm_flat_capacitor_capacity(capacity, area, distance)}")
                case 4:
                    capacity = float(input("Введите электроёмкость: "))
                    area = float(input("Введите площадь пластин: "))
                    relative_perm = float(input("Введите относительную диэлектрическую проницаемость: "))
                    print(f"Расстояние между пластинами = {calcs.calc_distance_flat_capacitor_capacity(capacity, area, relative_perm)}")

        case enum.CURRENT:
            match option:
                case 1:
                    charge = float(input("Введите величину заряда: "))
                    time = float(input("Введите время: "))
                    print(f"Сила тока = {calcs.calc_current(charge, time)}")
                case 2:
                    current = float(input("Введите силу тока: "))
                    time = float(input("Введите время: "))
                    print(f"Величина заряда = {calcs.calc_charge_current(current, time)}")
                case 3:
                    charge = float(input("Введите величину заряда: "))
                    current = float(input("Введите силу тока: "))
                    print(f"Время = {calcs.calc_time_current(charge, current)}")

        case enum.CONDUCTOR_RESISTANCE:
            match option:
                case 1:
                    resistivity = float(input("Введите удельное сопротивление: "))
                    length = float(input("Введите длину проводника: "))
                    area = float(input("Введите площадь: "))
                    print(f"Сопротивление = {calcs.calc_conductor_resistance(resistivity, length, area)}")
                case 2:
                    resistance = float(input("Введите сопротивление: "))
                    length = float(input("Введите длину проводника: "))
                    area = float(input("Введите площадь: "))
                    print(f"Удельное сопротивление = {calcs.calc_resistivity_conductor(resistance, length, area)}")
                case 3:
                    resistance = float(input("Введите сопротивление: "))
                    resistivity = float(input("Введите удельное сопротивление: "))
                    area = float(input("Введите площадь: "))
                    print(f"Длина проводника = {calcs.calc_length_conductor(resistance, resistivity, area)}")
                case 4:
                    resistivity = float(input("Введите удельное сопротивление: "))
                    length = float(input("Введите длину проводника: "))
                    resistance = float(input("Введите сопротивление: "))
                    print(f"Площадь = {calcs.calc_area_conductor(resistivity, length, resistance)}")

        case enum.SECTION_CIRCUIT_OHMS_LAW:
            match option:
                case 1:
                    voltage = float(input("Введите напряжение: "))
                    resistance = float(input("Введите сопротивление: "))
                    print(f"Сила тока = {calcs.calc_section_current(voltage, resistance)}")
                case 2:
                    current = float(input("Введите силу тока: "))
                    resistance = float(input("Введите сопротивление: "))
                    print(f"Напряжение = {calcs.calc_section_voltage(current, resistance)}")
                case 3:
                    voltage = float(input("Введите напряжение: "))
                    current = float(input("Введите силу тока: "))
                    print(f"Сопротивление = {calcs.calc_section_resistance(voltage, current)}")

        case enum.EL_CURRENT_POWER:
            match option:
                case 1:
                    current = float(input("Введите силу тока: "))
                    voltage = float(input("Введите напряжение: "))
                    print(f"Мощность = {calcs.calc_el_current_power(current, voltage)}")
                case 2:
                    power = float(input("Введите мощность: "))
                    voltage = float(input("Введите напряжение: "))
                    print(f"Сила тока = {calcs.calc_current_el_current_power(power, voltage)}")
                case 3:
                    power = float(input("Введите мощность: "))
                    current = float(input("Введите силу тока: "))
                    print(f"Напряжение = {calcs.calc_voltage_el_current_power(power, current)}")

        case enum.JOULE_LENZ_LAW:
            match option:
                case 1:
                    current = float(input("Введите силу тока: "))
                    resistance = float(input("Введите сопротивление: "))
                    time = float(input("Введите время: "))
                    print(f"Кол-во теплоты = {calcs.calc_joule_lenz_heat(current, resistance, time)}")
                case 2:
                    heat = float(input("Введите кол-во теплоты: "))
                    resistance = float(input("Введите сопротивление: "))
                    time = float(input("Введите время: "))
                    print(f"Сила тока = {calcs.calc_current_joule_lenz(heat, resistance, time)}")
                case 3:
                    heat = float(input("Введите кол-во теплоты: "))
                    current = float(input("Введите силу тока: "))
                    time = float(input("Введите время: "))
                    print(f"Сопротивление = {calcs.calc_resistance_joule_lenz(heat, current, time)}")
                case 4:
                    heat = float(input("Введите кол-во теплоты: "))
                    current = float(input("Введите силу тока: "))
                    resistance = float(input("Введите сопротивление: "))
                    print(f"Время = {calcs.calc_time_joule_lenz(heat, current, resistance)}")

        case enum.FULL_CIRCUIT_OHMS_LAW:
            match option:
                case 1:
                    emf = float(input("Введите электродвижущую силу: "))
                    external_resistance = float(input("Введите сопротивление внешней цепи: "))
                    internal_resistance = float(input("Введите внутреннее сопротивление: "))
                    print(f"Сила тока = {calcs.calc_full_circuit_current(emf, external_resistance, internal_resistance)}")
                case 2:
                    current = float(input("Введите силу тока: "))
                    external_resistance = float(input("Введите сопротивление внешней цепи: "))
                    internal_resistance = float(input("Введите внутреннее сопротивление: "))
                    print(f"ЭДС источника = {calcs.calc_emf_full_circuit(current, external_resistance, internal_resistance)}")
                case 3:
                    emf = float(input("Введите электродвижущую силу: "))
                    current = float(input("Введите силу тока: "))
                    internal_resistance = float(input("Введите внутреннее сопротивление: "))
                    print(f"Сопротивление внешней цепи = {calcs.calc_external_resistance_full_circuit(emf, current, internal_resistance)}")
                case 4:
                    emf = float(input("Введите электродвижущую силу: "))
                    current = float(input("Введите силу тока: "))
                    external_resistance = float(input("Введите сопротивление внешней цепи: "))
                    print(f"Внутреннее сопротивление = {calcs.calc_internal_resistance_full_circuit(emf, current, external_resistance)}")

        case enum.SHORT_CIRCUIT_CURRENT:
            match option:
                case 1:
                    emf = float(input("Введите электродвижущую силу: "))
                    internal_resistance = float(input("Введите внутреннее сопротивление: "))
                    print(f"Короткозамкнутый ток = {calcs.calc_short_circuit_current(emf, internal_resistance)}")
                case 2:
                    current = float(input("Введите силу тока: "))
                    internal_resistance = float(input("Введите внутреннее сопротивление: "))
                    print(f"ЭДС источника = {calcs.calc_emf_short_circuit(current, internal_resistance)}")
                case 3:
                    emf = float(input("Введите электродвижущую силу: "))
                    current = float(input("Введите силу тока: "))
                    print(f"Внутреннее сопротивление = {calcs.calc_internal_resistance_short_circuit(emf, current)}")

        case enum.MAGNETIC_INDUCTION_VECTOR:
            match option:
                case 1:
                    force_max = float(input("Введите максимальную силу Ампера: "))
                    length = float(input("Введите длину проводника: "))
                    current = float(input("Введите силу тока: "))
                    print(f"Вектор магнитной индукции = {calcs.calc_magnetic_induction_vector(force_max, length, current)}")
                case 2:
                    B = float(input("Введите вектор магнитной индукции: "))
                    length = float(input("Введите длину проводника: "))
                    current = float(input("Введите силу тока: "))
                    print(f"Максимальная сила Ампера = {calcs.calc_force_max_magnetic_induction(B, length, current)}")
                case 3:
                    force_max = float(input("Введите максимальную силу Ампера: "))
                    B = float(input("Введите вектор магнитной индукции: "))
                    current = float(input("Введите силу тока: "))
                    print(f"Длина проводника = {calcs.calc_length_magnetic_induction(force_max, B, current)}")
                case 4:
                    force_max = float(input("Введите максимальную силу Ампера: "))
                    B = float(input("Введите вектор магнитной индукции: "))
                    length = float(input("Введите длину проводника: "))
                    print(f"Сила тока = {calcs.calc_current_magnetic_induction(force_max, B, length)}")

        case enum.AMPERES_FORCE:
            match option:
                case 1:
                    current = float(input("Введите силу тока: "))
                    length = float(input("Введите длину проводника: "))
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Сила Ампера = {calcs.calc_amperes_force(current, length, magnetic_induction, angle)}")
                case 2:
                    force = float(input("Введите силу: "))
                    length = float(input("Введите длину проводника: "))
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Сила тока = {calcs.calc_current_amperes_force(force, length, magnetic_induction, angle)}")
                case 3:
                    force = float(input("Введите силу: "))
                    current = float(input("Введите силу тока: "))
                    length = float(input("Введите вектор магнитной индукции: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Вектор магнитной индукции = {calcs.calc_magnetic_induction_amperes_force(force, current, length, angle)}")
                case 4:
                    force = float(input("Введите силу: "))
                    current = float(input("Введите силу тока: "))
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Длина проводника = {calcs.calc_length_amperes_force(force, current, magnetic_induction, angle)}")
                case 5:
                    print("Введите угол (в радианах) в соответствующих формулах (используется переменная angle).")

        case enum.LORENTZ_FORCE:
            match option:
                case 1:
                    charge = float(input("Введите электрический заряд частицы: "))
                    velocity = float(input("Введите скорость: "))
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Сила Лоренца = {calcs.calc_lorentz_force(charge, velocity, magnetic_induction, angle)}")
                case 2:
                    force = float(input("Введите силу: "))
                    velocity = float(input("Введите скорость: "))
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Электрический заряд частицы = {calcs.calc_charge_lorentz_force(force, velocity, magnetic_induction, angle)}")
                case 3:
                    force = float(input("Введите силу: "))
                    charge = float(input("Введите электрический заряд частицы: "))
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Скорость = {calcs.calc_velocity_lorentz_force(force, charge, magnetic_induction, angle)}")
                case 4:
                    force = float(input("Введите силу: "))
                    charge = float(input("Введите электрический заряд частицы: "))
                    velocity = float(input("Введите скорость: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Вектор магнитной индукции = {calcs.calc_magnetic_induction_lorentz_force(force, charge, velocity, angle)}")

        case enum.MAGNETIC_FLUX:
            match option:
                case 1:
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    area = float(input("Введите площадь: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Магнитный поток = {calcs.calc_magnetic_flux(magnetic_induction, area, angle)}")
                case 2:
                    flux = float(input("Введите магнитный поток: "))
                    area = float(input("Введите площадь: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Вектор магнитной индукции = {calcs.calc_magnetic_induction_flux(flux, area, angle)}")
                case 3:
                    flux = float(input("Введите магнитный поток: "))
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Площадь = {calcs.calc_area_magnetic_flux(flux, magnetic_induction, angle)}")
                case 4:
                    flux = float(input("Введите магнитный поток: "))
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    area = float(input("Введите площадь: "))
                    print(f"Синус угла = {calcs.calc_sin_alpha_magnetic_flux(flux, magnetic_induction, area)}")

        case enum.ELECTROMAGNETIC_INDUCTION_LAW:
            match option:
                case 1:
                    delta_flux = float(input("Введите изменение магнитного потока: "))
                    time = float(input("Введите промежуток времени: "))
                    print(f"ЭДС индукции = {calcs.calc_emf_induction(delta_flux, time)}")
                case 2:
                    emf = float(input("Введите ЭДС индукции: "))
                    time = float(input("Введите промежуток времени: "))
                    print(f"Изменение магнитного потока = {calcs.calc_delta_flux_emf(emf, time)}")
                case 3:
                    delta_flux = float(input("Введите изменение магнитного потока: "))
                    emf = float(input("Введите ЭДС индукции: "))
                    print(f"Промежуток времени = {calcs.calc_time_emf(delta_flux, emf)}")

        case enum.EMF_MOVING_CONDUCTOR:
            match option:
                case 1:
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    length = float(input("Введите длину проводника: "))
                    velocity = float(input("Введите скорость: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"ЭДС = {calcs.calc_emf_moving_conductor(magnetic_induction, length, velocity, angle)}")
                case 2:
                    emf = float(input("Введите ЭДС: "))
                    length = float(input("Введите длину проводника: "))
                    velocity = float(input("Введите скорость: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Вектор магнитной индукции = {calcs.calc_magnetic_induction_moving_conductor(emf, length, velocity, angle)}")
                case 3:
                    emf = float(input("Введите ЭДС: "))
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    velocity = float(input("Введите скорость: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Длина проводника = {calcs.calc_length_moving_conductor(emf, magnetic_induction, velocity, angle)}")
                case 4:
                    emf = float(input("Введите ЭДС: "))
                    magnetic_induction = float(input("Введите вектор магнитной индукции: "))
                    length = float(input("Введите длину проводника: "))
                    angle = float(input("Введите угол (в радианах): "))
                    print(f"Скорость = {calcs.calc_velocity_moving_conductor(emf, magnetic_induction, length, angle)}")

        case enum.EMF_SELF_INDUCTION:
            match option:
                case 1:
                    inductance = float(input("Введите коэффициент самоиндукции: "))
                    delta_current = float(input("Введите изменение силы тока: "))
                    time = float(input("Введите промежуток времени: "))
                    print(f"ЭДС самоиндукции = {calcs.calc_emf_self_induction(inductance, delta_current, time)}")
                case 2:
                    emf = float(input("Введите ЭДС самоиндукции: "))
                    delta_current = float(input("Введите изменение силы тока: "))
                    time = float(input("Введите промежуток времени: "))
                    print(f"Коэффициент самоиндукции = {calcs.calc_inductance_self_induction(emf, delta_current, time)}")
                case 3:
                    emf = float(input("Введите ЭДС самоиндукции: "))
                    inductance = float(input("Введите коэффициент самоиндукции: "))
                    time = float(input("Введите промежуток времени: "))
                    print(f"Изменение силы тока = {calcs.calc_delta_current_self_induction(emf, inductance, time)}")
                case 4:
                    emf = float(input("Введите ЭДС самоиндукции: "))
                    inductance = float(input("Введите коэффициент самоиндукции: "))
                    delta_current = float(input("Введите изменение силы тока: "))
                    print(f"Промежуток времени = {calcs.calc_time_self_induction(emf, inductance, delta_current)}")

        case enum.COIL_MAGNETIC_FIELD_ENERGY:
            match option:
                case 1:
                    inductance = float(input("Введите индуктивность катушки: "))
                    current = float(input("Введите силу тока: "))
                    print(f"Энергия = {calcs.calc_coil_magnetic_field_energy(inductance, current)}")
                case 2:
                    energy = float(input("Введите энергию: "))
                    current = float(input("Введите силу тока: "))
                    print(f"Индуктивность катушки = {calcs.calc_inductance_coil_energy(energy, current)}")
                case 3:
                    energy = float(input("Введите энергию: "))
                    inductance = float(input("Введите индуктивность катушки: "))
                    print(f"Сила тока = {calcs.calc_current_coil_energy(energy, inductance)}")

        case enum.OSCILLATING_CIRCUIT_PERIOD:
            match option:
                case 1:
                    inductance = float(input("Введите индуктивность: "))
                    capacitance = float(input("Введите электроёмкость конденсатора: "))
                    print(f"Период = {calcs.calc_oscillating_circuit_period(inductance, capacitance)}")
                case 2:
                    period = float(input("Введите период: "))
                    capacitance = float(input("Введите электроёмкость конденсатора: "))
                    print(f"Индуктивность = {calcs.calc_inductance_oscillating_circuit(period, capacitance)}")
                case 3:
                    period = float(input("Введите период: "))
                    inductance = float(input("Введите индуктивность: "))
                    print(f"Электроёмкость = {calcs.calc_capacitance_oscillating_circuit(period, inductance)}")

        case enum.INDUCTIVE_RESISTANCE:
            match option:
                case 1:
                    frequency = float(input("Введите частоту: "))
                    inductance = float(input("Введите индуктивность: "))
                    print(f"Индуктивное сопротивление = {calcs.calc_inductive_resistance(frequency, inductance)}")
                case 2:
                    resistance = float(input("Введите сопротивление: "))
                    inductance = float(input("Введите индуктивность: "))
                    print(f"Частота = {calcs.calc_frequency_inductive_resistance(resistance, inductance)}")
                case 3:
                    resistance = float(input("Введите сопротивление: "))
                    frequency = float(input("Введите частоту: "))
                    print(f"Индуктивность = {calcs.calc_inductance_from_resistance(resistance, frequency)}")

        case enum.CAPACITIVE_RESISTANCE:
            match option:
                case 1:
                    capacitance = float(input("Введите электроёмкость: "))
                    angular_frequency = float(input("Введите угловую частоту: "))
                    print(f"Емкостное сопротивление = {calcs.calc_capacitive_resistance(capacitance, angular_frequency)}")
                case 2:
                    resistance = float(input("Введите сопротивление: "))
                    angular_frequency = float(input("Введите угловую частоту: "))
                    print(f"Электроёмкость = {calcs.calc_capacitance_from_capacitive_resistance(resistance, angular_frequency)}")
                case 3:
                    resistance = float(input("Введите сопротивление: "))
                    capacitance = float(input("Введите электроёмкость: "))
                    print(f"Угловая частота = {calcs.calc_angular_frequency_from_capacitive_resistance(resistance, capacitance)}")

        case enum.ACTUAL_CURRENT_VALUE:
            match option:
                case 1:
                    max_current = float(input("Введите максимальную силу тока: "))
                    print(f"Эффективная сила тока = {calcs.calc_actual_current_value(max_current)}")
                case 2:
                    actual_current = float(input("Введите эффективную силу тока: "))
                    print(f"Максимальная сила тока = {calcs.calc_max_current_from_actual(actual_current)}")

        case enum.ACTUAL_VOLTAGE_VALUE:
            match option:
                case 1:
                    max_voltage = float(input("Введите максимальное напряжение: "))
                    print(f"Эффективное напряжение = {calcs.calc_actual_voltage_value(max_voltage)}")
                case 2:
                    actual_voltage = float(input("Введите эффективное напряжение: "))
                    print(f"Максимальное напряжение = {calcs.calc_max_voltage_from_actual(actual_voltage)}")

        case enum.TOTAL_RESISTANCE:
            match option:
                case 1:
                    active_resistance = float(input("Введите активное сопротивление: "))
                    inductive_resistance = float(input("Введите индуктивное сопротивление: "))
                    capacitive_resistance = float(input("Введите емкостное сопротивление: "))
                    print(f"Полное сопротивление = {calcs.calc_total_resistance(active_resistance, inductive_resistance, capacitive_resistance)}")
                case 2:
                    total_resistance = float(input("Введите полное сопротивление: "))
                    active_resistance = float(input("Введите активное сопротивление: "))
                    inductive_resistance = float(input("Введите индуктивное сопротивление: "))
                    print(f"Емкостное сопротивление = {calcs.calc_capacitive_resistance_from_total(total_resistance, active_resistance, inductive_resistance)}")
                case 3:
                    total_resistance = float(input("Введите полное сопротивление: "))
                    active_resistance = float(input("Введите активное сопротивление: "))
                    capacitive_resistance = float(input("Введите емкостное сопротивление: "))
                    print(f"Индуктивное сопротивление = {calcs.calc_inductive_resistance_from_total(total_resistance, active_resistance, capacitive_resistance)}")
                case 4:
                    total_resistance = float(input("Введите полное сопротивление: "))
                    inductive_resistance = float(input("Введите индуктивное сопротивление: "))
                    capacitive_resistance = float(input("Введите емкостное сопротивление: "))
                    print(f"Активное сопротивление = {calcs.calc_active_resistance_from_total(total_resistance, inductive_resistance, capacitive_resistance)}")
