import json

python_dict = {"name": "Lilly", "age": 20, "city": "Busan", "islogin": True}
json_str = json.dumps(python_dict) # 딕셔너리를 JSON 문자열로 변환 . json은 불리안 소문자로 나옴
print(json_str)
# python_dict: 파이썬의 딕셔너리 객체
# json_str: JSON 형식의 텍스트 데이터

json_obj = json.loads(json_str) # loads(): JSON 문자열을 Python 객체로 변환
print(json_obj)
print(json_obj["name"])