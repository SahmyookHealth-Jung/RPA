#임의의 정수를 입력받아서 1~정수까지 합을 구하는 프로그램
#정수합을 구하면 로직은 함수(sumfunc)로 만들어야함

def sumfunc(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum + i
    return sum
    
num = int(input("정수를 입력하세요: "))
sum = sumfunc(num)

if num > 0:
    print(f"1~{num}까지의 정수의 합은 {sum}입니다.")

    
