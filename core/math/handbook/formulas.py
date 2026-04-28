from __future__ import annotations

SECTIONS: dict[str, list[dict]] = {
    "Алгебра": [
        {
            "title": "Квадрат суммы",
            "formula": "y=(a+b)**2",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
            ],
        },
        {
            "title": "Квадрат разности",
            "formula": "y=(a-b)**2",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
            ],
        },
        {
            "title": "Разность квадратов",
            "formula": "y=(a+b)*(a-b)",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
            ],
        },
        {
            "title": "Сумма кубов",
            "formula": "y=a**3+b**3",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
            ],
        },
        {
            "title": "Разность кубов",
            "formula": "y=a**3-b**3",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
            ],
        },
        {
            "title": "Дискриминант",
            "formula": "D=b**2-4*a*c",
            "variables": [
                {"name": "D", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
                {"name": "c", "unit_symbol": ""},
            ],
        },
        {
            "title": "Теорема Виета: сумма корней",
            "formula": "S=-b/a",
            "variables": [
                {"name": "S", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
            ],
        },
        {
            "title": "Теорема Виета: произведение корней",
            "formula": "P=c/a",
            "variables": [
                {"name": "P", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "c", "unit_symbol": ""},
            ],
        },
        {
            "title": "Координата вершины параболы",
            "formula": "x0=-b/(2*a)",
            "variables": [
                {"name": "x0", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
            ],
        },
        {
            "title": "Ордината вершины параболы",
            "formula": "y0=(4*a*c-b**2)/(4*a)",
            "variables": [
                {"name": "y0", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
                {"name": "c", "unit_symbol": ""},
            ],
        },
        {
            "title": "Квадратное уравнение",
            "formula": "a*x**2+b*x+c=0",
            "variables": [
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
                {"name": "c", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Парабола",
            "formula": "y=a*x**2+b*x+c",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
                {"name": "c", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Логарифм",
            "formula": "y=log(b, a)",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "a", "unit_symbol": ""},
                {"name": "b", "unit_symbol": ""},
            ],
        },
        {
            "title": "Арифметическая прогрессия",
            "formula": "an=a1+(n-1)*d",
            "variables": [
                {"name": "an", "unit_symbol": ""},
                {"name": "a1", "unit_symbol": ""},
                {"name": "n", "unit_symbol": ""},
                {"name": "d", "unit_symbol": ""},
            ],
        },
        {
            "title": "Геометрическая прогрессия",
            "formula": "an=a1*q**(n-1)",
            "variables": [
                {"name": "an", "unit_symbol": ""},
                {"name": "a1", "unit_symbol": ""},
                {"name": "q", "unit_symbol": ""},
                {"name": "n", "unit_symbol": ""},
            ],
        },
        {
            "title": "Тригонометрия (прямоугольный треугольник)",
            "formula": "sinx=opp/hyp",
            "variables": [
                {"name": "sinx", "unit_symbol": ""},
                {"name": "opp", "unit_symbol": ""},
                {"name": "hyp", "unit_symbol": ""},
            ],
        },
        {
            "title": "Тригонометрические тождества",
            "formula": "sinx**2+cosx**2=1",
            "variables": [
                {"name": "sinx", "unit_symbol": ""},
                {"name": "cosx", "unit_symbol": ""},
            ],
        },
    ],
    "Прогрессии": [
        {
            "title": "Арифметическая прогрессия: n-й член",
            "formula": "an=a1+(n-1)*d",
            "variables": [
                {"name": "an", "unit_symbol": ""},
                {"name": "a1", "unit_symbol": ""},
                {"name": "n", "unit_symbol": ""},
                {"name": "d", "unit_symbol": ""},
            ],
        },
        {
            "title": "Арифметическая прогрессия: сумма n членов",
            "formula": "Sn=n*(2*a1+(n-1)*d)/2",
            "variables": [
                {"name": "Sn", "unit_symbol": ""},
                {"name": "n", "unit_symbol": ""},
                {"name": "a1", "unit_symbol": ""},
                {"name": "d", "unit_symbol": ""},
            ],
        },
        {
            "title": "Геометрическая прогрессия: n-й член",
            "formula": "an=a1*q**(n-1)",
            "variables": [
                {"name": "an", "unit_symbol": ""},
                {"name": "a1", "unit_symbol": ""},
                {"name": "q", "unit_symbol": ""},
                {"name": "n", "unit_symbol": ""},
            ],
        },
        {
            "title": "Геометрическая прогрессия: сумма n членов",
            "formula": "Sn=a1*(q**n-1)/(q-1)",
            "variables": [
                {"name": "Sn", "unit_symbol": ""},
                {"name": "a1", "unit_symbol": ""},
                {"name": "q", "unit_symbol": ""},
                {"name": "n", "unit_symbol": ""},
            ],
        },
        {
            "title": "Геометрическая прогрессия: бесконечная сумма",
            "formula": "Sinf=a1/(1-q)",
            "variables": [
                {"name": "Sinf", "unit_symbol": ""},
                {"name": "a1", "unit_symbol": ""},
                {"name": "q", "unit_symbol": ""},
            ],
        },
    ],
    "Тригонометрия": [
        {
            "title": "Пифагорово тождество",
            "formula": "sinx**2+cosx**2=1",
            "variables": [
                {"name": "sinx", "unit_symbol": ""},
                {"name": "cosx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Связь tan и cos",
            "formula": "1+tanx**2=1/cosx**2",
            "variables": [
                {"name": "tanx", "unit_symbol": ""},
                {"name": "cosx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Связь cot и sin",
            "formula": "1+cotx**2=1/sinx**2",
            "variables": [
                {"name": "cotx", "unit_symbol": ""},
                {"name": "sinx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Синус в прямоугольном треугольнике",
            "formula": "sinx=opp/hyp",
            "variables": [
                {"name": "sinx", "unit_symbol": ""},
                {"name": "opp", "unit_symbol": ""},
                {"name": "hyp", "unit_symbol": ""},
            ],
        },
        {
            "title": "Косинус в прямоугольном треугольнике",
            "formula": "cosx=adj/hyp",
            "variables": [
                {"name": "cosx", "unit_symbol": ""},
                {"name": "adj", "unit_symbol": ""},
                {"name": "hyp", "unit_symbol": ""},
            ],
        },
        {
            "title": "Тангенс в прямоугольном треугольнике",
            "formula": "tanx=opp/adj",
            "variables": [
                {"name": "tanx", "unit_symbol": ""},
                {"name": "opp", "unit_symbol": ""},
                {"name": "adj", "unit_symbol": ""},
            ],
        },
        {
            "title": "Котангенс в прямоугольном треугольнике",
            "formula": "cotx=adj/opp",
            "variables": [
                {"name": "cotx", "unit_symbol": ""},
                {"name": "adj", "unit_symbol": ""},
                {"name": "opp", "unit_symbol": ""},
            ],
        },
        {
            "title": "Синус двойного угла",
            "formula": "sin2x=2*sinx*cosx",
            "variables": [
                {"name": "sin2x", "unit_symbol": ""},
                {"name": "sinx", "unit_symbol": ""},
                {"name": "cosx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Косинус двойного угла",
            "formula": "cos2x=cosx**2-sinx**2",
            "variables": [
                {"name": "cos2x", "unit_symbol": ""},
                {"name": "sinx", "unit_symbol": ""},
                {"name": "cosx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Тангенс двойного угла",
            "formula": "tan2x=2*tanx/(1-tanx**2)",
            "variables": [
                {"name": "tan2x", "unit_symbol": ""},
                {"name": "tanx", "unit_symbol": ""},
            ],
        },
    ],
    "Планиметрия": [
        {
            "title": "Площадь треугольника (сторона и высота)",
            "formula": "S=a*h/2",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "h", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Формула Герона",
            "formula": "S=sqrt(p*(p-a)*(p-b)*(p-c))",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "p", "unit_symbol": "м"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "b", "unit_symbol": "м"},
                {"name": "c", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Полупериметр треугольника",
            "formula": "p=(a+b+c)/2",
            "variables": [
                {"name": "p", "unit_symbol": "м"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "b", "unit_symbol": "м"},
                {"name": "c", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Теорема Пифагора",
            "formula": "c**2=a**2+b**2",
            "variables": [
                {"name": "c", "unit_symbol": "м"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "b", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Теорема синусов",
            "formula": "a/sina=b/sinb",
            "variables": [
                {"name": "a", "unit_symbol": "м"},
                {"name": "sina", "unit_symbol": ""},
                {"name": "b", "unit_symbol": "м"},
                {"name": "sinb", "unit_symbol": ""},
            ],
        },
        {
            "title": "Теорема косинусов",
            "formula": "c**2=a**2+b**2-2*a*b*cosg",
            "variables": [
                {"name": "c", "unit_symbol": "м"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "b", "unit_symbol": "м"},
                {"name": "cosg", "unit_symbol": ""},
            ],
        },
        {
            "title": "Площадь трапеции",
            "formula": "S=(a+b)*h/2",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "b", "unit_symbol": "м"},
                {"name": "h", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Средняя линия трапеции",
            "formula": "m=(a+b)/2",
            "variables": [
                {"name": "m", "unit_symbol": "м"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "b", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Площадь параллелограмма",
            "formula": "S=a*h",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "h", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Площадь прямоугольника",
            "formula": "S=a*b",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "b", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Площадь квадрата по стороне",
            "formula": "S=a**2",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "a", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Площадь квадрата по диагонали",
            "formula": "S=d**2/2",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "d", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Площадь ромба по диагоналям",
            "formula": "S=d1*d2/2",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "d1", "unit_symbol": "м"},
                {"name": "d2", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Длина окружности",
            "formula": "L=2*pi*R",
            "variables": [
                {"name": "L", "unit_symbol": "м"},
                {"name": "R", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Площадь круга",
            "formula": "S=pi*R**2",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "R", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Длина дуги",
            "formula": "l=2*pi*R*alpha/360",
            "variables": [
                {"name": "l", "unit_symbol": "м"},
                {"name": "R", "unit_symbol": "м"},
                {"name": "alpha", "unit_symbol": "град"},
            ],
        },
        {
            "title": "Площадь сектора",
            "formula": "S=pi*R**2*alpha/360",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "R", "unit_symbol": "м"},
                {"name": "alpha", "unit_symbol": "град"},
            ],
        },
        {
            "title": "Площадь кольца",
            "formula": "S=pi*(R**2-r**2)",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "R", "unit_symbol": "м"},
                {"name": "r", "unit_symbol": "м"},
            ],
        },
    ],
    "Стереометрия": [
        {
            "title": "Главная диагональ куба",
            "formula": "d=a*sqrt(3)",
            "variables": [
                {"name": "d", "unit_symbol": "м"},
                {"name": "a", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Объём куба",
            "formula": "V=a**3",
            "variables": [
                {"name": "V", "unit_symbol": "м^3"},
                {"name": "a", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Объём прямоугольного параллелепипеда",
            "formula": "V=a*b*c",
            "variables": [
                {"name": "V", "unit_symbol": "м^3"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "b", "unit_symbol": "м"},
                {"name": "c", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Диагональ параллелепипеда",
            "formula": "d=sqrt(a**2+b**2+c**2)",
            "variables": [
                {"name": "d", "unit_symbol": "м"},
                {"name": "a", "unit_symbol": "м"},
                {"name": "b", "unit_symbol": "м"},
                {"name": "c", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Объём призмы",
            "formula": "V=S0*h",
            "variables": [
                {"name": "V", "unit_symbol": "м^3"},
                {"name": "S0", "unit_symbol": "м^2"},
                {"name": "h", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Боковая поверхность прямой призмы",
            "formula": "Sb=P*h",
            "variables": [
                {"name": "Sb", "unit_symbol": "м^2"},
                {"name": "P", "unit_symbol": "м"},
                {"name": "h", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Объём цилиндра",
            "formula": "V=pi*R**2*h",
            "variables": [
                {"name": "V", "unit_symbol": "м^3"},
                {"name": "R", "unit_symbol": "м"},
                {"name": "h", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Боковая поверхность цилиндра",
            "formula": "Sb=2*pi*R*h",
            "variables": [
                {"name": "Sb", "unit_symbol": "м^2"},
                {"name": "R", "unit_symbol": "м"},
                {"name": "h", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Объём пирамиды",
            "formula": "V=S0*h/3",
            "variables": [
                {"name": "V", "unit_symbol": "м^3"},
                {"name": "S0", "unit_symbol": "м^2"},
                {"name": "h", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Боковая поверхность правильной пирамиды",
            "formula": "Sb=P*l/2",
            "variables": [
                {"name": "Sb", "unit_symbol": "м^2"},
                {"name": "P", "unit_symbol": "м"},
                {"name": "l", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Объём конуса",
            "formula": "V=pi*R**2*h/3",
            "variables": [
                {"name": "V", "unit_symbol": "м^3"},
                {"name": "R", "unit_symbol": "м"},
                {"name": "h", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Боковая поверхность конуса",
            "formula": "Sb=pi*R*l",
            "variables": [
                {"name": "Sb", "unit_symbol": "м^2"},
                {"name": "R", "unit_symbol": "м"},
                {"name": "l", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Образующая конуса",
            "formula": "l=sqrt(R**2+h**2)",
            "variables": [
                {"name": "l", "unit_symbol": "м"},
                {"name": "R", "unit_symbol": "м"},
                {"name": "h", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Объём шара",
            "formula": "V=4*pi*R**3/3",
            "variables": [
                {"name": "V", "unit_symbol": "м^3"},
                {"name": "R", "unit_symbol": "м"},
            ],
        },
        {
            "title": "Площадь сферы",
            "formula": "S=4*pi*R**2",
            "variables": [
                {"name": "S", "unit_symbol": "м^2"},
                {"name": "R", "unit_symbol": "м"},
            ],
        },
    ],
    "Координаты": [
        {
            "title": "Расстояние на оси",
            "formula": "d=abs(x2-x1)",
            "variables": [
                {"name": "d", "unit_symbol": ""},
                {"name": "x1", "unit_symbol": ""},
                {"name": "x2", "unit_symbol": ""},
            ],
        },
        {
            "title": "Расстояние на плоскости",
            "formula": "d=sqrt((x2-x1)**2+(y2-y1)**2)",
            "variables": [
                {"name": "d", "unit_symbol": ""},
                {"name": "x1", "unit_symbol": ""},
                {"name": "y1", "unit_symbol": ""},
                {"name": "x2", "unit_symbol": ""},
                {"name": "y2", "unit_symbol": ""},
            ],
        },
        {
            "title": "Расстояние в пространстве",
            "formula": "d=sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)",
            "variables": [
                {"name": "d", "unit_symbol": ""},
                {"name": "x1", "unit_symbol": ""},
                {"name": "y1", "unit_symbol": ""},
                {"name": "z1", "unit_symbol": ""},
                {"name": "x2", "unit_symbol": ""},
                {"name": "y2", "unit_symbol": ""},
                {"name": "z2", "unit_symbol": ""},
            ],
        },
        {
            "title": "Координата середины отрезка (x)",
            "formula": "xm=(x1+x2)/2",
            "variables": [
                {"name": "xm", "unit_symbol": ""},
                {"name": "x1", "unit_symbol": ""},
                {"name": "x2", "unit_symbol": ""},
            ],
        },
        {
            "title": "Координата середины отрезка (y)",
            "formula": "ym=(y1+y2)/2",
            "variables": [
                {"name": "ym", "unit_symbol": ""},
                {"name": "y1", "unit_symbol": ""},
                {"name": "y2", "unit_symbol": ""},
            ],
        },
        {
            "title": "Координата середины отрезка (z)",
            "formula": "zm=(z1+z2)/2",
            "variables": [
                {"name": "zm", "unit_symbol": ""},
                {"name": "z1", "unit_symbol": ""},
                {"name": "z2", "unit_symbol": ""},
            ],
        },
    ],
    "Математический анализ": [
        {
            "title": "Первый замечательный предел",
            "formula": "sinx/x=1",
            "variables": [
                {"name": "sinx", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Второй замечательный предел",
            "formula": "(1-cosx)/x**2=1/2",
            "variables": [
                {"name": "cosx", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Логарифмический предел",
            "formula": "log(1+x)/x=1",
            "variables": [
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Предел экспоненты",
            "formula": "(exp(x)-1)/x=1",
            "variables": [
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Предел арктангенса",
            "formula": "arctanx/x=1",
            "variables": [
                {"name": "arctanx", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Предел арксинуса",
            "formula": "arcsinx/x=1",
            "variables": [
                {"name": "arcsinx", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная степени",
            "formula": "dy_dx=n*x**(n-1)",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "n", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная экспоненты",
            "formula": "dy_dx=exp(x)",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная логарифма",
            "formula": "dy_dx=1/x",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная синуса",
            "formula": "dy_dx=cosx",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "cosx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная косинуса",
            "formula": "dy_dx=-sinx",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "sinx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная тангенса",
            "formula": "dy_dx=1/cosx**2",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "cosx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная котангенса",
            "formula": "dy_dx=-1/sinx**2",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "sinx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная арксинуса",
            "formula": "dy_dx=1/sqrt(1-x**2)",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная арккосинуса",
            "formula": "dy_dx=-1/sqrt(1-x**2)",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная арктангенса",
            "formula": "dy_dx=1/(1+x**2)",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Производная арккотангенса",
            "formula": "dy_dx=-1/(1+x**2)",
            "variables": [
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Дифференциал",
            "formula": "dy=dy_dx*dx",
            "variables": [
                {"name": "dy", "unit_symbol": ""},
                {"name": "dy_dx", "unit_symbol": ""},
                {"name": "dx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Неопределенный интеграл степени",
            "formula": "F=x**(n+1)/(n+1)",
            "variables": [
                {"name": "F", "unit_symbol": ""},
                {"name": "n", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Неопределенный интеграл экспоненты",
            "formula": "F=exp(x)",
            "variables": [
                {"name": "F", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Неопределенный интеграл синуса",
            "formula": "F=-cosx",
            "variables": [
                {"name": "F", "unit_symbol": ""},
                {"name": "cosx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Неопределенный интеграл косинуса",
            "formula": "F=sinx",
            "variables": [
                {"name": "F", "unit_symbol": ""},
                {"name": "sinx", "unit_symbol": ""},
            ],
        },
        {
            "title": "Неопределенный интеграл 1/x",
            "formula": "F=log(x)",
            "variables": [
                {"name": "F", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Ряд Маклорена для экспоненты",
            "formula": "y=1+x+x**2/2+x**3/6+x**4/24",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Ряд Маклорена для синуса",
            "formula": "y=x-x**3/6+x**5/120",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Ряд Маклорена для косинуса",
            "formula": "y=1-x**2/2+x**4/24",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Ряд Маклорена для логарифма",
            "formula": "y=x-x**2/2+x**3/3-x**4/4",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
        {
            "title": "Ряд Маклорена для 1/(1-x)",
            "formula": "y=1+x+x**2+x**3+x**4",
            "variables": [
                {"name": "y", "unit_symbol": ""},
                {"name": "x", "unit_symbol": ""},
            ],
        },
    ],
}
