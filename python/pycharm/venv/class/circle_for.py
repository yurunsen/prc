for item in 'ptthon':
    print(item)
#range()
for i in range(10):
    print(i)

#不需要自定义变量，可写为_
for _ in range(5):
    print('a')

#使用for计算1-100的偶数
sum=0
for item in range(1,101):
    if item%2==0:
        sum+=item
print('sum:',sum)
