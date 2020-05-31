import math

epsilon = 10**-6
a = 0
b = 1
def f(x):
    return x**2 * math.e**x
temp = {}

def h(n):
    return (b-a)/(2**n)

def f_sigma(f_start, f_step, f_times):
    sum = 0
    for i in range(f_times):
        sum += f(f_start + f_step * i)
    #print(f_start, f_step, f_times, sum)
    return sum

def r(n, m):
    if n*4+m not in temp:
        if m == 0:
            if n == 0:
                temp[n*4+m] = 1/2 * (f(a)+f(b))
            else:
                temp[n*4+m] = 1/2 * r(n-1, 0) + h(n)*f_sigma(a+h(n), 2*h(n), 2**(n-1))
        else:
            temp[n*4+m] = (4**m * r(n, m-1) - r(n-1, m-1)) / (4**m-1)
    #print("r()", str(n), str(m), temp[n*4+m])
    return temp[n*4+m]
    
for i in range(4,10):
    if math.fabs(r(i,3)-r(i-1,3)) < epsilon:
        print(r(i,3))
        break