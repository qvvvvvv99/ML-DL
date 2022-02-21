import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

mr=pd.read_csv("../Data/MUSH/mush.csv", header=None)

label=[]
data=[]
attr_list=[]

for row_index, row in mr.iterrows():
    label.append(row.iloc[0])
    row_data=[]
    for v in row.iloc[1:]:
        row_data.append(ord(v))
    data.append(row_data)

train_data, test_data, train_label, test_label=train_test_split(data, label)

clf=RandomForestClassifier()
clf.fit(train_data, train_label)

predict=clf.predict(test_data)

ac_score=metrics.accuracy_score(test_label, predict)
cl_report=metrics.classification_report(test_label, predict)
print(f'정답률={ac_score}')
print(f'리포트=\n{cl_report}')