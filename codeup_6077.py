#정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
total=0
n = int(input())

for i in range(n+1):
    if i%2==0:
        total+=i

print(total)
