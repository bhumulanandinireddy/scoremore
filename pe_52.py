def is_palindrome(n) :
    return str(n) == str(n)[::-1]

def is_lychrel(n) :
    count = 0
    while count < 50 :
        n += int(str(n)[::-1])
        count += 1
        if is_palindrome(n):
            return False
    return True
 
def lychrel_range(n):
    lychrel_numbers = []
    for i in range (1,n+1):
        if is_lychrel(i):
           lychrel_numbers.append(i)
    return lychrel_numbers

print(len(lychrel_range(10000)))
