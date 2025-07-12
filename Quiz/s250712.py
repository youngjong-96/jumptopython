import random
 #1
# print("a부터 b까지 정수의 합을 구합니다.")
# a=int(input('정수 a를 입력하세요: '))
# b=int(input('정수 b를 입력하세요: '))

# if a>b:
#     a,b=b,a

# sum=0
# for i in range(a, b+1):
#     sum += i

# print(f"{a}부터 {b}까지의 합은: {sum}")

# for i in range(a,b):
#     sum+=i
#     print(f"{i} + ", end="")
    
# print(f"{b} = ", end="")
# print(sum)

 #2
# print('+와 -를 번갈아 출력합니다. 몇 번 출력할까요?: ', end="")
# n=int(input())

# for _ in range(n//2):
#     print('+-',end="")
# if n%2==1: print('+')

 #3
# print('*을 출력합니다.')
# n=int(input('총 몇 개 출력할까요?: '))
# w=int(input('몇 개마다 줄바꿈을 할까요?: '))

# for _ in range(n//w): print('*'*w)
# rest=n%w
# if rest: print('*'*rest)

 #4 - 약수 찾기
# area=int(input('직사각형의 넓이를 입력하세요:'))
# for i in range(1, area+1):
#     if i*i>area: break
#     if area%i: continue
#     print(f"{i} * {area//i} = {area}")

 #5
n=int(input("난수를 몇 개 생성할까요?: "))

for _ in range(n):
    r=random.randint(10,20)
    print(r,end=" ")
    if r==13: print('\n 13 두두등장!'); break
else:
    print('\n난수 생성을 멈춥니다.')
