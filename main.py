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


dog2 = Dog('Buddy')
print(dog2.name)
dog2.name = 'Buddy Jr.'
print(dog2.name)
