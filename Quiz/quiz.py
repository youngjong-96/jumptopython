list=[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum=0
while list:
    if list[-1]>=80:
        sum+=list.pop()
    else:
        list.pop()
print(sum)
