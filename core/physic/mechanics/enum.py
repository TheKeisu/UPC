###########
# МЕХАНИКА
###########
PRESSURE = 1
DENSITY = 2
PRESSURE_DEPTH = 3
GRAVITY = 4
ARCHIMEDES_FORCE = 5
ACCELERATED_MOTION = 6
CIRCLE_SPEED = 7
CENTRIPETAL_ACCELERATION = 8
NEWTONS_SECOND_LAW = 9
ELASTIC_FORCE = 10
IMPULSE_BODY = 11
IMPULSE_FORCE = 12
MOMENT_OF_FORCE = 13
RAISED_POTENTIAL_ENERGY = 14
DEFORMED_POTENTIAL_ENERGY = 15
KINETIC_ENERGY = 16
WORK = 17
POWER_WT = 18
COP = 19 # КПД
PERIOD_SM = 20 # Период колебаний математического маятника
PERIOD_SP = 21 # Период колебаний пружинного маятника
HARMONIC_OSCILLATION = 22
WAVE_LENGTH = 23
FRICTIONAL_FORCE = 24
ACCELERATION = 25

FORMULAS = {
    "pressure": {
        "subject_key": "механика",
        "title": "Давление",
        "description": "Давление, создаваемое силой, действующей на единицу площади поверхности",
        "formula_view": "P = F / S",
        "cases": {
            1: {
                "name": "Найти давление",
                "inputs": [
                    ("F", "Сила"),
                    ("S", "Площадь")
                ],
                "output": "Давление",
                "function": "core.physic.mechanics.calculations.calc_pressure",
                "SI": "Па"
            },
            2: {
                "name": "Найти силу",
                "inputs": [
                    ("P", "Давление"),
                    ("S", "Площадь")
                ],
                "output": "Сила",
                "function": "core.physic.mechanics.calculations.calc_force_pressure"
            },
            3: {
                "name": "Найти площадь",
                "inputs": [
                    ("F", "Сила"),
                    ("P", "Давление")
                ],
                "output": "Площадь",
                "function": "core.physic.mechanics.calculations.calc_area_pressure"
            }
        }
    },
    "density": {
        "subject_key": "механика",
        "title": "Плотность",
        "description": "Плотность вещества, определяющая массу единицы объема",
        "formula_view": "ρ = m / V",
        "cases": {
            1: {
                "name": "Найти плотность",
                "inputs": [
                    ("m", "Масса"),
                    ("V", "Объем")
                ],
                "output": "Плотность",
                "function": "core.physic.mechanics.calculations.calc_density"
            },
            2: {
                "name": "Найти массу",
                "inputs": [
                    ("ρ", "Плотность"),
                    ("V", "Объем")
                ],
                "output": "Масса",
                "function": "core.physic.mechanics.calculations.calc_mass_density"
            },
            3: {
                "name": "Найти объем",
                "inputs": [
                    ("m", "Масса"),
                    ("ρ", "Плотность")
                ],
                "output": "Объем",
                "function": "core.physic.mechanics.calculations.calc_volume_density"
            }
        }
    },
    "pressure_depth": {
        "subject_key": "механика",
        "title": "Давление на глубине",
        "description": "Давление, создаваемое столбом жидкости на определенной глубине",
        "formula_view": "P = ρ * g * h",
        "cases": {
            1: {
                "name": "Найти давление",
                "inputs": [
                    ("ρ", "Плотность"),
                    ("h", "Высота")
                ],
                "output": "Давление",
                "function": "core.physic.mechanics.calculations.calc_pressure_depth"
            },
            2: {
                "name": "Найти плотность",
                "inputs": [
                    ("P", "Давление"),
                    ("h", "Высота")
                ],
                "output": "Плотность",
                "function": "core.physic.mechanics.calculations.calc_density_depth"
            },
            3: {
                "name": "Найти высоту",
                "inputs": [
                    ("ρ", "Плотность"),
                    ("P", "Давление")
                ],
                "output": "Высота",
                "function": "core.physic.mechanics.calculations.calc_height_depth"
            }
        }
    },
    "gravity": {
        "subject_key": "механика",
        "title": "Сила тяжести",
        "description": "Сила, с которой Земля притягивает тело к своей поверхности",
        "formula_view": "F = m * g",
        "cases": {
            1: {
                "name": "Найти силу тяжести",
                "inputs": [
                    ("m", "Масса")
                ],
                "output": "Сила тяжести",
                "function": "core.physic.mechanics.calculations.calc_gravity"
            },
            2: {
                "name": "Найти массу",
                "inputs": [
                    ("F", "Сила тяжести")
                ],
                "output": "Масса",
                "function": "core.physic.mechanics.calculations.calc_mass_gravity"
            }
    },
    "archimedes_force": {
        "subject_key": "механика",
        "title": "Сила Архимеда",
        "description": "Сила, с которой жидкость или газ действует на погруженное в них тело",
        "formula_view": "F = ρ * V * g",
        "cases": {
            1: {
                "name": "Найти силу Архимеда",
                "inputs": [
                    ("ρ", "Плотность"),
                    ("V", "Объем")
                ],
                "output": "Сила Архимеда",
                "function": "core.physic.mechanics.calculations.calc_archimedes_force"
            },
            2: {
                "name": "Найти плотность",
                "inputs": [
                    ("F", "Сила Архимеда"),
                    ("V", "Объем")
                ],
                "output": "Плотность",
                "function": "core.physic.mechanics.calculations.calc_density_archimedes_force"
            },
            3: {
                "name": "Найти объем",
                "inputs": [
                    ("ρ", "Плотность"),
                    ("F", "Сила Архимеда")
                ],
                "output": "Объем",
                "function": "core.physic.mechanics.calculations.calc_volume_archimedes_force"
            }
        }
    }
    },
    "accelerated_motion": {
        "subject_key": "механика",
        "title": "Ускоренное движение",
        "description": "Зависимость между скоростью, начальной скоростью, ускорением и временем при ускоренном движении",
        "formula_view": "v = v₀ + a * t",
        "cases": {
            1: {
                "name": "Найти скорость",
                "inputs": [
                    ("v₀", "Начальная скорость"),
                    ("a", "Ускорение"),
                    ("t", "Время")
                ],
                "output": "Скорость",
                "function": "core.physic.mechanics.calculations.calc_accelerated_motion"
            },
            2: {
                "name": "Найти начальную скорость",
                "inputs": [
                    ("v", "Скорость"),
                    ("a", "Ускорение"),
                    ("t", "Время")
                ],
                "output": "Начальная скорость",
                "function": "core.physic.mechanics.calculations.calc_initial_speed"
            },
            3: {
                "name": "Найти ускорение",
                "inputs": [
                    ("v", "Скорость"),
                    ("v₀", "Начальная скорость"),
                    ("t", "Время")
                ],
                "output": "Ускорение",
                "function": "core.physic.mechanics.calculations.calc_acceleration_accelerated_motion"
            },
            4: {
                "name": "Найти время",
                "inputs": [
                    ("v", "Скорость"),
                    ("v₀", "Начальная скорость"),
                    ("a", "Ускорение")
                ],
                "output": "Время",
                "function": "core.physic.mechanics.calculations.calc_time_accelerated_motion"
    },
        },
            },
    "circle_speed": {
        "subject_key": "механика",
        "title": "Скорость при круговом движении",
        "description": "Скорость тела, движущегося по окружности, зависит от радиуса и периода",
        "formula_view": "v = 2 * π * r / T",
        "cases": {
            1: {
                "name": "Найти скорость",
                "inputs": [
                    ("r", "Радиус"),
                    ("T", "Период")
                ],
                "output": "Скорость",
                "function": "core.physic.mechanics.calculations.calc_circle_speed"
            },
            2: {
                "name": "Найти радиус",
                "inputs": [
                    ("v", "Скорость"),
                    ("T", "Период")
                ],
                "output": "Радиус",
                "function": "core.physic.mechanics.calculations.calc_radius_circle_speed"
            },
            3: {
                "name": "Найти период",
                "inputs": [
                    ("v", "Скорость"),
                    ("r", "Радиус")
                ],
                "output": "Период",
                "function": "core.physic.mechanics.calculations.calc_period_circle_speed"
            }
    },
        },
    "centripetal_acceleration": {
        "subject_key": "механика",
        "title": "Центростремительное ускорение",
        "description": "Ускорение, направленное к центру окружности при круговом движении",
        "formula_view": "a = v² / r",
        "cases": {
            1: {
                "name": "Найти ускорение",
                "inputs": [
                    ("v", "Скорость"),
                    ("r", "Радиус")
                ],
                "output": "Ускорение",
                "function": "core.physic.mechanics.calculations.calc_centripetal_acceleration"
            },
            2: {
                "name": "Найти скорость",
                "inputs": [
                    ("a", "Ускорение"),
                    ("r", "Радиус")
                ],
                "output": "Скорость",
                "function": "core.physic.mechanics.calculations.calc_speed_centripetal_acceleration"
            },
            3: {
                "name": "Найти радиус",
                "inputs": [
                    ("v", "Скорость"),
                    ("a", "Ускорение")
                ],
                "output": "Радиус",
                "function": "core.physic.mechanics.calculations.calc_radius_centripetal_acceleration"
    },
        },
    },
    "newtons_second_law": {
        "subject_key": "механика",
        "title": "Второй закон Ньютона",
        "description": "Зависимость между силой, массой и ускорением тела",
        "formula_view": "F = m * a",
        "cases": {
            1: {
                "name": "Найти силу",
                "inputs": [
                    ("m", "Масса"),
                    ("a", "Ускорение")
                ],
                "output": "Сила",
                "function": "core.physic.mechanics.calculations.calc_force_newton_second_law"
            },
            2: {
                "name": "Найти массу",
                "inputs": [
                    ("F", "Сила"),
                    ("a", "Ускорение")
                ],
                "output": "Масса",
                "function": "core.physic.mechanics.calculations.calc_mass_newton_second_law"
            },
            3: {
                "name": "Найти ускорение",
                "inputs": [
                    ("F", "Сила"),
                    ("m", "Масса")
                ],
                "output": "Ускорение",
                "function": "core.physic.mechanics.calculations.calc_acceleration_newton_second_law"
    },
        },
    },
    "elastic_force": {
        "subject_key": "механика",
        "title": "Сила упругости",
        "description": "Сила, возникающая при деформации тела и пропорциональная величине деформации",
        "formula_view": "F = k * x",
        "cases": {
            1: {
                "name": "Найти силу",
                "inputs": [
                    ("k", "Жесткость пружины"),
                    ("x", "Деформация")
                ],
                "output": "Сила",
                "function": "core.physic.mechanics.calculations.calc_elastic_force",
            },
            2: {
                "name": "Найти жесткость пружины",
                "inputs": [
                    ("F", "Сила"),
                    ("x", "Деформация")
                ],
                "output": "Жесткость пружины",
                "function": "core.physic.mechanics.calculations.calc_spring_constant"
            },
            3: {
                "name": "Найти деформацию",
                "inputs": [
                    ("F", "Сила"),
                    ("k", "Жесткость пружины")
                ],
                "output": "Деформация",
                "function": "core.physic.mechanics.calculations.calc_displacement_elastic_force"
        }
            }
                },
    "impulse_body": {
        "subject_key": "механика",
        "title": "Импульс тела",
        "description": "Импульс тела, определяющий его движение и взаимодействие с другими телами",
        "formula_view": "p = m * v",
        "cases": {
            1: {
                "name": "Найти импульс",
                "inputs": [
                    ("m", "Масса"),
                    ("v", "Скорость")
                ],
                "output": "Импульс",
                "function": "core.physic.mechanics.calculations.calc_impulse_body"
                },
            2: {
                "name": "Найти массу",
                "inputs": [
                    ("p", "Импульс"),
                    ("v", "Скорость")
                ],
                "output": "Масса",
                "function": "core.physic.mechanics.calculations.calc_mass_impulse_body"
                },
            3: {
                "name": "Найти скорость",
                "inputs": [
                    ("p", "Импульс"),
                    ("m", "Масса")
                ],
                "output": "Скорость",
                "function": "core.physic.mechanics.calculations.calc_speed_impulse_body"
            }
    },
        },
    "impulse_force": {
        "subject_key": "механика",
        "title": "Импульс силы",
        "description": "Импульс силы, определяющий изменение импульса тела при воздействии силы в течение времени",
        "formula_view": "J = F * t",
        "cases": {
            1: {
                "name": "Найти импульс силы",
                "inputs": [
                    ("F", "Сила"),
                    ("t", "Время")                ],
                "output": "Импульс силы",
                "function": "core.physic.mechanics.calculations.calc_impulse_force"
            },
            2: {
                "name": "Найти силу",
                "inputs": [
                    ("J", "Импульс силы"),
                    ("t", "Время")                ],
                "output": "Сила",
                "function": "core.physic.mechanics.calculations.calc_force_impulse_force"
            },
            3: {
                "name": "Найти время",
                "inputs": [
                    ("J", "Импульс силы"),
                    ("F", "Сила")                ],
                "output": "Время",
                "function": "core.physic.mechanics.calculations.calc_time_impulse_force"
            }
        }
    },
    "moment_of_force": {
        "subject_key": "механика",
        "title": "Момент силы",
        "description": "Момент силы, определяющий вращательное действие силы относительно точки опоры",
        "formula_view": "M = F * r",
        "cases": {
            1: {
                "name": "Найти момент силы",
                "inputs": [
                    ("F", "Сила"),
                    ("r", "Плечо силы")
                ],
                "output": "Момент силы",
                "function": "core.physic.mechanics.calculations.calc_moment_of_force"
            },
            2: {
                "name": "Найти силу",
                "inputs": [
                    ("M", "Момент силы"),
                    ("r", "Плечо силы")
                ],
                "output": "Сила",
                "function": "core.physic.mechanics.calculations.calc_force_moment_of_force"
            },
            3: {
                "name": "Найти плечо силы",
                "inputs": [
                    ("M", "Момент силы"),
                    ("F", "Сила")
                ],
                "output": "Плечо силы",
                "function": "core.physic.mechanics.calculations.calc_lever_arm_moment_of_force"
            }
        }
    },
    "raised_potential_energy": {
        "subject_key": "механика",
        "title": "Потенциальная энергия при подъеме",
        "description": "Потенциальная энергия, приобретенная телом при подъеме на определенную высоту",
        "formula_view": "E = m * g * h",
        "cases": {
            1: {
                "name": "Найти потенциальную энергию",
                "inputs": [
                    ("m", "Масса"),
                    ("h", "Высота")
                ],
                "output": "Потенциальная энергия",
                "function": "core.physic.mechanics.calculations.calc_raised_potential_energy"
            },
            2: {
                "name": "Найти массу",
                "inputs": [
                    ("E", "Потенциальная энергия"),
                    ("h", "Высота")
                ],
                "output": "Масса",
                "function": "core.physic.mechanics.calculations.calc_mass_raised_potential_energy"
            },
            3: {
                "name": "Найти высоту",
                "inputs": [
                    ("E", "Потенциальная энергия"),
                    ("m", "Масса")
                ],
                "output": "Высота",
                "function": "core.physic.mechanics.calculations.calc_height_raised_potential_energy"
            }
        },
    },  
    "deformed_potential_energy": {
        "subject_key": "механика",
        "title": "Потенциальная энергия при деформации",
        "description": "Потенциальная энергия, накопленная в теле при его деформации",
        "formula_view": "E = 0.5 * k * x²",
        "cases": {
            1: {
                "name": "Найти потенциальную энергию",
                "inputs": [
                    ("k", "Жесткость пружины"),
                    ("x", "Деформация")
                ],
                "output": "Потенциальная энергия",
                "function": "core.physic.mechanics.calculations.calc_deformed_potential_energy"
            },
            2: {
                "name": "Найти жесткость пружины",
                "inputs": [
                    ("E", "Потенциальная энергия"),
                    ("x", "Деформация")
                ],
                "output": "Жесткость пружины",
                "function": "core.physic.mechanics.calculations.calc_spring_constant_deformed_potential_energy"
            },
            3: {
                "name": "Найти деформацию",
                "inputs": [
                    ("E", "Потенциальная энергия"),
                    ("k", "Жесткость пружины")
                ],
                "output": "Деформация",
                "function": "core.physic.mechanics.calculations.calc_displacement_deformed_potential_energy",
                "SI": ""
            }
        },
    },
    "kinetic_energy": {
        "subject_key": "механика",
        "title": "Кинетическая энергия",
        "description": "Кинетическая энергия, определяющая энергию движения тела",
        "formula_view": "KE = 0.5 * m * v²",
        "cases": {
            1: {
                "name": "Найти кинетическую энергию",
                "inputs": [
                    ("m", "Масса"),
                    ("v", "Скорость")
                ],
                "output": "Кинетическая энергия",
                "function": "core.physic.mechanics.calculations.calc_kinetic_energy",
                "SI": "Дж"
                },
            2: {
                "name": "Найти массу",
                "inputs": [
                    ("K", "Кинетическая энергия"),
                    ("v", "Скорость")
                ],
                "output": "Масса",
                "function": "core.physic.mechanics.calculations.calc_mass_kinetic_energy",
                "SI": "кг"
            },
            3: {
                "name": "Найти скорость",
                "inputs": [
                    ("K", "Кинетическая энергия"),
                    ("m", "Масса")
                ],
                "output": "Скорость",
                "function": "core.physic.mechanics.calculations.calc_speed_kinetic_energy",
                "SI": "м/с"
            },
        },
    },
    "work": {
        "subject_key": "механика",
        "title": "Работа",
        "description": "Работа, выполняемая силой при перемещении тела на определенное расстояние",
        "formula_view": "W = F * d",
        "cases": {
            1: {
                "name": "Найти работу",
                "inputs": [
                    ("F", "Сила"),
                    ("d", "Расстояние")
                ],
                "output": "Работа",
                "function": "core.physic.mechanics.calculations.calc_work",
                "SI": "Дж"
            },
            2: {
                "name": "Найти силу",
                "inputs": [
                    ("W", "Работа"),
                    ("d", "Расстояние")
                ],
                "output": "Сила",
                "function": "core.physic.mechanics.calculations.calc_force_work",
                "SI": "Н"
            },
            3: {
                "name": "Найти расстояние",
                "inputs": [
                    ("W", "Работа"),
                    ("F", "Сила")
                ],
                "output": "Расстояние",
                "function": "core.physic.mechanics.calculations.calc_distance_work",
                "SI": "м"
            }
        },
    },
    "power_wt": {
        "subject_key": "механика",
        "title": "Мощность",
        "description": "Мощность, определяющая скорость выполнения работы",
        "formula_view": "P = W / t",
        "cases": {
            1: {
                "name": "Найти мощность",
                "inputs": [
                    ("W", "Работа"),
                    ("t", "Время")                ],
                "output": "Мощность",
                "function": "core.physic.mechanics.calculations.calc_power_wt",
                "SI": "Вт"
            },
            2: {
                "name": "Найти работу",
                "inputs": [
                    ("P", "Мощность"),
                    ("t", "Время")                
                    ],
                "output": "Работа",
                "function": "core.physic.mechanics.calculations.calc_work_power_wt",
                "SI": "Дж"
            },
            3: {
                "name": "Найти время",
                "inputs": [
                    ("P", "Мощность"),
                    ("W", "Работа")                
                    ],
                "output": "Время",
                "function": "core.physic.mechanics.calculations.calc_time_power_wt",
                "SI": "с"
            },
        },
    },
    "cop": {
        "subject_key": "механика",
        "title": "Коэффициент полезного действия (КПД)",
        "description": "КПД, определяющий эффективность использования энергии в процессе выполнения работы",
        "formula_view": "COP = W₁ / W₂",
        "cases": {
            1: {
                "name": "Найти КПД",
                "inputs": [
                    ("W₁", "Полезная работа"),
                    ("W₂", "Затраченная работа")                ],
                "output": "КПД",
                "function": "core.physic.mechanics.calculations.calc_cop",
                "SI": "%"
            },
            2: {
                "name": "Найти полезную работу",
                "inputs": [
                    ("COP", "КПД"),
                    ("W₂", "Затраченная работа")                ],
                "output": "Полезная работа",
                "function": "core.physic.mechanics.calculations.calc_work_useful_cop",
                "SI": "Дж"
            },
            3: {
                "name": "Найти затраченную работу",
                "inputs": [
                    ("COP", "КПД"),
                    ("W₁", "Полезная работа")                ],
                "output": "Затраченная работа",
                "function": "core.physic.mechanics.calculations.calc_work_total_cop",
                "SI": "Дж"
            },
        },
    },
    "period_sm": {
        "subject_key": "механика",
        "title": "Период колебаний математического маятника",
        "description": "Период колебаний математического маятника, зависящий от его длины",
        "formula_view": "T = 2 * π * √(L / g)",
        "cases": {
            1: {
                "name": "Найти период",
                "inputs": [
                    ("L", "Длина маятника")
                ],
                "output": "Период колебаний",
                "function": "core.physic.mechanics.calculations.calc_period_sm",
                "SI": "с"
            },
            2: {
                "name": "Найти длину маятника",
                "inputs": [
                    ("T", "Период колебаний")
                ],
                "output": "Длина маятника",
                "function": "core.physic.mechanics.calculations.calc_length_period_sm",
                "SI": "м"
            }
        },
    },
    "period_sp": {
        "subject_key": "механика",
        "title": "Период колебаний пружинного маятника",
        "description": "Период колебаний пружинного маятника, зависящий от массы и жесткости пружины",
        "formula_view": "T = 2 * π * √(m / k)",
        "cases": {
            1: {
                "name": "Найти период",
                "inputs": [
                    ("m", "Масса"),
                    ("k", "Жесткость пружины")
                ],
                "output": "Период колебаний",
                "function": "core.physic.mechanics.calculations.calc_period_sp",
                "SI": "с"
            },
            2: {
                "name": "Найти массу",
                "inputs": [
                    ("T", "Период колебаний"),
                    ("k", "Жесткость пружины")
                ],
                "output": "Масса",
                "function": "core.physic.mechanics.calculations.calc_mass_period_sp",
                "SI": "кг"
            },
            3: {
                "name": "Найти жесткость пружины",
                "inputs": [
                    ("T", "Период колебаний"),
                    ("m", "Масса")
                ],
                "output": "Жесткость пружины",
                "function": "core.physic.mechanics.calculations.calc_spring_constant_period_sp",
                "SI": "Н/м"
            }
        },
    },
    "harmonic_oscillation": {
        "subject_key": "механика",
        "title": "Уравнение гармонических колебаний",
        "description": "Уравнение, описывающее гармонические колебания тела",
        "formula_view": "x(t) = A * cos(ωt)",
        "cases": {
            1: {
                "name": "Найти положение тела в момент времени t",
                "inputs": [
                    ("A", "Амплитуда"),
                    ("ω", "Угловая частота"),
                    ("t", "Время")
                ],
                "output": "Положение тела",
                "function": "core.physic.mechanics.calculations.calc_position_harmonic_oscillation",
                "SI": "м"
            },
            2: {
                "name": "Найти амплитуду",
                "inputs": [
                    ("x", "Положение тела"),
                    ("ω", "Угловая частота"),
                    ("t", "Время")
                ],
                "output": "Амплитуда",
                "function": "core.physic.mechanics.calculations.calc_amplitude_harmonic_oscillation",
                "SI": "м"
            },
            3: {
                "name": "Найти угловую частоту",
                "inputs": [
                    ("x", "Положение тела"),
                    ("A", "Амплитуда"),
                    ("t", "Время")
                ],
                "output": "Угловая частота",
                "function": "core.physic.mechanics.calculations.calc_cos_harmonic_oscillation",
                "SI": "рад/с"
            },
        },
    },
    "wave_length": {
        "subject_key": "механика",
        "title": "Длина волны",
        "description": "Длина волны, определяющая расстояние между двумя соседними максимумами или минимумами волны",
        "formula_view": "λ = v * T",
        "cases": {
            1: {
                "name": "Найти длину волны",
                "inputs": [
                    ("v", "Скорость волны"),
                    ("T", "Период волны")
                ],
                "output": "Длина волны",
                "function": "core.physic.mechanics.calculations.calc_wave_length",
                "SI": "м"
            },
            2: {
                "name": "Найти скорость волны",
                "inputs": [
                    ("λ", "Длина волны"),
                    ("T", "Период волны")
                ],
                "output": "Скорость волны",
                "function": "core.physic.mechanics.calculations.calc_wave_speed",
                "SI": "м/с"
            },
            3: {
                "name": "Найти период волны",
                "inputs": [
                    ("λ", "Длина волны"),
                    ("v", "Скорость волны")
                ],
                "output": "Период волны",
                "function": "core.physic.mechanics.calculations.calc_wave_period",
                "SI": "с"
            }
        },
    },
    "frictional_force": {
        "subject_key": "механика",
        "title": "Сила трения",
        "description": "Сила трения, возникающая при взаимодействии двух поверхностей и зависящая от коэффициента трения и силы реакции опоры",
        "formula_view": "F_friction = μ * N",
        "cases": {
            1: {
                "name": "Найти силу трения",
                "inputs": [
                    ("μ", "Коэффициент трения"),
                    ("N", "Сила реакции опоры")
                ],
                "output": "Сила трения",
                "function": "core.physic.mechanics.calculations.calc_frictional_force",
                "SI": "Н"
            },
            2: {
                "name": "Найти коэффициент трения",
                "inputs": [
                    ("F_friction", "Сила трения"),
                    ("N", "Сила реакции опоры")
                ],
                "output": "Коэффициент трения",
                "function": "core.physic.mechanics.calculations.calc_coefficient_frictional_force",
                "SI": ""
            },
            3: {
                "name": "Найти силу реакции опоры",
                "inputs": [
                    ("F_friction", "Сила трения"),
                    ("μ", "Коэффициент трения")
                ],
                "output": "Сила реакции опоры",
                "function": "core.physic.mechanics.calculations.calc_normal_force_frictional_force",
                "SI": "Н"
            },
        },
    },
    "acceleration": {
        "subject_key": "механика",
        "title": "Ускорение",
        "description": "Ускорение, определяющее изменение скорости тела во времени",
        "formula_view": "a = Δv / Δt",
        "cases": {
            1: {
                "name": "Найти ускорение",
                "inputs": [
                    ("Δv", "Изменение скорости"),
                    ("Δt", "Изменение времени")
                ],
                "output": "Ускорение",
                "function": "core.physic.mechanics.calculations.calc_acceleration",
                "SI": "м/с²"
            },
            2: {
                "name": "Найти изменение скорости",
                "inputs": [
                    ("a", "Ускорение"),
                    ("Δt", "Изменение времени")
                ],
                "output": "Изменение скорости",
                "function": "core.physic.mechanics.calculations.calc_change_speed_acceleration",
                "SI": "м/с"
            },
            3: {
                "name": "Найти изменение времени",
                "inputs": [
                    ("a", "Ускорение"),
                    ("Δv", "Изменение скорости")
                ],
                "output": "Изменение времени",
                "function": "core.physic.mechanics.calculations.calc_change_time_acceleration",
                "SI": "с"
            }
        }
    }
}
mechanics = {
    PRESSURE: """Выберите величину, которую нужно найти"
                             " (Давление - 1"
                             " Сила - 2"
                             " Площадь - 3): """,
    DENSITY: """Введите величину, которую нужно найти"
                         " (Плотность - 1"
                         " Масса - 2"
                         " Объем - 3): """,
    PRESSURE_DEPTH: """Выберите величину, которую нужно найти"
                             " (Давление - 1"
                             " Плотность - 2"
                             " Высоту - 3): """,
    GRAVITY: """Выберите величину, которую нужно найти"
                             " (Сила тяжести - 1"
                             " Масса - 2): """,
    ARCHIMEDES_FORCE: """Выберите величину, которую нужно найти"
                             " (Сила Архимеда - 1"
                             " Объём - 2"
                             " Плотность - 3): """,
    ACCELERATED_MOTION: """Выберите величину, которую нужно найти"
                             " (Скорость - 1"
                             " Начальная скорость - 2"
                             " Ускорение - 3)"
                             " Время - 4): """,
    CIRCLE_SPEED: """Выберите величину, которую нужно найти"
                             " (Скорость - 1"
                             " Радиус - 2"
                             " Период - 3): """,
    CENTRIPETAL_ACCELERATION: """Выберите величину, которую нужно найти"
                             " (Ускорение - 1"
                             " Скорость - 2"
                             " Радиус - 3): """,
    NEWTONS_SECOND_LAW: """Выберите величину, которую нужно найти
                             " Сила - 1"
                             " Масса - 2"
                             " Ускорение - 3: """,
    ELASTIC_FORCE : """Выберите величину, которую нужно найти
                             " Сила упругости - 1
                             " Коэффицент жесткости материала - 2
                             " Величина деформации - 3""",
    IMPULSE_BODY: """Выберите величину, которую нужно найти
                             " Импульс тела - 1
                             " Масса - 2
                             " Скорость - 3""",
    IMPULSE_FORCE: """Выберите величину, которую нужно найти
                             " Импульс силы - 1
                             " Сила - 2
                             " Время - 3""",
    MOMENT_OF_FORCE: """Выберите величину, которую нужно найти
                             " Момент силы - 1
                             " Плечо силы (r) - 2
                             " Сила - 3""",
    RAISED_POTENTIAL_ENERGY: """Выберите величину, которую нужно найти
                             " Потенциальная энергия - 1
                             " Масса - 2
                             " Высота - 3""",
    DEFORMED_POTENTIAL_ENERGY: """Выберите величину, которую нужно найти
                             " Потенциальная энергия - 1
                             " Коэффицент жесткости материала - 2
                             " Величина деформации - 3""",
    KINETIC_ENERGY: """Выберите величину, которую нужно найти
                             " Кинетическая энергия - 1
                             " Масса - 2
                             " Скорость - 3""",
    WORK: """Выберите величину, которую нужно найти
                             " Работа - 1
                             " Сила - 2
                             " Путь - 3""",
    POWER_WT: """Выберите величину, которую нужно найти
                             " Мощность - 1
                             " Работа - 2
                             " Время - 3""",
    COP: """Выберите величину, которую нужно найти
                             " КПД - 1
                             " Полезная работа - 2
                             " Затраченная работа - 3""",
    PERIOD_SM: """Выберите величину, которую нужно найти
                             " Период колебаний математического маятника - 1
                             " Длина маятника - 2""",
    PERIOD_SP: """Выберите величину, которую нужно найти
                             " Период колебаний пружинного маятника - 1
                             " Масса - 2
                             " Жёсткость пружины - 3""",
    HARMONIC_OSCILLATION: """Выберите величину, которую нужно найти
                             " Уравнение гармонических колебаний - 1
                             " Амплитуда - 2
                             " Косинус (coswt) - 3""",
    WAVE_LENGTH: """Выберите величину, которую нужно найти
                             " Длина волны - 1
                             " Скорость - 2
                             " Период - 3""",
    FRICTIONAL_FORCE: """Выберите величину, которую нужно найти
                             " Сила трения - 1
                             " Коэффицент трения - 2
                             " Сила реакции опоры - 3"""
}
