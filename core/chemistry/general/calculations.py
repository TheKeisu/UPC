from __future__ import annotations

import math

import chemparse
import periodictable as pt


GAS_CONSTANT_R = 8.314462618
AVOGADRO_NUMBER = 6.02214076e23
MOLAR_VOLUME_NORMAL = 22.4
FARADAY_CONSTANT = 96500
PLANCK_CONSTANT = 6.62607015e-34


def _molar_mass_from_formula(formula: str) -> float:
    parsed_formula = chemparse.parse_formula(formula)
    if not parsed_formula:
        raise ValueError("Не удалось распознать химическую формулу")

    total_mass = 0.0
    for symbol, count in parsed_formula.items():
        element = getattr(pt, symbol, None)
        if element is None:
            raise ValueError(f"Неизвестный элемент в формуле: {symbol}")

        mass = getattr(element, "mass", None)
        if mass is None:
            raise ValueError(f"Не удалось получить атомную массу элемента: {symbol}")

        total_mass += float(mass) * float(count)

    return total_mass


def calc_substance_amount(mass: float, molar_mass: float) -> float:
    return mass / molar_mass


def calc_mass_substance_amount(substance_amount: float, molar_mass: float) -> float:
    return substance_amount * molar_mass


def calc_molar_mass(mass: float, substance_amount: float) -> float:
    return mass / substance_amount


def calc_particles_count(substance_amount: float) -> float:
    return substance_amount * AVOGADRO_NUMBER


def calc_substance_amount_particles_count(particles_count: float) -> float:
    return particles_count / AVOGADRO_NUMBER


def calc_avogadro_number(particles_count: float, substance_amount: float) -> float:
    return particles_count / substance_amount


def calc_substance_amount_by_formula(mass: float, formula: str) -> float:
    molar_mass = _molar_mass_from_formula(formula)
    return mass / molar_mass


def calc_molar_mass_by_formula(formula: str) -> float:
    return _molar_mass_from_formula(formula)


def calc_ideal_gas_pressure(substance_amount: float, temperature: float, volume: float) -> float:
    return (substance_amount * GAS_CONSTANT_R * temperature) / volume


def calc_ideal_gas_volume(substance_amount: float, temperature: float, pressure: float) -> float:
    return (substance_amount * GAS_CONSTANT_R * temperature) / pressure


def calc_ideal_gas_substance_amount(pressure: float, volume: float, temperature: float) -> float:
    return (pressure * volume) / (GAS_CONSTANT_R * temperature)


def calc_ideal_gas_temperature(pressure: float, volume: float, substance_amount: float) -> float:
    return (pressure * volume) / (GAS_CONSTANT_R * substance_amount)


def calc_gas_volume_by_substance(substance_amount: float) -> float:
    return substance_amount * MOLAR_VOLUME_NORMAL


def calc_substance_amount_gas_volume(volume: float) -> float:
    return volume / MOLAR_VOLUME_NORMAL


def calc_molar_volume(volume: float, substance_amount: float) -> float:
    return volume / substance_amount


def calc_gas_density(molar_mass: float, molar_volume: float) -> float:
    return molar_mass / molar_volume


def calc_molar_mass_gas_density(gas_density: float, molar_volume: float) -> float:
    return gas_density * molar_volume


def calc_mass_fraction(substance_mass: float, solution_mass: float) -> float:
    return substance_mass / solution_mass


def calc_substance_mass_mass_fraction(mass_fraction: float, solution_mass: float) -> float:
    return mass_fraction * solution_mass


def calc_solution_mass_mass_fraction(substance_mass: float, mass_fraction: float) -> float:
    return substance_mass / mass_fraction


def calc_molar_concentration(substance_amount: float, volume: float) -> float:
    return substance_amount / volume


def calc_substance_amount_molar_concentration(concentration: float, volume: float) -> float:
    return concentration * volume


def calc_volume_molar_concentration(substance_amount: float, concentration: float) -> float:
    return substance_amount / concentration


def calc_solution_mass(substance_mass: float, solvent_mass: float) -> float:
    return substance_mass + solvent_mass


def calc_substance_mass_solution_mass(solution_mass: float, solvent_mass: float) -> float:
    return solution_mass - solvent_mass


def calc_solvent_mass_solution_mass(solution_mass: float, substance_mass: float) -> float:
    return solution_mass - substance_mass


