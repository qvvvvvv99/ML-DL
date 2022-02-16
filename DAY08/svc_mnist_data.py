# --------------------------------------------------------------------
# 목표 : 손글씨 숫자 0 ~ 9 식별
# 데이터 : 6만개 이미지 raw 데이터 + 1만개 이미지 raw 데이터
# 라벨 : 6만개 이미지 라벨 + 1만개 이미지 라벨
# 학습 : 데이터 + 라벨 => 지도 학습 - 분류 => SVC
# --------------------------------------------------------------------
import gzip

from sklearn import metrics
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import urllib.request as req
import os, pandas as pd

# (1) WEB 상에서 다운로드 받기 -------------------------------------------
savepath= "../Data/MNIST/"
baseurl="http://yann.lecun.com/exdb/mnist/"
files=[
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz"
]

# 폴더 존재 여부 체크 후 처리
if not os.path.exists(savepath): os.mkdir(savepath)

# 다운로드 => 파일 형태 => urlretrieve
for f in files:
    url=baseurl+f
    loc=savepath+f
    print("download:", url)
    if not os.path.exists(loc):
        req.urlretrieve(url, loc)

# GZip 압축 해제
for f in files:
    gz_file=savepath+f
    raw_file=savepath+f.replace(".gz", "")
    print("gzip:", f)
    with gzip.open(gz_file, "rb") as fp:
        body=fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)
print("ok")