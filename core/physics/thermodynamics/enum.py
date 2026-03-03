#####################################
# МОЛЕКУЛЯРНАЯ ФИЗИКА И ТЕРМОДИНАМИКА
#####################################

SUBSTANCE_AMOUNT = 1
AVG_KINETIC_ENERGY = 2
RELATIVE_HUMIDITY = 3
INTERNAL_ENERGY_IDEAL_GAS = 4
GAS_WORK = 5
HEAT_AMOUNT_HEATING = 6
HEAT_AMOUNT_MELTING = 7
HEAT_AMOUNT_VAPORIZATION = 8
HEAT_AMOUNT_COMBUSTION = 9
FIRST_THERMODYNAMICS_LAW = 10
COP_THERMAL_ENGINE = 11
COP_IDEAL_ENGINE = 12

FORMULAS = {
    "substance_amount": {
        "subject_key": "термодинамика",
        "title": "Кол-во вещества",
        "description": "Кол-во вещества - это физическая величина, которая характеризует количество частиц в веществе. Она измеряется в молях (моль) и обозначается символом n.",
        "formula_view": "n = m / M",
        "cases": {
            1: {
                "name": "Кол-во вещества",
                "inputs": [
                    ("m", "Масса вещества"),
                    ("M", "Молярная масса")
                ],
                "output": "Кол-во вещества",
                "function": "core.physics.thermodynamics.calculations.calc_substance_amount",
                "SI": "моль"
            },
            2: {
                "name": "Масса вещества",
                "inputs": [
                    ("n", "Кол-во вещества"),
                    ("M", "Молярная масса")
                ],
                "output": "Масса вещества",
                "function": "core.physics.thermodynamics.calculations.calc_mass_substance_amount",
                "SI": "кг"
            },
            3: {
                "name": "Молярная масса",
                "inputs": [
                    ("n", "Кол-во вещества"),
                    ("m", "Масса вещества")
                ],
                "output": "Молярная масса",
                "function": "core.physics.thermodynamics.calculations.calc_molar_mass_substance_amount",
                "SI": "кг/моль"
            },
        },
    },
    "avg_kinetic_energy": {
        "subject_key": "термодинамика",
        "title": "Средняя кинетическая энергия",
        "description": "Средняя кинетическая энергия - это физическая величина, которая характеризует среднюю энергию движения частиц в веществе. Она измеряется в джоулях (Дж) и обозначается символом E_k.",
        "formula_view": "E = (3/2) * k * T",
        "cases": {
            1: {
                "name": "Кинетическая энергия",
                "inputs": [
                    ("T", "Абсолютная температура")
                ],
                "output": "Средняя кинетическая энергия",
                "function": "core.physics.thermodynamics.calculations.calc_avg_kinetic_energy",
                "SI": "Дж"
            },
            2: {
                "name": "Абсолютная температура",
                "inputs": [
                    ("E", "Средняя кинетическая энергия")
                ],
                "output": "Абсолютная температура",
                "function": "core.physics.thermodynamics.calculations.calc_temperature_avg_kinetic_energy",
                "SI": "К"
            },
        },
    },
    "relative_humidity": {
        "subject_key": "термодинамика",
        "title": "Относительная влажность",
        "description": "Относительная влажность - это физическая величина, которая характеризует степень насыщенности воздуха водяным паром. Она измеряется в процентах (%) и обозначается символом φ.",
        "formula_view": "φ = (P_v / P_s) * 100%",
        "cases": {
            1: {
                "name": "Относительная влажность",
                "inputs": [
                    ("P_v", "Парциальное давление водяного пара в воздухе"),
                    ("P_s", "Давление насыщенного водяного пара при данной температуре")
                ],
                "output": "Относительная влажность",
                "function": "core.physics.thermodynamics.calculations.calc_relative_humidity",
                "SI": "%"
            },
            2: {
                "name": "Парциальное давление водяного пара в воздухе",
                "inputs": [
                    ("φ", "Относительная влажность"),
                    ("P_s", "Давление насыщенного водяного пара при данной температуре")
                ],
                "output": "Парциальное давление водяного пара в воздухе",
                "function": "core.physics.thermodynamics.calculations.calc_partial_vapor_pressure",
                "SI": "Па"
            },
            3: {
                "name": "Давление насыщенного водяного пара при данной температуре",
                "inputs": [
                    ("φ", "Относительная влажность"),
                    ("P_v", "Парциальное давление водяного пара в воздухе")
                ],
                "output": "Давление насыщенного водяного пара при данной температуре",
                "function": "core.physics.thermodynamics.calculations.calc_saturated_vapor_pressure",
                "SI": "Па"
            },
        },
    },
    "internal_energy_ideal_gas": {
        "subject_key": "термодинамика",
        "title": "Внутренняя энергия идеального газа",
        "description": "Внутренняя энергия идеального газа - это физическая величина, которая характеризует общую энергию всех частиц в газе. Она измеряется в джоулях (Дж) и обозначается символом U.",
        "formula_view": "U = (3/2) * n * R * T",
        "cases": {
            1: {
                "name": "Внутренняя энергия",
                "inputs": [
                    ("n", "Кол-во вещества"),
                    ("T", "Абсолютная температура")
                ],
                "output": "Внутренняя энергия",
                "function": "core.physics.thermodynamics.calculations.calc_internal_energy_ideal_gas",
                "SI": "Дж"
            },
            2: {
                "name": "Кол-во вещества",
                "inputs": [
                    ("U", "Внутренняя энергия"),
                    ("T", "Абсолютная температура")
                ],
                "output": "Кол-во вещества",
                "function": "core.physics.thermodynamics.calculations.calc_substance_amount_ideal_gas",
                "SI": "моль"
            },
            3: {
                "name": "Абсолютная температура",
                "inputs": [
                    ("U", "Внутренняя энергия"),
                    ("n", "Кол-во вещества")
                ],
                "output": "Абсолютная температура",
                "function": "core.physics.thermodynamics.calculations.calc_abs_temperature_ideal_gas",
                "SI": "К"
            }
        }
    },
    "gas_work": {
        "subject_key": "термодинамика",
        "title": "Работа газа",
        "description": "Работа газа - это физическая величина, которая характеризует количество энергии, передаваемой газом при изменении его объема. Она измеряется в джоулях (Дж) и обозначается символом W.",
        "formula_view": "W = P * ΔV",
        "cases": {
            1: {
                "name": "Работа газа",
                "inputs": [
                    ("P", "Давление"),
                    ("ΔV", "Изменение объёма")
                ],
                "output": "Работа газа",
                "function": "core.physics.thermodynamics.calculations.calc_gas_work",
                "SI": "Дж"
            },
            2: {
                "name": "Давление",
                "inputs": [
                    ("W", "Работа газа"),
                    ("ΔV", "Изменение объёма")
                ],
                "output": "Давление",
                "function": "core.physics.thermodynamics.calculations.calc_pressure_gas_work",
                "SI": "Па"
            },
            3: {
                "name": "Изменение объёма",
                "inputs": [
                    ("W", "Работа газа"),
                    ("P", "Давление")
                ],
                "output": "Изменение объёма",
                "function": "core.physics.thermodynamics.calculations.calc_volume_change_gas_work",
                "SI": "м³"
            }
        }
    },
    "heat_amount_heating": {
        "subject_key": "термодинамика",
        "title": "Теплота при нагревании",
        "description": "Теплота при нагревании - это физическая величина, которая характеризует количество энергии, передаваемой веществу при его нагревании. Она измеряется в джоулях (Дж) и обозначается символом Q.",
        "formula_view": "Q = c * m * ΔT",
        "cases": {
            1: {
                "name": "Теплота",
                "inputs": [
                    ("c", "Удельная теплоемкость"),
                    ("m", "Масса"),
                    ("ΔT", "Изменение температуры")
                ],
                "output": "Теплота",
                "function": "core.physics.thermodynamics.calculations.calc_heat_amount_heating",
                "SI": "Дж"
            },
            2: {
                "name": "Удельная теплоемкость",
                "inputs": [
                    ("Q", "Теплота"),
                    ("m", "Масса"),
                    ("ΔT", "Изменение температуры")
                ],
                "output": "Удельная теплоемкость",
                "function": "core.physics.thermodynamics.calculations.calc_heat_capacity",
                "SI": "Дж/(кг*К)"
            },
            3: {
                "name": "Масса",
                "inputs": [
                    ("Q", "Теплота"),
                    ("c", "Удельная теплоемкость"),
                    ("ΔT", "Изменение температуры")
                ],
                "output": "Масса",
                "function": "core.physics.thermodynamics.calculations.calc_mass_heat_amount_heating",
                "SI": "кг"
            },
            4: {
                "name": "Изменение температуры",
                "inputs": [
                    ("Q", "Теплота"),
                    ("m", "Масса"),
                    ("c", "Удельная теплоемкость")
                ],
                "output": "Изменение температуры",
                "function": "core.physics.thermodynamics.calculations.calc_temperature_change",
                "SI": "К"
            }
        }  
    },
    "heat_amount_melting": {
        "subject_key": "термодинамика",
        "title": "Теплота при плавлении",
        "description": "Теплота при плавлении - это физическая величина, которая характеризует количество энергии, передаваемой веществу при его плавлении. Она измеряется в джоулях (Дж) и обозначается символом Q.",
        "formula_view": "Q = λ * m",
        "cases": {
            1: {
                "name": "Теплота",
                "inputs": [
                    ("λ", "Удельная теплота плавления"),
                    ("m", "Масса")
                ],
                "output": "Теплота",
                "function": "core.physics.thermodynamics.calculations.calc_heat_amount_melting",
                "SI": "Дж"
            },
            2: {
                "name": "Удельная теплота плавления",
                "inputs": [
                    ("Q", "Теплота"),
                    ("m", "Масса")
                ],
                "output": "Удельная теплота плавления",
                "function": "core.physics.thermodynamics.calculations.calc_melting_point",
                "SI": "Дж/кг"
            },
            3: {
                "name": "Масса",
                "inputs": [
                    ("Q", "Теплота"),
                    ("λ", "Удельная теплота плавления")
                ],
                "output": "Масса",
                "function": "core.physics.thermodynamics.calculations.calc_mass_heat_amount_melting",
                "SI": "кг"
             }
        }
    },
    "heat_amount_vaporization": {
        "subject_key": "термодинамика",
        "title": "Теплота при парообразовании",
        "description": "Теплота при парообразовании - это физическая величина, которая характеризует количество энергии, передаваемой веществу при его парообразовании. Она измеряется в джоулях (Дж) и обозначается символом Q.",
        "formula_view": "Q = L * m",
        "cases": {
            1: {
                "name": "Теплота",
                "inputs": [
                    ("L", "Удельная теплота парообразования"),
                    ("m", "Масса")
                ],
                "output": "Теплота",
                "function": "core.physics.thermodynamics.calculations.calc_heat_amount_vaporization",
                "SI": "Дж"
            },
            2: {
                "name": "Удельная теплота парообразования",
                "inputs": [
                    ("Q", "Теплота"),
                    ("m", "Масса")
                ],
                "output": "Удельная теплота парообразования",
                "function": "core.physics.thermodynamics.calculations.calc_vaporization_heat",
                "SI": "Дж/кг"
            },
            3: {
                "name": "Масса",
                "inputs": [
                    ("Q", "Теплота"),
                    ("L", "Удельная теплота парообразования")
                ],
                "output": "Масса",
                "function": "core.physics.thermodynamics.calculations.calc_mass_heat_amount_vaporization",
                "SI": "кг"
             }
        }
    },
    "heat_amount_combustion": {
        "subject_key": "термодинамика",
        "title": "Теплота при сгорании",
        "description": "Теплота при сгорании - это физическая величина, которая характеризует количество энергии, выделяемой при сгорании вещества. Она измеряется в джоулях (Дж) и обозначается символом Q.",
        "formula_view": "Q = q * m",
        "cases": {
            1: {
                "name": "Теплота",
                "inputs": [
                    ("q", "Удельная теплота сгорания"),
                    ("m", "Масса")
                ],
                "output": "Теплота",
                "function": "core.physics.thermodynamics.calculations.calc_heat_amount_combustion",
                "SI": "Дж"
            },
            2: {
                "name": "Удельная теплота сгорания",
                "inputs": [
                    ("Q", "Теплота"),
                    ("m", "Масса")
                ],
                "output": "Удельная теплота сгорания",
                "function": "core.physics.thermodynamics.calculations.calc_combustion_heat",
                "SI": "Дж/кг"
            },
            3: {
                "name": "Масса",
                "inputs": [
                    ("Q", "Теплота"),
                    ("q", "Удельная теплота сгорания")
                ],
                "output": "Масса",
                "function": "core.physics.thermodynamics.calculations.calc_mass_heat_amount_combustion",
                "SI": "кг"
             }
        }
    },
    "first_thermodynamics_law": {
        "subject_key": "термодинамика",
        "title": "Первый закон термодинамики",
        "description": "Первый закон термодинамики - это физический закон, который утверждает, что энергия не может быть создана или уничтожена, а может только переходить из одной формы в другую. Он выражается формулой ΔU = Q - W.",
        "formula_view": "ΔU = Q - W",
        "cases": {
            1: {
                "name": "Изменение внутренней энергии",
                "inputs": [
                    ("Q", "Теплота"),
                    ("W", "Работа")
                ],
                "output": "Изменение внутренней энергии",
                "function": "core.physics.thermodynamics.calculations.calc_first_thermodynamics_law",
                "SI": "Дж"
             },
            2: {
                "name": "Теплота",
                "inputs": [
                    ("ΔU", "Изменение внутренней энергии"),
                    ("W", "Работа")
                ],
                "output": "Теплота",
                "function": "core.physics.thermodynamics.calculations.calc_heat_amount_first_thermodynamics_law",
                "SI": "Дж"
             },
            3: {
                "name": "Работа",
                "inputs": [
                    ("ΔU", "Изменение внутренней энергии"),
                    ("Q", "Теплота")
                ],
                "output": "Работа",
                "function": "core.physics.thermodynamics.calculations.calc_work_first_thermodynamics_law",
                "SI": "Дж"
             }
        }
    },
    "cop_thermal_engine": {
        "subject_key": "термодинамика",
        "title": "КПД теплового двигателя",
        "description": "КПД теплового двигателя - это физическая величина, которая характеризует эффективность работы теплового двигателя. Она измеряется в процентах (%) и обозначается символом η.",
        "formula_view": "η = (Q1 - Q2) / Q1 * 100%",
        "cases": {
            1: {
                "name": "КПД",
                "inputs": [
                    ("Q1", "Теплота №1"),
                    ("Q2", "Теплота №2")
                ],
                "output": "КПД",
                "function": "core.physics.thermodynamics.calculations.calc_cop_thermal_engine",
                "SI": "%"
            },
            2: {
                "name": "Теплота №1",
                "inputs": [
                    ("η", "КПД"),
                    ("Q2", "Теплота №2")
                ],
                "output": "Теплота №1",
                "function": "core.physics.thermodynamics.calculations.calc_heat_1",
                "SI": "Дж"
            },
            3: {
                "name": "Теплота №2",
                "inputs": [
                    ("η", "КПД"),
                    ("Q1", "Теплота №1")
                ],
                "output": "Теплота №2",
                "function": "core.physics.thermodynamics.calculations.calc_heat_2",
                "SI": "Дж"
             }
         }
    },
    "cop_ideal_engine": {
        "subject_key": "термодинамика",
        "title": "КПД идеального двигателя",
        "description": "КПД идеального двигателя - это физическая величина, которая характеризует эффективность работы идеального теплового двигателя. Она измеряется в процентах (%) и обозначается символом η.",
        "formula_view": "η = (T1 - T2) / T1 * 100%",
        "cases": {
            1: {
                "name": "КПД",
                "inputs": [
                    ("T1", "Температура №1"),
                    ("T2", "Температура №2")
                ],
                "output": "КПД",
                "function": "core.physics.thermodynamics.calculations.calc_cop_ideal_engine",
                "SI": "%"
            },
            2: {
                "name": "Температура №1",
                "inputs": [
                    ("η", "КПД"),
                    ("T2", "Температура №2")
                ],
                "output": "Температура №1",
                "function": "core.physics.thermodynamics.calculations.calc_temperature_1",
                "SI": "К"
            },
            3: {
                "name": "Температура №2",
                "inputs": [
                    ("η", "КПД"),
                    ("T1", "Температура №1")
                ],
                "output": "Температура №2",
                "function": "core.physics.thermodynamics.calculations.calc_temperature_2",
                "SI": "К"
            }
        }  
    }
}

