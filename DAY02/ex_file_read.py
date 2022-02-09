filename="test.txt"

# (1) 파일 열기
# mode='r'
file=open(filename, mode='r', encoding='utf-8')

# (2) 내용 읽기
'''
# (2-1) 파일 전체 내용 읽기
alldata=file.read()
print(f'alldata => {alldata}')'''

'''
# (2-2) 한 줄씩 읽기로 전체 내용 읽기
while True:
    line=file.readline()
    if not line: break
    print(f'line => {line.strip()}')'''


# (2-3) 전체 내용을 줄 단위로 한꺼번에 읽기
lines=file.readlines()
print(f'lines => \n{lines}')

# (3) 파일 닫기
file.close()