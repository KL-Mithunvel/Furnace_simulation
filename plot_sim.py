import csv

import matplotlib.pyplot as plt
import pandas as ps


def prepare_data(env):
    """
    Prepares data from the timeline for plotting. Returns Pandas DataFrame with variables needed for graph
    :param env: pass the environment dictionary
    :return: Pandas DataFrame
    """
    req = [x for x in env['var'].keys() if x != 'time' and env['var'][x]['graph']]
    time = get_var_data_series('time', env)
    data = dict()
    for i in req:
        data[i] = get_var_data_series(i, env)
    df = ps.DataFrame(data, index=time)

    return df


def get_var_data_series(key, e):

    data = ps.Series([x[key] for x in e["tl"]])
    return data


def display_graph(data_f):
    ax = data_f.plot()
    ax.grid(True)
    ax.set_ylabel('Temperature °C')
    ax.set_xlabel('time')
    ax.set_title('Simulation Result')
    plt.show()


def export_data(env, f):
    tl = env['tl']
    file_obj = open(f, 'w')
    file_obj.write(str(['f_target_temp','f_achieved_temp','fuel_added']))
    for i in range(len(tl)):
        file_obj.write(str([tl[i]['f_target_temp'], tl[i]['f_achieved_temp'], tl[i]['fuel_added']]))
    pass


def csv_write(env):
    f=input('Enter the file name:')
    tl = env['tl']
    file_obj = open(f, 'w', newline='')
    write_obj=csv.writer(file_obj)
    write_obj.writerow(['f_target_temp','f_achieved_temp','fuel_added'])
    for i in range(len(tl)):
        write_obj.writerow([tl[i]['f_target_temp'],tl[i]['f_achieved_temp'],tl[i]['fuel_added']])






