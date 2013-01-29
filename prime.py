import math

def isPrime(n):
    if n<=1: return False
    if n==2: return True
    m=round(math.sqrt(n))
    for i in range(3,m,2):
        if n%i==0: return False
    return True

def primeList(n):
    

'''public boolean[] sieve(int n)
{
   boolean[] prime=new boolean[n+1];
   Arrays.fill(prime,true);
   prime[0]=false;
   prime[1]=false;
   int m=Math.sqrt(n);

   for (int i=2; i<=m; i++)
      if (prime[i])
         for (int k=i*i; k<=n; k+=i)
            prime[k]=false;

   return prime;
} '''
