#定义一个食物类
class Yanhuangzisun():
    #属性头发为黑
    hair = 'black'
    #属性皮肤为黄
    skin = 'yellow'
    #属性中国人为真
    chinese = True
    #定义血脉觉醒的方法，两个参数self表示对象本身，words表示咒语
    def xuemaijuexing(self,words):
        #输出咒语
        print(words)
#定义炎黄子孙对象秦王
qinwang = Yanhuangzisun()
#输出秦王头发属性
print(qinwang.hair)
#输出秦王皮肤属性
print(qinwang.skin)
#输出秦王中国人属性
print(qinwang.chinese)
#调用秦王血脉觉醒方法
qinwang.xuemaijuexing('岂曰无衣？与子同裳。王于兴师，修我甲兵。与子偕行。')