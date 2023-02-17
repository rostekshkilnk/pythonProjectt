class Grandparent:
    def about(self):
        print('I am grandparent')
    def about_myself(self):
        print('I am grandparent')
class Parent(Grandparent):
    def about_myslef(self):
        print('I am parent')
class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()
nick = Child()


