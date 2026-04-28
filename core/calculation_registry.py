from core.physic.electrodynamics import calculations as electro_calcs
from core.chemistry.general import calculations as chemistry_general_calcs
# from core.physic.mechanics import calculations as mech_calcs
# from core.physic.optics import calculations as optic_calcs
# from core.physic.thermodynamics import calculations as thermo_calcs

CALCULATION_MODULES = {
    "физика": {
        "электродинамика": electro_calcs,
        # "mechanics": mech_calcs,
        # "optics": optic_calcs,
        # "thermodynamics": thermo_calcs,
    },
    "химия": {
        "общая химия": chemistry_general_calcs,
    },
}