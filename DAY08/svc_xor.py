from sklearn.svm import SVC

# (1) 데이터 준비 ----------------------------------------
xor_data=[[0,0,0],[0,1,0],[1,0,1],[1,1,0]]

# (2) 데이터 가공 ----------------------------------------
# 학습용 데이터 => Data, Label 분리
data=[]
label=[]

for data in xor_data:
    data.append([data[0],data[1]])
    label.append(data[2])

# 데이터 확인
print(f'data => {data}\nlabel => {label}')

# (3) 학습 ----------------------------------------------
# (3-1) 학습 객체 생성
svcModel=SVC()

# (3-2) 학습 진행 => fit()
svcModel.fit(data, label)
print(f'svcModel SV => {svcModel.support_vectors_}')

# (3-3) 학습 평가 => predict() & 정답률
pre=svcModel.predict(data)

# label - pre 동일 여부 체크 => 정확도
