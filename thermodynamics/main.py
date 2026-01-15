import thermodynamics.enum as enum
import thermodynamics.calculations as calcs

def formula_selection(input_text, enum_formula):
    option = int(input(input_text))

    match enum_formula:
        case enum.SUBSTANCE_AMOUNT:
            match option:
                case 1:
                    mass = float(input("Введите массу вещества: "))
                    molar_mass = float(input("Введите молярную массу: "))
                    print(f"Кол-во вещства = {calcs.calc_substance_amount(mass, molar_mass)}")
                case 2:
                    substance_amount = float(input("Введите кол-во вещества: "))
                    molar_mass = float(input("Введите молярную массу: "))
                    print(f"Масса = {calcs.calc_mass_substance_amount(substance_amount, molar_mass)}")
                case 3:
                    substance_amount = float(input("Введите кол-во вещества: "))
                    mass = float(input("Введите массу вещества: "))
                    print(f"Молярная масса = {calcs.calc_molar_mass_substance_amount(substance_amount, mass)}")
        case enum.AVG_KINETIC_ENERGY:
            match option:
                case 1:
                    abs_temperature = float(input("Введите абсолютную температуру: "))
                    print(f"Ср. кинетическая энергия = {calcs.calc_avg_kinetic_energy(abs_temperature)}")
                case 2:
                    avg_kinetic_energy = float(input("Введите ср.кинетическую энергию: "))
                    print(f"Абсолютная температура = {calcs.calc_abs_temperature_avg_kinetic_energy(avg_kinetic_energy)}")
        case enum.RELATIVE_HUMIDITY:
            match option:
                case 1:
                    partial_vapor_pressure = float(input("Введите парциальное давление водяного пара: "))
                    saturated_vapor_pressure = float(input("Введите давление насыщенного пара: "))
                    print(f"Относительная влажность = {calcs.calc_relative_humidity(partial_vapor_pressure, saturated_vapor_pressure)}")
                case 2:
                    relative_humidity = float(input("Введите относительную влажность: "))
                    saturated_vapor_pressure = float(input("Введите давление насыщенного пара: "))
                    print(f"Парциальное давление водяного пара = {calcs.calc_partial_vapor_pressure(relative_humidity, saturated_vapor_pressure)}")
                case 3:
                    relative_humidity = float(input("Введите относительную влажность: "))
                    partial_vapor_pressure = float(input("Введите парциальное давление водяного пара: "))
                    print(f"Давление насыщенного пара = {calcs.calc_saturated_vapor_pressure(relative_humidity, partial_vapor_pressure)}")
        case enum.INTERNAL_ENERGY_IDEAL_GAS:
            match option:
                case 1:
                    substance_amount = float(input("Введите кол-во вещества: "))
                    abs_temperature = float(input("Введите абсолютную температуру: "))
                    print(f"Внутренняя энергия идеального одноатомного газа = {calcs.calc_internal_energy_ideal_gas(substance_amount, abs_temperature)}")
                case 2:
                    internal_energy_ideal_gas = float(input("Введите внутреннюю энергию идеального одноатомного газа: "))
                    abs_temperature = float(input("Введите абсолютную температуру: "))
                    print(f"Кол-во вещества = {calcs.calc_substance_amount_ideal_gas(internal_energy_ideal_gas, abs_temperature)}")
                case 3:
                    internal_energy_ideal_gas = float(input("Введите внутреннюю энергию идеального одноатомного газа: "))
                    substance_amount = float(input("Введите кол-во вещества: "))
                    print(f"Абсолютная температура = {calcs.calc_abs_temperature_ideal_gas(internal_energy_ideal_gas, substance_amount)}")
        case enum.GAS_WORK:
            match option:
                case 1:
                    pressure = float(input("Введите давление: "))
                    volume_change = float(input("Введите изменение объёма: "))
                    print(f"Работа газа = {calcs.calc_gas_work(pressure, volume_change)}")
                case 2:
                    gas_work = float(input("Введите работу газа: "))
                    volume_change = float(input("Введите изменение объёма: "))
                    print(f"Давление = {calcs.calc_pressure_gas_work(gas_work, volume_change)}")
                case 3:
                    gas_work = float(input("Введите работу газа: "))
                    pressure = float(input("Введите давление: "))
                    print(f"Изменение объёма = {calcs.calc_volume_change_gas_work(gas_work, pressure)}")
        case enum.HEAT_AMOUNT_HEATING:
            match option:
                case 1:
                    heat_capacity = float(input("Введите удельную теплоемкость: "))
                    mass = float(input("Введите массу вещества: "))
                    temperature_change = float(input("Введите изменение температуры: "))
                    print(f"Кол-во теплоты при нагревании = {calcs.calc_heat_amount_heating(heat_capacity, mass, temperature_change)}")
                case 2:
                    heat_amount = float(input("Введите кол-во теплоты: "))
                    heat_capacity = float(input("Введите удельную теплоемкость: "))
                    mass = float(input("Введите массу вещества: "))
                    print(f"Удельная теплоемкость = {calcs.calc_heat_capacity(heat_amount, mass, heat_capacity)}")
                case 3:
                    heat_amount = float(input("Введите кол-во теплоты: "))
                    heat_capacity = float(input("Введите удельную теплоемкость: "))
                    temperature_change = float(input("Введите изменение температуры: "))
                    print(f"Масса = {calcs.calc_mass_heat_amount_heating(heat_amount, heat_capacity, temperature_change)}")
                case 4:
                    heat_amount = float(input("Введите кол-во теплоты: "))
                    heat_capacity = float(input("Введите удельную теплоемкость: "))
                    mass = float(input("Введите массу вещества: "))
                    print(f"Изменение температуры = {calcs.calc_temperature_change(heat_amount, mass, heat_capacity)}")
        case enum.HEAT_AMOUNT_MELTING:
            match option:
                case 1:
                    melting_point = float(input("Введите удельную теплоту плавления: "))
                    mass = float(input("Введите массу вещества: "))
                    print(f"Кол-во теплоты при плавление = {calcs.calc_heat_amount_melting(melting_point, mass)}")
                case 2:
                    heat_amount = float(input("Введите кол-во теплоты: "))
                    mass = float(input("Введите массу вещества: "))
                    print(f"Удельная теплота плавления = {calcs.calc_melting_point(heat_amount, mass)}")
                case 3:
                    heat_amount = float(input("Введите кол-во теплоты: "))
                    melting_point = float(input("Введите удельную теплоту плавления: "))
                    print(f"Масса = {calcs.calc_mass_heat_amount_melting(heat_amount, melting_point)}")
        case enum.HEAT_AMOUNT_VAPORIZATION:
            match option:
                case 1:
                    vaporization_heat = float(input("Введите удельную теплоту парообразования: "))
                    mass = float(input("Введите массу вещества: "))
                    print(f"Кол-во теплоты при парообразовании = {calcs.calc_heat_amount_vaporization(vaporization_heat, mass)}")
                case 2:
                    heat_amount = float(input("Введите кол-во теплоты: "))
                    mass = float(input("Введите массу вещества: "))
                    print(f"Удельная теплота парообразования = {calcs.calc_vaporization_heat(heat_amount, mass)}")
                case 3:
                    heat_amount = float(input("Введите кол-во теплоты: "))
                    vaporization_heat = float(input("Введите удельную теплоту парообразования: "))
                    print(f"Масса = {calcs.calc_mass_heat_amount_vaporization(heat_amount, vaporization_heat)}")
        case enum.HEAT_AMOUNT_COMBUSTION:
            match option:
                case 1:
                    combustion_heat = float(input("Введите удельную теплоту сгорания топлива: "))
                    mass = float(input("Введите массу вещества: "))
                    print(f"Кол-во теплоты при сгорании топлива = {calcs.calc_heat_amount_combustion(combustion_heat, mass)}")
                case 2:
                    heat_amount = float(input("Введите кол-во теплоты: "))
                    mass = float(input("Введите массу вещества: "))
                    print(f"Удельная теплота сгорания топлива = {calcs.calc_combustion_heat(heat_amount, mass)}")
                case 3:
                    heat_amount = float(input("Введите кол-во теплоты: "))
                    combustion_heat = float(input("Введите удельную теплоту сгорания топлива: "))
                    print(f"Масса = {calcs.calc_mass_heat_amount_combustion(heat_amount, combustion_heat)}")
        case enum.COP_THERMAL_ENGINE:
            match option:
                case 1:
                    heat_1 = float(input("Введите теплоту №1: "))
                    heat_2 = float(input("Введите теплоту №2: "))
                    print(f"КПД теплового двигателя = {calcs.calc_cop_thermal_engine(heat_1, heat_2)}")
                case 2:
                    cop = float(input("Введите КПД: "))
                    heat_2 = float(input("Введите теплоту №2: "))
                    print(f"Теплота №1 = {calcs.calc_heat_1(cop, heat_2)}")
                case 3:
                    cop = float(input("Введите КПД: "))
                    heat_1 = float(input("Введите теплоту №1: "))
                    print(f"Теплота №2 = {calcs.calc_heat_2(cop, heat_1)}")
        case enum.COP_IDEAL_ENGINE:
            match option:
                case 1:
                    temperature_1 = float(input("Введите температуру №1: "))
                    temperature_2 = float(input("Введите температуру №2: "))
                    print(f"КПД идеального двигателя = {calcs.calc_cop_ideal_engine(temperature_1, temperature_2)}")
                case 2:
                    cop = float(input("Введите КПД: "))
                    temperature_2 = float(input("Введите температуру №2: "))
                    print(f"Температура №1 = {calcs.calc_temperature_1(cop, temperature_2)}")
                case 3:
                    cop = float(input("Введите КПД: "))
                    temperature_1 = float(input("Введите температуру №1: "))
                    print(f"Температура №2 = {calcs.calc_temperature_2(cop, temperature_1)}")