def quadratic_function(x):
    return x ** 2 - 2 * x + 1


for i in range(-5, 6):
    print("f({0}) = {1}".format(i, quadratic_function(i)))
