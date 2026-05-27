from __future__ import annotations

from sympy import Symbol, expand, simplify, sympify, Rational, plot, log, sqrt
from sympy.core.expr import Expr
import math as m

import core.math.algebra.enum as enum

#########
# АЛГЕБРА
#########

a = Symbol("a")
b = Symbol("b")
c = Symbol("c")
x = Symbol("x")


def calc_square_sum() -> Expr:
	return expand((a + b) ** 2)


def calc_square_sum_values(a_value: float, b_value: float) -> Expr:
	return calc_square_sum().subs({a: a_value, b: b_value})


def calc_square_diff() -> Expr:
	return expand((a - b) ** 2)


def calc_square_diff_values(a_value: float, b_value: float) -> Expr:
	return calc_square_diff().subs({a: a_value, b: b_value})


def calc_diff_of_squares() -> Expr:
	return expand((a + b) * (a - b))


def calc_diff_of_squares_values(a_value: float, b_value: float) -> Expr:
	return calc_diff_of_squares().subs({a: a_value, b: b_value})


def calc_cube_sum() -> Expr:
	return expand((a + b) ** 3)


def calc_cube_sum_values(a_value: float, b_value: float) -> Expr:
	return calc_cube_sum().subs({a: a_value, b: b_value})


def calc_cube_diff() -> Expr:
	return expand((a - b) ** 3)


def calc_cube_diff_values(a_value: float, b_value: float) -> Expr:
	return calc_cube_diff().subs({a: a_value, b: b_value})


def calc_sum_of_cubes() -> Expr:
	return expand(a ** 3 + b ** 3)


def calc_sum_of_cubes_values(a_value: float, b_value: float) -> Expr:
	return calc_sum_of_cubes().subs({a: a_value, b: b_value})


def calc_diff_of_cubes() -> Expr:
	return expand(a ** 3 - b ** 3)


def calc_diff_of_cubes_values(a_value: float, b_value: float) -> Expr:
	return calc_diff_of_cubes().subs({a: a_value, b: b_value})


def calc_discriminant(a_val: float, b_val: float, c_val: float) -> Expr:
	return b_val ** 2 - 4 * a_val * c_val


def calc_vieta_sum(a_val: float, b_val: float) -> Expr:
	return -b_val / a_val


def calc_vieta_product(a_val: float, c_val: float) -> Expr:
	return c_val / a_val


def calc_parabola_vertex_x(a_val: float, b_val: float) -> Expr:
	return -b_val / (2 * a_val)


def calc_parabola_vertex_y(a_val: float, b_val: float, c_val: float) -> Expr:
	return (4 * a_val * c_val - b_val ** 2) / (4 * a_val)


def calc_expand_formula(formula_id: int) -> Expr:
	match formula_id:
		case enum.SQUARE_SUM:
			return calc_square_sum()
		case enum.SQUARE_DIFF:
			return calc_square_diff()
		case enum.DIFF_OF_SQUARES:
			return calc_diff_of_squares()
		case enum.CUBE_SUM:
			return calc_cube_sum()
		case enum.CUBE_DIFF:
			return calc_cube_diff()
		case enum.SUM_OF_CUBES:
			return calc_sum_of_cubes()
		case enum.DIFF_OF_CUBES:
			return calc_diff_of_cubes()
		case enum.DISCRIMINANT:
			return b ** 2 - 4 * a * c
		case enum.VIETA_SUM:
			return -b / a
		case enum.VIETA_PRODUCT:
			return c / a
		case enum.PARABOLA_VERTEX_X:
			return -b / (2 * a)
		case enum.PARABOLA_VERTEX_Y:
			return (4 * a * c - b ** 2) / (4 * a)
		case _:
			raise ValueError("Неизвестный идентификатор формулы")


