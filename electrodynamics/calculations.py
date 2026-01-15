import main.consts as const
import math as m

##################################
#ЭЛЕКТРОСТАТИКА И ЭЛЕКТРОДИНАМИКА#
##################################

# Закон Кулона
def calc_coulombs_law(electric_charge_1, electric_charge_2, distance):
    return const.coulombs * ((electric_charge_1 * electric_charge_2) / m.pow(distance, 2))

def calc_electric_charge_1_coulombs_law(force,  electric_charge_2, distance):
    return (force * m.pow(distance, 2)) / (const.coulombs * electric_charge_2)

def calc_electric_charge_2_coulombs_law(force, electric_charge_1, distance):
    return (force * m.pow(distance, 2)) / (const.coulombs * electric_charge_1)

def calc_distance_coulombs_law(force, electric_charge_1, electric_charge_2):
    return m.sqrt((const.coulombs * electric_charge_1 * electric_charge_2) / force)

# Напряженность эл. поля
def calc_el_field_intensity(force, electric_charge):
    return force / electric_charge

def calc_force_el_field_intensity(density, electric_charge):
    return density * electric_charge

def calc_electric_charge_el_field_intensity(force, density):
    return density * force

# Напряженность эл.поля точечного заряда
def calc_point_charge_el_field_intensity(electric_charge, distance):
    return (const.coulombs * electric_charge) / m.pow(distance, 2)

def calc_electric_charge_point_charge_el_field_intensity(intensity, distance):
    return (intensity * m.pow(distance, 2)) / const.coulombs

def calc_distance_charge_point_charge_el_field_intensity(intensity, electric_charge):
    return m.sqrt((const.coulombs * electric_charge) / intensity)

# Поверхностная плотность зарядов
def calc_surface_charge_density(electric_charge, area):
    return electric_charge / area

def calc_electric_charge_surface_charge_density(density, area):
    return density * area

def calc_area_surface_charge_density(density, electric_charge):
    return density * electric_charge

# Напряженность эл. поля бесконечной плоскости
def calc_infinity_surface_el_field_intensity(density):
    return 2 * m.pi * const.coulombs * density

def calc_density_infinity_surface_el_field_intensity(intensity):
    return intensity / (2 * m.pi * const.coulombs)

# Диэлектрическая проницаемость
def calc_dielectric_constant(intensity_1, intensity_2):
    return intensity_1 / intensity_2

def calc_intensity_1_dielectric_constant(dielectric_constant, intensity_2):
    return dielectric_constant * intensity_2

def calc_intensity_2_dielectric_constant(dielectric_constant, intensity_1):
    return dielectric_constant * intensity_1

# Потенциальная энергия взаимодействия зарядов
def calc_potential_energy(electric_charge_1, electric_charge_2, distance):
    return const.coulombs * ((electric_charge_1 * electric_charge_2) / distance)

def calc_electric_charge_1_potential_energy(force,  electric_charge_2, distance):
    return (force * distance) / (const.coulombs * electric_charge_2)

def calc_electric_charge_2_potential_energy(force, electric_charge_1, distance):
    return (force * distance) / (const.coulombs * electric_charge_1)

def calc_distance_potential_energy(force, electric_charge_1, electric_charge_2):
    return (const.coulombs * electric_charge_1 * electric_charge_2) / force

# Потенциал
def calc_potential(potential_energy, electric_charge):
    return potential_energy / electric_charge

def calc_potential_energy_potential(potential, electric_charge):
    return potential * electric_charge

def calc_electric_charge_potential(potential, potential_energy):
    return potential * potential_energy

# Потенциал точечного заряда
def calc_point_charge_potential(electric_charge, distance):
    return (const.coulombs * electric_charge) / distance

def calc_electric_charge_point_charge_potential(potential, distance):
    return (potential * distance) / const.coulombs

def calc_distance_point_charge_potential(potential, electric_charge):
    return (const.coulombs * electric_charge) / potential

# Напряжение
def calc_voltage(work, electric_charge):
    return work / electric_charge

def calc_work_voltage(voltage, electric_charge):
    return voltage * electric_charge

def calc_electric_charge_voltage(voltage, work):
    return voltage * work

# Электрическое поле и напряжение
def calc_el_field_voltage(intensity, distance):
    return intensity * distance

def calc_intensity_el_field_voltage(voltage, distance):
    return voltage / distance

def calc_distance_el_field_voltage(voltage, intensity):
    return voltage / intensity

# Электроёмкость (общая)
def calc_el_capacity(electric_charge, voltage):
    return electric_charge / voltage

def calc_charge_el_capacity(capacity, voltage):
    return capacity * voltage

def calc_voltage_el_capacity(capacity, electric_charge):
    return electric_charge / capacity

