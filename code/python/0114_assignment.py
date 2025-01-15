# 실습. 타자연습 게임

# 모둘 불러오기
import time, random

words = [
    "Amazon", "bubble", "courage", "dance", "exciting", "freedom", "garden", 
    "hire", "idea", "journey", "kindness", "love", "mountain", "ocean", 
    "peace", "quiet", "rainbow", "sunshine", "tournament", "united", "victory", 
    "wisdom", "xenon", "young", "zero"
]

# 타자 게임 클래스
class TypingGame:
    def start():
        count = 0
        while True:
            start_time = time.perf_counter() # 시간 측정
            word_choice = random.choice(words)
            while True:
                print(f"단어: {word_choice}")
                word_input = input("입력: ")

                if word_input == "exit":
                    end_time = time.perf_counter()

                    print("\n게임 종료!")
                    print(f"총 {count}개의 단어를 입력하셨습니다.")
                    print(f"평균 단어당 입력 시간:{((end_time - start_time) / (count)):.2f}초")
                    return
            
                if word_input == word_choice:
                    count += 1
                    print("통과!")
                    print()
                    break

                else:
                    print("오타! 다시 시도하세요")
                    print()

# 타자 게임 실행
TypingGame.start()

                    

            
                

