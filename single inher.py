class Animal:
    def legs(self):
        print("i have four legs")

    def fur(self):
            print("My body is covered with fur")

class Dog(Animal):
    def bark(self):
                print("The dog barks")

class Puppy(Dog):
    def young(self):
        print("Young one of a dog is called puppy")
        
d=Puppy()
d.bark()
d.legs()
d.fur()
d.young()


                