# Ёмкость плоского (пластинчатого) конденсатора
# Требуется константа диэлектрической проницаемости вакуума в `main.consts` как `epsilon_0`
def calc_flat_capacitor_capacity(area, relative_perm, distance):
    return (const.epsilon_0 * relative_perm * area) / distance

def calc_area_flat_capacitor_capacity(capacity, relative_perm, distance):
    return (capacity * distance) / (const.epsilon_0 * relative_perm)

def calc_relative_perm_flat_capacitor_capacity(capacity, area, distance):
    return (capacity * distance) / (const.epsilon_0 * area)

def calc_distance_flat_capacitor_capacity(capacity, area, relative_perm):
    return (const.epsilon_0 * relative_perm * area) / capacity

# Ток
def calc_current(charge, time):
    return charge / time

def calc_charge_current(current, time):
    return current * time

def calc_time_current(charge, current):
    return charge / current

# Сопротивление проводника
def calc_conductor_resistance(resistivity, length, area):
    return (resistivity * length) / area

def calc_resistivity_conductor(resistance, length, area):
    return (resistance * area) / length

def calc_length_conductor(resistance, resistivity, area):
    return (resistance * area) / resistivity

def calc_area_conductor(resistivity, length, resistance):
    return (resistivity * length) / resistance

# Закон Ома для участка цепи
def calc_section_current(voltage, resistance):
    return voltage / resistance

def calc_section_voltage(current, resistance):
    return current * resistance

def calc_section_resistance(voltage, current):
    return voltage / current

# Мощность электрического тока (P = I * U)
def calc_el_current_power(current, voltage):
    return current * voltage

def calc_current_el_current_power(power, voltage):
    return power / voltage

def calc_voltage_el_current_power(power, current):
    return power / current

# Закон Джоуля-Ленца (Q = I^2 * R * t)
def calc_joule_lenz_heat(current, resistance, time):
    return (current ** 2) * resistance * time

def calc_current_joule_lenz(heat, resistance, time):
    return m.sqrt(heat / (resistance * time))

def calc_resistance_joule_lenz(heat, current, time):
    return heat / (current ** 2 * time)

def calc_time_joule_lenz(heat, current, resistance):
    return heat / (current ** 2 * resistance)

# Закон Ома для полной цепи (I = E / (R + r))
def calc_full_circuit_current(emf, external_resistance, internal_resistance):
    return emf / (external_resistance + internal_resistance)

def calc_emf_full_circuit(current, external_resistance, internal_resistance):
    return current * (external_resistance + internal_resistance)

def calc_external_resistance_full_circuit(emf, current, internal_resistance):
    return (emf / current) - internal_resistance

def calc_internal_resistance_full_circuit(emf, current, external_resistance):
    return (emf / current) - external_resistance

# Короткозамкнутый ток (R внешнее = 0): I_sc = E / r
def calc_short_circuit_current(emf, internal_resistance):
    return emf / internal_resistance

def calc_emf_short_circuit(current, internal_resistance):
    return current * internal_resistance

def calc_internal_resistance_short_circuit(emf, current):
    return emf / current

# Вектор магнитной индукции (B): B = F_max / (I * l)
def calc_magnetic_induction_vector(force_max, length, current):
    return force_max / (current * length)

def calc_force_max_magnetic_induction(B, length, current):
    return B * current * length

def calc_length_magnetic_induction(force_max, B, current):
    return force_max / (B * current)

def calc_current_magnetic_induction(force_max, B, length):
    return force_max / (B * length)

# Сила Ампера: F = I * L * B * sin(угла)
def calc_amperes_force(current, length, magnetic_induction, angle):
    return current * length * magnetic_induction * m.sin(angle)

def calc_current_amperes_force(force, length, magnetic_induction, angle):
    return force / (length * magnetic_induction * m.sin(angle))

def calc_length_amperes_force(force, current, magnetic_induction, angle):
    return force / (current * magnetic_induction * m.sin(angle))

def calc_magnetic_induction_amperes_force(force, current, length, angle):
    return force / (current * length * m.sin(angle))

# Сила Лоренца (магнитная составляющая): F = q * v * B * sin(угла)
def calc_lorentz_force(charge, velocity, magnetic_induction, angle):
    return charge * velocity * magnetic_induction * m.sin(angle)

def calc_charge_lorentz_force(force, velocity, magnetic_induction, angle):
    return force / (velocity * magnetic_induction * m.sin(angle))

def calc_velocity_lorentz_force(force, charge, magnetic_induction, angle):
    return force / (charge * magnetic_induction * m.sin(angle))

def calc_magnetic_induction_lorentz_force(force, charge, velocity, angle):
    return force / (charge * velocity * m.sin(angle))

# Магнитный поток: Phi = B * S * sin(угла)
def calc_magnetic_flux(magnetic_induction, area, angle):
    return magnetic_induction * area * m.sin(angle)

def calc_magnetic_induction_flux(flux, area, angle):
    return flux / (area * m.sin(angle))

