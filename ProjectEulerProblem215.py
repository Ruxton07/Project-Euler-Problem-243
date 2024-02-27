from math import factorial
from time import sleep

def W(x, y):
    crackLocations = []
    def getCracks(c, p):
        if p < x:
            for n  in (1, 2):
                c.append(p+n+1)
                getCracks(c, p+n+1)
                c.pop()
        elif p == x:
            crackLocations.append(set(c[:-1]))
        else:
            return
    getCracks([], 0)
    non_colliding_index = []
    for crack in crackLocations:
        ncindexline = []
        for (i, relcrack) in enumerate(crackLocations):
            if relcrack.isdisjoint(crack):
                print(relcrack)
                print("_")
                print(crack)
                print("_________")
                ncindexline.append(i)
        non_colliding_index.append(ncindexline)
    print(crackLocations)
    combs = [1] * len(crackLocations)
    print(non_colliding_index)
    for i in range(1, y):
        newcombs = []
        for u in non_colliding_index:
            print("u: " + str(u))
            sumv = 0
            for k in u:
                print("k: " + str(k))
                print("combs:")
                print(combs)
                print("newcombs:")
                print(newcombs)
                print("combs[k]: " + str(combs[k]))
                sumv += combs[k]
            newcombs.append(sumv)
        combs = newcombs
    print(combs)
    return str(sum(combs))

def main():
    ROW_LEN = 9
    COL_LEN = 3
    print(W(ROW_LEN, COL_LEN))
    
if __name__ == "__main__":
    main()