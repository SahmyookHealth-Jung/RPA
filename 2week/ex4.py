a = int(input("정수를 입력하세요: "))

if a % 2 == 0:
    print("짝수이다 - True")
else:
    print("짝수이다 - False")

result = (a%2) == 0
print('짝수이다 - ', result)