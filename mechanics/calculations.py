import main.consts as const
import math as m

##########
#МЕХАНИКА#
##########

# Давление
def calc_pressure(force, area):
    return force / area

def calc_force_pressure(pressure, area):
    return pressure * area

def calc_area_pressure(pressure, force):
    return pressure * force

# Плотность
def calc_density(mass, volume):
    return mass / volume

def calc_volume_density(mass, density):
    return mass * density

def calc_mass_density(volume, density):
    return volume * density

# Давление на глубине
def calc_pressure_depth(density, height):
    return density * height * const.gn

def calc_density_depth(pressure, height):
    return pressure / (height * const.gn)

def calc_height_depth(density, pressure):
    return pressure / (density * const.gn)

# Сила тяжести
def calc_gravity(mass):
    return mass * const.gn

def calc_mass_gravity(gravity):
    return gravity / const.gn

# Сила Архимеда
def calc_archimedes_force(density, volume):
    return density * volume * const.gn

def calc_density_archimedes_force(archimedes_force, volume):
    return archimedes_force / (volume * const.gn)

def calc_volume_archimedes_force(density, archimedes_force):
    return archimedes_force / (density * const.gn)

#Скорость при равноускоренном движении
def calc_accelerated_motion(initial_speed, acceleration, time):
    return initial_speed + acceleration * time

def calc_initial_speed(accelerated_motion, acceleration, time):
    return accelerated_motion - acceleration * time

def calc_acceleration_accelerated_motion(initial_speed, accelerated_motion, time):
    return (initial_speed - accelerated_motion) / time

def calc_time_accelerated_motion(accelerated_motion, acceleration, initial_speed):
    return (initial_speed - accelerated_motion) / acceleration

# Скорость при движении по окружности
def calc_circle_speed(radius, period):
    return (2 * m.pi * radius) / period

def calc_radius_circle_speed(circle_speed, period):
    return (circle_speed * period) / (2 * m.pi)

def calc_period_circle_speed(circle_speed, radius):
    return (2 * m.pi * radius) / circle_speed

# Центростремительное ускорение
def calc_centripetal_acceleration(speed, radius):
    return m.pow(speed, 2) / radius

def calc_speed_centripetal_acceleration(centripetal_acceleration, radius):
    return m.sqrt(centripetal_acceleration * radius)

def calc_radius_centripetal_acceleration(speed, centripetal_acceleration):
    return m.pow(centripetal_acceleration, 2) / speed

# Второй закон Ньютона
def calc_force_newtons_second_law(mass, acceleration):
    return mass * acceleration

def calc_mass_newtons_second_law(force_newtons_second_law, acceleraion):
    return force_newtons_second_law / acceleraion

def calc_acceleration_newtons_second_law(force_newtons_second_law, mass):
    return force_newtons_second_law / mass

# Сила упругости
def calc_elastic_force(spring_constant, displacement):
    return -(spring_constant * displacement)

def calc_spring_constant(elastic_force, displacement):
    return elastic_force / -displacement

def calc_displacement_elastic_force(elastic_force, spring_constant):
    return -elastic_force / spring_constant

# Импульс тела
def calc_impulse_body(mass, speed):
    return mass * speed

def calc_mass_impulse_body(impulse_body, speed):
    return impulse_body / speed

def calc_speed_impulse_body(impulse_body, mass):
    return impulse_body / mass

# Импульс силы
def calc_impulse_force(force, time):
    return force * time

def calc_force_impulse_force(impulse_force, time):
    return impulse_force / time

def calc_time_impulse_force(impulse_force, force):
    return impulse_force / force

# Момент силы
def calc_moment_of_force(force, lever_arm):
    return force * lever_arm

def calc_force_moment_of_force(moment_of_force, lever_arm):
    return moment_of_force / lever_arm

def calc_lever_arm_moment_of_force(force, moment_of_force):
    return moment_of_force / force

# Потенциальная энергия тела, поднятого над землей
def calc_raised_potential_energy(mass, height):
    return mass * height * const.gn

def calc_mass_raised_potential_energy(raised_potential_energy, height):
    return raised_potential_energy / (height * const.gn)

def calc_height_raised_potential_energy(raised_potential_energy, mass):
    return raised_potential_energy / (mass * const.gn)

# Потенциальная энергия упруго-деформированного тела
def calc_deformed_potential_energy(spring_constant, displacement):
    return spring_constant * m.pow(displacement, 2) / 2

def calc_spring_constant_deformed_potential_energy(deformed_potential_energy, displacement):
    return 2 * deformed_potential_energy / m.pow(displacement,2)

def calc_displacement_deformed_potential_energy(deformed_potential_energy, spring_constant):
    return m.sqrt((2 * deformed_potential_energy) / spring_constant)

# Кинетическая энергия
def calc_kinetic_energy(mass, speed):
    return mass * m.pow(speed, 2) / 2

def calc_mass_kinetic_energy(kinetic_energy, speed):
    return kinetic_energy (2 * kinetic_energy) / m.pow(speed, 2)

def calc_speed_kinetic_energy(kinetic_energy, mass):
    return m.sqrt((2 * kinetic_energy) / mass)

# Работа
def calc_work(force, distance):
    return force * distance

def calc_force_work(work, distance):
    return work / distance

def calc_distance_work(work, force):
    return work / force

# Мощность (Работа / Время)
def calc_power_wt(work, time):
    return work / time

def calc_work_power_wt(power, time):
    return power * time

def calc_time_power_wt(power, work):
    return power * work

# КПД
def calc_cop(work_useful, work_total):
    return work_useful / work_total

def calc_work_useful_cop(cop, work_total):
    return cop * work_total

def calc_work_total_cop(cop, work_useful):
    return cop * work_useful

# Период колебаний математического маятника
def calc_period_sm(length):
    return 2 * m.pi * m.sqrt(length / const.gn)

def calc_length_period_sm(period_sm):
    return (const.gn * m.pow(period_sm, 2)) / (4 * m.pow(m.pi, 2))

# Период колебаний пружинного маятника
def calc_period_sp(mass, spring_constant):
    return 2 * m.pi * m.sqrt(mass / spring_constant)

def calc_mass_period_sp(period_sp, spring_constant):
    return (spring_constant * m.pow(period_sp, 2)) / (4 * m.pow(m.pi, 2))

def calc_spring_constant_period_sp(period_sp, mass):
    return (4 * m.pow(m.pi, 2) * mass) / m.pow(period_sp, 2)

# Уравнение гармонических колебаний
def calc_harmonic_oscillation(amplitude, frequency, time):
    return amplitude * m.cos(frequency * time)

def calc_amplitude_harmonic_oscillation(harmonic_oscillation, frequency, time):
    return harmonic_oscillation / m.cos(frequency * time)

def calc_cos_harmonic_oscillation(harmonic_oscillation, amplitude):
    return harmonic_oscillation / amplitude

# Длина волны
def calc_wave_length(speed, period):
    return speed * period

def calc_speed_wave_length(wave_length, period):
    return wave_length / period

def calc_period_wave_length(wave_length, speed):
    return wave_length / speed

# Сила трения
def calc_frictional_force(normal_force, friction_coefficient):
    return normal_force * friction_coefficient

def calc_normal_force_frictional_force(frictional_force, friction_coefficient):
    return frictional_force / friction_coefficient

def calc_friction_coefficient_frictional_force(frictional_force, normal_force):
    return frictional_force / normal_force
