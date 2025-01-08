# 아이고님 평균 풀이
''''''
students = {
    "학생1": {"국어": 83, "영어": 92, "수학": 88},
    "학생2": {"국어": 90, "영어": 79, "수학": 94},
    "학생3": {"국어": 88, "영어": 86, "수학": 94}
} #딕셔너리 안에 딕셔너리 (중첩)

for student, scores in students.items():
    total_score = sum(scores.values()) # 국어 영어 수학 점수의 합계
    average_score = total_score / len(scores) # 평균 계산
    print(f"{student}의 평균 점수: {average_score:.2f}")
    round(average_score, 2)