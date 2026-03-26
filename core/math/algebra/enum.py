#########
# АЛГЕБРА
#########

SQUARE_SUM = 1
SQUARE_DIFF = 2
DIFF_OF_SQUARES = 3
CUBE_SUM = 4
CUBE_DIFF = 5
SUM_OF_CUBES = 6
DIFF_OF_CUBES = 7

smf_formulas = {
	SQUARE_SUM: "(a + b)^2",
	SQUARE_DIFF: "(a - b)^2",
	DIFF_OF_SQUARES: "(a + b)(a - b)",
	CUBE_SUM: "(a + b)^3",
	CUBE_DIFF: "(a - b)^3",
	SUM_OF_CUBES: "a^3 + b^3",
	DIFF_OF_CUBES: "a^3 - b^3",
}

COMMON_MENU = """Выберите действие
						 "Раскрыть формулу - 1"
						 "Вычислить по значениям a и b - 2": """

algebra = {
	SQUARE_SUM: COMMON_MENU,
	SQUARE_DIFF: COMMON_MENU,
	DIFF_OF_SQUARES: COMMON_MENU,
	CUBE_SUM: COMMON_MENU,
	CUBE_DIFF: COMMON_MENU,
	SUM_OF_CUBES: COMMON_MENU,
	DIFF_OF_CUBES: COMMON_MENU,
}