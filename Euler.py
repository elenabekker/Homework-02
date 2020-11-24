import matplotlib.pyplot as plt
import numpy as np

def euler(f, x0, t):
    x = np.zeros(len(t))
    x[0] = x0
    for n in range(0,len(t)-1):
        x[n+1] = x[n] + f(x[n],t[n])*(t[n+1] - t[n])
    return x

def opinion_function(x,t):
    global d; u; a; b
    return (-d*x + u*np.tanh(a*x) + b)

h=0.001; Tend=7 # für a), b) und d)
#h=0.1; Tend=7 # für c)
t = np.arange(0, Tend+h, h)

#d=1; u=0.31; a=1.2; b=0 # a)
d=1; u=0.31; a=1.2; b=3 # b)
#d=1; u=0.31; a=1.2; b=3 # c)
#d=4; u=0.31; a=1.2; b=0 # d)

x = euler(opinion_function, 0, t)

plt.scatter(t,x,s=2)

plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()