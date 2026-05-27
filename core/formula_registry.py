from core.physic.electrodynamics.enum import FORMULAS as ELECTRO
from core.physic.mechanics.enum import FORMULAS as MECHANICS
from core.physic.optics.enum import FORMULAS as OPTICS
from core.physic.thermodynamics.enum import FORMULAS as THERMO
from core.chemistry.general.enum import FORMULAS as CHEMISTRY_GENERAL
from core.custom.formula_store import as_registry_map as CUSTOM

ALL_DATA = {
    "физика": {
        "электродинамика": ELECTRO,
        "механика": MECHANICS,
        "оптика": OPTICS,
        "термодинамика": THERMO,
    },
    "химия": {
        "общая химия": CHEMISTRY_GENERAL,
    },
    "свои формулы": {
        "кастомные формулы": CUSTOM,
    },
}