# 내장 함수
numbers = [10, 20, 30, 40]

a = sum(numbers)
print(a)

print(sum(numbers))

scores = {"국어": 83, "영어": 90, "수학": 95}
print(scores.values())
total_score = sum(scores.values())
print(total_score)

print(max(sum))
print(min(sum))

print(max(scores.values()))
print(min(scores.values()))

names = ["Alice", "Bob", "Charlie", "Lilly"] #짝 안맞으면 버림(Lilly 버림)
scores = [80, 90, 95]
zipped = list(zip(names, scores))
zipped2 = dict(zip(names, scores))
print(zipped)
print(zipped2)