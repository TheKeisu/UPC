import sections.enum as enum
import mechanics.main as mech
import mechanics.enum as mech_enum
import thermodynamics.main as therm
import thermodynamics.enum as therm_enum
import electrodynamics.main as electro
import electrodynamics.enum as electro_enum
import optics.main as optic
import optics.enum as optic_enum

def section_selection(input_text, enum_section):
    option = int(input(input_text))

    match enum_section:
        case enum.MECHANICS:
             mech.formula_selection(mech_enum.mechanics[option], option)
        case enum.MP_N_THERMODYNAMICS:
            therm.formula_selection(therm_enum.mp_n_thermodynamics[option], option)
        case enum.ELECTRODYNAMICS:
            electro.formula_selection(electro_enum.electrostatic_n_electrodynamics[option], option)
        case enum.OPTICS:
            optic.formula_selection(optic_enum.optics[option], option)


