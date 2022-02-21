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
with open(dataFile, "w", encoding="utf-8") as fp:
    # csv 파일의 첫번째 줄에 컬럼명 추가
    fp.write("height,weight,bmi\n")

    # 무작위로 데이터 생성하기
    for i in range(20000):
        h=random.randint(120, 200)  # 120~200 의 random int
        w=random.randint(35,80)
        label=calc_bmi(h, w)
        fp.write("{0},{1},{2}\n".format(h, w, label))

if os.path.exists(dataFile):
    print("Create Data File OK")
else : print("Fail! check your code..")