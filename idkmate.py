import random
class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 1
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_work(self):
        print('I will work because I need money')
        self.money += 2

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def to_go_shopping(self):
        print('I need some food dawg')
        self.progress += 1
        self.money -= 3

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print('was too smart(?)')
            self.alive = False
        elif self.money < -10:
            print('too broke so he/she didnt pay taxes so the irs got them')

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f'Money = {self.money}')

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_go_shopping()
        elif live_cube == 5:
            self.to_work()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
kate = Student(name="Kate")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
    if kate.alive == False:
        break
    kate.live(day)
print(nick)
