# Какое набор значений будет хранить список


# функция в любом случае риймет значение по умолчанию пустой список
def my_function(some_argument: list = []):
    some_argument.append(1)
    return some_argument


# будет использоваться один и тот же список
my_function()  # -> [1]
my_function()  # -> [1, 1]
my_function()  # -> [1, 1, 1]


# функция не будет работать потому, что для изменяемых обьектов нужно передавать позиционные аргументы
def my_function2(some_argument):
    some_argument.append(1)
    return some_argument


# print(my_function2())  # -> TypeError
