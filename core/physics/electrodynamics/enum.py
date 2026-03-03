import core.physics.electrodynamics.calculations as calc


##################################
#ЭЛЕКТРОСТАТИКА И ЭЛЕКТРОДИНАМИКА#
##################################

COULOMBS_LAW = 1
EL_FIELD_INTENSITY = 2
POINT_CHARGE_EL_FIELD_INTENSITY = 3
SURFACE_CHARGE_DENSITY  = 4
INFINITY_SURFACE_EL_FIELD_INTENSITY = 5
DIELECTRIC_CONSTANT = 6
INTERACTING_CHARGES_POTENTIAL_ENERGY = 7
POTENTIAL = 8
POINT_CHARGE_POTENTIAL = 9
VOLTAGE = 10
EL_FIELD_VOLTAGE = 11
EL_CAPACITY = 12
FLAT_CAPACITOR_EL_CAPACITY = 13
CURRENT = 14
CONDUCTOR_RESISTANCE = 15
SECTION_CIRCUIT_OHMS_LAW = 16
EL_CURRENT_POWER = 17
JOULE_LENZ_LAW = 18
FULL_CIRCUIT_OHMS_LAW = 19
SHORT_CIRCUIT_CURRENT = 20
MAGNETIC_INDUCTION_VECTOR = 21
AMPERES_FORCE = 22
LORENTZ_FORCE = 23
MAGNETIC_FLUX = 24
ELECTROMAGNETIC_INDUCTION_LAW = 25
EMF_MOVING_CONDUCTOR = 26
EMF_SELF_INDUCTION = 27
COIL_MAGNETIC_FIELD_ENERGY = 28
OSCILLATING_CIRCUIT_PERIOD = 29
INDUCTIVE_RESISTANCE = 30
CAPACITIVE_RESISTANCE = 31
ACTUAL_CURRENT_VALUE = 32
ACTUAL_VOLTAGE_VALUE = 33
TOTAL_RESISTANCE = 34

