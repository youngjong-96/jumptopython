#1 원의 면적과 둘레를 구하는 함수 만들어 활용하기
# PI=3.14

# def input_radius():
#     radius_str=input("반지름을 입력하세요: ")
#     return float(radius_str)

# def calc_circle_area(r):
#     return PI*r*r

# def calc_circumference(r):
#     return 2*PI*r

# radius=input_radius()
# circle_area = calc_circle_area(radius)
# circumference = calc_circumference(radius)

# print("원의 면적: {0:0.2f}, 원의 둘레: {1:0.2f}".format(circle_area, circumference))


#2 단어를 거꾸로 반환하고 회문 여부를 판단
# word=input()

# #단어를 거꾸로 반환하는 함수
# def check(str):
#     change=str[::-1]
#     return change

# new_word=check(word)
# print(new_word)
# if word==new_word:
#     print("입력하신 단어는 회문(Palindrome)입니다.")
# else:
#     print("입력하신 단어는 회문(Palindrome)이 아닙니다.")

#3 사용자 2명으로부터 가위, 바위, 보를 입력받아 가위바위보 규칙이 정의된 함수를 이용해 승패 반환
# player1=input()
# player2=input()
# player1_choice=input()
# player2_choice=input()

# def game(c1,c2):
#     if (c1=="가위" and c2=="바위") or (c1=="바위" and c2=="가위"):
#         print("바위가 이겼습니다!")
#     elif (c1=="가위" and c2=="보") or (c1=="보" and c2=="가위"):
#         print("가위가 이겼습니다!")
#     elif (c1=="보" and c2=="바위") or (c1=="바위" and c2=="보"):
#         print("보가 이겼습니다!")
#     else:
#         print("비겼습니다.")
        
# game(player1_choice,player2_choice)

#4 소수를 검사하는 함수를 정의하고 입력한 숫자가 소수인지 판단
# num=int(input())

# def sosu(num):
#     yaksu=[]
#     for i in range(1,num+1):
#         if num%i==0:
#             yaksu.append(i)
#     if len(yaksu)==2:
#         print("소수입니다.")

# sosu(num)

#5 피보나치 수열 만드는 프로그램
# count=int(input())

# def pivonachi(count):
#     if count==1:
#         pivonachi=[1]
#     else:
#         pivonachi=[1,1]
#     for i in range(2,count):
#         pivonachi.append(pivonachi[i-2]+pivonachi[i-1])
#     return pivonachi

# print(pivonachi(count))

#6 리스트의 중복제거
# def only(list):
#     check=[]
#     for i in list:
#         if i in check:
#             pass
#         else:
#             check.append(i)
#     return check
# a=[1,2,3,4,3,2,1]
# print(a)
# print(only(a))

#7 정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고, 이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.
# def find(list,num):
#     if num in list:
#         return num
    
# a=[2, 4, 6, 8, 10]
# print(a)
# print(f"5 => {bool(find(a,5))}")
# print(f"10 => {bool(find(a,10))}")

#8 팩토리얼 구하기
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))

#9 숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면 정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.
# def sibam(num):
#     return num**2
# num1, num2=map(int, input().split(','))
# print(f"square({num1}) => {sibam(num1)}")
# print(f"square({num2}) => {sibam(num2)}")

#10 인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고 결과를 출력하는 프로그램을 작성하십시오.
# def long(str1, str2):
#     if len(str1)>len(str2):
#         return str1
#     else: return str2
# str1, str2=map(str, input().split(','))
# print(long(str1.strip(), str2.strip()))

#11 인자로 전달된 숫자를 이용해 카운트다운하는 함수 countdown을 정의하고,이 함수를 이용하여 countdown(0), countdown(10)을 순서대로 실행하십시오.
# 0보다 작거나 같은 인자가 전달되었을 경우 "카운트다운을 하려면 0보다 큰 입력이 필요합니다."를 출력하십시오.
# def countdown(num):
#     if num==0:
#         print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
#     else:
#         while num>=1:
#             print(num) 
#             num-=1
# countdown(0)
# countdown(10)