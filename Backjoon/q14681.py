#숫자를 입력받아 4사분면 중 어디에 속하는지 출력하기
x=int(input())
y=int(input())
if x>0 and y>0:
    print(1)
elif x>0 and y<0:
    print(4)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(0)