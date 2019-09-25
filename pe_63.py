def is_power(n) :
    count,power,i = 0,1,1
    while len(str(power)) <= n :
        if len(str(power)) == n :
            count += 1
        i += 1
        power = i ** n
    return count
def is_sum() :
    count = 0
    for i in range(1,100) :
        count += is_power(i)
    return count
print(is_sum())        