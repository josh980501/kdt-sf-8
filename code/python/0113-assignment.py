'''
# 부모 클래스
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # 재고 업데이트 메서드
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")
        
    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")

# 자식 1
class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period = 12):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.warranty_period = warranty_period

    def extend_warranty(self, months):
        self.warranty_period += months
        print(f"보증 기간이 {months}개월 연장되었습니다. 현재 보증기간: {self.warranty_period}개월")
    
    def display_info(self):
        super().display_info()
        print(f"보증 기간: {self.warranty_period}개월")

# 자식 2
class Food(Product):

    def __init__(self, name, price, quantity, expiration_date):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date

    def is_expired(self, current_date):
        ex_year, ex_month, ex_day = map(int, self.expiration_date.split("-"))
        year, month, day = map(int, current_date.split("-")) #split: 쪼개서 문자열로, 각각 int로 바꿔서 대입
        if ex_year < year:
            print(f"{self.name}는 유통기한이 지났습니다.")
        if ex_year > year:
            print(f"{self.name}는 유통기한이 지나지 않았습니다.")
        if ex_year == year and ex_month < month:
            print(f"{self.name}는 유통기한이 지났습니다.")
        if ex_year == year and ex_month > month:
            print(f"{self.name}는 유통기한이 지나지 않았습니다.")
        if ex_year == year and ex_month == month and ex_day < day:
            print(f"{self.name}는 유통기한이 지났습니다.")
        if ex_year == year and ex_month == month and ex_day >= day:
            print(f"{self.name}는 유통기한이 지나지 않았습니다.")
        
    def display_info(self):
        super().display_info()
        print(f"유통기한: {self.expiration_date}")
        
e1 = Electronic("스마트 TV", 1500000, 5, 24)
e1.display_info()
e1.extend_warranty(12)
e1.display_info()

f1 = Food("사과", 3000, 50, "2025-05-04")
f1.is_expired("2025-05-04")
f1.is_expired("2025-05-31")
f1.display_info()
'''

# 실습 종합 프로그래밍
# 날짜별 전력 사용량
electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]

from abc import ABC, abstractmethod # abc 모듈로부터 ABC, abstractmethod 불러온다는 뜻


class ElectricityData:
    def __init__(self, usage_data, total_usage):
        self.__usage_data = usage_data
        self.__total_usage = total_usage

    # getter, setter
    @property
    def usage_data(self):
        return self.__usage_data
    
    @property
    def total_usage(self):
        return self.__total_usage
    
    @usage_data.setter
    def usage_data(self, value):
        self.__usage_data = value

    @total_usage.setter
    def total_usage(self, value):
        self.__total_usage = value
    
    # 추상 메서드: 선언만 되어 있고, 구현하지 않은 메서드
    @abstractmethod
    def calculate_total_usage(self):
        pass
    
    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    # 일반 메서드
    def add_usage(self, date, usage):
        self.date = date
        self.usage = usage
        electricity_usage.append({"date": self.date, "usage": self.usage})
    def remove_usage(self, date):
        self.date = date
        del_elec_data = list(map(lambda x: x['date'] == self.date, electricity_usage)) 
        electricity_usage.remove(del_elec_data)

class HomeElectricityData(ElectricityData):
    pass