def is_dig(n) :
    if list(str(n)) == sorted(str(n)) or list((str(n))) == sorted(str(n))[::-1] :
        return True
    return False
def is_count(n) :
    count = 0
    for i in range(1,n+1) :
        if is_dig(i) :
            count += 1
    return count
print(is_count(1000000))