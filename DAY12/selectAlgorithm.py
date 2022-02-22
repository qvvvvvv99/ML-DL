# -----------------------------------------------------------------------
# 해당 데이터를 학습할 최고 성능의 학습 방법 찾기
# -----------------------------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.utils import all_estimators
import warnings

# 데이터 변수 선언 ----------------------------------------------------------
CSV_FILE='../Data/iris2.csv'

iris_data=pd.read_csv(CSV_FILE, encoding="utf-8")

y=iris_data.loc[:, iris_data.columns[-1]]
x=iris_data.loc[:, iris_data.columns[:-1]]

x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)

warnings.filterwarnings('ignore')
allAlgoritms = all_estimators(type_filter="classifier")

allscores={}
for(name, algorithm) in allAlgoritms:
    try:
        clf=algorithm()
        clf.fit(x_train, y_train)
        y_pred=clf.predict(x_test)
        scores=round(accuracy_score(y_test, y_pred), 2)
        allscores[name]=scores
        print(name,"의 정답률 = ", scores)
    except Exception:
        pass
sr=pd.Series(allscores)
print('--------------- CLASSIFICATION ---------------')
print(sr.sort_values(ascending=False))
print('----------------------------------------------')