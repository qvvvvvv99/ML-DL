# ----------------------------------------------------------
# 비만도 판별을 위한 데이터 생성
# => 파일명 : bmi.csv
# => 데이터 : 기, 몸모게, BMI
# ----------------------------------------------------------
import os
import random

dataDir='../Data/BMI/'
dataFile=f'{dataDir}bmi.csv'

# BMI 폴더 존재하지 않을 경우 생성
if not os.path.exists(dataDir): os.mkdir(dataDir)

def calc_bmi(h, w):
    bmi=w/(h/100)**2
    if bmi < 18.5: return "thin"
    if bmi < 25: return "normal"
    return "fat"

# 출력 파일 준비하기
fp=open(dataFile, "w", encoding="utf-8")
fp.write("height,weight,label\r\n")

# 무작위로 데이터 생성하기
cnt={"thin":0, "normal":0, "fat":0}
for i in range(20000):
    h=random.randint(120, 200)
    w=random.randint(35,80)
    label=calc_bmi(h, w)
    cnt[label]+=1
    fp.write("{0},{1},{2}\r\n".format(h, w, label))
fp.close()
print("ok, ", cnt)