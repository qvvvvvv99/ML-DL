import yaml

# YAML 정의하기
yaml_str = ""

fileName='test.yaml'

with open(fileName, mode='r', encoding='utf-8') as f:
  data=yaml.load(f, Loader=yaml.FullLoader)

for item in data:
    print(item["name"], item["age"])