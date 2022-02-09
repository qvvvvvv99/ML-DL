filename1='test.txt'
filename2='test_copy.txt'

# 파일 읽기
with open(filename1, mode='r', encoding='utf-8') as f:
    print(f.read())

# 파일 쓰기
with open(filename2, mode='w', encoding='utf-8') as f:
    print(f.write("GOOD"))