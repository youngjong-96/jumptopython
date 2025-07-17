#분을 더해서 알맞은 시간을 출력하기 (24시간 기준)
h, m=map(int, input().split())
c = int(input())
mc=m+c

if mc<60:
    print(h, mc)
elif mc>=60:
    h+=mc//60
    mc%=60
    if h<24:
        print(h, mc)
    elif h>=24:
        print(h%24, mc)