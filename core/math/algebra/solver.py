from __future__ import annotations

from sympy.core.expr import Expr

import core.math.algebra.calculations as calcs
import core.math.algebra.enum as enum

#########
# АЛГЕБРА
#########


def expand_formula(formula_id: int) -> Expr:
	return calcs.calc_expand_formula(formula_id)


def identify_formula(expression: str) -> tuple[int | None, Expr]:
	return calcs.calc_identify_formula(expression)


def formula_selection(input_text, enum_formula):
	option = int(input(input_text))

	match enum_formula:
		case enum.SQUARE_SUM | enum.SQUARE_DIFF | enum.DIFF_OF_SQUARES | enum.CUBE_SUM | enum.CUBE_DIFF | enum.SUM_OF_CUBES | enum.DIFF_OF_CUBES:
			match option:
				case 1:
					steps, result = calcs.calc_solution_steps(enum_formula)
					print("Пошаговое решение:")
					for step in steps:
						print(step)
					print(f"Ответ = {result}")
				case 2:
					a_value = float(input("Введите a: "))
					b_value = float(input("Введите b: "))
					steps, result = calcs.calc_solution_steps(enum_formula, a_value, b_value)
					print("Пошаговое решение:")
					for step in steps:
						print(step)
					print(f"Ответ = {result}")
				case _:
					print("Неверный вариант.")
		case _:
			print("Неверная формула.")
