y=[['A','B','C','D']]
k=-1
x=-1
z=0
print(y[0])
while True:
    k+=1
    for i in range(0,4):
        for j in range(i+1,4):
            x+=1
            if x>22:
                z=1
                break
            print(y[k])
            y.append(y[k])
            y[x+1][i],y[x+1][j]=y[x][j],y[x][i]
            print(y[x])
        if z==1:
            break
    if z==1:
        break
           
