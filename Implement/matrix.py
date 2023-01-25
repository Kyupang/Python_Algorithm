for i in range(5):
    for j in range(5):
        print('(',i,',',j,')',end =' ')
    print()

#동,북,서,남
dx =[0,-1,0,1] #행을기준
dy =[1,0,-1,0] #열을기준
x,y = 2,2
for i in range(4):
    x = x +dx[i]
    y = y +dy[i]
    print(x,y)
