# #1 map()함수와 filter()함수 활용하여 프로그램 만들기

# data_list=list(range(1,21))

# e1 = input("항목 x에 대해 적용할 표현식을 입력하세요: ")
# e2 = input("필터할 표현식을 입력하세요: ")

# t=list(map(lambda x: eval(e1), data_list))
# f=list(filter(lambda x: eval(e2), t))

# print(f"map 함수 적용 결과: {t}")
# print(f"filter 함수 적용 결과: {f}")


# #2 다음의 결과와 같이 이름과 나이를 입력 받아 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.
# year=2019

# def age100(name, age):
#     print(f"{name}(은)는 {year+100-age}년에 100세가 될 것입니다.")

# a=input()
# b=int(input())

# age100(a,b)


##3 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.
#word="ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

# def score():
#     result_list=[]
#     for i in word:
#         if i=='A': result_list.append(4)
#         elif i=='B': result_list.append(3)
#         elif i=='C': result_list.append(2)
#         elif i=='D': result_list.append(1)
#     return result_list
# print(sum(score()))

#print(sum(list(map(lambda x:{'A': 4, 'B': 3, 'C': 2, 'D': 1}[x],word))))


# #4 예외처리 프로그램
# def input_index():
#     num = 0
#     try:
#         num = int(input("인덱스로 사용할 숫자를 입력하세요: "))
#     except ValueError as exception:
#         raise exception
#     else:
#         return num
        
# def print_in_bounds(list, index):
#     value = 0
#     try:
#         value = list[index] 
#     except IndexError as exception:
#         print(f"{type(exception)}")
#         index = len(list)-1
#         print(f"인덱스는 0~{index}까지 사용할 수 있습니다.")
#         value = list[index]
#     finally:
#         print(f"[{index}]:{value}")

# data_list = list(range(1,11))

# try:
#     num = input_index()
#     print_in_bounds(data_list, num)
# except ValueError as exception:
#     print(f"{type(exception)}숫자만 입력이여~")
# except Exception as exception:
#     print(exception)


# #5 가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고, 단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.
# def mul(*numbers):
#     try:
#         sum = 0
#         for i in numbers:
#             sum+=i
#     except ValueError as ve:
#         print("에러발생")
#     except Exception as exception:
#         print("에러발생")
#     else:
#         return sum

# mul(1,2,'4',3)


# #6 ASCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오.
# def ascii(num):
#     print(f"ASCII {num} => {chr(num)}")
# ascii(65)


# #7 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해 짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.
# data_list=list(range(1,11))
# print(list(filter(lambda x:x%2==0, data_list)))


# #8 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.
# data_list=list(range(1,11))
# print(list(map(lambda x:x**2,data_list)))


# #9 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해 짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.
# data_list=list(range(1,11))
# odd_list=list(filter(lambda x:x%2==0,data_list))
# print(list(map(lambda x:x**2,odd_list)))


# #10 가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의하고,다음과 같은 결과를 출력하는 프로그램을 작성하십시오.
# def maxxx(*numbers):
#     max_num=max(numbers)
#     return max_num
# numbers="3, 5, 4, 1, 8, 10, 2"
# print(f"max({numbers}) => {maxxx(3, 5, 4, 1, 8, 10, 2)}")