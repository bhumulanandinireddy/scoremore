
def permuted_multiples(i) :
        t = sorted(str(i))
        if t == sorted(str(i*2)) and t == sorted(str(i*3)) and t == sorted(str(i*4)) and t == sorted(str(i*5)) and t == sorted(str(i*6)) :
            return True
        return False
for i in range(10000,10000000) :
    if permuted_multiples(i) :
        print(i)
        break
            
            