def calc_formula_values(formula_id: int, a_value: float, b_value: float) -> Expr:
	match formula_id:
		case enum.SQUARE_SUM:
			return calc_square_sum_values(a_value, b_value)
		case enum.SQUARE_DIFF:
			return calc_square_diff_values(a_value, b_value)
		case enum.DIFF_OF_SQUARES:
			return calc_diff_of_squares_values(a_value, b_value)
		case enum.CUBE_SUM:
			return calc_cube_sum_values(a_value, b_value)
		case enum.CUBE_DIFF:
			return calc_cube_diff_values(a_value, b_value)
		case enum.SUM_OF_CUBES:
			return calc_sum_of_cubes_values(a_value, b_value)
		case enum.DIFF_OF_CUBES:
			return calc_diff_of_cubes_values(a_value, b_value)
		case _:
			raise ValueError("Неизвестный идентификатор формулы")


def calc_identify_formula(expression: str) -> tuple[int | None, Expr]:
	user_expr = simplify(sympify(expression))

	for formula_id in enum.ALGEBRA_FORMULAS:
		expanded = calc_expand_formula(formula_id)
		if simplify(user_expr - expanded) == 0:
			return formula_id, expanded

	return None, user_expr


def calc_solution_steps(formula_id: int, a_value: float | None = None, b_value: float | None = None) -> tuple[list[str], Expr]:
	formula = enum.ALGEBRA_FORMULAS.get(formula_id, "Неизвестная формула")
	expanded = calc_expand_formula(formula_id)

	steps = [
		f"1) Формула: {formula}",
		f"2) Раскрываем скобки: {formula} = {expanded}",
	]

	if a_value is None or b_value is None:
		return steps, expanded

	result = expanded.subs({a: a_value, b: b_value})
	steps.append(f"3) Подставляем значения: a = {a_value}, b = {b_value}")
	steps.append(f"4) Вычисляем: {result}")

	return steps, result

def calc_square_equation(a,b,c):
	d = b ** 2 - 4 * a * c
	if d < 0:
		return "Нет действительных корней"
	elif d == 0:
		x = -b / (2 * a)
		return f"Один корень: x = {Rational(x)}"
	else:
		x1 = (-b + m.sqrt(d)) / (2 * a)
		x2 = (-b - m.sqrt(d)) / (2 * a)
		return f"Два корня: x1 = {Rational(x1)}, x2 = {Rational(x2)}"

def calc_parabola_vertex(a, b, c):
	x_vertex = -b / (2 * a)
	y_vertex = a * x_vertex ** 2 + b * x_vertex + c
	return f"Вершина параболы (x, y): ({Rational(x_vertex)}, {Rational(y_vertex)})"

def calc_parabola_plot(a, b, c):
	x = Symbol('x')
	y = a * x ** 2 + b * x + c
	p = plot(y, (x, -50, 50), show=False)
	p.show()

def calc_logarithm(base, value):
	return Rational(log(value, base))

def _validate_logarithm_values(base: float, *values: float) -> None:
	if base <= 0 or base == 1:
		raise ValueError("Основание логарифма должно быть больше 0 и не равно 1")
	for value in values:
		if value <= 0:
			raise ValueError("Аргументы логарифма должны быть больше 0")

def calc_logarithm_properties_multiplication(base: float, x_value: float, y_value: float) -> list[str]:
	_validate_logarithm_values(base, x_value, y_value)

	lhs = log(x_value * y_value, base)
	rhs_x = log(x_value, base)
	rhs_y = log(y_value, base)
	rhs_sum = rhs_x + rhs_y

	return [
		"Логарифм произведения:",
		"log_a(x·y) = log_a(x) + log_a(y)",
		f"1) Подставляем: log_{Rational(base)}({Rational(x_value)}·{Rational(y_value)}) = log_{Rational(base)}({Rational(x_value)}) + log_{Rational(base)}({Rational(y_value)})",
		f"2) Вычисляем левую часть: log_{Rational(base)}({Rational(x_value * y_value)}) = {lhs}",
		f"3) Вычисляем правую часть: {Rational(rhs_x)} + {Rational(rhs_y)} = {Rational(rhs_sum)}",
		f"4) Проверка: {Rational(lhs)} = {Rational(rhs_sum)}",
	]

