def init_sim():
    v = {
        'amb_Temp': 30,
        'furnace_temp': 35,
        'time': 0,
        "furnace_target_temp": 0
    }

    sim_s = {
        'dt': 1,
        'duration': 25

    }

    furn_s = {
        'furnace_heatcap': 1,
        'furnace_mass': 2,
        'max_power_W': 1000,
        'max_feed_kgps':100,

        }
    p = [(0,v['furnace_temp']),
         (2,50),
         (4,70),
         (6,30),
         (8,30),
         (10,0),
         (12,80),
         (14,80),
         (16,100),
         (20,500),]
    return v, sim_s, furn_s, p


def print_all_var(v):
    for i in v.keys():
        print(i, ' = ', v[i])


def construct_timeline(start_vars, sim_settings):
    time_line = []
    i = 0
    while i <= sim_settings['duration']:
        clone = start_vars.copy()
        clone['time'] = i
        left, right = get_ramp_edges(program, i)
        clone['furnace_target_temp'] = t_ramp(left, right, i)
        time_line.append(clone)
        i += sim_settings['dt']
    return time_line


def t_ramp(l, r, t):
    r = r if r else l
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


variables, settings, furnace_settings, program = init_sim()
tl = construct_timeline(variables, settings)
for i in tl:
    print("furnace_target_temp", ' = ', i["furnace_target_temp"], ' ,', 'time', ' = ', i['time'])

