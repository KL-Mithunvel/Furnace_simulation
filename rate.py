import math
def cooling(Ts,To,k,t):
    #T(t) = Ts + (Ts – To) e^(-kt)
    #for the time being just returns final temp
    return Ts+(Ts-To)*(math.e)**(-1*k*t)
