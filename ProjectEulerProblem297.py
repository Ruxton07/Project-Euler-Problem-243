from math import factorial
from bitmap import BitMap

print("hi")

def evaluateBinomialFactorial(n, k):
    return (factorial(n)/(factorial(k)*factorial(n-k)))

def main():
    print("2^83 is " + str(2**83))
    THRESHOLD = 10**6
    FibonacciArray83Without0and1 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497]
    print("F_82 is: " + str(FibonacciArray83Without0and1[-1])) #This is the 83rd Fibonacci number, which is the number we are trying to sum to
    MinSumArrayForF83 = []
    MinSumArrayForThresholdMinusF81 = []
    MinSumArrayForThresholdMinusF82 = []
    FibBitMap = BitMap(len(FibonacciArray83Without0and1))
    # In a bit map of length 82, we will set the bits to 1 to represent the presence of the Fibonacci numbers in the array
    # To start, let's find how many possibilities there are for putting three 1's in the bit map, but EXCLUDING cases where two 1's are next to each other
    def findNonAdjacentOnesPossibilities(n):
        count = 0
        for i in range(2**(82-n)):
            binary = bin(i)[2:].zfill(82-n)
            if '11' not in binary:
                count += 1
        return count
    print("Number of possibilities for two 1's in the bit map: " + str(findNonAdjacentOnesPossibilities(2)))
    print("Actual possibilities for two 1's in the bit map: " + str(evaluateBinomialFactorial(82, 2)-81))

#                                       *****OLDER IMPLEMENTATION: attempt 2, but returned an incorrect answer due to overcounting some of the possibilities
#                                                                  because it did not account for two Fibonacci numbers next to each other being added.   
#    sum = 0
#    i = 0
#     m = 0
#     o = 0
#     while sum+FibonacciArray83Without0and1[i] < THRESHOLD:
#         sum += FibonacciArray83Without0and1[i]
#         MinSumArrayForF83.append(FibonacciArray83Without0and1[i])
#         i+=1
#     sum = 0
#     while sum+FibonacciArray83Without0and1[m] < (THRESHOLD-FibonacciArray83Without0and1[-2]):
#         sum += FibonacciArray83Without0and1[m]
#         MinSumArrayForThresholdMinusF81.append(FibonacciArray83Without0and1[m])
#         m+=1
#     sum = 0
#     while sum+FibonacciArray83Without0and1[o] < (THRESHOLD-FibonacciArray83Without0and1[-1]):
#         sum += FibonacciArray83Without0and1[o]
#         MinSumArrayForThresholdMinusF82.append(FibonacciArray83Without0and1[o])
#         o+=1
#     print("Array is: " + str(MinSumArrayForF83))
#     print("Length of the array with sum less than 10^17 is: " + str(len(MinSumArrayForF83)))
#     print("Length of fib array is: " + str(len(FibonacciArray83Without0and1))) #This is the length of the array without the 0 and 1 at the beginning
#     print("Length of the array with sum less than (10^17-F_81): " + str(len(MinSumArrayForThresholdMinusF81)))
#     print("Length of the array with sum less than (10^17-F_82): " + str(len(MinSumArrayForThresholdMinusF82)))
#     binomialWithCofficientsSum = 0
#     #Case 1: 1 to 80 as Coefficients multiplied by binomials
#     for j in range(1, len(MinSumArrayForF83)):
#         binomialWithCofficientsSum += (j*evaluateBinomialFactorial(len(MinSumArrayForF83), j))
#         print("j = " + str(j) + ", value to add: " + str(j*evaluateBinomialFactorial(len(MinSumArrayForF83), j)))
#     print("BWCS after case 1: " + str(binomialWithCofficientsSum))
#     #Case 2: Same thing as case one but using "MinSumArrayForThresholdMinusF81" instead of "MinSumArrayForF83"
#     for l in range(1, len(MinSumArrayForThresholdMinusF81)):
#         binomialWithCofficientsSum += (l*evaluateBinomialFactorial(len(MinSumArrayForThresholdMinusF81), l))
#         print("l = " + str(l) + ", value to add: " + str(l*evaluateBinomialFactorial(len(MinSumArrayForThresholdMinusF81), l)))
#     print("BWCS after case 2: " + str(binomialWithCofficientsSum))
#     #Case 3: Same thing as case one and two but using "MinSumArrayForThresholdMinusF82" instead of "MinSumArrayForThresholdMinusF81"
#     for n in range(1, len(MinSumArrayForThresholdMinusF82)):
#         binomialWithCofficientsSum += (n*evaluateBinomialFactorial(len(MinSumArrayForThresholdMinusF82), n))
#         print("n = " + str(n) + ", value to add: " + str(n*evaluateBinomialFactorial(len(MinSumArrayForThresholdMinusF82), n)))
#     print("BWCS after case 3: " + str(binomialWithCofficientsSum))
#     binomialWithCofficientsSum += 83
#     print("Final Sum (BWCS after case 4): " + str(binomialWithCofficientsSum))
# main()

# def nearestSmallerEqFib(n):   *****OLDER IMPLEMENTATION: this was used to brute force. would work if you had a higher computational
#                                                          computer to use that could make more computations per unit time, but in reality
#                                                          takes way to long to be feasible to simply brute force it. See optimized
#                                                          implementation above.
# 	if (n == 0 or n == 1):
# 		return n
# 	f1, f2, f3 = 0, 1, 1
# 	while (f3 <= n):
# 		f1 = f2
# 		f2 = f3
# 		f3 = f1 + f2
# 	return f2
# def printFibRepresntation(n):
# 	numTerms = 0
# 	while (n>0):
# 		f = nearestSmallerEqFib(n)
# 		#print(f,end=" ")
# 		n = n-f
# 		numTerms += 1
# 	return numTerms
# def main():
#     n, termSum = 100000000000000000, 0
#     k = n-1
#     while k>0:
#         #print("Non-neighbouring Zeckendorf Representation of ", k , " is ")
#         thisTerms = printFibRepresntation(k)
#         #print("z("+str(k)+")="+str(thisTerms))
#         k-=1
#         termSum+=thisTerms
#     print("TermSum for " + str(n) + " is " + str(termSum))
	
main()