def calc_logarithm_properties_division(base: float, x_value: float, y_value: float) -> list[str]:
	_validate_logarithm_values(base, x_value, y_value)

	lhs = log(x_value / y_value, base)
	rhs_x = log(x_value, base)
	rhs_y = log(y_value, base)
	rhs_diff = rhs_x - rhs_y

	return [
		"Логарифм дроби:",
		"log_a(x/y) = log_a(x) - log_a(y)",
		f"1) Подставляем: log_{Rational(base)}({Rational(x_value)}/{Rational(y_value)}) = log_{Rational(base)}({Rational(x_value)}) - log_{Rational(base)}({Rational(y_value)})",
		f"2) Вычисляем левую часть: log_{Rational(base)}({Rational(x_value / y_value)}) = {lhs}",
		f"3) Вычисляем правую часть: {Rational(rhs_x)} - {Rational(rhs_y)} = {Rational(rhs_diff)}",
		f"4) Проверка: {Rational(lhs)} = {Rational(rhs_diff)}",
	]

def calc_arithmetic_progression_nth_term(a1, d, n):
	an = a1 + (n - 1) * d
	return f"n-й член арифметической прогрессии: a_n = {Rational(an)}"

def calc_arithmetic_progression_sum(a1, d, n):
	sn = n * (2 * a1 + (n - 1) * d) / 2
	return f"Сумма n членов арифметической прогрессии: S_n = {Rational(sn)}"

def calc_arithmetic_progression_difference(a1, a2):
	d = a2 - a1
	return f"Разность арифметической прогрессии: d = {Rational(d)}"

def calc_arithmetic_progression_first_term(an, d, n):
	a1 = an - (n - 1) * d
	return f"Первый член арифметической прогрессии: a_1 = {Rational(a1)}"

def calc_geometric_progression_nth_term(a1, r, n):
	an = a1 * r ** (n - 1)
	return f"n-й член геометрической прогрессии: a_n = {Rational(an)}"

def calc_geometric_progression_sum(a1, r, n):
	if r == 1:
		sn = a1 * n
	else:
		sn = a1 * (r ** n - 1) / (r - 1)
	return f"Сумма n членов геометрической прогрессии: S_n = {Rational(sn)}"

def calc_geometric_progression_ratio(a1, an, n):
	r = (an / a1) ** (1 / (n - 1))
	return f"Знаменатель геометрической прогрессии: r = {Rational(r)}"

def calc_geometric_progression_infinite_sum(a1, r):
	if r >= 1:
		return "Знаменатель прогрессии должен быть меньше 1 для бесконечно-убывающей прогрессии."
	sn = a1 / (1 - r)
	return f"Сумма бесконечно-убывающей геометрической прогрессии: S = {Rational(sn)}"

def calc_geometric_progression_first_term(an, r, n):
	a1 = an / r ** (n - 1)
	return f"Первый член геометрической прогрессии: a_1 = {Rational(a1)}"

def calc_trigonometry_sin(a, c):
	return f"sin(α) = {Rational(a / c)}"

def calc_trigonometry_cos(b, c):
	return f"cos(α) = {Rational(b / c)}"

def calc_trigonometry_tan(a, b):
	return f"tan(α) = {Rational(a / b)}"

def calc_trigonometry_cot(a, b):
	return f"cot(α) = {Rational(b / a)}"


def _normalize_sign(sign: int) -> int:
	if sign not in (-1, 1):
		raise ValueError("Знак должен быть равен 1 или -1")
	return sign


def _validate_interval_value(value: Rational, name: str) -> None:
	if value < -1 or value > 1:
		raise ValueError(f"{name} должен быть в диапазоне [-1; 1]")


def _validate_nonzero(value: Rational, name: str) -> None:
	if value == 0:
		raise ValueError(f"{name} не должен быть равен 0")


