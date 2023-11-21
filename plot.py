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
    ax.set_ylabel('Temperature °C')
    ax.set_xlabel('time')
    ax.set_title('Simulation Result')
    ax.grid(True)
    plt.show()
