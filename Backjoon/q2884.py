#시간 계산해서 바르게 출력하기
h, m=map(int, input().split())

if 60>=m>=45:
    print(f"{h} {m-45}")
elif 24>=h>0 and m<45:
    print(f"{h-1} {m+(60-45)}")
elif h==0 and m<45:
    print(f"23 {m+(60-45)}")
else:
    print("올바른 시간을 입력하세요.")