from core.physics.electrodynamics import calculations as electro_calcs
from core.physics.mechanics import calculations as mech_calcs
from core.physics.optics import calculations as optic_calcs
from core.physics.thermodynamics import calculations as thermo_calcs

CALCULATION_MODULES = {
    "физика": {
        "электродинамика": electro_calcs,
        "механика": mech_calcs,
        "оптика": optic_calcs,
        "термодинамика": thermo_calcs,
    }}