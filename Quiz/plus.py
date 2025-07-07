n = int(input("1부터 9999까지 중 한 자연수를 입력하세요: "))
sum = 0

while n > 0:
    sum += n % 10
    n //= 10

print(sum)