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
DISCRIMINANT = 8
VIETA_SUM = 9
VIETA_PRODUCT = 10
PARABOLA_VERTEX_X = 11
PARABOLA_VERTEX_Y = 12
SQUARE_EQUATION = 13
PARABOLA = 14
LOGARITHM = 15
ARITHMETIC_PROGRESSION = 16
GEOMETRIC_PROGRESSION = 17
TRIGONOMETRY = 18
TRIGONOMETRICAL_IDENTITIES = 19
HANDBOOK_FORMULAS = 20

ALGEBRA_FORMULAS = {
	SQUARE_SUM: "(a + b)^2",
	SQUARE_DIFF: "(a - b)^2",
	DIFF_OF_SQUARES: "(a + b)(a - b)",
	CUBE_SUM: "(a + b)^3",
	CUBE_DIFF: "(a - b)^3",
	SUM_OF_CUBES: "a^3 + b^3",
	DIFF_OF_CUBES: "a^3 - b^3",
	DISCRIMINANT: "D = b^2 - 4ac",
	VIETA_SUM: "Sum of roots: x1 + x2 = -b/a",
	VIETA_PRODUCT: "Product of roots: x1 * x2 = c/a",
	PARABOLA_VERTEX_X: "Vertex x-coordinate: x0 = -b/(2a)",
	PARABOLA_VERTEX_Y: "Vertex y-coordinate: y0 = (4ac - b^2)/(4a)",
	SQUARE_EQUATION: "ax^2 +- 2bx +- с  = 0",
	PARABOLA: "y = ax^2 + bx + c",
    LOGARITHM: "log_a(b)",
    ARITHMETIC_PROGRESSION: "a_n = a_1 + (n - 1)d",
    GEOMETRIC_PROGRESSION: "a_n = a_1 * r^(n - 1)",
    TRIGONOMETRY: "sin(x), cos(x), tan(x)",
	TRIGONOMETRICAL_IDENTITIES: "sin^2(x) + cos^2(x) = 1",
	HANDBOOK_FORMULAS: "Все формулы из справочника"
}


COMMON_MENU = """Выберите действие
						 "Раскрыть формулу - 1"
						 "Вычислить по значениям a и b - 2": """

GRAPH_MENU = """Выберите действие
						 "Построить график - 1"
						 "Найти вершины - 3" """


SQUARE_EQUATION_MENU = """Выберите действие
						 "Решить квадратное уравнение - 1" """

LOGARITHM_MENU = """Выберите действие
						 "Вычислить логарифм - 1"
                         "Логарифм произведения - 2"
                         "Логарифм дроби - 3" """

ARITHMETIC_PROGRESSION_MENU = """Выберите действие
						 "Найти n-й член прогрессии - 1"
						 "Найти сумму n членов прогрессии - 2"
                         "Найти разность прогрессии - 3" 
                         "Найти первый член прогрессии - 4" """

GEOMETRIC_PROGRESSION_MENU = """Выберите действие
						 "Найти n-й член прогрессии - 1"
						 "Найти сумму n членов прогрессии - 2"
                         "Найти знаменатель прогрессии - 3"
                         "Найти первый член прогрессии - 4" 
                         "Найти сумму бесконечно-убывающей прогрессии - 5" """

TRIGONOMETRY_MENU = """Выберите действие (прямоугольный треугольник)
						 "Определение синуса - 1"
                         "Определение косинуса - 2"
                         "Определение тангенса - 3"
                         "Определение котангенса - 4" """

TRIGONOMETRICAL_IDENTITIES_MENU = """Выберите действие
						 "Найти sin(x) по cos(x) (sin^2(x) + cos^2(x) = 1) - 1"
						 "Найти cos(x) по sin(x) (sin^2(x) + cos^2(x) = 1) - 2"
						 "Найти tan(x) по cos(x) (1 + tan^2(x) = 1/cos^2(x)) - 3"
						 "Найти cot(x) по sin(x) (1 + cot^2(x) = 1/sin^2(x)) - 4" """

HANDBOOK_MENU = """Выберите действие
						 "Открыть справочник и решить формулу - 1" """

ALGEBRA_MENUS = {
	HANDBOOK_FORMULAS: HANDBOOK_MENU,
}