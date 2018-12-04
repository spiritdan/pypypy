name='abc'
address='defg'

print("test{0} and {1}".format(name,address))

#递归函数
def fact(n):
    if n==1:
        return 1
    return n *fact(n-1)

#n=fact(4)
#print(n)

#上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
n=fact_iter(4,1)
print(n)