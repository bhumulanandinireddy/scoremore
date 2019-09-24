def power_sum(i) :
    return i**i
def sum_power(n) :
    return str(sum(power_sum(i) for i in range(1,n+1)))
print(sum_power(1000)[-10:])
      
