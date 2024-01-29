from math import factorial

potentialPSquares = [4, 9, 25, 49]
seen = []

squarefreeSum = 0
# input n
n = 51
for i in range(n):
    for j  in range(n-i+1):
 
        # for left spacing
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        PTVal = factorial(i)//(factorial(j)*factorial(i-j))
        sqf = True
        for p in potentialPSquares:
            if PTVal % p == 0:
                sqf = False
                break
        inSeen = False
        for v in seen:
            if v == PTVal:
                inSeen = True
                break
        if sqf and not inSeen:
            squarefreeSum += PTVal
            seen.append(PTVal)
            
        print(PTVal, end=" ")
 
    # for new line
    print()
print(squarefreeSum)