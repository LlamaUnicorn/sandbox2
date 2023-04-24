class Person:
    def __init__(self, name='Adam', age=13):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is", self.name, 'my age is', self.age)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    

p1 = Person()
p1.myfunc()
p1.set_name('Jeff')
p1.set_age(33)
p1.myfunc()