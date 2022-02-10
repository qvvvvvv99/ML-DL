import csv, codecs

filename = "test.csv"
fp=codecs.open(filename, mode="r", encoding="utf-8")

# 한 줄씩 읽어 들이기
reader=csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])