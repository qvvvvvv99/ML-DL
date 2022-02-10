import  codecs

filename = "test.csv"
csv=codecs.open(filename, mode="r", encoding="utf-8").read()

# CSV을 파이썬 리스트로 변환하기
data=[]
rows=csv.split("\r\n")
for row in rows:
    if row == "": continue
    cells=row.split(",")
    data.append(cells)

for c in data:
    print(c[1], c[2])