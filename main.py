def temp_disp(ts, t0, t, rate):
    print('rate is ', rate)
    T_vs_t = []
    for i in range(t+1):
        x = ts+i*rate
        print(x)
        T_vs_t.append(x)
    print(T_vs_t)

def heat_coil(R,V):
    #P=V^2/R
    return V**2/R

def v_resistivity(r0,a,t):
    #rt=r0(1+at)
    #temperature cofficient of nichrome is 0.00017
    return r0*(1+a*t)

def resistance():

    return


T_hot = 50
T_room = 100
t_min = 20
rate = (T_room-T_hot)/t_min
temp_disp(T_hot, T_room, t_min, rate)

