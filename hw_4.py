import time
def my_sum(a, b):
    return a + b

def my_decorator(my_function):
    def wrapper(a, b):
        start=time.time()
        result=my_function(a, b)
        end=time.time()
        runtime=end-start
        print('Time taken for program: ', runtime )
        return result
    return wrapper

print(my_sum(7,7))
print(my_decorator(my_sum)(7,7))