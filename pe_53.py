import math
def ncr(n,r) :
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
def count() :
    return len([i for i in range(1,101) for j in range(1,i+1) if (ncr(i,j)) > 1000000])
print(count())