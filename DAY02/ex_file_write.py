# * coding : utf-8 *

# ---------------------------------------
# 파일 입출력 - 파일 쓰기
# ---------------------------------------

filename="test.txt"

# (1) 파일 열기
# mode='w' : 파일 없으면 생성 후 쓰기, 파일 있으면 덮어 쓰기
file=open(filename, mode='w', encoding='utf-8')
# mode='a' : 파일 없으면 생성 후 쓰기, 파일 있으면 마지막 부분에 내용 추가
# file=open(filename, mode='a', encoding='utf-8')
# file.write("0000\n") 파일 마지막 부분에 내용이 추가된다.

# (2) 내용 쓰기
file.write("1234\n")
file.write("Happy New Year\n")
file.write("오늘은 눈이 올까요?\n")

# (3) 파일 닫기
file.close()