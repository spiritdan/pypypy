def flow():
    x=int(input('输入x：'))
    y=(x**2)*2-4
    if y>0:
        return y
    else:
        print("y={0},y小于0，重新输入x".format(y))
        return flow()


y=flow()
print("y={0}".format(y))