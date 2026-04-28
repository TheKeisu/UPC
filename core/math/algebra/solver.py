from __future__ import annotations

from sympy.core.expr import Expr

import core.math.algebra.calculations as calcs
import core.math.algebra.enum as enum
from core.math.handbook import run_handbook_console
#########
# АЛГЕБРА
#########


def expand_formula(formula_id: int) -> Expr:
	return calcs.calc_expand_formula(formula_id)


def identify_formula(expression: str) -> tuple[int | None, Expr]:
	return calcs.calc_identify_formula(expression)


def formula_selection(input_text, enum_formula):
	try:
		option = int(input(input_text))
		if enum_formula != enum.HANDBOOK_FORMULAS:
			print("Неверная формула.")
			return

		match option:
			case 1:
				run_handbook_console()
			case _:
				print("Неверный вариант.")
	except (ValueError, ZeroDivisionError) as error:
		print(f"Ошибка ввода/вычисления: {error}")