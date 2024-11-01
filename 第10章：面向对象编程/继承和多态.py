class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    pass

d = Dog()
d.run()
d.eat()

c = Cat ()
c.run()

def run_twice(animal):
    animal.run()
    animal.run()
    return

run_twice(d)
run_twice(c)
run_twice(Animal())
