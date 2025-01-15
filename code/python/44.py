# 타자 연습 게임

import random, time

words = [
    "Amazon", "bubble", "courage", "dance", "exciting", "freedom", "garden", 
    "hire", "idea", "journey", "kindness", "love", "mountain", "ocean", 
    "peace", "quiet", "rainbow", "sunshine", "tournament", "united", "victory", 
    "wisdom", "xenon", "young", "zero"
]

def game():
    print("영어 타자 연습 게임")
    print("게임 종료를 원하시면 exit를 입력하세요")

    total_words = 0 # 게임한 단어 갯수
    start_time = time.time() # 게임 시작 시간

    while True:
        word = random.choice(words)
        print(f"단어:{word}")

        while True:
            user_input = input("입력: ")
            
            if user_input == "exit": # 게임 종료
                end_time = time.time() # .perf_counter()는 디테일하게 측정함
                total_time = end_time - start_time
                print("\n게임종료")
                print(f"총 입력한 단어는 {total_words}개입니다.")
                print(f"총 걸린 시간은 {total_time:.2f}초")
                print(f"단어당 평균 시간은 {total_time / total_words:.2f}초")
                return # 함수를 종료시키는건 return
            
            if user_input == word:
                print("통과!")
                total_words += 1
                break

            else:
                print("오타! 다시 입력하세요")

game()
