from __future__ import annotations

from sympy import Symbol, expand, simplify, sympify
from sympy.core.expr import Expr

import core.math.algebra.enum as enum

#########
# АЛГЕБРА
#########

a = Symbol("a")
b = Symbol("b")


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

	for formula_id in enum.smf_formulas:
		expanded = calc_expand_formula(formula_id)
		if simplify(user_expr - expanded) == 0:
			return formula_id, expanded

	return None, user_expr


def calc_solution_steps(formula_id: int, a_value: float | None = None, b_value: float | None = None) -> tuple[list[str], Expr]:
	formula = enum.smf_formulas.get(formula_id, "Неизвестная формула")
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
