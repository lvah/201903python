import  time

def desc(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fun(*args, **kwargs)
        end_time = time.time()
        print("%s run %.5f" %(fun.__name__, end_time-start_time))
        # wrapper需要返回的是被装饰函数的返回值；
        return  result
    return  wrapper



@desc   # add=desc(add)   ====> add = wrapper
def add(x:int, y:int)->int:
    return  x + y


result = add(1, 2)  # wrapper()
print(result)
