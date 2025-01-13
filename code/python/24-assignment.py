'''
# Supermarket 클래스

class Supermarket:
    total_customer = 0
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        Supermarket.total_customer += customer

    def print_location(self):
        print(f"위치: {self.location}")
    
    def change_category(self, product2):
        self.product = product2
    
    def show_list(self):
        print(f"상품: {self.product}")

    def enter_customer(self):
        Supermarket.total_customer += 1
    
    def show_info(self):
        print(f"위치: {self.location}, 이름: {self.name}, 상품: {self.product}, 고객수: {Supermarket.total_customer}")

super1 = Supermarket("문래동", "나들가게", "담배", 15)
super1.print_location()
super1.change_category("라면")
super1.enter_customer()
super1.show_info()
super1.enter_customer()
super1.show_info()
super1.change_category("껌")
super1.show_info()
'''

# 건강상태 클래스

class Health:
    total_hp = 0
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def workout(self, hour):
        total_hp = total_hp + 1*hour
        print(f"{hour}시간 운동하다")

    def drink(self, glass):
        total_hp = total_hp - 1*glass
        print(f"술을 {glass}잔 마시다")

    def status(self):
        print(f"{self.name} - hp: {Health.total_hp}")

    if total_hp > 100:
        total_hp = 100
    if total_hp < 1:
        total_hp = 1


person1 = Health("나튼튼", 100)

    

    

