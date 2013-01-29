

def isPrime(n):
    if n<=1 return false
    if n==2 return true
    int m=sqrt(n)
    for i in range(3,m,2):
        if n%i==0: return false
    return true

