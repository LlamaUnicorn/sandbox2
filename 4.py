# -*- coding: utf-8 -*-
def another_function(func):
    """
    Функция которая принимает другую функцию.
    """
    
    def other_func():
        val = "Результат от %s это %s" % (func(),
            eval(func())
        )
        
        return val
    return other_func
 
 
def a_function():
    """Обычная функция"""
    return "1+1"
 
if __name__ == "__main__":
    value = a_function()
    print(value)
    decorator = another_function(a_function)
    print(decorator())
# # Напишите класс SquareFactory с одним статическим методом, принимающим единственный аргумент — сторону квадрата. Данный метод должен возвращать объект класса Square с переданной стороной.

# class Square:
#     def __init__(self, side):
#         self.side = side

# class SquareFactory:
#     @staticmethod
#     def create_square(side):
#         return Square(side)


# sq1 = SquareFactory.create_square(1)
# print(sq1.side)




# def to_jaden_case(string):
#     return string.capitalize()

# quote = "How can mirrors be real if our eyes aren't real"

# x = to_jaden_case(quote)
# print(x)

