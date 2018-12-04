class Food():
#定义一个食物的类别
    delicious = True
    #属性“好吃”为真
    def taste(self,people):
    #定义一个“品尝”的方法，参数有两个。其中self是系统预设关键词，代表的是这个对象本身，调用该方法时可省略这个参数的填写。
    #people是吃食物的人。
        print(people,'说：真香！')
        #输出people,'说：真香！'
zhaji = Food()
#定义一个食物，炸鸡
print(type(zhaji))
#输出食物炸鸡的数据类型
print(zhaji.delicious)
#输出食物炸鸡的delicious属性
zhaji.taste('wufeng')
#调用品尝的方法，吴枫吃掉炸鸡