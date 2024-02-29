class Dog:
    '''a simple attemp to model a dog'''
    def __init__(self, name, age):
        '''initialize name and age attribute'''
        self.name = name
        self.age = age

    def sit(self):
        # return f'{self.name} is now sitting'
        print(f'{self.name} is now sitting')

    def roll_over(self):
        print((f'{self.name} rolled over !'))


dog = Dog('zooey', 10)

print(dog.name, dog.age)
dog.sit()
