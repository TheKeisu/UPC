import main.consts as const
import math as m



#####################################
# МОЛЕКУЛЯРНАЯ ФИЗИКА И ТЕРМОДИНАМИКА
#####################################

# Кол-во вещества
def calc_substance_amount(mass, molar_mass):
    return mass / molar_mass

def calc_mass_substance_amount(substance_amount, molar_mass):
    return substance_amount * molar_mass

def calc_molar_mass_substance_amount(substance_amount, mass):
    return substance_amount * mass

# Cр. кин. энергия молекул одноатомного газа
def calc_avg_kinetic_energy(abs_temperature):
    return 1.5 * const.boltzmann * abs_temperature

def calc_abs_temperature_avg_kinetic_energy(avg_kinetic_energy):
    return (2 * avg_kinetic_energy) / (3 * const.boltzmann)

# Относительная влажность
def calc_relative_humidity(partial_vapor_pressure, saturated_vapor_pressure):
    return (partial_vapor_pressure / saturated_vapor_pressure) * 100

def calc_partial_vapor_pressure(relative_humidity, saturated_vapor_pressure):
    return (relative_humidity / 100) * saturated_vapor_pressure

def calc_saturated_vapor_pressure(relative_humidity, partial_vapor_pressure):
    return (partial_vapor_pressure * 100) / relative_humidity

# Внутр. энергия идеал. одноатомного газа
def calc_internal_energy_ideal_gas(substance_amount, abs_temperature):
    return 1.5 * substance_amount * abs_temperature * const.R

def calc_substance_amount_ideal_gas(internal_energy_ideal_gas, abs_temperature):
    return (2 * internal_energy_ideal_gas) / (3 * const.R * abs_temperature)

def calc_abs_temperature_ideal_gas(internal_energy_ideal_gas, substance_amount):
    return (2 * internal_energy_ideal_gas) / (3 * const.R * substance_amount)

# Работа газа
def calc_gas_work(pressure, volume_change):
    return pressure * volume_change

def calc_pressure_gas_work(gas_work, volume_change):
    return gas_work / volume_change

def calc_volume_change_gas_work(gas_work, pressure):
    return gas_work / pressure

# Кол-во теплоты при нагревании
def calc_heat_amount_heating(heat_capacity, mass, temperature_change):
    return heat_capacity * mass * temperature_change

def calc_heat_capacity(heat_amount, mass, temperature_change):
    return heat_amount / (mass * temperature_change)

def calc_mass_heat_amount_heating(heat_amount, heat_capacity, temperature_change):
    return heat_amount / (heat_capacity * temperature_change)

def calc_temperature_change(heat_amount, mass, heat_capacity):
    return heat_amount / (mass * heat_capacity)

# Кол-во теплоты при плавлении
def calc_heat_amount_melting(melting_point, mass):
    return melting_point * mass

def calc_melting_point(heat_amount, mass):
    return heat_amount / mass

def calc_mass_heat_amount_melting(heat_amount, melting_point):
    return heat_amount / melting_point

# Кол-во теплоты при парообразовании
def calc_heat_amount_vaporization(vaporization_heat, mass):
    return vaporization_heat * mass

def calc_vaporization_heat(heat_amount, mass):
    return heat_amount / mass

def calc_mass_heat_amount_vaporization(heat_amount, vaporization_heat):
    return heat_amount / vaporization_heat

# Кол-во теплоты при сгорании топлива
def calc_heat_amount_combustion(combustion_heat, mass):
    return combustion_heat * mass

def calc_combustion_heat(heat_amount, mass):
    return heat_amount / mass

def calc_mass_heat_amount_combustion(heat_amount, combustion_heat):
    return heat_amount / combustion_heat

# КПД теплового двигателя
def calc_cop_thermal_engine(heat_1, heat_2):
    return (heat_1 - heat_2) / heat_1

def calc_heat_1(cop, heat_2):
    return heat_2 / (1 - cop)

def calc_heat_2(cop, heat_1):
    return heat_1 * (1 - cop)

#КПД идеального двигателя
def calc_cop_ideal_engine(temperature_1, temperature_2):
    return (temperature_1 - temperature_2) / temperature_1

def calc_temperature_1(cop, temperature_2):
    return temperature_2 / (1 - cop)

def calc_temperature_2(cop, temperature_1):
    return temperature_1 * (1 - cop)