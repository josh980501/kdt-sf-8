# 실습. 상속과 오버라이딩

# 부모 클래스
class Product:
    def __init__(self, name, price, quantity):
        self.name = name # 상품명
        self.price = price # 가격
        self.quantity = quantity # 재고
 
    # 재고 업데이트 메서드
    def update_quantity(self, amount): # amount: 수량
        self.quantity += amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")
        
    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")

class Electronic(Product): # 자식 클래스 1
    def __init__(self, name, price, quantity, warranty_period = 12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period # 보증기간

    # (메서드) 보증기간 연장
    def extend_warranty(self, months):
        self.warranty_period += months
        print(
            f"보증기간이 {months}개월 연장. 현재 보증기간은 {self.warranty_period}개월"
            )
        
    # 오버라이딩
    def display_info(self):
        super().display_info() # 부모 클래스의 display_info() 메서드 호출
        print(
            f"보증기간: {self.warranty_period}개월"
        ) # 자식 크래스 1에서만 추가되는 코드


class Food(Product): # 자식 클래스 2
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date # 유통기한

    # (메서드) 유통기한 확인
    def is_expired(self, current_date): # current_date: 현재 날짜
        if current_date > self.expiration_date: # 문자열 자료형에서도 비교 연산자 사용 가능. 사전순서.
            print(f"{self.name}은(는) 유통기한이 지났습니다.")
        else:
            print(f"{self.name}은(는) 유통기한이 지나지 않았습니다.")

    # (메서드) 오버 라이딩
    def display_info(self):
        super().display_info()
        print(f"유통기한: {self.expiration_date}")



tv = Electronic("삼성 스마트 TV", 1500000, 2, 24)
tv.display_info() # 상품정보 출력
tv.extend_warranty(12) # 보증 기간 연장
tv.update_quantity(3) # TV 재고 3개 확보
tv.update_quantity(-2) # TV 재고 2개 판매
tv.display_info() # 상품정보 출력
print()

milk = Food("초코에몽", 3000, 56, "2025-05-31")
milk.is_expired("2025-01-14")
milk.is_expired("2025-06-14")
milk.display_info()
