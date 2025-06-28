import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.satiety = 40
        self.happiness = 40
        self.cat_avatar = self.set_new_avatar()

    cat_avatar = "images/cat.jpg"

    def set_new_avatar(self):
        Cat.cat_avatar = "images/cat.jpg"
        if self.happiness < 20:
            return "images/cat2.jpg"
        elif self.happiness < 50:
            return "images/cat1.jpg"
        else:
            return "images/cat3.jpg"

    def get_name(self):

        return self.name

    def __str__(self):
        return f"{self.name}: age {self.age}, satiety {self.satiety}, happiness {self.happiness}"

    def play(self):
        if self.happiness > 0:
            self.happiness += 15
            self.satiety -= 10
            if random.random() < 1/3:
                self.happiness = 0
                return "Кот пришел в ярость!"
            return "Вы поиграли с котом!"
        return "Кот спит."

    def eat(self):
        if self.satiety + 15 > 100:
            self.happiness -= 30
            self.satiety = 100
            return "Кот переел."
        else:
            self.satiety += 15
            self.happiness += 5
            return "Кот покормлен!"

    def sleep(self):
        self.happiness = max(0, self.happiness - 5)
        return "Кот уложен спать."