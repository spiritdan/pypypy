num = [0,1,2,3]
for x in num:
    try:
    #尝试执行下列代码
        print (6/x)
        #使用6除以num中的元素，并输出
    except ZeroDivisionError:
    #除非发生ZeroDivisionError报错，执行下列代码：
        print('0是不能做除数的！')
        #打印“0是不能做除数的！”