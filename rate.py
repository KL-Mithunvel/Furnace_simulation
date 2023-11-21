import math


def cooling(e):
    #T(t) = Ts + (Ts – To) e^(-kt)
    #for the time being just returns final temp
    t = e['settings']['duration']
    k = e["f_settings"]['newton_cooling_con']
    for i in range(len(e['tl'])):
        Ts = e['tl'][i]['amb_Temp']
        To = e['tl'][i]['furnace_temp']
        e['tl'][i]['temp_drop'] = Ts+(Ts-To)*math.e**(-1*k*t)
    return None





