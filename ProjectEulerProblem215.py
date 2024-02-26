from math import factorial
from time import sleep

def W(x, y):
    crackLocations = []
    def getCracks(c, p):
        if p < x:
            for i in (1, 2):
                c.append(p+i+1)
                getCracks(c, p+i+1)
                c.pop()
        elif p == x:
            crackLocations.append(set(c[:-1]))
        else:
            return
    getCracks([], 0)
    ncindex = []
    for crack in crackLocations:
        ncindexline = []
        for (i, relcrack) in enumerate(crackLocations):
            if relcrack.isdisjoint(crack):
                ncindexline.append(i)
        ncindex.append(ncindexline)
    combs = [1] * len(crackLocations)
    for i in range(1, y):
        newcombs = [sum(combs[k] for k in nci) for nci in ncindex]
        combs = newcombs
    return str(sum(combs))

def main():
    ROW_LEN = 32
    COL_LEN = 10
    print(W(ROW_LEN, COL_LEN))
    
if __name__ == "__main__":
    main()