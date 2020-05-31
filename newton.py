import math

def calculate(x):
    #return math.cos(x) - x
    #return math.e ** (-x) - math.sin(x)
    #return x - math.e ** (-x)
    #return x**2 - 2*x*math.e**(-x) + math.e**(-2*x)
    return (1/16) * (231*(x**6) - 315*(x**4) + 105*(x**2) - 5)

class parameters:
    epsilon1 = 10**-6
    epsilon2 = 10**-4
    n = 10
    cur_x = 0.785398163
    formula = ""

    next_x = 0
    cf = 0
    df = 0

    def __init__(self):
        with open("input.txt", "r") as input:
            nums = input.readlines()
            #print(nums)
            self.formula = nums[0]
            self.epsilon1 = float(nums[1])
            self.epsilon2 = float(nums[2])
            self.n = int(nums[3])
            self.cur_x = float(nums[4])
            #print(self.formula, self.epsilon1, self.epsilon2, self.n, self.cur_x)

def iter(paras):
    formula = paras.formula
    epsilon1 = paras.epsilon1
    epsilon2 = paras.epsilon2
    n = paras.n
    cur_x = paras.cur_x

    for count in range(n):
        #print(str(count)+'th')
        #print(cur_x)
        cf = calculate(cur_x)
        df = (calculate(cur_x) - calculate(cur_x - epsilon1)) / epsilon1
        if math.fabs(cf) < epsilon1:
            return cur_x
        if math.fabs(df) < epsilon2:
            return 'error'
        tol = cf/df
        next_x = cur_x - tol
        if math.fabs(tol) < epsilon1:
            return next_x
        cur_x = next_x
    return 'error'

newquiz = parameters()
ans = []
for alpha in range(0, 100):
    newquiz.cur_x = alpha/100
    ans.append(iter(newquiz))
print(ans)