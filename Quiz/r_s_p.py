case=input("가위바위보에 해당하는 숫자를 한 칸 공백으로 입력하세요. (ex. 1 3): ")
a=int(case[0])
b=int(case[2])

if a==1 and b==2:
    print('B')
elif a==1 and b==3:
    print('A')
elif a==2 and b==1:
    print('A')
elif a==2 and b==3:
    print('B')
elif a==3 and b==1:
    print('B')
elif a==3 and b==2:
    print('A')