
# lis=(1,2,3,4)
# p=lis[0]=5
# print(lis)

# def make_pretty(func):
#     def inner():
#         print("i got decorator ")
#         func()
#     return inner
# def ordinary():
#     print("in am data")
#
#
# dec_fun=make_pretty(ordinary)
# dec_fun()









def sqr(n):
    for i in range(1, n+1):
        yield i*i
a = sqr(3)
print(next(a))
print(next(a))
print(next(a))


