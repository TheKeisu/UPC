import optics.enum as enum
import optics.calculations as calcs

########
#ОПТИКА#
########

def formula_selection(input_text, enum_formula):
    option = int(input(input_text))

    match enum_formula:
        case enum.REFRACTION_LAW:
            match option:
                case 1:
                    n2 = float(input("Введите n2: "))
                    n1 = float(input("Введите n1: "))
                    print(f"n21 = {calcs.calc_n21_from_n2_n1(n2, n1)}")
                case 2:
                    n21 = float(input("Введите n21: "))
                    n1 = float(input("Введите n1: "))
                    print(f"n2 = {calcs.calc_n2_from_n21_n1(n21, n1)}")
                case 3:
                    n2 = float(input("Введите n2: "))
                    n21 = float(input("Введите n21: "))
                    print(f"n1 = {calcs.calc_n1_from_n2_n21(n2, n21)}")
                case 4:
                    v1 = float(input("Введите v1: "))
                    v2 = float(input("Введите v2: "))
                    print(f"n21 = {calcs.calc_n21_from_v1_v2(v1, v2)}")
                case 5:
                    n21 = float(input("Введите n21: "))
                    v2 = float(input("Введите v2: "))
                    print(f"v1 = {calcs.calc_v1_from_n21_v2(n21, v2)}")
                case _:
                    print("Неверный вариант.")

        case enum.REFRACTIVE_INDEX:
            match option:
                case 1:
                    sin_alpha = float(input("Введите sin(alpha): "))
                    sin_gamma = float(input("Введите sin(gamma): "))
                    print(f"n21 = {calcs.calc_n21_from_sin_alpha_sin_gamma(sin_alpha, sin_gamma)}")
                case 2:
                    n21 = float(input("Введите n21: "))
                    sin_gamma = float(input("Введите sin(gamma): "))
                    print(f"sin(alpha) = {calcs.calc_sin_alpha_from_n21_sin_gamma(n21, sin_gamma)}")
                case 3:
                    sin_alpha = float(input("Введите sin(alpha): "))
                    n21 = float(input("Введите n21: "))
                    print(f"sin(gamma) = {calcs.calc_sin_gamma_from_sin_alpha_n21(sin_alpha, n21)}")
                case _:
                    print("Неверный вариант.")

        case enum.THIN_LENS:
            match option:
                case 1:
                    d = float(input("Введите d (предметное расстояние): "))
                    f = float(input("Введите f (изображение): "))
                    print(f"F = {calcs.calc_F_from_d_f(d, f)}")
                case 2:
                    F = float(input("Введите F (фокусное расстояние): "))
                    f = float(input("Введите f (изображение): "))
                    print(f"d = {calcs.calc_d_from_F_f(F, f)}")
                case 3:
                    F = float(input("Введите F (фокусное расстояние): "))
                    d = float(input("Введите d (предметное расстояние): "))
                    print(f"f = {calcs.calc_f_from_F_d(F, d)}")
                case _:
                    print("Неверный вариант.")

        case enum.OPTICAL_POWER:
            match option:
                case 1:
                    F = float(input("Введите F (фокусное расстояние): "))
                    print(f"D = {calcs.calc_D_from_F(F)}")
                case 2:
                    D = float(input("Введите D (оптическая сила): "))
                    print(f"F = {calcs.calc_F_from_D(D)}")
                case _:
                    print("Неверный вариант.")

        case enum.INTERFERENCE:
            match option:
                case 1:  # max: Δd = k * λ
                    k = float(input("Введите k (порядок): "))
                    lam = float(input("Введите λ (длина волны): "))
                    print(f"Δd = {calcs.calc_delta_from_k_lambda(k, lam)}")
                case 2:  # min: Δd = (2k+1)λ/2
                    k = float(input("Введите k (порядок): "))
                    lam = float(input("Введите λ (длина волны): "))
                    print(f"Δd (min) = {calcs.calc_delta_min_from_k_lambda(k, lam)}")
                case 3:
                    delta = float(input("Введите Δd: "))
                    lam = float(input("Введите λ (длина волны): "))
                    print(f"k = {calcs.calc_k_from_delta_lambda(delta, lam)}")
                case 4:
                    delta = float(input("Введите Δd (min или max в зависимости от формулы): "))
                    lam = float(input("Введите λ (длина волны): "))
                    # assume min formula if user intends min
                    print(f"k (min formula, float) = {calcs.calc_k_from_delta_min_lambda(delta, lam)}")
                case 5:
                    delta = float(input("Введите Δd: "))
                    k = float(input("Введите k (порядок): "))
                    print(f"λ (max) = {calcs.calc_lambda_from_delta_k(delta, k)}")
                case _:
                    print("Неверный вариант.")

        case enum.DIFFRACTION_GRATING:
            match option:
                case 1:
                    k = float(input("Введите k (порядок): "))
                    lam = float(input("Введите λ (длина волны): "))
                    phi = float(input("Введите φ (в радианах): "))
                    print(f"d = {calcs.calc_d_from_k_lambda_phi(k, lam, phi)}")
                case 2:
                    k = float(input("Введите k (порядок): "))
                    lam = float(input("Введите λ (длина волны): "))
                    d = float(input("Введите d (шаг решетки): "))
                    value = (k * lam) / d
                    value = max(min(value, 1.0), -1.0)
                    print(f"φ (в радианах) = {calcs.calc_phi_from_k_lambda_d(k, lam, d)}")
                case 3:
                    d = float(input("Введите d (шаг решетки): "))
                    lam = float(input("Введите λ (длина волны): "))
                    phi = float(input("Введите φ (в радианах): "))
                    print(f"k = {calcs.calc_k_from_d_lambda_phi(d, lam, phi)}")
                case 4:
                    d = float(input("Введите d (шаг решетки): "))
                    phi = float(input("Введите φ (в радианах): "))
                    k = float(input("Введите k (порядок): "))
                    print(f"λ = {calcs.calc_lambda_from_d_phi_k(d, phi, k)}")
                case _:
                    print("Неверный вариант.")
        case _:
            print("Неверная формула.")
