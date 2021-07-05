#切片索引
lst=[10,20,30,40,50,60,70]
print(lst[1:6:1])    #切出来的为新列表
#省略步长 默认为1
print(lst[1:5])
#省略start
print(lst[:6:2])
#省略stop
print(lst[1::2])
print('---------step步长为负数-------')
print(lst[::-1])