def calc_area_magnetic_flux(flux, magnetic_induction, angle):
    return flux / (magnetic_induction * m.sin(angle))

def calc_sin_alpha_magnetic_flux(flux, magnetic_induction, area):
    return flux / (magnetic_induction * area)

# Электромагнитная индукция (закон Фарадея): emf = - (delta_phi / delta_t)
def calc_emf_induction(delta_flux, time):
    return - delta_flux / time

def calc_delta_flux_emf(emf, time):
    return - emf * time

def calc_time_emf(delta_flux, emf):
    return - delta_flux / emf

# ЭДС в движущемся проводнике: emf = B * l * v * sin(угла)
def calc_emf_moving_conductor(magnetic_induction, length, velocity, angle):
    return magnetic_induction * length * velocity * m.sin(angle)

def calc_magnetic_induction_moving_conductor(emf, length, velocity, angle):
    return emf / (length * velocity * m.sin(angle))

def calc_length_moving_conductor(emf, magnetic_induction, velocity, angle):
    return emf / (magnetic_induction * velocity * m.sin(angle))

def calc_velocity_moving_conductor(emf, magnetic_induction, length, angle):
    return emf / (magnetic_induction * length * m.sin(angle))

# Самоиндукция: emf = - L * (delta_I / delta_t)
def calc_emf_self_induction(inductance, delta_current, time):
    return - inductance * (delta_current / time)

def calc_inductance_self_induction(emf, delta_current, time):
    return - emf * time / delta_current

def calc_delta_current_self_induction(emf, inductance, time):
    return - (emf * time) / inductance

def calc_time_self_induction(emf, inductance, delta_current):
    return - (emf * delta_current) / inductance

# Энергия магнитного поля катушки: W = 0.5 * L * I^2
def calc_coil_magnetic_field_energy(inductance, current):
    return 0.5 * inductance * (current ** 2)

def calc_inductance_coil_energy(energy, current):
    return (2 * energy) / (current ** 2)

def calc_current_coil_energy(energy, inductance):
    return m.sqrt((2 * energy) / inductance)

# Период колебательного контура: T = 2 * pi * sqrt(L * C)
def calc_oscillating_circuit_period(inductance, capacitance):
    return 2 * m.pi * m.sqrt(inductance * capacitance)

def calc_inductance_oscillating_circuit(period, capacitance):
    return (period / (2 * m.pi)) ** 2 / capacitance

def calc_capacitance_oscillating_circuit(period, inductance):
    return (period / (2 * m.pi)) ** 2 / inductance

# Индуктивное сопротивление: X_L = 2 * pi * f * L
def calc_inductive_resistance(frequency, inductance):
    return 2 * m.pi * frequency * inductance

def calc_frequency_inductive_resistance(resistance, inductance):
    return resistance / (2 * m.pi * inductance)

def calc_inductance_from_resistance(resistance, frequency):
    return resistance / (2 * m.pi * frequency)

# Ёмкостное сопротивление: X_C = 1 / (omega * C)
def calc_capacitive_resistance(capacitance, angular_frequency):
    return 1 / (angular_frequency * capacitance)

def calc_capacitance_from_capacitive_resistance(resistance, angular_frequency):
    return 1 / (angular_frequency * resistance)

def calc_angular_frequency_from_capacitive_resistance(resistance, capacitance):
    return 1 / (resistance * capacitance)

# Эффективные (действующие) значения тока и напряжения: I_rms = I_max / sqrt(2)
def calc_actual_current_value(max_current):
    return max_current / m.sqrt(2)

def calc_max_current_from_actual(actual_current):
    return actual_current * m.sqrt(2)

def calc_actual_voltage_value(max_voltage):
    return max_voltage / m.sqrt(2)

def calc_max_voltage_from_actual(actual_voltage):
    return actual_voltage * m.sqrt(2)

# Полное сопротивление (последовательные R, Xl, Xc): Z = sqrt(R^2 + (Xl - Xc)^2)
def calc_total_resistance(active_resistance, inductive_resistance, capacitive_resistance):
    return m.sqrt(active_resistance ** 2 + (inductive_resistance - capacitive_resistance) ** 2)

def calc_capacitive_resistance_from_total(total_resistance, active_resistance, inductive_resistance):
    diff = m.sqrt(max(total_resistance ** 2 - active_resistance ** 2, 0))
    return inductive_resistance - diff

def calc_inductive_resistance_from_total(total_resistance, active_resistance, capacitive_resistance):
    diff = m.sqrt(max(total_resistance ** 2 - active_resistance ** 2, 0))
    return capacitive_resistance + diff

def calc_active_resistance_from_total(total_resistance, inductive_resistance, capacitive_resistance):
    return m.sqrt(max(total_resistance ** 2 - (inductive_resistance - capacitive_resistance) ** 2, 0))