FORMULAS = {
    # Закон Кулона
    "coulombs_law": {
        "subjects_key": "электродинамика",
        "title": "Закон Кулона",
        "formula_view": "F = k * (q1 * q2) / r^2",
        "description": "Закон, описывающий силу взаимодействия между двумя точечными зарядами",
        "cases": {
            1: {
                "name": "Найти силу",
                "inputs": [
                    ("q1", "Введите заряд №1"),
                    ("q2", "Введите заряд №2"),
                    ("r", "Введите расстояние между зарядами")
                ],
                "output": "Сила",
                "function": "core.physic.electrodynamics.calculations.calc_coulombs_law",
                "SI": "Н"
            },
            2: {
                "name": "Найти заряд №1",
                "inputs": [
                    ("F", "Введите силу"),
                    ("q2", "Введите заряд №2"),
                    ("r", "Введите расстояние между зарядами")
                ],
                "output": "Заряд №1",
                "function": "core.physic.electrodynamics.calculations.calc_electric_charge_1_coulombs_law",
                "SI": "Кл"
            },
            3: {
                "name": "Найти заряд №2",
                "inputs": [
                    ("F", "Введите силу"),
                    ("q1", "Введите заряд №1"),
                    ("r", "Введите расстояние между зарядами")
                ],
                "output": "Заряд №2",
                "function": "core.physic.electrodynamics.calculations.calc_electric_charge_2_coulombs_law",
                "SI": "Кл"
            },
            4: {
                "name": "Найти расстояние",
                "inputs": [
                    ("F", "Введите силу"),
                    ("q1", "Введите заряд №1"),
                    ("q2", "Введите заряд №2")
                ],
                "output": "Расстояние",
                "function": "core.physic.electrodynamics.calculations.calc_distance_coulombs_law",
                "SI": "м"
            }
        }
    },
    # Напряженность эл. поля
    "el_field_intensity": {
        "subjects_key": "электродинамика",
        "title": "Напряженность электрического поля",
        "description": "Величина, характеризующая электрическое поле",
        "formula_view": "E = F / q",
        "cases": {
            1: {
                "name": "Найти напряженность",
                "inputs": [
                    ("F", "Введите силу, действующую на заряд"),
                    ("q", "Введите величину заряда")
                ],
                "output": "Напряженность",
                "function": "core.physic.electrodynamics.calculations.calc_el_field_intensity",
                "SI": "Н/Кл"
            },
            2: {
                "name": "Найти силу",
                "inputs": [
                    ("E", "Введите напряженность электрического поля"),
                    ("q", "Введите величину заряда")
                ],
                "output": "Сила",
                "function": "core.physic.electrodynamics.calculations.calc_force_el_field_intensity",
                "SI": "Н"
            },
            3: {
                "name": "Найти величину заряда",
                "inputs": [
                    ("E", "Введите напряженность электрического поля"),
                    ("F", "Введите силу, действующую на заряд")
                ],
                "output": "Величина заряда",
                "function": "core.physic.electrodynamics.calculations.calc_electric_charge_el_field_intensity",
                "SI": "Кл"
            }
        }
    },
    # Напряженность эл.поля точечного заряда
    "point_charge_el_field_intensity": {
        "subjects_key": "электродинамика",
        "title": "Напряженность электрического поля точечного заряда",
        "description": "Напряженность электрического поля, создаваемого точечным зарядом",
        "formula_view": "E = k * q / r^2",
        "cases": {
            1: {
                "name": "Найти напряженность",
                "inputs": [
                    ("q", "Введите величину заряда"),
                    ("r", "Введите расстояние от заряда до точки, в которой нужно найти напряженность")
                ],
                "output": "Напряженность",
                "function": "core.physics.electrodynamics.calculations.calc_point_charge_el_field_intensity",
                "SI": "Н/Кл"
            },
            2: {
                "name": "Найти величину заряда",
                "inputs": [
                    ("E", "Введите напряженность электрического поля"),
                    ("r", "Введите расстояние от заряда до точки, в которой нужно найти напряженность")
                ],
                "output": "Величина заряда",
                "function": "core.physic.electrodynamics.calculations.calc_electric_charge_point_charge_el_field_intensity",
                "SI": "Кл"
            },
            3: {
                "name": "Найти расстояние",
                "inputs": [
                    ("E", "Введите напряженность электрического поля"),
                    ("q", "Введите величину заряда")
                ],
                "output": "Расстояние",
                "function": "core.physics.electrodynamics.calculations.calc_distance_charge_point_charge_el_field_intensity",
                "SI": "м"
            }
        }
    },
    # Поверхностная плотность зарядов
    "surface_charge_density": {
        "subjects_key": "электродинамика",
        "title": "Поверхностная плотность зарядов",
        "description": "Величина, характеризующая распределение зарядов на поверхности",
        "formula_view": "σ = q / S",
        "cases": {
            1: {
                "name": "Найти поверхностную плотность зарядов",
                "inputs": [
                    ("q", "Введите величину заряда"),
                    ("S", "Введите площадь поверхности")
                ],
                "output": "Поверхностная плотность зарядов",
                "function": "core.physic.electrodynamics.calculations.calc_surface_charge_density",
                "SI": "Кл/м^2"
            },
            2: {
                "name": "Найти величину заряда",
                "inputs": [
                    ("σ", "Введите поверхностную плотность зарядов"),
                    ("S", "Введите площадь поверхности")
                ],
                "output": "Величина заряда",
                "function": "core.physic.electrodynamics.calculations.calc_electric_charge_surface_charge_density",
                "SI": "Кл"
            },
            3: {
                "name": "Найти площадь поверхности",
                "inputs": [
                    ("σ", "Введите поверхностную плотность зарядов"),
                    ("q", "Введите величину заряда")
                ],
                "output": "Площадь поверхности",
                "function": "core.physic.electrodynamics.calculations.calc_area_surface_charge_density",
                "SI": "м^2"
            }
        
        }
    },
    # Напряженность эл. поля бесконечной плоскости
    "infinity_surface_el_field_intensity": {
        "subjects_key": "электродинамика",
        "title": "Напряженность электрического поля бесконечной поверхности",
        "description": "Напряженность электрического поля, создаваемого бесконечной поверхностью с зарядом",
        "formula_view": "E = σ / (2 * ε0)",
        "cases": {
            1: {
                "name": "Найти напряженность",
                "inputs": [
                    ("σ", "Введите поверхностную плотность зарядов")
                ],
                "output": "Напряженность",
                "function": "core.physics.electrodynamics.calculations.calc_infinity_surface_el_field_intensity",
                "SI": "Н/Кл"
            },
            2: {
                "name": "Найти поверхностную плотность зарядов",
                "inputs": [
                    ("E", "Введите напряженность электрического поля")
                ],
                "output": "Поверхностная плотность зарядов",
                "function": "core.physics.electrodynamics.calculations.calc_density_infinity_surface_el_field_intensity",
                "SI": "Кл/м^2"
            }
        }
    },
    # Диэлектрическая проницаемость
    "dielectric_constant": {
        "subjects_key": "электродинамика",
        "title": "Диэлектрическая проницаемость",
        "description": "Величина, характеризующая способность материала пропускать электрическое поле",
        "formula_view": "ε = E0 / E",
        "cases": {
            1: {
                "name": "Найти диэлектрическую проницаемость",
                "inputs": [
                    ("E0", "Введите напряженность электрического поля в вакууме"),
                    ("E", "Введите напряженность электрического поля в диэлектрике")
                ],
                "output": "Диэлектрическая проницаемость",
                "function": "core.physic.electrodynamics.calculations.calc_dielectric_constant",
                "SI": ""
            },
            2: {
                "name": "Найти напряженность электрического поля в вакууме",
                "inputs": [
                    ("ε", "Введите диэлектрическую проницаемость"),
                    ("E", "Введите напряженность электрического поля в диэлектрике")
                ],
                "output": "Напряженность электрического поля в вакууме",
                "function": "core.physic.electrodynamics.calculations.calc_intensity_1_dielectric_constant",
                "SI": "Н/Кл"
            },
            3: {
                "name": "Найти напряженность электрического поля в диэлектрике",
                "inputs": [
                    ("ε", "Введите диэлектрическую проницаемость"),
                    ("E0", "Введите напряженность электрического поля в вакууме")
                ],
                "output": "Напряженность электрического поля в диэлектрике",
                "function": "core.physic.electrodynamics.calculations.calc_intensity_2_dielectric_constant",
                "SI": "Н/Кл"
            }
        }
    },
    # Потенциальная энергия взаимодействия зарядов
    "interacting_charges_potential_energy": {
        "subjects_key": "электродинамика",
        "title": "Потенциальная энергия взаимодействия зарядов",
        "description": "Энергия, которая возникает при взаимодействии двух зарядов",
        "formula_view": "U = k * (q1 * q2) / r",
        "cases": {
            1:{
                "name": "Найти потенциальную энергию взаимодействия зарядов",
                "inputs": [
                    ("q1", "Введите электрический заряд №1"),
                    ("q2", "Введите электрический заряд №2"),
                    ("r", "Введите расстояние между зарядами")
                ],
                "output": "Потенциальная энергия взаимодействия зарядов",
                "function": "core.physic.electrodynamics.calculations.calc_potential_energy",
                "SI": "Дж"
            },
            2: {
                "name": "Электрический заряд №1",
                "inputs": [
                    ("U", "Введите потенциальную энергию взаимодействия зарядов"),
                    ("q2", "Введите заряд №2"),
                    ("r", "Введите расстояние между зарядами")
                ],
                "output": "Электрический заряд №1",
                "function": "core.physic.electrodynamics.calculations.calc_electric_charge_1_potential_energy",
                "SI": "Кл"
            },
            3: {
                "name": "Электрический заряд №2",
                "inputs": [
                    ("U", "Введите потенциальную энергию взаимодействия зарядов"),
                    ("q1", "Введите заряд №1"),
                    ("r", "Введите расстояние между зарядами")
                ],
                "output": "Электрический заряд №2",
                "function": "core.physic.electrodynamics.calculations.calc_electric_charge_2_potential_energy",
                "SI": "Кл"
            },
            4: {
                "name": "Расстояние между зарядами",
                "inputs": [
                    ("U", "Введите потенциальную энергию взаимодействия зарядов"),
                    ("q1", "Введите электрический заряд №1"),
                    ("q2", "Введите электрический заряд №2")
                ],
                "output": "Расстояние между зарядами",
                "function": "core.physic.electrodynamics.calculations.calc_distance_potential_energy",
                "SI": "м"
            }
    }    },
    # Потенциал
    "potential": {
        "subjects_key": "электродинамика",
        "title": "Потенциал",
        "description": "Величина, характеризующая электрическое поле в данной точке",
        "formula_view": "V = U / q",
        "cases": {
            1: {
                "name": "Найти потенциал",
                "inputs": [
                    ("U", "Введите потенциальную энергию"),
                    ("q", "Введите величину заряда")
                ],
                "output": "Потенциал",
                "function": "core.physics.electrodynamics.calculations.calc_potential",
                "SI": "В"
            },
            2: {
                "name": "Найти потенциальную энергию",
                "inputs": [
                    ("V", "Введите потенциал"),
                    ("q", "Введите величину заряда")
                ],
                "output": "Потенциальная энергия",
                "function": "core.physics.electrodynamics.calculations.calc_potential_energy_potential",
                "SI": "Дж"
            },
            3: {
                "name": "Найти величину заряда",
                "inputs": [
                    ("U", "Введите потенциальную энергию"),
                    ("V", "Введите потенциал")
                ],
                "output": "Величина заряда",
                "function": "core.physics.electrodynamics.calculations.calc_electric_charge_potential",
                "SI": "Кл"
            }
            }},     
    # Потенциал точечного заряда
    "point_charge_potential": {
        "subjects_key": "электродинамика",
        "title": "Потенциал точечного заряда",
        "description": "Потенциал, создаваемый точечным зарядом",
        "formula_view": "V = k * q / r",
        "cases": {
            1: {
                "name": "Найти потенциал",
                "inputs": [
                    ("q", "Введите величину заряда"),
                    ("r", "Введите расстояние от заряда до точки, в которой нужно найти потенциал")
                ],
                "output": "Потенциал",
                "function": "core.physics.electrodynamics.calculations.calc_point_charge_potential",
                "SI": "В"
            },
            2: {
                "name": "Найти величину заряда",
                "inputs": [
                    ("V", "Введите потенциал"),
                    ("r", "Введите расстояние от заряда до точки, в которой нужно найти потенциал")
                ],
                "output": "Величина заряда",
                "function": "core.physics.electrodynamics.calculations.calc_electric_charge_point_charge_potential",
                "SI": "Кл"
            },
            3: {
                "name": "Найти расстояние",
                "inputs": [
                    ("V", "Введите потенциал"),
                    ("q", "Введите величину заряда")
                 ],
                "output": "Расстояние",
                "function": "core.physics.electrodynamics.calculations.calc_distance_point_charge_potential",
                "SI": "м"
        }
    }},
    # Напряжение
    "voltage": {
        "subjects_key": "электродинамика",
        "title": "Напряжение",
        "description": "Разность потенциалов между двумя точками",
        "formula_view": "V = W / q",
        "cases": {
            1: {
                "name": "Найти напряжение",
                "inputs": [
                    ("W", "Введите работу"),
                    ("q", "Введите величину заряда")
                ],
                "output": "Напряжение",
                "function": "core.physics.electrodynamics.calculations.calc_voltage_work",
                "SI": "В"
            },
            2: {
                "name": "Найти работу",
                "inputs": [
                    ("V", "Введите напряжение"),
                    ("q", "Введите величину заряда")
                ],
                "output": "Работа",
                "function": "core.physics.electrodynamics.calculations.calc_work_voltage",
                "SI": "Дж"
            },
            3: {
                "name": "Найти величину заряда",
                "inputs": [
                    ("V", "Введите напряжение"),
                    ("W", "Введите работу")
                ],
                "output": "Величина заряда",
                "function": "core.physics.electrodynamics.calculations.calc_electric_charge_voltage",
                "SI": "Кл"
            }
        }
    },
    # Электрическое поле и напряжение
    "el_field_voltage": {
        "subjects_key": "электродинамика",
        "title": "Напряжение в электрическом поле",
        "description": "Напряжение, создаваемое электрическим полем на определенном расстоянии",
        "formula_view": "V = E * d",
        "cases": {
            1: {
                "name": "Найти напряжение",
                "inputs": [
                    ("E", "Введите напряженность электрического поля"),
                    ("d", "Введите расстояние")
                ],
                "output": "Напряжение",
                "function": "core.physics.electrodynamics.calculations.calc_el_field_voltage",
                "SI": "В"
            },
            2: {
                "name": "Найти напряженность электрического поля",
                "inputs": [
                    ("V", "Введите напряжение"),
                    ("d", "Введите расстояние")
                ],
                "output": "Напряженность электрического поля",
                "function": "core.physics.electrodynamics.calculations.calc_intensity_el_field_voltage",
                "SI": "Н/Кл"
            },
            3: {
                "name": "Найти расстояние",
                "inputs": [
                    ("V", "Введите напряжение"),
                    ("E", "Введите напряженность электрического поля")
                ],
                "output": "Расстояние",
                "function": "core.physics.electrodynamics.calculations.calc_distance_el_field_voltage",
                "SI": "м"
            }
        }
    },
    # Электроёмкость (общая)
    "el_capacity": {
        "subjects_key": "электродинамика",
        "title": "Электроёмкость",
        "description": "Способность тела накапливать электрический заряд",
        "formula_view": "C = q / V",
        "cases": {
            1: {
                "name": "Найти электроёмкость",
                "inputs": [
                    ("q", "Введите величину заряда"),
                    ("V", "Введите напряжение")
                ],
                "output": "Электроёмкость",
                "function": "core.physics.electrodynamics.calculations.calc_el_capacity",
                "SI": "Ф"
                },
            2: {
                "name": "Найти величину заряда",
                "inputs": [
                    ("C", "Введите электроёмкость"),
                    ("V", "Введите напряжение")
                ],
                "output": "Величина заряда",
                "function": "core.physics.electrodynamics.calculations.calc_charge_el_capacity",
                "SI": "Кл"
            },
            3: {
                "name": "Найти напряжение",
                "inputs": [
                    ("C", "Введите электроёмкость"),
                    ("q", "Введите величину заряда")
                ],
                "output": "Напряжение",
                "function": "core.physics.electrodynamics.calculations.calc_voltage_el_capacity",
                "SI": "В"
            }
        }
    },
    # Ёмкость плоского (пластинчатого) конденсатора
    "flat_capacitor_el_capacity": {
        "subjects_key": "электродинамика",
        "title": "Электроёмкость плоского конденсатора",
        "description": "Электроёмкость плоского конденсатора, состоящего из двух параллельных пластин",
        "formula_view": "C = ε0 * εr * S / d",
        "cases": {
            1:{
                "name": "Найти электроёмкость плоского конденсатора",
                "inputs": [
                    ("εr", "Введите относительную диэлектрическую проницаемость"),
                    ("S", "Введите площадь пластин"),
                    ("d", "Введите расстояние между пластинами")
                ],
                "output": "Электроёмкость плоского конденсатора",
                "function": "core.physics.electrodynamics.calculations.calc_flat_capacitor_capacity",
                "SI": "Ф"
            },
            2: {
                "name": "Найти площадь пластин",
                "inputs": [
                    ("C", "Введите электроёмкость плоского конденсатора"),
                    ("εr", "Введите относительную диэлектрическую проницаемость"),
                    ("d", "Введите расстояние между пластинами")
                ],
                "output": "Площадь пластин",
                "function": "core.physics.electrodynamics.calculations.calc_flat_capacitor_plate_area",
                "SI": "м^2"
            },
            3: {
                "name": "Найти относительную диэлектрическую проницаемость",
                "inputs": [
                    ("C", "Введите электроёмкость плоского конденсатора"),
                    ("d", "Введите расстояние между пластинами"),
                    ("S", "Введите площадь пластин")
                ],
                "output": "Относительная диэлектрическая проницаемость",
                "function": "core.physics.electrodynamics.calculations.calc_relative_perm_flat_capacitor_capacity",
                "SI": ""
            },
            4: {
                "name": "Найти расстояние между пластинами",
                "inputs": [
                    ("C", "Введите электроёмкость плоского конденсатора"),
                    ("εr", "Введите относительную диэлектрическую проницаемость"),
                    ("S", "Введите площадь пластин")
                ],
                "output": "Расстояние между пластинами",
                "function": "core.physics.electrodynamics.calculations.calc_distance_flat_capacitor_capacity",
                "SI": "м"
            }
    }},
    # Ток
    "current": {
        "subjects_key": "электродинамика",
        "title": "Сила тока",
        "description": "Количество электрического заряда, проходящего через поперечное сечение проводника в единицу времени",
        "formula_view": "I = q / t",
        "cases": {
        1: {
            "name": "Найти силу тока",
            "inputs": [
                ("q", "Введите величину заряда"),
                ("t", "Введите время")
            ],
            "output": "Сила тока",
            "function": "core.physics.electrodynamics.calculations.calc_current",
            "SI": "А"
        },
        2: {
            "name": "Найти величину заряда",
            "inputs": [
                ("I", "Введите силу тока"),
                ("t", "Введите время")
            ],
            "output": "Величина заряда",
            "function": "core.physics.electrodynamics.calculations.calc_charge_current",
            "SI": "Кл"
        },
        3: {
            "name": "Найти время",
            "inputs": [
                ("I", "Введите силу тока"),
                ("q", "Введите величину заряда")
            ],
            "output": "Время",
            "function": "core.physics.electrodynamics.calculations.calc_time_current",
            "SI": "с"
        }
    }
        },
    # Сопротивление проводника
    "conductor_resistance": {
        "subjects_key": "электродинамика",
        "title": "Сопротивление проводника",
        "description": "Величина, характеризующая сопротивление проводника прохождению электрического тока",
        "formula_view": "R = ρ * (l / A)",
        "cases": {
            1: {
                "name": "Найти сопротивление проводника",
                "inputs": [
                    ("ρ", "Введите удельное сопротивление материала"),
                    ("l", "Введите длину проводника"),
                    ("A", "Введите площадь поперечного сечения проводника")
                ],
                "output": "Сопротивление проводника",
                "function": "core.physics.electrodynamics.calculations.calc_conductor_resistance",
                "SI": "Ом"
            },
            2: {
                "name": "Найти удельное сопротивление материала",
                "inputs": [
                    ("R", "Введите сопротивление проводника"),
                    ("l", "Введите длину проводника"),
                    ("A", "Введите площадь поперечного сечения проводника")
                ],
                "output": "Удельное сопротивление материала",
                "function": "core.physics.electrodynamics.calculations.calc_resistivity_conductor",
                "SI": "Ом*м"
            },
            3: {
                "name": "Найти длину проводника",
                "inputs": [
                    ("R", "Введите сопротивление проводника"),
                    ("ρ", "Введите удельное сопротивление материала"),
                    ("A", "Введите площадь поперечного сечения проводника")
                ],
                "output": "Длина проводника",
                "function": "core.physics.electrodynamics.calculations.calc_length_conductor",
                "SI": "м"
            },
            4: {
                "name": "Найти площадь поперечного сечения проводника",
                "inputs": [
                    ("R", "Введите сопротивление проводника"),
                    ("ρ", "Введите удельное сопротивление материала"),
                    ("l", "Введите длину проводника")
                ],
                "output": "Площадь поперечного сечения проводника",
                "function": "core.physics.electrodynamics.calculations.calc_area_conductor",
                "SI": "м^2"
            }}
    },
    # Закон Ома для участка цепи
    "section_circuit_ohms_law": {
        "subjects_key": "электродинамика",
        "title": "Закон Ома для участка цепи",
        "description": "Зависимость силы тока от напряжения и сопротивления в участке электрической цепи",
        "formula_view": "I = V / R",
        "cases": {
            1: {
                "name": "Найти силу тока",
                "inputs": [
                    ("V", "Введите напряжение"),
                    ("R", "Введите сопротивление")
                ],
                "output": "Сила тока",
                "function": "core.physics.electrodynamics.calculations.calc_section_current",
                "SI": "А"
            },
            2: {
                "name": "Найти напряжение",
                "inputs": [
                    ("I", "Введите силу тока"),
                    ("R", "Введите сопротивление")
                ],
                "output": "Напряжение",
                "function": "core.physics.electrodynamics.calculations.calc_section_voltage",
                "SI": "В"
            },
            3: {
                "name": "Найти сопротивление",
                "inputs": [
                    ("V", "Введите напряжение"),
                    ("I", "Введите силу тока")
                ],
                "output": "Сопротивление",
                "function": "core.physics.electrodynamics.calculations.calc_section_resistance",
                "SI": "Ом"
            }
    }},
    # Мощность электрического тока (P = I * U)
    "el_current_power": {
        "subjects_key": "электродинамика",
        "title": "Мощность электрического тока",
        "description": "Количество энергии, передаваемой электрическим током в единицу времени",
        "formula_view": "P = I * V",
        "cases": {
            1: {
                "name": "Найти мощность",
                "inputs": [
                    ("I", "Введите силу тока"),
                    ("V", "Введите напряжение")
                ],
                "output": "Мощность",
                "function": "core.physics.electrodynamics.calculations.calc_el_current_power",
                "SI": "Вт"
            },
            2: {
                "name": "Найти силу тока",
                "inputs": [
                    ("P", "Введите мощность"),
                    ("V", "Введите напряжение")
                ],
                "output": "Сила тока",
                "function": "core.physics.electrodynamics.calculations.calc_current_el_current_power",
                "SI": "А"
            },
            3: {
                "name": "Найти напряжение",
                "inputs": [
                    ("P", "Введите мощность"),
                    ("I", "Введите силу тока")
                ],
                "output": "Напряжение",
                "function": "core.physics.electrodynamics.calculations.calc_voltage_el_current_power",
                "SI": "В"
            }
    }},
    # Закон Джоуля-Ленца (Q = I^2 * R * t)
    "joule_lenz_law": {
        "subjects_key": "электродинамика",
        "title": "Закон Джоуля-Ленца",
        "description": "Количество теплоты, выделяемое проводником при прохождении электрического тока",
        "formula_view": "Q = I^2 * R * t",
        "cases": {
            1: {
                "name": "Найти количество теплоты",
                "inputs": [
                    ("I", "Введите силу тока"),
                    ("R", "Введите сопротивление"),
                    ("t", "Введите время")
                ],
                "output": "Количество теплоты",
                "function": "core.physics.electrodynamics.calculations.calc_joule_lenz_heat",
                "SI": "Дж"
            },
            2: {
                "name": "Найти силу тока",
                "inputs": [
                    ("Q", "Введите количество теплоты"),
                    ("R", "Введите сопротивление"),
                    ("t", "Введите время")
                ],
                "output": "Сила тока",
                "function": "core.physics.electrodynamics.calculations.calc_current_joule_lenz",
                "SI": "А"
            },
            3: {
                "name": "Найти сопротивление",
                "inputs": [
                    ("Q", "Введите количество теплоты"),
                    ("I", "Введите силу тока"),
                    ("t", "Введите время")
                ],
                "output": "Сопротивление",
                "function": "core.physics.electrodynamics.calculations.calc_resistance_joule_lenz",
                "SI": "Ом"
            },
            4: {
                "name": "Найти время",
                "inputs": [
                    ("Q", "Введите количество теплоты"),
                    ("I", "Введите силу тока"),
                    ("R", "Введите сопротивление")
                ],
                "output": "Время",
                "function": "core.physics.electrodynamics.calculations.calc_time_joule_lenz",
                "SI": "с"
    }}},
    # Закон Ома для полной цепи (I = E / (R + r))
    "full_circuit_ohms_law": {
        "subjects_key": "электродинамика",
        "title": "Закон Ома для полной цепи",
        "description": "Зависимость силы тока от электродвижущей силы источника и сопротивлений в полной электрической цепи",
        "formula_view": "I = ε / (R + r)",
        "cases": {
            1: {
                "name": "Найти силу тока",
                "inputs": [
                    ("ε", "Введите электродвижущую силу"),
                    ("R", "Введите сопротивление внешней цепи"),
                    ("r", "Введите внутреннее сопротивление источника")
                ],
                "output": "Сила тока",
                "function": "core.physics.electrodynamics.calculations.calc_full_circuit_current",
                "SI": "А"
            },
            2: {
                "name": "Найти электродвижущую силу",
                "inputs": [
                    ("I", "Введите силу тока"),
                    ("R", "Введите сопротивление внешней цепи"),
                    ("r", "Введите внутреннее сопротивление источника")
                ],
                "output": "Электродвижущая сила",
                "function": "core.physics.electrodynamics.calculations.calc_emf_full_circuit",
                "SI": "В"
            },
            3: {
                "name": "Найти сопротивление внешней цепи",
                "inputs": [
                    ("I", "Введите силу тока"),
                    ("ε", "Введите электродвижущую силу"),
                    ("r", "Введите внутреннее сопротивление источника")
                ],
                "output": "Сопротивление внешней цепи",
                "function": "core.physics.electrodynamics.calculations.calc_external_resistance_full_circuit",
                "SI": "Ом"
            },
            4: {
                "name": "Найти внутреннее сопротивление источника",
                "inputs": [
                    ("I", "Введите силу тока"),
                    ("ε", "Введите электродвижущую силу"),
                    ("R", "Введите сопротивление внешней цепи")
                ],
                "output": "Внутреннее сопротивление источника",
                "function": "core.physics.electrodynamics.calculations.calc_internal_resistance_full_circuit",
                "SI": "Ом"
    }
        }},
    # Короткозамкнутый ток (R внешнее = 0): I_sc = E / r
    "short_circuit_current": {
        "subjects_key": "электродинамика",
        "title": "Сила тока короткого замыкания",
        "description": "Сила тока, возникающая при коротком замыкании источника питания",
        "formula_view": "I = ε / r",
        "cases": {
            1: {
                "name": "Найти силу тока короткого замыкания (Кроткозамкнутый ток)",
                "inputs": [
                    ("ε", "Введите электродвижущую силу"),
                    ("r", "Введите внутреннее сопротивление (ЭДС) источника")
                ],
                "output": "Сила тока короткого замыкания (Короткозамкнутый ток)",
                "function": "core.physics.electrodynamics.calculations.calc_short_circuit_current",
                "SI": "А"
            },
            2: {
                "name": "Найти электродвижущую силу (ЭДС) источника",
                "inputs": [
                    ("I", "Введите силу тока короткого замыкания (Кроткозамкнутый ток)"),
                    ("r", "Введите внутреннее сопротивление источника")
                ],
                "output": "Электродвижущая сила",
                "function": "core.physics.electrodynamics.calculations.calc_emf_short_circuit",
                "SI": "В"
            },
            3: {
                "name": "Найти внутреннее сопротивление источника",
                "inputs": [
                    ("I", "Введите силу тока короткого замыкания (Кроткозамкнутый ток)"),
                    ("ε", "Введите электродвижущую силу (ЭДС) источника")
                ],
                "output": "Внутреннее сопротивление источника",
                "function": "core.physics.electrodynamics.calculations.calc_internal_resistance_short_circuit",
                "SI": "Ом"
    }
        }},
    # Вектор магнитной индукции (B): B = F_max / (I * l)
    "magnetic_induction_vector": {
        "subjects_key": "электродинамика",
        "title": "Вектор магнитной индукции",
        "description": "Величина, характеризующая магнитное поле в данной точке",
        "formula_view": "B = F / (I * l * sin(α))",
        "cases": {
            1: {
                "name": "Найти вектор магнитной индукции",
                "inputs": [
                    ("F", "Введите силу, действующую на проводник"),
                    ("I", "Введите силу тока в проводнике"),
                    ("l", "Введите длину проводника"),
                ],
                "output": "Вектор магнитной индукции",
                "function": "core.physics.electrodynamics.calculations.calc_magnetic_induction_vector",
                "SI": "Тл"
            },
            2: {
                "name": "Найти максимальную силу Ампера",
                "inputs": [
                    ("I", "Введите силу тока в проводнике"),
                    ("l", "Введите длину проводника"),
                    ("B", "Введите вектор магнитной индукции"),
                ],
                "output": "Максимальная сила Ампера",
                "function": "core.physics.electrodynamics.calc_force_max_magnetic_induction",
                "SI": "Н"
            },
            3: {
                "name": "Найти длину проводника",
                "inputs": [
                    ("F", "Введите силу, действующую на проводник"),
                    ("I", "Введите силу тока в проводнике"),
                    ("B", "Введите вектор магнитной индукции"),
                ],
                "output": "Длина проводника",
                "function": "core.physics.electrodynamics.calculations.calc_length_magnetic_induction",
                "SI": "м"
            },
            4: {
                "name": "Найти силу тока в проводнике",
                "inputs": [
                    ("F", "Введите силу, действующую на проводник"),
                    ("l", "Введите длину проводника"),
                    ("B", "Введите вектор магнитной индукции"),
                ],
                "output": "Сила тока в проводнике",
                "function": "core.physics.electrodynamics.calculations.calc_current_magnetic_induction",
                "SI": "А"
            }
        }},
    # Сила Ампера: F = I * L * B * sin(угла)
    "amperes_force": {
        "subjects_key": "электродинамика",
        "title": "Сила Ампера",
        "description": "Сила, действующая на проводник с током в магнитном поле",
        "formula_view": "F = I * l * B * sin(α)",
        "cases": {
            1: {
                "name": "Найти силу Ампера",
                "inputs": [
                    ("I", "Введите силу тока в проводнике"),
                    ("l", "Введите длину проводника"),
                    ("B", "Введите вектор магнитной индукции"),
                    ("α", "Введите угол между проводником и вектором магнитной индукции")
                ],
                "output": "Сила Ампера",
                "function": "core.physics.electrodynamics.calculations.calc_amperes_force",
                "SI": "Н"
            },
            2: {
                "name": "Найти силу тока в проводнике",
                "inputs": [
                    ("F", "Введите силу Ампера"),
                    ("l", "Введите длину проводника"),
                    ("B", "Введите вектор магнитной индукции"),
                    ("α", "Введите угол между проводником и вектором магнитной индукции")
                ],
                "output": "Сила тока в проводнике",
                "function": "core.physics.electrodynamics.calculations.calc_current_amperes_force",
                "SI": "А"
            },
            3: {
                "name": "Вектор магнитной индукции",
                "inputs": [
                    ("F", "Введите силу Ампера"),
                    ("I", "Введите силу тока в проводнике"),
                    ("l", "Введите длину проводника"),
                    ("α", "Введите угол между проводником и вектором магнитной индукции")
                ],
                "output": "Вектор магнитной индукции",
                "function": "core.physics.electrodynamics.calculations.calc_magnetic_induction_amperes_force",
                "SI": "Тл"
            },
            4: {
                "name": "Найти длину проводника",
                "inputs": [
                    ("F", "Введите силу Ампера"),
                    ("I", "Введите силу тока в проводнике"),
                    ("B", "Введите вектор магнитной индукции"),
                    ("α", "Введите угол между проводником и вектором магнитной индукции")
                ],
                "output": "Длина проводника",
                "function": "core.physics.electrodynamics.calculations.calc_length_amperes_force",
                "SI": "м"
            }
            
        }
    },
    # Сила Лоренца (магнитная составляющая): F = q * v * B * sin(угла)
    "lorentz_force": {
        "subjects_key": "электродинамика",
        "title": "Сила Лоренца",
        "description": "Сила, действующая на заряженную частицу в электромагнитном поле",
        "formula_view": "F = q * (E + v × B)",
        "cases": {
            1: {
                "name": "Найти силу Лоренца",
                "inputs": [
                    ("q", "Введите величину заряда"),
                    ("v", "Введите скорость частицы"),
                    ("B", "Введите вектор магнитной индукции"),
                    ("α", "Введите угол между скоростью частицы и вектором магнитной индукции")
                ],
                "output": "Сила Лоренца",
                "function": "core.physics.electrodynamics.calculations.calc_lorentz_force",
                "SI": "Н"
            },
            2: {
                "name": "Найти электрический заряд частицы",
                "inputs": [
                    ("F", "Введите силу Лоренца"),
                    ("v", "Введите скорость частицы"),
                    ("B", "Введите вектор магнитной индукции"),
                    ("α", "Введите угол между скоростью частицы и вектором магнитной индукции")
                ],
                "output": "Величина заряда",
                "function": "core.physics.electrodynamics.calculations.calc_charge_lorentz_force",
                "SI": "Кл"
            },
            3: {
                "name": "Найти скорость частицы",
                "inputs": [
                    ("F", "Введите силу Лоренца"),
                    ("q", "Введите величину заряда"),
                    ("B", "Введите вектор магнитной индукции"),
                    ("α", "Введите угол между скоростью частицы и вектором магнитной индукции")
                ],
                "output": "Скорость частицы",
                "function": "core.physics.electrodynamics.calculations.calc_velocity_lorentz_force",
                "SI": "м/с"
            },
            4: {
                "name": "Найти вектор магнитной индукции",
                "inputs": [
                    ("F", "Введите силу Лоренца"),
                    ("q", "Введите величину заряда"),
                    ("v", "Введите скорость частицы"),
                    ("α", "Введите угол между скоростью частицы и вектором магнитной индукции")
                ],
                "output": "Вектор магнитной индукции",
                "function": "core.physics.electrodynamics.calculations.calc_magnetic_induction_lorentz_force",
                "SI": "Тл"
            }
            }},
    # Магнитный поток: Phi = B * S * sin(угла)
    "magnetic_flux": {
        "subjects_key": "электродинамика",
        "title": "Магнитный поток",
        "description": "Величина, характеризующая количество магнитного поля, проходящего через поверхность",
        "formula_view": "Φ = B * S * sin(α)",
        "cases": {
            1: {
                "name": "Найти магнитный поток",
                "inputs": [
                    ("B", "Введите вектор магнитной индукции"),
                    ("S", "Введите площадь поверхности"),
                    ("α", "Введите угол между вектором магнитной индукции и нормалью к поверхности")
                ],
                "output": "Магнитный поток",
                "function": "core.physics.electrodynamics.calculations.calc_magnetic_flux",
                "SI": "Вб"
            },
            2: {
                "name": "Найти вектор магнитной индукции",
                "inputs": [
                    ("Φ", "Введите магнитный поток"),
                    ("S", "Введите площадь поверхности"),
                    ("α", "Введите угол между вектором магнитной индукции и нормалью к поверхности")
                ],
                "output": "Вектор магнитной индукции",
                "function": "core.physics.electrodynamics.calculations.calc_magnetic_induction_flux",
                "SI": "Тл"
            },
            3: {
                "name": "Найти площадь поверхности",
                "inputs": [
                    ("Φ", "Введите магнитный поток"),
                    ("B", "Введите вектор магнитной индукции"),
                    ("α", "Введите угол между вектором магнитной индукции и нормалью к поверхности")
                ],
                "output": "Площадь поверхности",
                "function": "core.physics.electrodynamics.calculations.calc_area_magnetic_flux",
                "SI": "м^2"
            },
            4: {
                "name": "Найти угол между вектором магнитной индукции и нормалью к поверхности",
                "inputs": [
                    ("Φ", "Введите магнитный поток"),
                    ("B", "Введите вектор магнитной индукции"),
                    ("S", "Введите площадь поверхности")
                ],
                "output": "Угол между вектором магнитной индукции и нормалью к поверхности",
                "function": "core.physics.electrodynamics.calculations.calc_sin_alpha_magnetic_flux",
                "SI": "рад"
            }
        }
    },
    # Электромагнитная индукция (закон Фарадея): emf = - (delta_phi / delta_t)
    "electromagnetic_induction_law": {
        "subjects_key": "электродинамика",
        "title": "Закон электромагнитной индукции",
        "description": "Зависимость электродвижущей силы индукции от изменения магнитного потока",
        "formula_view": "ε = -ΔΦ / Δt",
        "cases": {
            1: {
                "name": "Найти электродвижущую силу (ЭДС) индукции",
                "inputs": [
                    ("ΔΦ", "Введите изменение магнитного потока"),
                    ("Δt", "Введите время, за которое произошло изменение потока")
                ],
                "output": "Электродвижущая сила (ЭДС) индукции",
                "function": "core.physics.electrodynamics.calculations.calc_emf_induction_law",
                "SI": "В"
            },
            2: {
                "name": "Найти изменение магнитного потока",
                "inputs": [
                    ("ε", "Введите электродвижущую силу (ЭДС) индукции"),
                    ("Δt", "Введите время, за которое произошло изменение потока")
                ],
                "output": "Изменение магнитного потока",
                "function": "core.physics.electrodynamics.calculations.calc_delta_phi_induction_law",
                    "SI": "Вб"
            },
            3: {
                "name": "Найти время изменения магнитного потока",
                "inputs": [
                    ("ε", "Введите электродвижущую силу (ЭДС) индукции"),
                    ("ΔΦ", "Введите изменение магнитного потока")
                ],
                "output": "Время изменения магнитного потока",
                "function": "core.physics.electrodynamics.calculations.calc_delta_t_induction_law",
                "SI": "с"
            }
    }},
    # ЭДС в движущемся проводнике: emf = B * l * v * sin(угла)
    "emf_moving_conductor": {
        "title": "ЭДС индукции в движущемся проводнике",
        "description": "ЭДС, возникающая в проводнике, движущемся в магнитном поле",
        "formula_view": "ε = B * l * v * sin(α)",
            "cases": {
                1: {
                    "name": "Найти ЭДС индукции в движущемся проводнике",
                    "inputs": [
                        ("B", "Введите вектор магнитной индукции"),
                        ("l", "Введите длину проводника"),
                        ("v", "Введите скорость движения проводника"),
                        ("α", "Введите угол между направлением движения проводника и вектором магнитной индукции")
                    ],
                    "output": "ЭДС индукции в движущемся проводнике",
                    "function": "core.physics.electrodynamics.calculations.calc_emf_moving_conductor",
                    "SI": "В"
                },
                2: {
                    "name": "Найти вектор магнитной индукции",
                    "inputs": [
                        ("ε", "Введите ЭДС индукции в движущемся проводнике"),
                        ("l", "Введите длину проводника"),
                        ("v", "Введите скорость движения проводника"),
                        ("α", "Введите угол между направлением движения проводника и вектором магнитной индукции")
                    ],
                    "output": "Вектор магнитной индукции",
                    "function": "core.physics.electrodynamics.calculations.calc_magnetic_induction_moving_conductor",
                    "SI": "Тл"
                },
                3: {
                    "name": "Найти длину проводника",
                    "inputs": [
                        ("ε", "Введите ЭДС индукции в движущемся проводнике"),
                        ("B", "Введите вектор магнитной индукции"),
                        ("v", "Введите скорость движения проводника"),
                        ("α", "Введите угол между направлением движения проводника и вектором магнитной индукции")
                    ],
                    "output": "Длина проводника",
                    "function": "core.physics.electrodynamics.calculations.calc_length_moving_conductor",
                    "SI": "м"
                },
                4: {
                    "name": "Найти скорость движения проводника",
                    "inputs": [
                        ("ε", "Введите ЭДС индукции в движущемся проводнике"),
                        ("B", "Введите вектор магнитной индукции"),
                        ("l", "Введите длину проводника"),
                        ("α", "Введите угол между направлением движения проводника и вектором магнитной индукции")
                    ],
                    "output": "Скорость движения проводника",
                    "function": "core.physics.electrodynamics.calculations.calc_velocity_moving_conductor",
                    "SI": "м/с"
                }
                }},
    # Самоиндукция: emf = - L * (delta_I / delta_t)
    "emf_self_induction": {
        "subjects_key": "электродинамика",
        "title": "ЭДС самоиндукции",
        "description": "ЭДС, возникающая в катушке при изменении силы тока в ней",
        "formula_view": "ε = -L * (ΔI / Δt)",
        "cases": {
            1: {
                "name": "Найти ЭДС самоиндукции",
                "inputs": [
                    ("L", "Введите индуктивность катушки"),
                    ("ΔI", "Введите изменение силы тока"),
                    ("Δt", "Введите время, за которое произошло изменение силы тока")
                ],
                "output": "ЭДС самоиндукции",
                "function": "core.physics.electrodynamics.calculations.calc_emf_self_induction",
                "SI": "В"
            },
            2: {
                "name": "Найти индуктивность катушки (Коэффициент самоиндукции)",
                "inputs": [
                    ("ε", "Введите ЭДС самоиндукции"),
                    ("ΔI", "Введите изменение силы тока"),
                    ("Δt", "Введите время, за которое произошло изменение силы тока")
                ],
                "output": "Индуктивность катушки (Коэффициент самоиндукции)",
                "function": "core.physics.electrodynamics.calculations.calc_inductance_self_induction",
                "SI": "Гн"
            },
            3: {
                "name": "Найти изменение силы тока",
                "inputs": [
                    ("ε", "Введите ЭДС самоиндукции"),
                    ("L", "Введите индуктивность катушки (Коэффициент самоиндукции)"),
                    ("Δt", "Введите время, за которое произошло изменение силы тока")
                ],
                "output": "Изменение силы тока",
                "function": "core.physics.electrodynamics.calculations.calc_delta_current_self_induction",
                "SI": "А"
            },
            4: {
                "name": "Найти время изменения силы тока",
                "inputs": [
                    ("ε", "Введите ЭДС самоиндукции"),
                    ("L", "Введите индуктивность катушки (Коэффициент самоиндукции)"),
                    ("ΔI", "Введите изменение силы тока")
                ],
                "output": "Время изменения силы тока",
                "function": "core.physics.electrodynamics.calculations.calc_time_self_induction",
                "SI": "с"
    }
            }},
    # Энергия магнитного поля катушки: W = 0.5 * L * I^2
    "coil_magnetic_field_energy": {
        "subjects_key": "электродинамика",
        "title": "Энергия магнитного поля катушки",
        "description": "Энергия, запасаемая в магнитном поле катушки с током",
        "formula_view": "W = (1/2) * L * I^2",
        "cases": {
            1: {
                "name": "Найти энергию магнитного поля катушки",
                "inputs": [
                    ("L", "Введите индуктивность катушки"),
                    ("I", "Введите силу тока в катушке")
                ],
                "output": "Энергия магнитного поля катушки",
                "function": "core.physics.electrodynamics.calculations.calc_coil_magnetic_field_energy",
                "SI": "Дж"
            },
            2: {
                "name": "Найти индуктивность катушки",
                "inputs": [
                    ("W", "Введите энергию магнитного поля катушки"),
                    ("I", "Введите силу тока в катушке")
                ],
                "output": "Индуктивность катушки",
                "function": "core.physics.electrodynamics.calculations.calc_inductance_coil_energy",
                    "SI": "Гн"
            },
            3: {
                "name": "Найти силу тока в катушке",
                "inputs": [
                    ("W", "Введите энергию магнитного поля катушки"),
                    ("L", "Введите индуктивность катушки")
                ],
                "output": "Сила тока в катушке",
                "function": "core.physics.electrodynamics.calculations.calc_current_coil_energy",
                "SI": "А"
            }
    }},
    # Период колебательного контура: T = 2 * pi * sqrt(L * C)
    "oscillating_circuit_period": {
        "subjects_key": "электродинамика",
        "title": "Период колебаний в колебательном контуре",
        "description": "Период колебаний в колебательном контуре, состоящем из катушки и конденсатора",
        "formula_view": "T = 2 * π * √(L * C)",
        "cases": {
            1: {
                "name": "Найти период колебаний в колебательном контуре",
                "inputs": [
                    ("L", "Введите индуктивность катушки"),
                    ("C", "Введите ёмкость конденсатора")
                ],
                "output": "Период колебаний в колебательном контуре",
                "function": "core.physics.electrodynamics.calculations.calc_oscillating_circuit_period",
                "SI": "с"
            },
            2: {
                "name": "Найти индуктивность катушки",
                "inputs": [
                    ("T", "Введите период колебаний в колебательном контуре"),
                    ("C", "Введите ёмкость конденсатора")
                ],
                "output": "Индуктивность катушки",
                "function": "core.physics.electrodynamics.calculations.calc_inductance_oscillating_circuit",
                "SI": "Гн"
            },
            3: {
                "name": "Найти ёмкость конденсатора",
                "inputs": [
                    ("T", "Введите период колебаний в колебательном контуре"),
                    ("L", "Введите индуктивность катушки")
                ],
                "output": "Ёмкость конденсатора",
                "function": "core.physics.electrodynamics.calculations.calc_capacitance_oscillating_circuit",
                "SI": "Ф"
            }
    }},
    # Индуктивное сопротивление: X_L = 2 * pi * f * L
    "inductive_resistance": {
        "subjects_key": "электродинамика",
        "title": "Индуктивное сопротивление",
        "description": "Сопротивление, создаваемое катушкой при прохождении переменного тока",
        "formula_view": "X_L = 2 * π * f * L",
        "cases": {
            1: {
                "name": "Найти индуктивное сопротивление",
                "inputs": [
                    ("f", "Введите частоту переменного тока"),
                    ("L", "Введите индуктивность катушки")
                ],
                "output": "Индуктивное сопротивление",
                "function": "core.physics.electrodynamics.calculations.calc_inductive_resistance",
                "SI": "Ом"
            },
            2: {
                "name": "Найти частоту переменного тока",
                "inputs": [
                    ("X_L", "Введите индуктивное сопротивление"),
                    ("L", "Введите индуктивность катушки")
                ],
                "output": "Частота переменного тока",
                "function": "core.physics.electrodynamics.calculations.calc_frequency_inductive_resistance",
                "SI": "Гц"
            },
            3: {
                "name": "Найти индуктивность катушки",
                "inputs": [
                    ("X_L", "Введите индуктивное сопротивление"),
                    ("f", "Введите частоту переменного тока")
                ],
                "output": "Индуктивность катушки",
                "function": "core.physics.electrodynamics.calculations.calc_inductance_from_resistance",
                "SI": "Гн"
    }
        }},
    # Емкостное сопротивление: X_C = 1 / (2 * pi * f * C)
    "capacitive_resistance": {
        "subjects_key": "электродинамика",
        "title": "Емкостное сопротивление",
        "description": "Сопротивление, создаваемое конденсатором при прохождении переменного тока",
        "formula_view": "X_C = 1 / (2 * π * f * C)",
        "cases": {
            1: {
                "name": "Найти емкостное сопротивление",
                "inputs": [
                    ("f", "Введите частоту переменного тока"),
                    ("C", "Введите электрическую ёмкость конденсатора")
                ],
                "output": "Емкостное сопротивление",
                "function": "core.physics.electrodynamics.calculations.calc_capacitive_resistance",
                "SI": "Ом"
            },
            2: {
                "name": "Найти электрическую ёмкость конденсатора",
                "inputs": [
                    ("X_C", "Введите емкостное сопротивление"),
                    ("f", "Введите частоту переменного тока")
                ],
                "output": "Электрическая ёмкость конденсатора",
                "function": "core.physics.electrodynamics.calculations.calc_capacitance_from_capacitive_resistance",
                "SI": "Ф"
            },
            3: {
                "name": "Найти угловую частоту переменного тока",
                "inputs": [
                    ("X_C", "Введите емкостное сопротивление"),
                    ("C", "Введите электрическую ёмкость конденсатора")
                ],
                "output": "Угловая частота переменного тока",
                "function": "core.physics.electrodynamics.calculations.calc_angular_frequency_from_capacitive_resistance"  ,
                "SI": "рад/с"  
            }   
        }},
    # Эффективные (действующие) значения тока: I_rms = I_max / sqrt(2)
    "actual_current_value": {
        "subjects_key": "электродинамика",
        "title": "Действующее значение силы тока",
        "description": "Действующее значение силы тока в переменном токе",
        "formula_view": "I = I_max / √2",
        "cases": {
            1: {
                "name": "Найти действующее значение силы тока",
                "inputs": [
                    ("I_max", "Введите максимальное значение силы тока")
                ],
                "output": "Действующее значение силы тока",
                "function": "core.physics.electrodynamics.calculations.calc_actual_current_value",
                "SI": "А"
            },
            2: {
                "name": "Найти максимальное значение силы тока",
                "inputs": [
                    ("I", "Введите действующее значение силы тока")
                ],
                "output": "Максимальное значение силы тока",
                "function": "core.physics.electrodynamics.calculations.calc_max_current_from_actual",
                "SI": "А"
    }
            }},
    # Эффективные (действующие) значения напряжения: V_rms = V_max / sqrt(2)
    "actual_voltage_value": {
        "subjects_key": "электродинамика",
        "title": "Действующее значение напряжения",
        "description": "Действующее значение напряжения в переменном токе",
        "formula_view": "V = V_max / √2",
        "cases": {
            1: {
                "name": "Найти действующее значение напряжения",
                "inputs": [
                    ("V_max", "Введите максимальное значение напряжения")
                ],
                "output": "Действующее значение напряжения",
                "function": "core.physics.electrodynamics.calculations.calc_actual_voltage_value",
                "SI": "В"
            },
            2: {
                "name": "Найти максимальное значение напряжения",
                "inputs": [
                    ("V", "Введите действующее значение напряжения")
                ],
                "output": "Максимальное значение напряжения",
                "function": "core.physics.electrodynamics.calculations.calc_max_voltage_from_actual",
                "SI": "В"
    }
            }},
    # Полное сопротивление (последовательные R, Xl, Xc): Z = sqrt(R^2 + (Xl - Xc)^2)
    "total_resistance": {
        "subjects_key": "электродинамика",
        "title": "Полное сопротивление",
        "description": "Полное сопротивление в цепи переменного тока, учитывающее активное, индуктивное и емкостное сопротивления",
        "formula_view": "Z = √(R^2 + (X_L - X_C)^2)",
        "cases": {
            1: {
                "name": "Найти полное сопротивление",
                "inputs": [
                    ("R", "Введите активное сопротивление"),
                    ("X_L", "Введите индуктивное сопротивление"),
                    ("X_C", "Введите емкостное сопротивление")
                ],
                "output": "Полное сопротивление",
                "function": "core.physics.electrodynamics.calculations.calc_total_resistance",
                "SI": "Ом"
            },
            2: {
                "name": "Найти активное сопротивление",
                "inputs": [
                    ("Z", "Введите полное сопротивление"),
                    ("X_L", "Введите индуктивное сопротивление"),
                    ("X_C", "Введите емкостное сопротивление")
                ],
                "output": "Активное сопротивление",
                "function": "core.physics.electrodynamics.calculations.calc_capacitive_resistance_from_total",
                "SI": "Ом"
            },
            3: {
                "name": "Найти индуктивное сопротивление",
                "inputs": [
                    ("Z", "Введите полное сопротивление"),
                    ("R", "Введите активное сопротивление"),
                    ("X_C", "Введите емкостное сопротивление")
                ],
                "output": "Индуктивное сопротивление",
                "function": "core.physics.electrodynamics.calculations.calc_inductive_resistance_from_total",
                "SI": "Ом"
            },
            4: {
                "name": "Найти емкостное сопротивление",
                "inputs": [
                    ("Z", "Введите полное сопротивление"),
                    ("R", "Введите активное сопротивление"),
                    ("X_L", "Введите индуктивное сопротивление")
                ],
                "output": "Емкостное сопротивление",
                "function": "core.physics.electrodynamics.calculations.calc_capacitive_resistance_from_total",
                "SI": "Ом"
    }
        }}   
}

