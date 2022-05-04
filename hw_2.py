def your_function(*args,**kwargs):
    global my_list
    my_list = []
    my_list=args
    summ = 0
    for i in my_list:
        try:
            summ += i
        except:
            summ += 0
    return summ
print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1=2))

n=int(input())
def get_sum(n):
    if n==0:
        return 0

    return n+get_sum(n-1)
print(get_sum(n))

n=int(input())
def get_sum(n):
    if n==0:
        return 0
    if n%2==0:
        return n+get_sum(n-1)
    else: return get_sum(n-1)
print(get_sum(n))

n=int(input())
def get_sum(n):
    if n==0:
        return 0
    if n%2!=0:
        return n+get_sum(n-1)
    else: return get_sum(n-1)
print(get_sum(n))

def tryexcept_function(n):
    try:
        n=int(input())
        print(n)
    except:
        print(0)
tryexcept_function(n)