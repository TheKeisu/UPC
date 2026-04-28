from __future__ import annotations

import math

import periodictable as pt


RUSSIAN_NAMES_BY_SYMBOL: dict[str, str] = {
	"H": "Водород",
	"He": "Гелий",
	"Li": "Литий",
	"Be": "Бериллий",
	"B": "Бор",
	"C": "Углерод",
	"N": "Азот",
	"O": "Кислород",
	"F": "Фтор",
	"Ne": "Неон",
	"Na": "Натрий",
	"Mg": "Магний",
	"Al": "Алюминий",
	"Si": "Кремний",
	"P": "Фосфор",
	"S": "Сера",
	"Cl": "Хлор",
	"Ar": "Аргон",
	"K": "Калий",
	"Ca": "Кальций",
	"Sc": "Скандий",
	"Ti": "Титан",
	"V": "Ванадий",
	"Cr": "Хром",
	"Mn": "Марганец",
	"Fe": "Железо",
	"Co": "Кобальт",
	"Ni": "Никель",
	"Cu": "Медь",
	"Zn": "Цинк",
	"Ga": "Галлий",
	"Ge": "Германий",
	"As": "Мышьяк",
	"Se": "Селен",
	"Br": "Бром",
	"Kr": "Криптон",
	"Rb": "Рубидий",
	"Sr": "Стронций",
	"Y": "Иттрий",
	"Zr": "Цирконий",
	"Nb": "Ниобий",
	"Mo": "Молибден",
	"Tc": "Технеций",
	"Ru": "Рутений",
	"Rh": "Родий",
	"Pd": "Палладий",
	"Ag": "Серебро",
	"Cd": "Кадмий",
	"In": "Индий",
	"Sn": "Олово",
	"Sb": "Сурьма",
	"Te": "Теллур",
	"I": "Иод",
	"Xe": "Ксенон",
	"Cs": "Цезий",
	"Ba": "Барий",
	"La": "Лантан",
	"Ce": "Церий",
	"Pr": "Празеодим",
	"Nd": "Неодим",
	"Pm": "Прометий",
	"Sm": "Самарий",
	"Eu": "Европий",
	"Gd": "Гадолиний",
	"Tb": "Тербий",
	"Dy": "Диспрозий",
	"Ho": "Гольмий",
	"Er": "Эрбий",
	"Tm": "Тулий",
	"Yb": "Иттербий",
	"Lu": "Лютеций",
	"Hf": "Гафний",
	"Ta": "Тантал",
	"W": "Вольфрам",
	"Re": "Рений",
	"Os": "Осмий",
	"Ir": "Иридий",
	"Pt": "Платина",
	"Au": "Золото",
	"Hg": "Ртуть",
	"Tl": "Таллий",
	"Pb": "Свинец",
	"Bi": "Висмут",
	"Po": "Полоний",
	"At": "Астат",
	"Rn": "Радон",
	"Fr": "Франций",
	"Ra": "Радий",
	"Ac": "Актиний",
	"Th": "Торий",
	"Pa": "Протактиний",
	"U": "Уран",
	"Np": "Нептуний",
	"Pu": "Плутоний",
	"Am": "Америций",
	"Cm": "Кюрий",
	"Bk": "Берклий",
	"Cf": "Калифорний",
	"Es": "Эйнштейний",
	"Fm": "Фермий",
	"Md": "Менделевий",
	"No": "Нобелий",
	"Lr": "Лоуренсий",
	"Rf": "Резерфордий",
	"Db": "Дубний",
	"Sg": "Сиборгий",
	"Bh": "Борий",
	"Hs": "Хассий",
	"Mt": "Мейтнерий",
	"Ds": "Дармштадтий",
	"Rg": "Рентгений",
	"Cn": "Коперниций",
	"Nh": "Нихоний",
	"Fl": "Флеровий",
	"Mc": "Московий",
	"Lv": "Ливерморий",
	"Ts": "Теннессин",
	"Og": "Оганесон",
}


ELEMENTS = [element for element in pt.elements]
ELEMENTS_BY_NUMBER = {element.number: element for element in ELEMENTS}
ELEMENTS_BY_SYMBOL = {element.symbol: element for element in ELEMENTS}
ELEMENTS_BY_ENGLISH_NAME = {element.name.lower(): element for element in ELEMENTS}
RUSSIAN_TO_SYMBOL = {
	name.lower(): symbol for symbol, name in RUSSIAN_NAMES_BY_SYMBOL.items()
}


