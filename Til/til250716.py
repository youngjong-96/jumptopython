#로또 번호 생성하는 모듈 만들기
import random

def input_start():
    start = 0
    try:
        start = int(input("로또 번호의 시작 번호를 입력하세요 (기본값: 1): "))
    except:
        start = 1
    finally:
        return start

def input_end():
    end = 0
    try:
        end = int(input("로또 번호의 끝 번호를 입력하세요 (기본값: 45): "))
    except:
        end = 45
    finally:
        return end
    
def input_count():
    try:
        count = int(input("로또 공의 개수를 입력하세요(기본값: 6): "))
    except:
        count = 6
    finally:
        return count
    
def print_lotto(start, end, count, set):
    for i in range(set):
        lotto = random.sample(range(start, end+1), count)
        print("행운의 로또 번호는 ", end="")
        for i, num in enumerate(sorted(lotto)):
            if i == len(lotto) -1:
                print(f"{num}",end="")
            else:
                print(f"{num}, ",end="")
        print("입니다.")
    
print_lotto(1, 45, 6, 5)

#튜플 다루기
data_tuple=(1,2,3,4,5)

data_tuple2=(x*y for x in data_tuple if x%2==1
                  for y in data_tuple if y%2==0)
print(tuple(data_tuple2))

#학생 총점, 평균 구하기
scores = []
count = int(input("총 학생 수를 입력하세요: "))

for i in range(1, count+1):
    score=[]
    kor = int(input(f"학생{i}의 국어 점수를 입력하세요: "))
    score.append(kor)
    mat = int(input(f"학생{i}의 수학 점수를 입력하세요: "))
    score.append(mat)
    eng = int(input(f"학생{i}의 영어 점수를 입력하세요: "))
    score.append(eng)
    scores.append(score)

for i, score in enumerate(scores):
    total = 0
    for s in score:
        total += s
    print(f"학생{i+1} 총점: {total}, 평균: {total/len(score):.2f}")
