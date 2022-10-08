N = input()
ini = N
cycle = 0

while True:
    if len(ini) == 1 :
        ini = "0" +ini
    result = str(int(ini[0]) + int(ini[1]))
    ini = ini[-1] + result[-1]
    cycle+=1
    if N == ini:
        print(cycle)
        break









