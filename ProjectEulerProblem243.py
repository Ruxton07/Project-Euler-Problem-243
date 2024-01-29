from math import factorial
from time import sleep

def findGCF(n, b):
    if (n%2==0 and b%2==0):
        #print("True1 " + str(n) + " " + str(b))
        return True
    for t in range(3, b, 2):
        if b%t==0 and n%t==0:
            #print("True2 " + str(n) + " " + str(b) + " " + str(t))
            return True
    return False

def phi(n) :
    result = n
    p = 2
    while p * p<= n :
        if n % p == 0 :
            while n % p == 0 :
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
         
    if n > 1 :
        result -= result // n
  
    return int(result)

def resilience(d):
    return phi(d)/(d-1)

def main():
    primes = []
    for i in range(2, 10000):
        primes.append(i)
        for t in range(2, i):
            if i%t==0:
                primes.pop()
                break
        

    iterate = []
    iterate.append(primes[0])
    for k in range(1, len(primes)):
        iterate.append(iterate[k-1]*primes[k])


    print("WANTED " + str(15499/94744))
    smallestDenom = 1
    for j in iterate:
        if resilience(j) < 15499/94744:
            smallestDenom = j
            break
        else:
            print("non-candidate" + str(j) + " | " + str(resilience(j)))
    newiterate = []
    newiterate.append(223092870)
    for u in range(2, 10):
        newiterate.append(newiterate[0]*u)
    for o in newiterate:
        if resilience(o) < 15499/94744:
            print("nth multiple: " + str(o) + " | " + str(resilience(o)))
            smallestDenom = o
            break
        else:
            print(str(o) + " | " + str(resilience(o)))
    print(smallestDenom)

if __name__ == "__main__":
    main()