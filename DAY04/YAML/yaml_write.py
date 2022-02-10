import yaml

# 파이썬 데이터를 YAML 데이터로 출력하기
customer = [
    {"name": "Inseong", "age": "24", "gender": "man"},
    {"name": "Akatsuki", "age": "22", "gender": "woman"},
    {"name": "Harin", "age": "23", "gender": "man"},
    {"name": "Yuu", "age": "31", "gender": "woman"},
]

# 파이썬 데이터를 YAML 데이터로 변환
yaml_str = yaml.dump(customer)
print(yaml_str)
print("--- --- ---")

# YAML 데이터를 파이썬 데이터로 변환하기
data=yaml.safe_load(yaml_str)

# 이름 출력하기
for p in data:
    print(p["name"])