def calc_identity_sin_by_cos(cos_value: float, sign: int = 1) -> list[str]:
	sign = _normalize_sign(sign)
	cos_expr = Rational(str(cos_value))
	_validate_interval_value(cos_expr, "cos(x)")

	sin_squared = simplify(1 - cos_expr ** 2)
	if sin_squared < 0:
		raise ValueError("Подкоренное выражение отрицательно")

	sin_abs = simplify(sqrt(sin_squared))
	sin_result = sin_abs if sign == 1 else -sin_abs

	return [
		"Основное тождество: sin^2(x) + cos^2(x) = 1",
		f"1) Подставляем: sin^2(x) + ({cos_expr})^2 = 1",
		f"2) Выражаем: sin^2(x) = 1 - ({cos_expr})^2 = {sin_squared}",
		f"3) Извлекаем корень: sin(x) = ±sqrt({sin_squared})",
		f"4) С учётом выбранного знака: sin(x) = {sin_result}",
	]


def calc_identity_cos_by_sin(sin_value: float, sign: int = 1) -> list[str]:
	sign = _normalize_sign(sign)
	sin_expr = Rational(str(sin_value))
	_validate_interval_value(sin_expr, "sin(x)")

	cos_squared = simplify(1 - sin_expr ** 2)
	if cos_squared < 0:
		raise ValueError("Подкоренное выражение отрицательно")

	cos_abs = simplify(sqrt(cos_squared))
	cos_result = cos_abs if sign == 1 else -cos_abs

	return [
		"Основное тождество: sin^2(x) + cos^2(x) = 1",
		f"1) Подставляем: ({sin_expr})^2 + cos^2(x) = 1",
		f"2) Выражаем: cos^2(x) = 1 - ({sin_expr})^2 = {cos_squared}",
		f"3) Извлекаем корень: cos(x) = ±sqrt({cos_squared})",
		f"4) С учётом выбранного знака: cos(x) = {cos_result}",
	]


def calc_identity_tan_by_cos(cos_value: float, sign: int = 1) -> list[str]:
	sign = _normalize_sign(sign)
	cos_expr = Rational(str(cos_value))
	_validate_interval_value(cos_expr, "cos(x)")
	_validate_nonzero(cos_expr, "cos(x)")

	tan_squared = simplify(1 / (cos_expr ** 2) - 1)
	if tan_squared < 0:
		raise ValueError("Подкоренное выражение отрицательно")

	tan_abs = simplify(sqrt(tan_squared))
	tan_result = tan_abs if sign == 1 else -tan_abs

	return [
		"Основное тождество: 1 + tan^2(x) = 1/cos^2(x)",
		f"1) Подставляем: 1 + tan^2(x) = 1/({cos_expr})^2",
		f"2) Выражаем: tan^2(x) = 1/({cos_expr})^2 - 1 = {tan_squared}",
		f"3) Извлекаем корень: tan(x) = ±sqrt({tan_squared})",
		f"4) С учётом выбранного знака: tan(x) = {tan_result}",
	]


def calc_identity_cot_by_sin(sin_value: float, sign: int = 1) -> list[str]:
	sign = _normalize_sign(sign)
	sin_expr = Rational(str(sin_value))
	_validate_interval_value(sin_expr, "sin(x)")
	_validate_nonzero(sin_expr, "sin(x)")

	cot_squared = simplify(1 / (sin_expr ** 2) - 1)
	if cot_squared < 0:
		raise ValueError("Подкоренное выражение отрицательно")

	cot_abs = simplify(sqrt(cot_squared))
	cot_result = cot_abs if sign == 1 else -cot_abs

	return [
		"Основное тождество: 1 + cot^2(x) = 1/sin^2(x)",
		f"1) Подставляем: 1 + cot^2(x) = 1/({sin_expr})^2",
		f"2) Выражаем: cot^2(x) = 1/({sin_expr})^2 - 1 = {cot_squared}",
		f"3) Извлекаем корень: cot(x) = ±sqrt({cot_squared})",
		f"4) С учётом выбранного знака: cot(x) = {cot_result}",
	]