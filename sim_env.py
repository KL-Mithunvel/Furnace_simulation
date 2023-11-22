import pprint as pp


def init_env():
    """
    Creates and returns environment dictionary. Initialized to default variables.
    :return: <dict> with keys var, settings, f_settings, program.
    """

    # dict for simulation variables.
    v = {
        'amb_Temp': {'default': 30, 'graph': True, 'disp_text': 'Ambient Temp (°C)'},
        'furnace_temp': {'default': 35, 'graph': True, 'disp_text': 'Furnace Temp (°C)'},
        'time': {'default': None, 'graph': False, 'disp_text': 'Time (s)'},
        'f_target_temp': dict(default=30, graph=True, disp_text='Furnace Target Temp (°C)'),
        'f_achieved_temp': dict(default=30, graph=True, disp_text='Furnace achieved Temp (°C)'),
        'fuel_added':dict(default=0, graph=True, disp_text='Fuel quantity'),
        'temp_drop':dict(default=0, graph=False, disp_text='Drop dew to Newton cooling')
    }

    # dict for simulation settings
    sim_s = {
        'dt': 1,
        'duration': 250
    }

    # dict for furnace settings
    furn_s = {
        'furnace_heatcap': 1,
        'furnace_mass': 2,
        'max_power_W': 1000,
        'max_feed_kgps': 100,
        'fuel_name': 'Electricity',
        'fuel_unit': 'w',
        'fuel_kj_per_unit': 5,
        'newton_cooling_con': 4,
        'max_fuel': 5,
        'pay_load_kg': 5,
        'shc_pay_load': 5
    }

    # list of all settings that are strings. Rest are all assumed to be float
    str_inp = ['fuel_name', 'fuel_unit']

    # Default 'Target Temp Program'
    p = [(0, v['furnace_temp']['default']),     # First step HAS to be (0, ambient)
         (20, 50),
         (40, 70),
         (60, 75),
         (80, 80),
         (100, 85),
         (120, 95),
         (140, 120),
         (160, 100),
         (200, 50),
         ]

    env = { "var": v, "settings": sim_s, "f_settings": furn_s, "program": p, "status": None,
            "str_inputs": str_inp}
    return env


def interpolate_ramp_t(l, r, t):
    """
    Given two ramp points (Left_time, Left_temp) -> (Right_time, Right_temp), calculates the
    linear interpolated value for the given point of time 't'
    :param l: tuple of (left_time, left_temp)
    :param r: tuple of (right_time, right_temp)
    :param t: time value for which target temp is to be interpolated
    :return: target_temp <float>
    """
    r = r if r else l       # if right value for ramp is not there, assume left continues.
    l_time = l[0]
    l_target = l[1]
    r_time = r[0]
    r_target = r[1]

    t_diff = t - l_time
    if r_time == t:
        return r_target
    if l_time == t:
        return l_target
    if l_time == r_time:
        return l_target
    rate = (r_target - l_target) / (r_time - l_time)
    t_target = l_target + rate * t_diff
    return t_target


def get_ramp_edges(p, t):
    """
    from a given ramp program, finds the ramp points which are applicable for a given time instance.
    :param p: ramp program
    :param t: time value for which to find ramp points
    :return: (left, right) values from the ramp program
    """
    # returns the left and right boundary steps for the given time
    # returns (l_step, r_step)
    l = p[0]
    r = None

    for i in p:
        if i[0] < t:
            l = i
        else:
            r = i
            break
    return l, r


def construct_timeline(e):
    """
    Constructs a timeline list that has 1 element for each instance of time of simulation. Each time instance is
    represented as a <dict> object.
    :param e: pass the environment dict to this function. Needed to read default variables, settings config
    :return: returns a dictionary
    """
    time_line = []
    i = 0
    dur = e["settings"]['duration']
    start_vars = {k: v['default'] for (k, v) in e["var"].items()}
    program = e["program"]
    sim_settings = e["settings"]
    while i <= dur:
        clone = start_vars.copy()
        clone['time'] = i
        left, right = get_ramp_edges(program, i)
        clone['f_target_temp'] = interpolate_ramp_t(left, right, i)
        time_line.append(clone)
        i += sim_settings['dt']
    return time_line


def new_env():
    e = init_env()
    e["tl"] = construct_timeline(e)
    return e
