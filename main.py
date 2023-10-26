import time
def heat_up(ts,t0,t):
    rate=(t0-ts)/t
    print('rate is ',rate)
    T_vs_t=[]
    for i in range(t):
        time.sleep(2)
        x=ts+i*rate
        print(x)
        T_vs_t.append(x)
    print(T_vs_t)


T_hot=100
T_room=50
t_min=20
print('2 sec is one min')
heat_up(T_hot,T_room,t_min)
