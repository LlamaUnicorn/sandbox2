
# установим аргумент name_arg пустым а внутри функции будем проверять его
def correct_func(name_arg=None):
   if name_arg is None:
       name_arg = []
   print("Аргумент до изменения", name_arg)
   name_arg.append(1)
   print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
correct_func()
print('-----')
correct_func()
print('-----')
correct_func([123])
print('-----')
correct_func(name_arg=[234])
print('-----')
correct_func()

# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения [123]
# Аргумент после изменения [123, 1]
# -----
# Аргумент до изменения [123]
# Аргумент после изменения [123, 1]



# def counter(func):
#     numcalls = 0
#     def wrap(*args, **kwargs):
#         nonlocal numcalls
#         result = func(*args, **kwargs)
#         numcalls += 1
#         result = func(*args, **kwargs)
#         print(numcalls)
#         return result
#     return wrap

# @counter
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-2)+fib(n-1)
# print(fib(10))