import pandas as pd

col_name = ['과목번호','과목명','강의실','시간수']

list1 = (['C1','인공지능개론','R1',3],
         ['C2','웃음치료','R2',2],
         ['C3','경영학','R3',3],
         ['C4','3D디자인','R4',4],
         ['C5','스포츠경영','R2',2],
         ['C6','예술의 세계','R3',1],
         )

df = pd.DataFrame(list1, columns=col_name)
print(df, end='\n\n')

print("################################")

data = {
    '과목번호' : ['C1','C2','C3','C4','C5','C6'],
    '과목명' : ['인공지능개론','웃음치료', '경영학', '3D디자인', '스포츠경영', ' 예술의 세계'],
    '강의실' : ['R1','R2','R3','R4','R2','R3'],
    '시간수' : [3,2,3,4,2,1]
}

df = pd.DataFrame(data)
print(df, end='\n\n')

sr_name = df['과목명']  #열 추출
print(sr_name, end='\n\n')

sr_no = df.loc[2]       #행 추출
print(sr_no, end='\n\n')

cell_name = df.loc[2]['과목명'] #셀 추출
print(cell_name, end='\n\n')

df['담당교수'] = ['홍길동','김철수','이영희','박영수','최영희','김영수']
print(df, end='\n\n')

df.loc[6] = ['C7', '통계학','R7' ,3 ,'이철수']
print(df, end='\n\n')

df1 = df.drop(['강의실'],axis=1)   # axis = 1 은 열 , axis = 0은 행
print(df1, end='\n\n')

df2 = df.drop([5],axis=0)
print(df2, end='\n\n')

print("################################", end='\n\n')

print(df.loc[0:2], end='\n\n')   # [0:2] 안의 값을 인덱스로 판단하기 때문에 0~2 
print(df.iloc[0:2], end='\n\n')  # [0:2] -> 0~1
print(df[['과목명','담당교수']],end='\n\n')
print(df.loc[:, '강의실' : '담당교수'], end='\n\n')

print("3주차 연습 ################################", end='\n\n')

print(df["과목명"] == '경영학', end='\n\n')
print(df.loc[df['과목명']=='경영학'], end='\n\n')
print(df.loc[df['시간수'] > 2], end='\n\n')

print(df.loc[df['과목명']=='경영학']['담당교수'], end='\n\n')
print(df.loc[df['과목명']=='경영학']['담당교수'].values[0], end='\n\n')

df.loc[3, '담당교수'] = '이경영'
print(df)

df.loc[df['과목명']=='경영학', '담당교수'] = '이경영'
print(df, end='\n\n')

print(df.loc[df['과목명']== '경영학' , '담당교수'].values[0], end='\n\n')



