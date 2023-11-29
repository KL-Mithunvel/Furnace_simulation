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
        # 4. clamp fuel qty with max & if required, recalculate temp diff achieved
        # 5. save calculation in TL
        r = (100 - (random.randrange(-10, 10)))/100
        ti['furnace_temp'] = ti['f_target_temp'] * r
        prev_ti = ti

    print("Simulation Run.")
    env['status'] = True

