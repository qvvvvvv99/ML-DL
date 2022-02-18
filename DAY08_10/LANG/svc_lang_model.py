# --------------------------------------------------------------------------
import os.path

import joblib
import pandas as pd
from sklearn import metrics
from sklearn.svm import SVC

dataFile = '../../Data/LANG/freq.json'

# 데이터 파일 존재 여부 체크
if not os.path.exists(dataFile):
    print(f"{dataFile}이 존재하지 않습니다.")
else:
    # (1) 데이터 파일 로딩
    df = pd.read_json(dataFile)

    # 데이터 확인
    df.info()
    print(f'DATA ----------------------\n{df.head()}')
    print(f'df.index =>{df.index}\ndf.columns =>{df.columns}')

    # (2) 학습용 & 테스트용 데이터 분리
    train_data = df.iloc[0, 0]
    train_label = df.iloc[0, 1]
    test_data = df.iloc[1, 0]
    test_label = df.iloc[1, 1]
    print(f'train_data -----------------\n{train_data}')
    print(f'train_lable ----------------\n{train_label}')

    # (3) 학습 객체 생성
    svcModel = SVC()

    # (4) 학습 진행
    svcModel.fit(train_data, train_label)

    # 에측하기
    predict = svcModel.predict(test_data)
    score=metrics.accuracy_score(test_label, predict)
    metrics.classification_report(test_label, predict)
    print(f'정답률 : {score}')

    # (6) 기준이상 정답률인 경우 모델 저장하기
    if score >= 0.98:
        modelName='../../DATA/LANG/lang.pkl'
        joblib.dump(svcModel, modelName)
        if os.path.exists(modelName): print("save model!")