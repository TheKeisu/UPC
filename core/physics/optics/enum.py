########
#ОПТИКА#
########

REFRACTION_LAW = 1
REFRACTIVE_INDEX = 2
THIN_LENS = 3
OPTICAL_POWER = 4
INTERFERENCE = 5
DIFFRACTION_GRATING = 6

FORMULAS = {
   "reflection_law": {
        "subject_key": "оптика",
        "title": " Закон преломления света",
        "description": "Закон преломления света, связывающий показатели преломления и углы падения и преломления",
        "formula_view": "n21 = n2/n1 = v1/v2",
        "cases": {
            1: {
                "name": "Найти относительный показатель преломления",
                "inputs": [
                    ("n1", "Показатель преломления первой среды"),
                    ("n2", "Показатель преломления второй среды")
                ],
                "output": "Относительный показатель преломления",
                "function": "core.physics.optics.calculations.calc_n21_from_n2_n1"
            },
            2: {
                "name": "Найти показатель преломления второй среды",
                "inputs": [
                    ("n21", "Относительный показатель преломления"),
                    ("n1", "Показатель преломления первой среды")
                ],
                "output": "Показатель преломления второй среды",
                "function": "core.physics.optics.calculations.calc_n2_from_n21_n1"
            },
            3: {
                "name": "Найти показатель преломления первой среды",
                "inputs": [
                    ("n2", "Показатель преломления второй среды"),
                    ("n21", "Относительный показатель преломления")
                ],
                "output": "Показатель преломления первой среды",
                "function": "core.physics.optics.calculations.calc_n1_from_n2_n21"
            }
        }
    },
   "refractive_index": {
        "subject_key": "оптика",
        "title": "Показатель преломления",
        "description": "Показатель преломления, определяющий отношение синусов углов падения и преломления",
        "formula_view": "n21 = sin α / sin γ",
        "cases": {
            1: {
                "name": "Найти относительный показатель преломления",
                "inputs": [
                    ("sin_alpha", "Синус угла падения"),
                    ("sin_gamma", "Синус угла преломления")
                ],
                "output": "Относительный показатель преломления",
                "function": "core.physics.optics.calculations.calc_n21_from_sin_alpha_sin_gamma"
            },
            2: {
                "name": "Найти синус угла падения",
                "inputs": [
                    ("n21", "Относительный показатель преломления"),
                    ("sin_gamma", "Синус угла преломления")
                ],
                "output": "Синус угла падения",
                "function": "core.physics.optics.calculations.calc_sin_alpha_from_n21_sin_gamma"
            },
            3: {
                "name": "Найти синус угла преломления",
                "inputs": [
                    ("sin_alpha", "Синус угла падения"),
                    ("n21", "Относительный показатель преломления")
                ],
                "output": "Синус угла преломления",
                "function": "core.physics.optics.calculations.calc_sin_gamma_from_sin_alpha_n21"
            }
        }     
    },
   "thin_lens": {
        "subject_key": "оптика",
        "title": "Формула тонкой линзы",
        "description": "Формула тонкой линзы, связывающая фокусное расстояние, предметное расстояние и изображение",
        "formula_view": "1/F = 1/d + 1/f",
        "cases": {
            1: {
                "name": "Найти фокусное расстояние",
                "inputs": [
                    ("d", "Предметное расстояние"),
                    ("f", "Изображение")
                ],
                "output": "Фокусное расстояние",
                "function": "core.physics.optics.calculations.calc_F_from_d_f"
            },
            2: {
                "name": "Найти предметное расстояние",
                "inputs": [
                    ("F", "Фокусное расстояние"),
                    ("f", "Изображение")
                ],
                "output": "Предметное расстояние",
                "function": "core.physics.optics.calculations.calc_d_from_F_f"
            },
            3: {
                "name": "Найти изображение",
                "inputs": [
                    ("F", "Фокусное расстояние"),
                    ("d", "Предметное расстояние")
                ],
                "output": "Изображение",
                "function": "core.physics.optics.calculations.calc_f_from_F_d"
            }
        }
    },
    "optical_power": {
          "subject_key": "оптика",
          "title": "Оптическая сила линзы",
          "description": "Оптическая сила линзы, определяющаяся как обратная величина фокусного расстояния",
          "formula_view": "D = 1/F",
          "cases": {
              1: {
                  "name": "Найти оптическую силу",
                  "inputs": [
                      ("F", "Фокусное расстояние")
                  ],
                  "output": "Оптическая сила",
                  "function": "core.physics.optics.calculations.calc_D_from_F"
              },
              2: {
                  "name": "Найти фокусное расстояние",
                  "inputs": [
                      ("D", "Оптическая сила")
                  ],
                  "output": "Фокусное расстояние",
                  "function": "core.physics.optics.calculations.calc_F_from_D"
              }
          }
     },
    "interference": {
          "subject_key": "оптика",
          "title": "Интерференция",
          "description": "Макс. интерференции (Δd = kλ) и Мин. интерференции (Δd = (2k+1)λ/2)",
          "formula_view": "Макс. интерференции: Δd = kλ, Мин. интерференции: Δd = (2k+1)λ/2",
          "cases": {
              1: {
                  "name": "Найти Δd для макс. интерференции",
                  "inputs": [
                      ("k", "Порядок"),
                      ("lam", "Длина волны")
                  ],
                  "output": "Δd для макс. интерференции",
                  "function": "core.physics.optics.calculations.calc_delta_from_k_lambda"
              },
              2: {
                  "name": "Найти Δd для мин. интерференции",
                  "inputs": [
                      ("k", "Порядок"),
                      ("lam", "Длина волны")
                  ],
                  "output": "Δd для мин. интерференции",
                  "function": "core.physics.optics.calculations.calc_delta_min_from_k_lambda"
              },
              3: {
                  "name": "Найти k по Δd и λ",
                  "inputs": [
                      ("delta", "Δd"),
                      ("lam", "Длина волны")
                  ],
                  "output": "Порядок k",
                  "function": "core.physics.optics.calculations.calc_k_from_delta_lambda"
              },
              4: {
                  "name": "Найти k по Δd (мин. или макс.) и λ",
                  "inputs": [
                      ("delta", "Δd (мин. или макс. в зависимости от формулы)"),
                      ("lam", "Длина волны")
                  ],
                  "output": "Порядок k (для мин. формулы)",
                  "function": "core.physics.optics.calculations.calc_k_from_delta_min_lambda"
              },
              5: {
                  "name": "Найти λ по Δd и k",
                  "inputs": [
                      ("delta", "Δd"),
                      ("k", "Порядок")
                  ],
                  "output": "Длина волны λ (для макс. формулы)",
                  "function": "core.physics.optics.calculations.calc_lambda_from_delta_k"
              }
          }
     },
    "diffraction_grating": {
          "subject_key": "оптика",
          "title": "Дифракционная решетка",
          "description": "Дифракционная решетка, связывающая шаг решетки, угол дифракции, порядок и длину волны",
          "formula_view": "d · sin φ = k λ",
          "cases": {
              1: {
                  "name": "Найти шаг решетки",
                  "inputs": [
                      ("k", "Порядок"),
                      ("lam", "Длина волны"),
                      ("phi", "Угол дифракции")
                  ],
                  "output": "Шаг решетки d",
                  "function": "core.physics.optics.calculations.calc_d_from_k_lambda_phi"
              },
              2: {
                  "name": "Найти угол дифракции",
                  "inputs": [
                      ("k", "Порядок"),
                      ("lam", "Длина волны"),
                      ("d", "Шаг решетки")
                  ],
                  "output": "Угол дифракции φ",
                  "function": "core.physics.optics.calculations.calc_phi_from_k_lambda_d"
              },
              3: {
                  "name": "Найти порядок k",
                  "inputs": [
                      ("d", "Шаг решетки"),
                      ("lam", "Длина волны"),
                      ("phi", "Угол дифракции")
                  ],
                  "output": "Порядок k",
                  "function": "core.physics.optics.calculations.calc_k_from_d_lambda_phi"
              },
              4: {
                  "name": "Найти длину волны λ",
                  "inputs": [
                      ("d", "Шаг решетки"),
                      ("phi", "Угол дифракции"),
                      ("k", "Порядок")
                  ],
                  "output": "Длина волны λ",
                  "function": "core.physics.optics.calculations.calc_lambda_from_d_phi_k"
              }
          }
     }
}

