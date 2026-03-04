from core.physics.electrodynamics.enum import FORMULAS as ELECTRO
from core.physics.mechanics.enum import FORMULAS as MECHANICS
from core.physics.optics.enum import FORMULAS as OPTICS
from core.physics.thermodynamics.enum import FORMULAS as THERMO
from core.custom.formula_store import as_registry_map as CUSTOM

ALL_DATA = {
    "физика": {
        "электродинамика": ELECTRO,
        "механика": MECHANICS,
        "оптика": OPTICS,
        "термодинамика": THERMO,
    },
    "пользовательские формулы": {
        "кастомные формулы": CUSTOM
     }
}