def calc_mass_conservation(reactants_mass: float) -> float:
    return reactants_mass


def calc_reactants_mass_conservation(products_mass: float) -> float:
    return products_mass


def calc_reaction_yield(practical_mass: float, theoretical_mass: float) -> float:
    return (practical_mass / theoretical_mass) * 100


def calc_practical_mass_reaction_yield(reaction_yield: float, theoretical_mass: float) -> float:
    return (reaction_yield / 100) * theoretical_mass


def calc_theoretical_mass_reaction_yield(practical_mass: float, reaction_yield: float) -> float:
    return practical_mass / (reaction_yield / 100)


def calc_heat_amount(heat_capacity: float, mass: float, delta_temperature: float) -> float:
    return heat_capacity * mass * delta_temperature


def calc_heat_capacity_heat_amount(heat_amount: float, mass: float, delta_temperature: float) -> float:
    return heat_amount / (mass * delta_temperature)


def calc_reaction_heat_effect(substance_amount: float, enthalpy_change: float) -> float:
    return substance_amount * enthalpy_change


def calc_substance_amount_reaction_heat_effect(heat_amount: float, enthalpy_change: float) -> float:
    return heat_amount / enthalpy_change


def calc_faraday_law(molar_mass: float, current: float, time: float, electrons_count: float) -> float:
    return (molar_mass * current * time) / (electrons_count * FARADAY_CONSTANT)


def calc_current_faraday_law(deposited_mass: float, molar_mass: float, time: float, electrons_count: float) -> float:
    return (deposited_mass * electrons_count * FARADAY_CONSTANT) / (molar_mass * time)


def calc_time_faraday_law(deposited_mass: float, molar_mass: float, current: float, electrons_count: float) -> float:
    return (deposited_mass * electrons_count * FARADAY_CONSTANT) / (molar_mass * current)


def calc_equilibrium_constant(products_concentration: float, reactants_concentration: float) -> float:
    return products_concentration / reactants_concentration


def calc_equilibrium_constant_with_coefficients(
    products_concentration: float,
    products_coefficient: float,
    reactants_concentration: float,
    reactants_coefficient: float,
) -> float:
    return (products_concentration ** products_coefficient) / (
        reactants_concentration ** reactants_coefficient
    )


def calc_reaction_rate(delta_concentration: float, delta_time: float) -> float:
    return delta_concentration / delta_time


def calc_delta_concentration_reaction_rate(rate: float, delta_time: float) -> float:
    return rate * delta_time


def calc_rate_constant_reaction_rate(
    rate: float,
    concentration_a: float,
    order_a: float,
    concentration_b: float,
    order_b: float,
) -> float:
    return rate / ((concentration_a ** order_a) * (concentration_b ** order_b))


def calc_reaction_rate_law(
    rate_constant: float,
    concentration_a: float,
    order_a: float,
    concentration_b: float,
    order_b: float,
) -> float:
    return rate_constant * (concentration_a ** order_a) * (concentration_b ** order_b)


def calc_ph(hydrogen_ion_concentration: float) -> float:
    return -math.log10(hydrogen_ion_concentration)


def calc_poh(hydroxide_ion_concentration: float) -> float:
    return -math.log10(hydroxide_ion_concentration)


def calc_hydrogen_ion_concentration(ph: float) -> float:
    return 10 ** (-ph)


def calc_hydroxide_ion_concentration(poh: float) -> float:
    return 10 ** (-poh)


def calc_poh_from_ph(ph: float) -> float:
    return 14 - ph


def calc_ph_from_poh(poh: float) -> float:
    return 14 - poh


def calc_freezing_point_depression(cryoscopic_constant: float, molality: float) -> float:
    return cryoscopic_constant * molality


def calc_cryoscopic_constant(freezing_point_depression: float, molality: float) -> float:
    return freezing_point_depression / molality


def calc_boiling_point_elevation(ebullioscopic_constant: float, molality: float) -> float:
    return ebullioscopic_constant * molality


def calc_ebullioscopic_constant(boiling_point_elevation: float, molality: float) -> float:
    return boiling_point_elevation / molality


def calc_photon_energy(frequency: float) -> float:
    return PLANCK_CONSTANT * frequency


def calc_frequency_photon_energy(energy: float) -> float:
    return energy / PLANCK_CONSTANT
