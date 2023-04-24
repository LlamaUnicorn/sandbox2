# print("i am", 25, 'years old')

# a = ["asd", "bbd", "ddfa", "mcsa"]

# print(list(len(i) for i in a))
# print(list(map(len, a)))

# a = ["это", "маленький", "текст", "обидно"]
# print(list(map(str.upper, a)))

# print(list(x.upper() for x in a))


# def D(a, b, c):
#     return b ** 2 - 4 * a * c


# def quadratic_solve(a, b, c):
#     if D(a, b, c) < 0:
#         return "Нет вещественных корней"
#     elif D(a, b, c) == 0:
#         return -b / (2 * a)
#     else:
#         return (-b - D(a,b,c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)

# list_ = [1, 0, -1]

# x = quadratic_solve(1, 0, -1)
# print(x)


# # *list = list items as *args
# x = quadratic_solve(*list_)
# print(x)

# a = "foo"
# b = "bar"

# print(1 and a or b)


# a = None # пустая строка
# b = a or 1
# print(b)


# some_var = (2,)

# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))


# text = "The Zen of Python"

# unique = set(text)

# print("Количество уникальных символов: ", len(unique))


# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])

# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])

# print(list_id_before)
# print(list_id_after)
# print(list_id_before == list_id_after)

# a = 0
# b = 0

# while id(a) == id(b):
#     a -= 1
#     b -= 1

# print(a)

# a = 0
# b = 0

# while id(a) == id(b):
#     a += 1
#     b += 1

# print(a)

# L = ['a', 'b', 'c']
# print(id(L))

# L.append('d')
# print(id(L))

