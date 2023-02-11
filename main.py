import random

brand_list = {'Toshiba': {"storage": 100, "power": 10},
              'Bochs': {"storage": 30, "power": 30},
              'Panasonic': {"storage": 60, "power": 30}}


class Human:
    def __init__(self, name="Human"):
        self.name = name

    def clothes(self, amount=0):
        self.amount = amount
        return self.amount


class Machine:
    def __init__(self, clothes=0):
        self.brand = random.choice(list(brand_list))
        self.storage = brand_list[self.brand]["storage"]
        self.power = brand_list[self.brand]["power"]
        print(f'Brand: {self.brand}')
        print(f'Storage: {self.storage}')
        print(f'Power: {self.power}')
        self.progress(clothes)

    def progress(self, clothes):
        print(f"Wash will be completed in {(100 - self.power) * (clothes / self.storage)} minutes")


human = Human(input("What is your name? - "))
number = int(input(f"Amount of clothes that {human.name} will give - "))
machine = Machine(human.clothes(number))
