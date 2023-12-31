import math


def cooling_delta_t(t_duration, k_constant, ambient, furnace_temp):
    delta = (ambient-furnace_temp)*math.e**(-1*k_constant*t_duration)
    return delta


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
        # debug output - REMOVE BEFORE FLIGHT:

        print("Iter:")
        print(ti)
        # 1. calculate cooling of furnace
        cur_f_temp = prev_ti['f_achieved_temp']
        ambient = ti['amb_temp']
        target_temp = ti['f_target_temp']
        payload_shc = env['f_settings']['payload_sp_heat_capacity']
        payload_mass = env['f_settings']['payload_kg']
        max_allowed_fuel =  env['f_settings']['fuel_max_feed_rate']
        fuel_calorific_value = env['f_settings']['fuel_calorific_value']

        cooling = cooling_delta_t(env['settings']['dt'], env['f_settings']['newton_cooling_con'], ambient, cur_f_temp)
        cooled_f_temp = cur_f_temp - abs(cooling)
        print(f'cooled from {cur_f_temp} by {cooling} to {cooled_f_temp}')
        # 2. required temp difference = target temp - cooled furnace temp
        temp_diff = target_temp - cooled_f_temp
        joules_required = temp_diff * payload_shc * payload_mass

        if temp_diff > 0:
            # 3. calculate fuel qty required to produce the temp diff required
            fuel_required_kg = joules_required / fuel_calorific_value
            temp_diff_achieved = temp_diff
            joules_achieved = joules_required
        # 4. clamp fuel qty with max & if required, recalculate temp diff achieved
            if fuel_required_kg > max_allowed_fuel:
                fuel_required_kg = max_allowed_fuel
                joules_achieved = fuel_required_kg * fuel_calorific_value
                temp_diff_achieved = joules_achieved / payload_shc / payload_mass
        else:
            temp_diff_achieved = 0
            joules_required = 0
            joules_achieved = 0
            fuel_required_kg = 0
            print(f"Cooling only. cooled_f_temp: {cooled_f_temp} + temp_diff_achieved: {temp_diff_achieved}")


        # 5. save calculation in TL
        ti['f_achieved_temp'] = cooled_f_temp + temp_diff_achieved
        ti['fuel_added'] = fuel_required_kg
        ti['temp_drop'] = cooling

        # debug output - REMOVE BEFORE FLIGHT:
        print(ti)
        print(f'temp_diff:{temp_diff}, joules_required:{joules_required}, joules_achieved:{joules_achieved},' 
              f' fuel_required_kg:{fuel_required_kg}')

        # Prepare for next iteration
        prev_ti = ti


    print("Simulation Run.")
    env['status'] = True

