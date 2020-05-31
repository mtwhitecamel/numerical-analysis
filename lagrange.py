nodes = {}
def data_init():
    with open("input.csv", "r") as input:
        for line in input:
            #print(line)
            numlist = line.split(',')
            nodes[float(numlist[0])] = float(numlist[1])
        #print(nodes)

def polynomial_mul(left_poly, right_poly):
    new_poly = {}
    for index_L in left_poly:
        for index_R in right_poly:
            new_index = index_L + index_R
            if new_index in new_poly:
                new_poly[new_index] += left_poly[index_L] * right_poly[index_R]
            else:
                new_poly[new_index] = left_poly[index_L] * right_poly[index_R]
    return new_poly

def polynomial_add(left_poly, right_poly):
    new_poly = {}
    for index_L in left_poly:
        new_poly[index_L] = left_poly[index_L]
    for index_R in right_poly:
        if index_R in new_poly:
            new_poly[index_R] += right_poly[index_R]
        else:
            new_poly[index_R] = right_poly[index_R]
    return new_poly

def polynomial_print(poly):
    print("L(x) = ",end='')
    for i in range(1, num):
        index = num-i
        if poly[index] != 0:
            if poly[index] > 0:
                print('+',end='')
            print(str(poly[index])+'x^'+str(index)+' ',end='')
    if poly[0] > 0:
        print('+',end='')
        print(str(poly[0]))
    elif poly[0] < 0:
        print(str(poly[0]))

ans = {}
data_init()
num = len(nodes)
#print(num)
for i in nodes:
    fraction = {0:1}
    denominator = 1
    for j in nodes:
        if i != j:
            denominator *= i-j
            fraction = polynomial_mul(fraction, {1:1, 0:(-1*j)})
    for index in fraction:
        fraction[index] = nodes[i] * fraction[index] / denominator
    #print(fraction)
    ans = polynomial_add(ans, fraction)
#print(ans)
polynomial_print(ans)