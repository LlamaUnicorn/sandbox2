# @property
class Dog():
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        print('Deleting...')
        del self.__name


dog1 = Dog('Buddy')
print(dog1.name)
dog1.name = 'Buddy Jr.'
print(dog1.name)