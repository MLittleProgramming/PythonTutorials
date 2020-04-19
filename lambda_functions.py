# double = lambda num, b: num+b
# print(double(5, 6))

def my_function(a):
    return lambda u: a + u


addNum = my_function(1)

print(addNum(2))
