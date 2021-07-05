#range三种使用
'''第一种：只有一个参数'''
r=range(10) #默认从0开始，步长为1
print(r)
print(list(r))
'''第二种：给出两个参数'''
r=range(1,10)  #指定起始值
print(list(r))
'''第三种：给出三个参数'''
r=range(1,10,2)   #给出步长
print(list(r))

'''判断指定整数是否存在在序列中'''
print(5 in r)
print(8 not in r)

