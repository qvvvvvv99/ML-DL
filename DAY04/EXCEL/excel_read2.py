import openpyxl

filename="stats_100701.xlsx"
book=openpyxl.load_workbook(filename)

# 맨 앞의 시트 추출하기
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출하기
data=[]
for row in sheet.rows:
    data.append([
        row[0].value,
        row[8].value
    ])

# 필요없는 줄 제거하기
for i in range(4):
    del data[0]

print(data)

# 데이터 인구 순으로 정렬
data=sorted(data, key=lambda x:x[1])

# 하위 5위를 출력
for i, a in enumerate(data):
    if(i>=5): break
    print(i+1, a[0], int(a[1]))