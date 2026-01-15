import math as m

########
#ОПТИКА#
########

# Закон преломления света: n21 = n2 / n1 = v1 / v2
def calc_n21_from_n2_n1(n2, n1):
    return n2 / n1

def calc_n2_from_n21_n1(n21, n1):
    return n21 * n1

def calc_n1_from_n2_n21(n2, n21):
    return n2 / n21

def calc_n21_from_v1_v2(v1, v2):
    return v1 / v2

def calc_v1_from_n21_v2(n21, v2):
    return n21 * v2

def calc_v2_from_v1_n21(v1, n21):
    return v1 / n21


# Показатель преломления (n21 = sin(alpha) / sin(gamma))
def calc_n21_from_sin_alpha_sin_gamma(sin_alpha, sin_gamma):
    return sin_alpha / sin_gamma

def calc_sin_alpha_from_n21_sin_gamma(n21, sin_gamma):
    return n21 * sin_gamma

def calc_sin_gamma_from_sin_alpha_n21(sin_alpha, n21):
    return sin_alpha / n21


# Формула тонкой линзы: 1/F = 1/d + 1/f
def calc_F_from_d_f(d, f):
    denom = (1.0 / d) + (1.0 / f)
    return 1.0 / denom

def calc_d_from_F_f(F, f):
    denom = (1.0 / F) - (1.0 / f)
    return 1.0 / denom

def calc_f_from_F_d(F, d):
    denom = (1.0 / F) - (1.0 / d)
    return 1.0 / denom


# Оптическая сила линзы: D = 1 / F
def calc_D_from_F(F):
    return 1.0 / F

def calc_F_from_D(D):
    return 1.0 / D


# Интерференция
# max: delta = k * lambda
def calc_delta_from_k_lambda(k, lam):
    return k * lam

def calc_k_from_delta_lambda(delta, lam):
    return delta / lam

def calc_lambda_from_delta_k(delta, k):
    return delta / k

# min: delta = (2k + 1) * lambda / 2
def calc_delta_min_from_k_lambda(k, lam):
    return ((2 * k) + 1) * lam / 2.0

def calc_k_from_delta_min_lambda(delta, lam):
    return (delta / lam) - 0.5

def calc_lambda_from_delta_min_k(delta, k):
    return (2.0 * delta) / ((2 * k) + 1)


# Дифракционная решетка: d * sin(phi) = k * lambda
def calc_d_from_k_lambda_phi(k, lam, phi):
    sin_phi = m.sin(phi)
    return (k * lam) / sin_phi

def calc_phi_from_k_lambda_d(k, lam, d):
    value = (k * lam) / d
    value = max(min(value, 1.0), -1.0)
    return m.asin(value)

def calc_k_from_d_lambda_phi(d, lam, phi):
    return (d * m.sin(phi)) / lam

def calc_lambda_from_d_phi_k(d, phi, k):
    return (d * m.sin(phi)) / k
