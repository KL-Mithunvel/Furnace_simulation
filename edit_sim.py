import pickle
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

    no_input = no_input or []
    for setting, val in d.items():
        if setting not in no_input:
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
    for s,v in e['var'].items():
        prompt = f'Show Variable {s}? {"YES" if v["graph"] else "* NO *"}. Enter new value: [y/n]? '
        res = input(prompt)
        if len(res) != 0:
            v["graph"] = res.strip().lower() == 'y'

    selected = [x for x in e['var'].keys() if e['var'][x]['graph']]
    print("Selected Variables:")
    for i in selected:
        print(i)


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



def pic_dump(env):
    f=input('enter the file:')
    file_obj = open(f, 'wb')
    pickle.dump(env['furn_s'],file_obj)
    pickle.dump(env['settings'],file_obj)


def pic_load():
    f=input('enter the file:')
    file_obj = open(f, 'rb')
    x=pickle.load(file_obj)
    return x
