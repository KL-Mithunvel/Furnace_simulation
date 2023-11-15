def init_sim():
    v = {
        'amb_Temp': 30,
        'furnace_Temp': 35,
        'time': 0
    }

    sim_s = {
        'dt': 2,
        'duration': 15
    }

    furn_s = {
        'furnace_heatcap': 1,
        'furnace_mass': 2,
        'max_power_W': 1000,
        'max_feed_kgps':100,

        }
    p = [(0,v['furnace_Temp']),
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
        time_line.append(clone)
        i += sim_settings['dt']
    return time_line


def t_ramp(l, r, t):
    l_time = l[0]
    l_target = l[1]
    r_time = r[0]
    r_target = r[1]

    # l_target + (l[1]-r[1])/(l[0]-r[0]) * t-r[0]
    t_diff = t - l_time
    rate = (r_target - l_target) / (r_time - l_time)
    t_target = l_target + rate * t_diff
    return t_target


def locate_program_step(p, t):
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


variables, settings, furnace_settings, programe = init_sim()
tl = construct_timeline(variables, settings)
for i in tl:
    print('furnace_Temp', ' = ', i['furnace_Temp'], ' ,', 'time', ' = ', i['time'])


left, right = locate_program_step(programe, 9)
print(left)
print(right)
