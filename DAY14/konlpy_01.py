from konlpy.tag import Okt

# (1) 형태소 분석기 객체 생성
okt = Okt()

# (2) 문장을 형태소로 분석하기
malList=okt.pos("아버지 가방에 들어가신다.", norm=True, stem=True)

for mal in malList:
    print(mal)