import time
def my_sum(n):
    sum=0
    for i in range(n):
        sum+=i
    return sum


def my_decorator(my_function):
    def wrapper(n):
        start=time.time()
        result=my_function(n)
        end=time.time()
        runtime=end-start
        print('Time taken for program: ', runtime )
        return result
    return wrapper

print(my_sum(1000000))
print(my_decorator(my_sum)(1000000))