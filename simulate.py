import random


def run_sim(env):
    """
    Runs the simulation calculations
    :param env: Pass the environment dictionary
    :return: Nothing. Result of execution will be saved in the env
    """
    pass
    tl = env["tl"][1:]
    prev_ti = env["tl"][0]

    for ti in tl:   # iterate through each time instance in timeline
        # 1. calculate cooling of furnace
        # 2. required temp difference = target temp - cooled furnace temp
        # 3. calculate fuel qty required to produce the temp diff required
        fuel_required_kg = joules_required / fuel_calorific value
        # 4. clamp fuel qty with max & if required, recalculate temp diff achieved
        if fuel_required_kg > max_allowed_fuel:
            fuel_required_kg = max_allowed_fuel
            joules_achieved = fuel_required_kg * fuel_calorific_value
        else:
            joules_achieved = joules_required
            temp_diff_achieved = joules_achieved / material_specific_heat

        # 5. save calculation in TL
        r = (100 - (random.randrange(-10, 10)))/100
        ti['furnace_temp'] = ti['f_target_temp'] * r
        prev_ti = ti

    print("Simulation Run.")
    env['status'] = True

