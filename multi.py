class Breakfirst:
    def meal(self):
        print("Taken in the morning")
class Tea:
    def drink(self):
        print("Mainly served as breakfirst")

class Bread:
    def snack(self):
        print("Eaten along with tea")

class Banana(Breakfirst,Tea,Bread):
    def fruit(self):
        print("Taken as a vitamin in breakfirst")
        
d=Banana()
d.meal()
d.snack()
d.drink()
d.fruit()
