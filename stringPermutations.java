y=[['A','B','C','D']]
k=-1
x=0
while True:
    k+=1
    for i in range(0,4):
        for j in range(i+1,4):
            x+=1
            if x>23:
                break
            y[k][i],y[k][j]=y[k][j],y[k][i]
            y.append(y[k])
           
for i in range(0,24):
    print(y[i])
