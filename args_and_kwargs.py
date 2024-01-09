def add3(a, b, c):
    return sum([a, b, c])

def unpacking1():
    items = [1, 2, 3]
    result = add3(*items)
    print(result)

def unpacking2():
    kwargs = {'a': 1, 'b': 2, 'c': 3}
    result = add3(**kwargs)
    print(result)

def call_function_using_keyword_arguments_example():
    a = 1
    b = 2
    c = 3
    result = add3(a=a, b=b, c=c)
    print(result)

def add_n(*args):
    return sum(args)

def add_kwargs(a, b):
    return a + b

def universal_acceptor(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword arguments:", kwargs)

# Testing the functions
unpacking1() 
unpacking2()  
call_function_using_keyword_arguments_example()

result_add_n = add_n(1, 2, 3, 4)
print(result_add_n)

result_add_kwargs = add_kwargs(a=5, b=3)
print(result_add_kwargs) 

universal_acceptor(1, 2, 'a', name='John', age=25)