optics = {
    REFRACTION_LAW: """Выберите величину, которую нужно найти
                         "Закон преломления света (n21 = n2/n1 = v1/v2) - 1"
                         "n2 - 2"
                         "n1 - 3"
                         "v1 - 4"
                         "v2 - 5" """,
    REFRACTIVE_INDEX: """Выберите величину, которую нужно найти
                         "Показатель преломления (n21 = sin α / sin γ) - 1"
                         "sin α - 2"
                         "sin γ - 3" """,
    THIN_LENS: """Выберите величину, которую нужно найти
                         "Формула тонкой линзы (1/F = 1/d + 1/f) - 1"
                         "F (фокусное расстояние) - 2"
                         "d (предметное расстояние) - 3"
                         "f (изображение) - 4" """,
    OPTICAL_POWER: """Выберите величину, которую нужно найти
                         "Оптическая сила линзы (D = 1/F) - 1"
                         "D (оптическая сила) - 2"
                         "F (фокусное расстояние) - 3" """,
    INTERFERENCE: """Выберите величину, которую нужно найти
                         "Макс. интерференции (Δd = kλ) - 1"
                         "Мин. интерференции (Δd = (2k+1)λ/2) - 2"
                         "Δd - 3"
                         "k (порядок) - 4"
                         "λ (длина волны) - 5" """,
    DIFFRACTION_GRATING: """Выберите величину, которую нужно найти
                         "Дифракционная решетка (d · sin φ = k λ) - 1"
                         "d (шаг решетки) - 2"
                         "φ (угол) - 3"
                         "k (порядок) - 4"
                         "λ (длина волны) - 5" """
}