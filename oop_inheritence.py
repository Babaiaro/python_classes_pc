class Father:
    def skill1 (self):
        print("Father's skill: Gardening")

class Mother:
    def skill2 (self):
        print("Mother's skill: Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()
    