# 1st function
lst = ['Element', 'start', 'finish']
def append_str(str_lst):
    lst.insert(2, str_lst[2])
    lst.insert(2, str_lst[1])
    lst.insert(2, str_lst[0])
    return lst
print(append_str(['hello', 5, 'John']))

# 2nd function
def func(list):
    a = 0
    dic = {}
    for i in list:
        a = a + 1
        dic.update({i:a})
    print(dic)

list_ = ['x', 5, 'John',]
dict = func(list_)

# 3rd function
def tuple_lst(n):
        a = list(filter(lambda x: x % 2 == 0, n))
        b = list(map(lambda x: x ** 2, n))
        print(a, b)
tuple_lst((1,2,3,4,5))