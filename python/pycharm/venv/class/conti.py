#输入1-50之间5的倍数
for item in range(1,51):
    if item%5==0:
        print(item)


print('----------------------')
for item in range(1,51):
    if item%5!=0:
        continue
    else:
        print(item)

