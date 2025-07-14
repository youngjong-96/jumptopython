f=int(input("첫 번째 숫자를 입력하세요: "))
u=input("연산자를 입력하세요(+,-,*,/): ")
ck=int(input("두 번째 숫자를 입력하세요: "))

if u=="+":
    print(f"{f}*{ck}={f+ck}")
elif u=="-":
    print(f"{f}*{ck}={f-ck}")
elif u=="*":
    print(f"{f}*{ck}={f*ck}")
elif u=="/":
    print(f"{f}*{ck}={f/ck:.2f}")
else:
    print("본 프로그램에서 지원하지 않는 연산자입니다.")