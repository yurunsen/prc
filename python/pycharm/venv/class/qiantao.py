#输出三行四列的矩形
for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t')
    print()
#输出三角形
for m in range(1,10):  #行数
    for n in range(1,m+1):
        print('*',end='')
    print()
#乘法表
for m in range(1,10):  #行数
    for n in range(1,m+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()