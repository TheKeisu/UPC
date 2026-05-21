from __future__ import annotations

from builtins import print as builtin_print
from collections.abc import Mapping, Sequence
from numbers import Real


def _format_number(value: float) -> str:
	return f"{value:.10g}"


def _format_unit(unit: str | None) -> str:
	unit_text = str(unit or "").strip()
	if unit_text:
		return f" {unit_text}"
	return ""


def _iter_variables(variables: Sequence[dict | Sequence[str]] | None) -> list[tuple[str, str]]:
	items: list[tuple[str, str]] = []
	for variable in variables or []:
		if isinstance(variable, dict):
			name = str(variable.get("name") or "").strip()
			label = str(variable.get("display_name") or variable.get("name") or name).strip()
		elif isinstance(variable, (list, tuple)) and len(variable) >= 2:
			name = str(variable[0]).strip()
			label = str(variable[1]).strip() or name
		else:
			continue

		if not name:
			continue
		items.append((name, label or name))

	return items


def build_solution_report(
	*,
	title: str,
	formula_view: str,
	variables: Sequence[dict | Sequence[str]] | None,
	output: str,
	known_values: Mapping[str, float],
	result: float,
	unit: str | None = None,
	) -> dict:
	ordered_variables = _iter_variables(variables)
	known_values_parts: list[str] = []
	for name, label in ordered_variables:
		if name not in known_values:
			continue
		known_values_parts.append(f"{label} = {_format_number(float(known_values[name]))}")

	steps: list[str] = [f"1. Формула: {title or output}"]
	if formula_view:
		steps.append(f"2. Записываем: {formula_view}")

	step_index = len(steps) + 1
	if known_values_parts:
		steps.append(f"{step_index}. Известные значения: {'; '.join(known_values_parts)}")
		step_index += 1

	answer = f"{output} = {_format_number(float(result))}{_format_unit(unit)}"
	steps.append(f"{step_index}. Ответ: {answer}")

	return {
		"title": title,
		"formula_view": formula_view,
		"known_values": dict(known_values),
		"result": float(result),
		"answer": answer,
		"steps": steps,
		"text": "\n".join(steps),
	}


def _collect_console_values(context: Mapping[str, object]) -> list[tuple[str, float]]:
	excluded_names = {
		"input_text",
		"enum_formula",
		"option",
		"enum",
		"calcs",
		"sp",
		"ptbl",
		"self",
		"cls",
	}

	items: list[tuple[str, float]] = []
	for name, value in context.items():
		if name.startswith("_") or name in excluded_names:
			continue
		if isinstance(value, bool):
			continue
		if isinstance(value, Real):
			items.append((name, float(value)))

	return items


def print_console_solution(message: str, context: Mapping[str, object], *, heading: str = "Пошаговое решение:") -> bool:
	text = str(message).strip()
	if " = " not in text:
		return False
	if text.startswith(("Ошибка", "Невер", "Неизвест", "Нет ")):
		return False

	known_values = _collect_console_values(context)
	builtin_print(heading)

	step_index = 1
	if known_values:
		known_text = "; ".join(f"{name} = {_format_number(value)}" for name, value in known_values)
		builtin_print(f"{step_index}. Известные значения: {known_text}")
		step_index += 1

	builtin_print(f"{step_index}. Вычисляем: {text}")
	return True