electrostatic_n_electrodynamics = {
COULOMBS_LAW: """Введите величину, которую нужно найти:
             "Сила - 1" 
             "Электрический заряд №1 - 2"
             "Электрический заряд №2 - 3"
             "Расстояние - 4" """,
EL_FIELD_INTENSITY: """Введите величину, которую нужно найти:
             "Напряженность - 1"
             "Сила - 2"
             "Величина заряда - 3" """,
POINT_CHARGE_EL_FIELD_INTENSITY: """Введите величину, которую нужно найти:
             "Напряженность - 1"
             "Величина заряда - 2"
             "Расстояние - 3" """,
SURFACE_CHARGE_DENSITY: """Введите величину, которую нужно найти:
             "Поверхностная плотность зарядов - 1"
             "Электрический заряд - 2"
             "Площадь - 3" """,
INFINITY_SURFACE_EL_FIELD_INTENSITY: """Введите величину, которую нужно найти:
             "Напряженность - 1"
             "Поверхностная плотность зарядов - 2" """,
DIELECTRIC_CONSTANT: """Введите величину, которую нужно найти:
             "Диэлектрическая проницаемость - 1"
             "Напряженность эл. поля в вакууме - 2"
             "Напряженность эл. поля в диэлектрике - 3" """,
INTERACTING_CHARGES_POTENTIAL_ENERGY: """Введите величину, которую нужно найти:
             "Потенциальная энергия взаимодействия зарядов - 1"
             "Электрический заряд №1 - 2"
             "Электрический заряд №2 - 3"
             "Расстояние - 4" """,
POTENTIAL: """Введите величину, которую нужно найти:
             "Потенциал - 1"
             "Потенциальная энергия - 2"
             "Величина заряда - 3" """,
POINT_CHARGE_POTENTIAL: """Введите величину, которую нужно найти:
             "Потенциал - 1"
             "Величина заряда - 2"
             "Расстояние - 3" """,
VOLTAGE: """Введите величину, которую нужно найти:
             "Напряжение - 1"
             "Работа - 2"
             "Величина заряда - 3" """,
EL_FIELD_VOLTAGE: """Введите величину, которую нужно найти:
            "Напряжение - 1"
            "Напряженность эл.поля - 2"
            "Расстояние - 3" """,
EL_CAPACITY: """Введите величину, которую нужно найти:
             "Электроёмкость - 1"
             "Величина заряда - 2"
             "Напряжение - 3" """,
FLAT_CAPACITOR_EL_CAPACITY: """Введите величину, которую нужно найти:
             "Электроёмкость - 1"
             "Площадь пластин - 2"
             "Относительная диэлектрическая проницаемость - 3"
             "Расстояние между пластинами - 4" """,
CURRENT: """Введите величину, которую нужно найти:
             "Сила тока - 1"
             "Величина заряда - 2"
             "Время - 3" """,
CONDUCTOR_RESISTANCE: """Введите величину, которую нужно найти:
             "Сопротивление - 1"
             "Удельное сопротивление - 2"
             "Длина проводника - 3"
             "Площадь - 4" """,
SECTION_CIRCUIT_OHMS_LAW: """Введите величину, которую нужно найти:
             "Сила тока - 1"
             "Напряжение - 2"
             "Сопротивление - 3" """,
EL_CURRENT_POWER:  """Введите величину, которую нужно найти:
             "Мощность - 1"
             "Сила тока - 2"
             "Напряжение - 3" """,
JOULE_LENZ_LAW:  """Введите величину, которую нужно найти:
             "Кол-во теплоты - 1"
             "Сила тока - 2"
             "Сопротивление - 3"
             "Время - 4" """,
FULL_CIRCUIT_OHMS_LAW: """Введите величину, которую нужно найти:
             "Сила тока - 1"
             "Электродвижущая сила источника - 2"
             "Сопротивление внешней цепи - 3"
             "Внутреннее сопротивление источника питания - 4" """,
SHORT_CIRCUIT_CURRENT: """Введите величину, которую нужно найти:
             "Сила тока - 1"
             Сила тока - 1"
             "Электродвижущая сила источника - 2"
             "Внутреннее сопротивление источника питания - 3" """,
MAGNETIC_INDUCTION_VECTOR: """Введите величину, которую нужно найти:
             "Вектор - 1"
             "Максимальная сила Ампера - 2"
             "Длина проводника - 3"
             "Сила тока - 4" """,
AMPERES_FORCE: """Введите величину, которую нужно найти:
             "Сила Ампера - 1"
             "Сила тока - 2"
             "Вектор - 3"
             "Длина проводника - 4"
             "Синус угла - 5" """,
LORENTZ_FORCE: """Введите величину, которую нужно найти:
             "Сила Лоренца - 1"
             "Электрический заряд частицы - 2"
             "Скорость - 3"
             "Вектор - 4"
             "Синус угла - 5" """,
MAGNETIC_FLUX: """Введите величину, которую нужно найти:
             "Магнитный поток - 1"
             "Вектор магнитной индукции - 2"
             "Площадь - 3"
             "Синус угла - 4" """,
ELECTROMAGNETIC_INDUCTION_LAW: """Введите величину, которую нужно найти:
             "ЭДС индукции - 1"
             "Изменение магнитного потока - 2"
             "Промежуток времени - 3" """,
EMF_MOVING_CONDUCTOR: """Введите величину, которую нужно найти:
             "ЭДС индукции - 1"
             "Вектор магнитной индукции - 2"
             "Длина проводника - 3"
             "Скорость - 4"
             "Синус угла - 5" """,
EMF_SELF_INDUCTION: """Введите величину, которую нужно найти:
             "ЭДС самоиндукции - 1"
             "Коэффициент самоиндукции - 2"
             "Изменение силы тока - 3"
             "Промежуток времени - 4" """,
COIL_MAGNETIC_FIELD_ENERGY: """Введите величину, которую нужно найти:
             "Энергия - 1"
             "Индуктивность катушки - 2"
             "Сила тока - 3" """,
OSCILLATING_CIRCUIT_PERIOD: """Введите величину, которую нужно найти:
             "Период колебаний - 1"
             "Индуктивность катушки - 2"
             "Электроёмкость конденсатора - 3" """,
INDUCTIVE_RESISTANCE: """Введите величину, которую нужно найти:
             "Сопротивление - 1"
             "Частота - 2"
             "Индуктивность - 3" """,
CAPACITIVE_RESISTANCE: """Введите величину, которую нужно найти:
             "Сопротивление - 1"
             "Электроёмкость - 2"
             "Угловая частота - 3" """,
ACTUAL_CURRENT_VALUE: """Введите величину, которую нужно найти:
             "Сила тока - 1"
             "Максимальная сила тока - 2" """,
ACTUAL_VOLTAGE_VALUE: """Введите величину, которую нужно найти:
             "Напряжение - 1"
             "Максимальное напряжение - 2" """,
TOTAL_RESISTANCE: """Введите величину, которую нужно найти:
             "Полное сопротивление - 1"
             "Емкостное сопротивление - 2"
             "Индуктивное сопротивление - 3"
             "Активное сопротивление - 4" """
}