MAIN_TABLE_LAYOUT: dict[int, list[int | None]] = {
	1: [1] + [None] * 16 + [2],
	2: [3, 4] + [None] * 10 + [5, 6, 7, 8, 9, 10],
	3: [11, 12] + [None] * 10 + [13, 14, 15, 16, 17, 18],
	4: [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
	5: [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
	6: [55, 56, 57, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86],
	7: [87, 88, 89, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
}


def _period_by_number(number: int) -> int:
	if number <= 2:
		return 1
	if number <= 10:
		return 2
	if number <= 18:
		return 3
	if number <= 36:
		return 4
	if number <= 54:
		return 5
	if number <= 86:
		return 6
	return 7


def _group_by_number(number: int) -> int | str:
	for period, row in MAIN_TABLE_LAYOUT.items():
		if number not in row:
			continue
		position = row.index(number) + 1
		return position

	if 57 <= number <= 71:
		return "Ln"
	if 89 <= number <= 103:
		return "An"
	return "—"


def _block_by_number(number: int) -> str:
	if 57 <= number <= 71 or 89 <= number <= 103:
		return "f"
	if number in {1, 2, 3, 4, 11, 12, 19, 20, 37, 38, 55, 56, 87, 88}:
		return "s"
	if number in {
		21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
		39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
		72, 73, 74, 75, 76, 77, 78, 79, 80,
		104, 105, 106, 107, 108, 109, 110, 111, 112,
	}:
		return "d"
	return "p"


def _format_mass(value: object) -> str:
	if value is None:
		return "—"

	try:
		mass = float(value)
	except (TypeError, ValueError):
		return str(value)

	if math.isnan(mass):
		return "—"
	return f"{mass:.3f}".rstrip("0").rstrip(".")


def _normalize_symbol(query: str) -> str:
	query = query.strip()
	if not query:
		return query
	if len(query) == 1:
		return query.upper()
	return query[0].upper() + query[1:].lower()


def _find_element(query: str):
	text = query.strip()
	if not text:
		return None

	if text.isdigit():
		return ELEMENTS_BY_NUMBER.get(int(text))

	normalized_symbol = _normalize_symbol(text)
	element = ELEMENTS_BY_SYMBOL.get(normalized_symbol)
	if element is not None:
		return element

	element = ELEMENTS_BY_ENGLISH_NAME.get(text.lower())
	if element is not None:
		return element

	symbol = RUSSIAN_TO_SYMBOL.get(text.lower())
	if symbol is not None:
		return ELEMENTS_BY_SYMBOL.get(symbol)

	return None


def _build_card(element) -> str:
	russian_name = RUSSIAN_NAMES_BY_SYMBOL.get(element.symbol, element.name.title())
	mass = _format_mass(getattr(element, "mass", None))
	return f"{element.number:>3} {element.symbol:<2} {russian_name:<13} {mass:>8}"


def print_periodic_table() -> None:
	print("Таблица Менделеева на русском языке")
	print("=" * 40)
	print("Основная таблица")

	for period in range(1, 8):
		row_numbers = MAIN_TABLE_LAYOUT[period]
		cards = []
		for number in row_numbers:
			if number is None:
				cards.append(" " * 28)
				continue
			cards.append(_build_card(ELEMENTS_BY_NUMBER[number]))
		print(f"Период {period}: " + " | ".join(cards))

	print()
	print("Лантаноиды:")
	print(" | ".join(_build_card(ELEMENTS_BY_NUMBER[number]) for number in range(57, 72)))

	print()
	print("Актиноиды:")
	print(" | ".join(_build_card(ELEMENTS_BY_NUMBER[number]) for number in range(89, 104)))


def print_element_info(query: str) -> None:
	element = _find_element(query)
	if element is None:
		print("Элемент не найден")
		return

	russian_name = RUSSIAN_NAMES_BY_SYMBOL.get(element.symbol, element.name.title())
	print("Подробная карточка элемента")
	print("-" * 30)
	print(f"Атомный номер: {element.number}")
	print(f"Символ: {element.symbol}")
	print(f"Название: {russian_name}")
	print(f"Английское название: {element.name}")
	print(f"Период: {_period_by_number(element.number)}")
	print(f"Группа: {_group_by_number(element.number)}")
	print(f"Блок: {_block_by_number(element.number)}")
	print(f"Относительная атомная масса: {_format_mass(getattr(element, 'mass', None))}")


def run_console_chemistry() -> None:
	action = input(
		"Химия: (Показать таблицу - 1; Найти элемент - 2;)"
	).strip()

	if action == "1":
		print_periodic_table()
		return

	if action == "2":
		query = input("Введите номер, символ или название элемента: ").strip()
		print_element_info(query)
		return

	print("Неизвестное действие")
