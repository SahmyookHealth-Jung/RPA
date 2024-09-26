import pandas as pd

data = {
    '이름' : ['kim', 'park', 'Lee', 'Ho'],
    '국어' : [90,58,88,100],
    '영어' : [100,60,80,70],
    '수학' : [55,65,76,88]
}

print("1번", end='\n\n')
df = pd.DataFrame(data)

print("2번", end='\n\n')
print(df, end='\n\n')

print("3번", end='\n\n')
sr_name = df['이름']
print(sr_name)

print("4번", end='\n\n')
sr = df.loc[1]
print(sr)


print("5번", end='\n\n')
df.loc[df['이름'] == 'Ho', '수학' ] = 90
print(df)

print("6번", end='\n\n')
df.loc[4] = ['Oh', 100, 70, 80]
print(df)

print("7번", end='\n\n')
df = df.drop([2], axis=0)
print(df)

