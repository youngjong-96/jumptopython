count=int(input())
chr=input()
for i in range(0,count):
    if 65<=ord(chr) and ord(chr)<=90:
        print("#%d %s 는 대문자 입니다."%(i+1,chr))
    else:
        print("#%d %s 는 소문자 입니다."%(i+1,chr))