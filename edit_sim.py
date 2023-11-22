
def sim_dirty(e):
    """
    Function that marks that the simulation timeline is 'dirty' and needs to
    be recalculated.
    :param e: pass the env dict
    """
    e['status'] = False


def get_dict_input(d, str_inputs, no_input=None):
    """
    Gets input from user for all keys in dict d.
    :param d: dictionary containing keys, values which need to be edited
    :param str_inputs: list containing names of variable/setting to treat as string. others are float
    :param no_input: Optional. list containing keys which need not be input, even though it is in dict
    """
    changed = False
    for setting, val in d.items():
        if no_input and setting not in no_input:
            prompt = f'{setting} [{val}]:'
            new_val = input(prompt)
            if len(new_val) != 0:
                if setting not in str_inputs:
                    new_val = float(new_val)
                d[setting] = new_val
                print("Value changed.")
                changed = True
    return changed


def edit_var(e):
    print(">>> Editing Starting Value for Variables...")
    no_inp = [x for x in e['var'].keys() if e['var'][x]['is_internal']]
    changed = get_dict_input(e['tl'][0], e["str_inputs"], no_inp)
    if changed:
        sim_dirty(e)


def edit_f_settings(e):
    print(">>> Editing Furnace Settings...")
    changed = get_dict_input(e['f_settings'], e["str_inputs"])
    if changed:
        sim_dirty(e)


def edit_sim_settings(e):
    print(">>> Editing Simulation Settings...")
    changed = get_dict_input(e['settings'], e["str_inputs"])
    if changed:
        sim_dirty(e)


def conf_out(e):
    pass


def print_all_settings(e):
    print(">>> Printing all settings...")
    print("\nFurnace Settings:\n")
    for setting, value in e['f_settings'].items():
        print(f'{setting}: {value}')
    print("\nSimulation Settings:\n")
    for setting, value in e['settings'].items():
        print(f'{setting}: {value}')
    print("\nVariables:\n")
    for setting, value in e['tl'][0].items():
        print(f'{setting}: {value}')