mp_n_thermodynamics = {
    SUBSTANCE_AMOUNT: """Выберите величину, которую нужно найти
                         "Кол-во вещества - 1"
                         "Масса вещества - 2"
                         "Молярная масса - 3" """,
    AVG_KINETIC_ENERGY: """Выберите величину, которую нужно найти
                         "Кинетическая энергия - 1"
                         "Абсолютная температура - 2" """,
    RELATIVE_HUMIDITY: """Выберите величину, которую нужно найти
                         "Относительная влажность - 1"
                         "Парциальное давление водяного пара в воздухе - 2
                         "Давление насыщенного водяного пара при данной температуре - 3""",
    INTERNAL_ENERGY_IDEAL_GAS: """Выберите величину, которую нужно найти
                         "Внутренняя энергия - 1"
                         "Кол-во вещества - 2"
                         "Абсолютная температура - 3" """,
    GAS_WORK: """Выберите величину, которую нужно найти
                         "Работа газа - 1"
                         "Давление - 2"
                         "Изменение объёма - 3" """,
    HEAT_AMOUNT_HEATING: """Выберите величину, которую нужно найти
                         "Теплота - 1"
                         "Удельная теплоемкость - 2"
                         "Масса - 3"
                         "Изменение температуры - 4" """,
    HEAT_AMOUNT_MELTING: """Выберите величину, которую нужно найти
                         "Теплота - 1"
                         "Удельная теплота плавления - 2"
                         "Масса - 3" """,
    HEAT_AMOUNT_VAPORIZATION: """Выберите величину, которую нужно найти
                         "Теплота - 1"
                         "Удельная теплота парообразования - 2"
                         "Масса - 3" """,
    HEAT_AMOUNT_COMBUSTION: """Выберите величину, которую нужно найти
                         "Теплота - 1"
                         "Удельная теплота сгорания - 2"
                         "Масса - 3" """,
    FIRST_THERMODYNAMICS_LAW: """Выберите величину, которую нужно найти
                         "Изменение внутренней энергии - 1"
                         "Кол-во теплоты - 2"
                         "Работа - 3" """,
    COP_THERMAL_ENGINE: """Выберите величину, которую нужно найти
                         "КПД - 1"
                         "Теплота №1 - 2"
                         "Теплота №2 - 3" """,
    COP_IDEAL_ENGINE: """Выберите величину, которую нужно найти
                         "КПД - 1"
                         "Температура №1 - 2"
                         "Температура №2 - 3" """
}