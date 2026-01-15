import mechanics.enum as enum
import mechanics.calculations as calcs


def formula_selection(input_text, enum_formula):
    option = int(input(input_text))

    match enum_formula:
        case enum.PRESSURE:
            match option:
                case 1:
                    force = float(input("Введите силу: "))
                    area = float(input("Введите площадь: "))
                    print(f"Давление = {calcs.calc_pressure(force, area)}")
                case 2:
                    pressure = float(input("Введите давление: "))
                    area = float(input("Введите площадь: "))
                    print(f"Сила = {calcs.calc_force_pressure(pressure, area)}")
                case 3:
                    pressure = float(input("Введите давление: "))
                    force = float(input("Введите силу: "))
                    print(f"Площадь = {calcs.calc_area_pressure(pressure, force)}")
        case enum.DENSITY:
            match option:
                case 1:
                    mass = float(input("Введите массу: "))
                    volume = float(input("Введите объем: "))
                    print(f"Плотность = {calcs.calc_density(mass, volume)}")
                case 2:
                    volume = float(input("Введите объем: "))
                    density = float(input("Введите плотность: "))
                    print(f"Масса = {calcs.calc_mass_density(volume, density)}")
                case 3:
                    mass = float(input("Введите массу: "))
                    density = float(input("Введите плотность: "))
                    print(f"Объем = {calcs.calc_volume_density(mass, density)}")
        case enum.PRESSURE_DEPTH:
            match option:
                case 1:
                    density = float(input("Введите плотность: "))
                    height = float(input("Введите высоту: "))
                    print(f"Давление = {calcs.calc_pressure_depth(height, density)}")
                case 2:
                    pressure = float(input("Введите давление: "))
                    height = float(input("Введите высоту: "))
                    print(f"Плотность = {calcs.calc_density_depth(pressure, height)}")
                case 3:
                    density = float(input("Введите плотность: "))
                    pressure = float(input("Введите давление: "))
                    print(f"Высота = {calcs.calc_height_depth(density, pressure)}")
        case enum.GRAVITY:
            match option:
                case 1:
                    mass = float(input("Введите массу: "))
                    print(f"Сила тяжести = {calcs.calc_gravity(mass)}")
                case 2:
                    gravity = float(input("Введите силу тяжести: "))
                    print(f"Масса = {calcs.calc_mass_gravity(gravity)}")
        case enum.ARCHIMEDES_FORCE:
            match option:
                case 1:
                    density = float(input("Введите плотность: "))
                    volume = float(input("Введите объем: "))
                    print(f"Сила Архимеда = {calcs.calc_archimedes_force(density, volume)}")
                case 2:
                    density = float(input("Введите плотность: "))
                    archimedes_force = float(input("Введите силу Архимеда: "))
                    print(f"Объем = {calcs.calc_volume_archimedes_force(density, archimedes_force)}")
                case 3:
                    archimedes_force = float(input("Введите силу Архимеда: "))
                    volume = float(input("Введите объем: "))
                    print(f"Плотность = {calcs.calc_density_archimedes_force(archimedes_force, volume)}")
        case enum.ACCELERATED_MOTION:
            match option:
                case 1:
                    initial_speed = float(input("Введите начальную скорость: "))
                    acceleration = float(input("Введите ускорение: "))
                    time = float(input("Введите время: "))
                    print(f"Скорость = {calcs.calc_initial_speed(initial_speed, acceleration, time)}")
                case 2:
                    accelerated_motion = float(input("Введите скорость: "))
                    acceleration = float(input("Введите ускорение: "))
                    time = float(input("Введите время: "))
                    print(f"Начальная скорость = {calcs.calc_initial_speed(accelerated_motion, acceleration, time)}")
                case 3:
                    initial_speed = float(input("Введите начальную скорость: "))
                    time = float(input("Введите время: "))
                    accelerated_motion = float(input("Введите скорость: "))
                    print(f"Ускорение = {calcs.calc_acceleration_accelerated_motion(initial_speed, accelerated_motion, time)}")
                case 4:
                    accelerated_motion = float(input("Введите скорость: "))
                    initial_speed = float(input("Введите начальную скорость: "))
                    acceleration = float(input("Введите ускорение: "))
                    print(f"Время = {calcs.calc_time_accelerated_motion(accelerated_motion, acceleration, initial_speed)}")
        case enum.CIRCLE_SPEED:
            match option:
                case 1:
                    radius = float(input("Введите радиус: "))
                    period = float(input("Введите период: "))
                    print(f"Скорость = {calcs.calc_circle_speed(radius, period)}")
                case 2:
                    circle_speed = float(input("Введите скорость: "))
                    period = float(input("Введите период: "))
                    print(f"Радиус = {calcs.calc_radius_circle_speed(circle_speed, period)}")
                case 3:
                    circle_speed = float(input("Введите скорость: "))
                    radius = float(input("Введите радиус: "))
                    print(f"Период = {calcs.calc_period_circle_speed(circle_speed, radius)}")
        case enum.CENTRIPETAL_ACCELERATION:
            match option:
                case 1:
                    speed = float(input("Введите скорость: "))
                    radius = float(input("Введите радиус: "))
                    print(f"Ускорение = {calcs.calc_centripetal_acceleration(speed, radius)}")
                case 2:
                    centripetal_acceleration = float(input("Введите ускорение: "))
                    radius = float(input("Введите радиус: "))
                    print(f"Скорость = {calcs.calc_speed_centripetal_acceleration(centripetal_acceleration, radius)}")
                case 3:
                    centripetal_acceleration = float(input("Введите ускорение: "))
                    speed = float(input("Введите скорость: "))
                    print(f"Радиус = {calcs.calc_radius_centripetal_acceleration(speed, centripetal_acceleration)}")
        case enum.NEWTONS_SECOND_LAW:
            match option:
                case 1:
                    mass = float(input("Введите массу: "))
                    acceleration = float(input("Введите ускорение: "))
                    print(f"Сила = {calcs.calc_force_newtons_second_law(mass, acceleration)}")
                case 2:
                    force_newtons_second_law = float(input("Введите силу: "))
                    acceleration = float(input("Введите ускорение: "))
                    print(f"Масса = {calcs.calc_mass_newtons_second_law(force_newtons_second_law, acceleration)}")
                case 3:
                    force_newtons_second_law = float(input("Введите силу: "))
                    mass = float(input("Введите массу: "))
                    print(f"Ускорение = {calcs.calc_acceleration_newtons_second_law(force_newtons_second_law, mass)}")
        case enum.ELASTIC_FORCE:
            match option:
                case 1:
                    spring_constant = float(input("Введите коэффицент жесткости материала: "))
                    displacement = float(input("Введите величину деформации: "))
                    print(f"Сила упругости = {calcs.calc_elastic_force(spring_constant, displacement)}")
                case 2:
                    elastic_force = float(input("Ввведите силу упругости: "))
                    displacement = float(input("Введите величину деформации: "))
                    print(f"Коэффицент жесткости материала = {calcs.calc_spring_constant(elastic_force, displacement)}")
                case 3:
                    elastic_force = float(input("Ввведите силу упругости: "))
                    spring_constant = float(input("Введите коэффицент жесткости материала: "))
                    print(f"Величина деформации = {calcs.calc_displacement_elastic_force(elastic_force, spring_constant)}")
        case enum.IMPULSE_BODY:
            match option:
                case 1:
                    mass = float(input("Введите массу: "))
                    speed = float(input("Введите скорость: "))
                    print(f"Импульс тела = {calcs.calc_impulse_body(mass, speed)}")
                case 2:
                    impulse = float(input("Введите импульс тела: "))
                    speed = float(input("Введите скорость: "))
                    print(f"Масса = {calcs.calc_mass_impulse_body(impulse, speed)}")
                case 3:
                    impulse = float(input("Введите импульс тела: "))
                    mass = float(input("Введите массу: "))
                    print(f"Скорость = {calcs.calc_speed_impulse_body(impulse, mass)}")
        case enum.IMPULSE_FORCE:
            match option:
                case 1:
                    force = float(input("Введите силу: "))
                    time = float(input("Введите время: "))
                    print(f"Импульс силы = {calcs.calc_impulse_force(force, time)}")
                case 2:
                    impulse_force = float(input("Введите импульс силы: "))
                    time = float(input("Введите время: "))
                    print(f"Сила = {calcs.calc_force_impulse_force(impulse_force, time)}")
                case 3:
                    impulse_force = float(input("Введите импульс силы: "))
                    force = float(input("Введите силу: "))
                    print(f"Время = {calcs.calc_time_impulse_force(impulse_force, force)}")

        case enum.MOMENT_OF_FORCE:
            match option:
                case 1:
                    force = float(input("Введите силу: "))
                    lever_arm = float(input("Введите плечо силы: "))
                    print(f"Момент силы = {calcs.calc_moment_of_force(force, lever_arm)}")
                case 2:
                    moment_of_force = float(input("Введите момент силы: "))
                    force = float(input("Введите силу: "))
                    print(f"Плечо силы = {calcs.calc_lever_arm_moment_of_force(moment_of_force, force)}")
                case 3:
                    moment_of_force = float(input("Введите момент силы: "))
                    lever_arm = float(input("Введите плечо силы: "))
                    print(f"Сила = {calcs.calc_moment_of_force(moment_of_force, lever_arm)}")
        case enum.RAISED_POTENTIAL_ENERGY:
            match option:
                case 1:
                    mass = float(input("Введите массу: "))
                    height = float(input("Введите высоту: "))
                    print(f"Потенциальная энергия = {calcs.calc_raised_potential_energy(mass, height)}")
                case 2:
                    raised_potential_energy = float(input("Введите потенциальную энергию"))
                    height = float(input("Введите высоту: "))
                    print(f"Масса = {calcs.calc_mass_raised_potential_energy(raised_potential_energy, height)}")
                case 3:
                    raised_potential_energy = float(input("Введите потенциальную энергию"))
                    mass = float(input("Введите массу: "))
                    print(f"Высота = {calcs.calc_height_raised_potential_energy(raised_potential_energy, mass)}")
        case enum.DEFORMED_POTENTIAL_ENERGY:
            match option:
                case 1:
                    spring_constant = float(input("Введите коэффицент жесткости материала: "))
                    displacement = float(input("Введите величину деформации: "))
                    print(f"Потенциальная энергия = {calcs.calc_deformed_potential_energy(displacement, spring_constant)}")
                case 2:
                    deformed_potential_energy = float(input("Введите потенциальную энергию"))
                    displacement = float(input("Введите величину деформации: "))
                    print(f"Коэффицент жесткости пружины = {calcs.calc_spring_constant_deformed_potential_energy(displacement, deformed_potential_energy)}")
                case 3:
                    deformed_potential_energy = float(input("Введите потенциальную энергию"))
                    spring_constant = float(input("Введите коэффицент жесткости материала: "))
                    print(f"Величина деформации = {calcs.calc_displacement_deformed_potential_energy(deformed_potential_energy, spring_constant)}")
        case enum.KINETIC_ENERGY:
            match option:
                case 1:
                    mass = float(input("Введите массу: "))
                    speed = float(input("Введите скорость: "))
                    print(f"Кинетическая энергия = {calcs.calc_kinetic_energy(mass, speed)}")
                case 2:
                    kinetic_energy = float(input("Введите кинетическую энергию: "))
                    speed = float(input("Введите скорость: "))
                    print(f"Масса = {calcs.calc_mass_kinetic_energy(kinetic_energy, speed)}")
                case 3:
                    kinetic_energy = float(input("Введите кинетическую энергию: "))
                    mass = float(input("Введите массу: "))
                    print(f"Скорость = {calcs.calc_speed_kinetic_energy(kinetic_energy, mass)}")
        case enum.WORK:
            match option:
                case 1:
                    force = float(input("Введите силу: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Работа = {calcs.calc_work(force, distance)}")
                case 2:
                    work = float(input("Введите работу: "))
                    distance = float(input("Введите расстояние: "))
                    print(f"Сила = {calcs.calc_force_work(work, distance)}")
                case 3:
                    work = float(input("Введите работу: "))
                    force = float(input("Введите силу: "))
                    print(f"Расстояние = {calcs.calc_distance_work(work, force)}")
        case enum.POWER_WT:
            match option:
                case 1:
                    work = float(input("Введите работу: "))
                    time = float(input("Введите время: "))
                    print(f"Мощность = {calcs.calc_power_wt(work, time)}")
                case 2:
                    power = float(input("Введите мощность: "))
                    time = float(input("Введите время: "))
                    print(f"Работа = {calcs.calc_work_power_wt(power, time)}")
                case 3:
                    power = float(input("Введите мощность: "))
                    work = float(input("Введите работу: "))
                    print(f"Время = {calcs.calc_time_power_wt(power, work)}")
        case enum.COP:
            match option:
                case 1:
                    work_useful = float(input("Введите полезную работу: "))
                    work_total = float(input("Введите затраченную работу: "))
                    print(f"КПД = {calcs.calc_cop(work_useful, work_total)}")
                case 2:
                    cop = float(input("Введите КПД: "))
                    work_total = float(input("Введите затраченную работу: "))
                    print(f"Полезная работа = {calcs.calc_work_useful_cop(cop, work_total)}")
                case 3:
                    cop = float(input("Введите КПД: "))
                    work_useful = float(input("Введите полезную работу: "))
                    print(f"Затраченная работа = {calcs.calc_work_total_cop(cop, work_useful)}")
        case enum.PERIOD_SM:
            match option:
                case 1:
                    length = float(input("Введите длину маятника: "))
                    print(f"Период колебаний математического маятника = {calcs.calc_length_period_sm(length)}")
                case 2:
                    period_sm = float(input("Введите период: "))
                    print(f"Длина маятника = {calcs.calc_length_period_sm(period_sm)}")
        case enum.PERIOD_SP:
            match option:
                case 1:
                    mass = float(input("Введите массу: "))
                    spring_constant = float(input("Введите коэффициент жесткости: "))
                    print(f"Период колебаний пружинного маятника = {calcs.calc_period_sp(mass, spring_constant)}")
                case 2:
                    period_sp = float(input("Введите период: "))
                    spring_constant = float(input("Введите коэффициент жесткости: "))
                    print(f"Масса = {calcs.calc_mass_period_sp(period_sp, spring_constant)}")
                case 3:
                    period_sp = float(input("Введите период: "))
                    mass = float(input("Введите массу: "))
                    print(f"Коэффициент жесткости = {calcs.calc_spring_constant_period_sp(period_sp, mass)}")
        case enum.HARMONIC_OSCILLATION:
            match option:
                case 1:
                    amplitude = float(input("Введите амплитуду колебаний: "))
                    frequency = float(input("Введите частоту колебаний: "))
                    time = float(input("Введите время: "))
                    print(f"Уравнение гармонических колебаний = {calcs.calc_harmonic_oscillation(amplitude, frequency, time)}")
                case 2:
                    harmonic_oscillation = float(input("Введите гармонический колебания: "))
                    frequency = float(input("Введите частоту колебаний: "))
                    time = float(input("Введите время: "))
                    print(f"Амплитуда колебаний = {calcs.calc_amplitude_harmonic_oscillation(harmonic_oscillation, frequency, time)}")
                case 3:
                    harmonic_oscillation = float(input("Введите гармонический колебания: "))
                    amplitude = float(input("Введите амплитуду колебаний: "))
                    print(f"Косинус = {calcs.calc_cos_harmonic_oscillation(harmonic_oscillation, amplitude)}")
        case enum.WAVE_LENGTH:
            match option:
                case 1:
                    speed = float(input("Введите скорость: "))
                    period = float(input("Введите период: "))
                    print(f"Длина волны = {calcs.calc_wave_length(speed, period)}")
                case 2:
                    wave_length = float(input("Введите длину волны: "))
                    period = float(input("Введите период: "))
                    print(f"Скорость = {calcs.calc_speed_wave_length(wave_length, period)}")
                case 3:
                    wave_length = float(input("Введите длину волны: "))
                    speed = float(input("Введите скорость: "))
                    print(f"Период = {calcs.calc_period_wave_length(wave_length, speed)}")
        case enum.FRICTIONAL_FORCE:
            match option:
                case 1:
                    normal_force = float(input("Введите силу реакции опоры: "))
                    friction_coefficient = float(input("Введите коэффициент трения: "))
                    print(f"Сила трения = {calcs.calc_frictional_force(normal_force, friction_coefficient)}")
                case 2:
                    frictional_force = float(input("Введите силу трения: "))
                    normal_force = float(input("Введите силу реакции опоры: "))
                    print(f"Коэффициент трения = {calcs.calc_friction_coefficient_frictional_force(frictional_force, normal_force)}")
                case 3:
                    frictional_force = float(input("Введите силу трения: "))
                    friction_coefficient = float(input("Введите коэффициент трения: "))
                    print(f"Сила реакции опоры = {calcs.calc_normal_force_frictional_force(frictional_force, friction_coefficient)}")
