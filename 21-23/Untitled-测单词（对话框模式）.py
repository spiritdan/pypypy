#-*- coding: utf-8 -*- 
import requests,json,time
#将Tkinter包的子组件，为其定义别名
import tkinter as tk
#生成root主窗口
root = tk.Tk()
#新建表,单选表
ciku_type = [["GMAT", "GMAT"], ["NGEE", "考研"], ["NCEE", "高考"], ["CET4", "四级"], ["CET6", "六级"], [
    "TEM", "英专"], ["TOEFL", "托福"], ["GRE", "GRE"], ["IELTS", "雅思"], ["NONE", "任意"]]
#新建变量，变量的类为整数变量
va = tk.IntVar()
#新建多个本地变量
for i in range(50):
    locals()['v'+str(i)] = tk.IntVar()
#将本地变量放入列表中
vlist = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24,
         v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43, v44, v45, v46, v47, v48, v49]
#再新建多个本地变量
for i in range(50):
    locals()['var'+str(i)] = tk.IntVar()
#再将本地变量放入列表中
varlist = [var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16, var17, var18, var19, var20, var21, var22, var23, var24,
         var25, var26, var27, var28, var29, var30, var31, var32, var33, var34, var35, var36, var37, var38, var39, var40, var41, var42, var43, var44, var45, var46, var47, var48, var49]
#新建一个多选项返回函数
def callCheckbutton():
    #声明变量为全局变量
    global danci,words_knows,not_knows,word_ranks
    #创建一个空的列表
    danci = []
    words_knows = []
    #创建一个空的列表，用于记录用户认识的单词。
    not_knows = []
    #创建一个空的列表，用于记录用户单词的rank。
    word_ranks = []
    #计数
    m = 0
    #循环执行单词库中的每一项
    for x in words['data']:
        #如果勾选子项目，则变量v*就是真的
        if vlist[m].get()==True:
            #把认识的单词放入表中
            danci.append(x['content'])
            #就把这个单词，追加进列表words_knows。
            words_knows.append(x)
            #把认识的单词的rank放入表中
            word_ranks.append(str(x['rank']))
        else:
        #否则
            #把不认识的单词放入表中
            not_knows.append(x)
            #把不认识的单词的rank放入表中
            word_ranks.append(str(x['rank']))
        m = m+1
#新建一个全选时返回函数
def callCheckbutton_2():
    #声明全局变量
    global danci,words_knows,not_knows,word_ranks
    #创建一个空的列表
    danci = []
    #创建一个空的列表
    words_knows = []
    #创建一个空的列表，用于记录用户认识的单词。
    not_knows = []
    #创建一个空的列表，用于记录用户单词的rank。
    word_ranks = []
    #如果全选勾选时
    if va.get()==True:
        m = 0
        #循环执行单词库中的每一项
        for x in words['data']:
            #就把这个单词，追加进列表
            danci.append(x['content'])
            #就把这个单词，追加进列表words_knows。
            words_knows.append(x)
            #就把这个单词的rank，追加进列表words_knows。
            word_ranks.append(str(x['rank']))
            #把所有单词设为勾选，以保持显示上的一致性
            vlist[m].set(1)
            m = m+1
    else:
        m = 0
        #循环执行单词库中的每一项
        for x in words['data']:
            #把不认识的单词放入表中
            not_knows.append(x)
            #把不认识的单词的rank放入表中
            word_ranks.append(str(x['rank']))
            #把所有单词设为不勾选，以保持显示上的一致性
            vlist[m].set(0)
            m = m+1
#新建类，显示第1个窗口
class firstpage(object):
    #此函数代表执行类时，马上需要执行的代码
    def __init__(self, master=None):
        #root属于最顶层
        self.root = master 
        #在root中建立一框架
        self.page = tk.Frame(self.root) 
        #把框架放入窗口中
        self.page.pack()
        #在框架中建立标签
        tk.Label(self.page, text=u'评估过程包括三步：').grid(sticky='W')
        tk.Label(self.page, text=u'1. 选择适合你的出题范围').grid(sticky='W')
        tk.Label(self.page, text=u'2. 通过50个单词得到你的大致词汇量范围').grid(sticky='W')
        tk.Label(self.page, text=u'3. 检验你是否真的掌握你在第二步中选择的单词').grid(sticky='W')
        #在框架中建立按钮，当按下按钮时，执行函数secpage
        tk.Button(self.page, text=u'下一步',command=self.secpage).grid() 
    #当按下按钮时执行的函数
    def secpage(self):
        #清空框架
        self.page.destroy()
        #执行下一页
        mainpage(self.root)
#新建类，显示主窗口
class mainpage(object):
    #此函数代表执行类时，马上需要执行的代码
    def __init__(self, master=None):
        #root属于最顶层
        self.root = master 
        #在root中建立一框架
        self.page = tk.Frame(self.root)
        #把框架放入窗口中 
        self.page.pack()
        #在框架中建立标签
        tk.Label(self.page, text=u'第 1 步，请选择出题范围\n').grid(columnspan=5,sticky='W')
        #在框架中建立按钮，当按下按钮时，执行函数secpage*
        tk.Button(self.page, text=u' GMAT ',command=self.secpage0).grid(column=0,row=1,sticky='EW') 
        tk.Button(self.page, text=u'   考研   ',command=self.secpage1).grid(column=1,row=1,sticky='EW')
        tk.Button(self.page, text=u'   高考   ',command=self.secpage2).grid(column=2,row=1,sticky='EW')
        tk.Button(self.page, text=u'   四级   ',command=self.secpage3).grid(column=3,row=1,sticky='EW') 
        tk.Button(self.page, text=u'   六级   ',command=self.secpage4).grid(column=4,row=1,sticky='EW') 
        tk.Button(self.page, text=u'   英专   ',command=self.secpage5).grid(column=0,row=2,sticky='EW') 
        tk.Button(self.page, text=u'   托福   ',command=self.secpage6).grid(column=1,row=2,sticky='EW') 
        tk.Button(self.page, text=u'   GRE   ',command=self.secpage7).grid(column=2,row=2,sticky='EW') 
        tk.Button(self.page, text=u'   雅思   ',command=self.secpage8).grid(column=3,row=2,sticky='EW') 
        tk.Button(self.page, text=u'   任意   ',command=self.secpage9).grid(column=4,row=2,sticky='EW')
    #第0个按钮的执行函数 
    def secpage0(self):
        #声明全局变量
        global ciku,words
        #取得词库的名称
        ciku = ciku_type[0][0]
        #按词库名取得网站上的相应的数据
        test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
        #把res数据转化成表或字典
        words = json.loads(test.text)
        #清空框架
        self.page.destroy()
        #执行下一页
        secondpage(self.root)
    #第1个按钮的执行函数
    def secpage1(self):
        global ciku
        ciku = ciku_type[1][0]
        test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
        global words
        words = json.loads(test.text)
        self.page.destroy()
        secondpage(self.root)
    #第2个按钮的执行函数
    def secpage2(self):
        global ciku
        ciku = ciku_type[2][0]
        test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
        global words
        words = json.loads(test.text)
        self.page.destroy()
        secondpage(self.root)
    #第3个按钮的执行函数
    def secpage3(self):
        global ciku
        ciku = ciku_type[3][0]
        test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
        global words
        words = json.loads(test.text)
        self.page.destroy()
        secondpage(self.root)
    #第4个按钮的执行函数
    def secpage4(self):
        global ciku
        ciku = ciku_type[4][0]
        test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
        global words
        words = json.loads(test.text)
        self.page.destroy()
        secondpage(self.root)
    #第5个按钮的执行函数
    def secpage5(self):
        global ciku
        ciku = ciku_type[5][0]
        test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
        global words
        words = json.loads(test.text)
        self.page.destroy()
        secondpage(self.root)
    #第6个按钮的执行函数
    def secpage6(self):
        global ciku
        ciku = ciku_type[6][0]
        test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
        global words
        words = json.loads(test.text)
        self.page.destroy()
        secondpage(self.root)
    #第7个按钮的执行函数
    def secpage7(self):
        global ciku
        ciku = ciku_type[7][0]
        test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
        global words
        words = json.loads(test.text)
        self.page.destroy()
        secondpage(self.root)
    #第8个按钮的执行函数
    def secpage8(self):
        global ciku
        ciku = ciku_type[8][0]
        test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
        global words
        words = json.loads(test.text)
        self.page.destroy()
        secondpage(self.root)
    #第9个按钮的执行函数
    def secpage9(self):
        global ciku
        ciku = ciku_type[9][0]
        test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
        global words
        words = json.loads(test.text)
        self.page.destroy()
        secondpage(self.root)
    
#新建类，显示第二页窗口
class secondpage(object):
    #此函数代表执行类时，马上需要执行的代码
    def __init__(self, master=None):
        #root属于最顶层
        self.root = master
        #在root中建立一框架
        self.page = tk.Frame(self.root)
        #把框架放入窗口中
        self.page.pack()
        #新建一个标签
        tk.Label(self.page, text=u'第 2 步，请选择你认识的单词\n').grid(columnspan=5,sticky='W')
        #新建一个‘全选’的复选项
        tk.Checkbutton(self.page,
                            variable = va,
                            text = '全选',
                            command = callCheckbutton_2).grid(column=9,sticky='E',row=0)
        n = 0
        #新建50个复选项，每一行10个
        for i in words['data']:
            if n<10:
                tk.Checkbutton(self.page,
                            variable = vlist[n],
                            text = i['content'],
                            command = callCheckbutton).grid(column=n,sticky='W',row=1)
            elif n<20:
                tk.Checkbutton(self.page,
                            variable = vlist[n],
                            text = i['content'],
                            command = callCheckbutton).grid(column=n-10,sticky='W',row=2) 
            elif n<30:
                tk.Checkbutton(self.page,
                            variable = vlist[n],
                            text = i['content'],
                            command = callCheckbutton).grid(column=n-20,sticky='W',row=3) 
            elif n<40:
                tk.Checkbutton(self.page,
                            variable = vlist[n],
                            text = i['content'],
                            command = callCheckbutton).grid(column=n-30,sticky='W',row=4)
            else :
                 tk.Checkbutton(self.page,
                            variable = vlist[n],
                            text = i['content'],
                            command = callCheckbutton).grid(column=n-40,sticky='W',row=5)
            n = n+1 
        self.Button = tk.Button(self.page, text=u'下一步',command=self.thipage) 
        self.Button.grid(columnspan=5,sticky='E') 
    #新建一个‘下一页’时的返回函数
    def thipage(self):
        #清空页面框架
        self.page.destroy()
        #执行第三页
        thirdpage(self.root)   
#新建类，显示第三页窗口
class thirdpage(object):
    #此函数代表执行类时，马上需要执行的代码
    def __init__(self, master=None):
        #root属于最顶层
        self.root = master
        #在root中建立一框架
        self.page = tk.Frame(self.root)
        #把框架放入窗口中
        self.page.pack()
        #新建一个标签
        tk.Label(self.page, text=u'第 3 步，单词测试，请选择正确的词义\n').grid(columnspan=5,sticky='W')
        #声明全局变量
        global right_ranks,wrong_words,right_num,slaves01,slaves11,slaves12,slaves13,slaves14,s
        right_ranks = []
        wrong_words = []
        right_num = 0
        slaves01 = []
        slaves11 = []
        slaves12 = []
        slaves13 = []
        slaves14 = []
        n = 0
        #将所有等待测试的单词和四个选择项放在相同的位置
        for y in words_knows:
            tk.Label(self.page, text=y['content']).grid(sticky='NS',row=1,column=0,rowspan=4,ipadx=50)
            #‘anchor=tk.W’代表按钮内的文字左（W代表西方）对齐
            tk.Button(self.page,anchor=tk.W,
                      text='A:'+y['definition_choices'][0]['definition'],
                      command=self.forgetButton0).grid(sticky='EW',row=1,column=1)
            tk.Button(self.page,anchor=tk.W,
                      text='B:'+y['definition_choices'][1]['definition'],
                      command=self.forgetButton1).grid(sticky='EW',row=2,column=1)
            tk.Button(self.page,anchor=tk.W,
                      text='C:'+y['definition_choices'][2]['definition'],
                      command=self.forgetButton2).grid(sticky='EW',row=3,column=1)
            tk.Button(self.page,anchor=tk.W,
                      text='D:'+y['definition_choices'][3]['definition'],
                      command=self.forgetButton3).grid(sticky='EW',row=4,column=1)
            #除最后一组单词外，其它单词全部隐藏
            if n<len(words_knows)-1:
                slaves01.append(self.page.grid_slaves(1,0)[0])
                slaves11.append(self.page.grid_slaves(1,1)[0])
                slaves12.append(self.page.grid_slaves(2,1)[0])
                slaves13.append(self.page.grid_slaves(3,1)[0])
                slaves14.append(self.page.grid_slaves(4,1)[0])
                self.page.grid_slaves(1,0)[0].grid_forget()
                self.page.grid_slaves(1,1)[0].grid_forget()
                self.page.grid_slaves(2,1)[0].grid_forget()
                self.page.grid_slaves(3,1)[0].grid_forget()
                self.page.grid_slaves(4,1)[0].grid_forget()   
            n = n+1
        #新建一个变量，等于单词数量-1
        s = len(slaves01)
    #点击按钮A时，执行此函数
    def forgetButton0(self):
            #声明全局变量
            global right_ranks,wrong_words,right_num,words_knows,s
            #将去掉单词表中最后一个单词并把这个单词赋于y
            y = words_knows.pop()
            #如果y单词中A选项的单词是正确的翻译
            if y['definition_choices'][0]['rank']==y['rank']:
                right_num = right_num+1
                right_ranks.append(str(y['rank']))
            else:
                wrong_words.append(y)
            # grid_slaves返回grid中(0,0)位置的所有组件
            # grid_forget将这个组件从grid中移除（并未删除，可以使用grid再将它显示出来)
            #隐藏正前的单词按钮，显示前一个单词按钮
            if s>0:
                self.page.grid_slaves(1,0)[0].grid_forget()
                self.page.grid_slaves(1,1)[0].grid_forget()
                self.page.grid_slaves(2,1)[0].grid_forget()
                self.page.grid_slaves(3,1)[0].grid_forget()
                self.page.grid_slaves(4,1)[0].grid_forget()
                slaves01[s-1].grid(sticky='NS',row=1,column=0,rowspan=4,ipadx=50)
                slaves11[s-1].grid(sticky='EW',row=1,column=1)
                slaves12[s-1].grid(sticky='EW',row=2,column=1)
                slaves13[s-1].grid(sticky='EW',row=3,column=1)
                slaves14[s-1].grid(sticky='EW',row=4,column=1)
            else:
                self.page.destroy()
                fourthpage(self.root)  
            s = s-1
    def forgetButton1(self):
            global right_ranks,wrong_words,right_num,words_knows,s
            y = words_knows.pop()
            # for y in words_knows:
            if y['definition_choices'][1]['rank']==y['rank']:
                right_num = right_num+1
                right_ranks.append(str(y['rank']))
            else:
                wrong_words.append(y)
            # grid_slaves返回grid中(0,0)位置的所有组件
            # grid_forget将这个组件从grid中移除（并未删除，可以使用grid再将它显示出来)
            if s>0:
                self.page.grid_slaves(1,0)[0].grid_forget()
                self.page.grid_slaves(1,1)[0].grid_forget()
                self.page.grid_slaves(2,1)[0].grid_forget()
                self.page.grid_slaves(3,1)[0].grid_forget()
                self.page.grid_slaves(4,1)[0].grid_forget()
                slaves01[s-1].grid(sticky='NS',row=1,column=0,rowspan=4,ipadx=50)
                slaves11[s-1].grid(sticky='EW',row=1,column=1)
                slaves12[s-1].grid(sticky='EW',row=2,column=1)
                slaves13[s-1].grid(sticky='EW',row=3,column=1)
                slaves14[s-1].grid(sticky='EW',row=4,column=1)
            else:
                self.page.destroy()
                fourthpage(self.root)  
            s = s-1
    def forgetButton2(self):
            global right_ranks,wrong_words,right_num,words_knows,s
            y = words_knows.pop()
            # for y in words_knows:
            if y['definition_choices'][2]['rank']==y['rank']:
                right_num = right_num+1
                right_ranks.append(str(y['rank']))
            else:
                wrong_words.append(y)
            # grid_slaves返回grid中(0,0)位置的所有组件
            # grid_forget将这个组件从grid中移除（并未删除，可以使用grid再将它显示出来)
            if s>0:
                self.page.grid_slaves(1,0)[0].grid_forget()
                self.page.grid_slaves(1,1)[0].grid_forget()
                self.page.grid_slaves(2,1)[0].grid_forget()
                self.page.grid_slaves(3,1)[0].grid_forget()
                self.page.grid_slaves(4,1)[0].grid_forget()
                slaves01[s-1].grid(sticky='NS',row=1,column=0,rowspan=4,ipadx=50)
                slaves11[s-1].grid(sticky='EW',row=1,column=1)
                slaves12[s-1].grid(sticky='EW',row=2,column=1)
                slaves13[s-1].grid(sticky='EW',row=3,column=1)
                slaves14[s-1].grid(sticky='EW',row=4,column=1)
            else:
                self.page.destroy()
                fourthpage(self.root)  
            s = s-1
    def forgetButton3(self):
            global right_ranks,wrong_words,right_num,words_knows,s
            y = words_knows.pop()
            # for y in words_knows:
            if y['definition_choices'][3]['rank']==y['rank']:
                right_num = right_num+1
                right_ranks.append(str(y['rank']))
            else:
                wrong_words.append(y)
            # grid_slaves返回grid中(0,0)位置的所有组件
            # grid_forget将这个组件从grid中移除（并未删除，可以使用grid再将它显示出来)
            if s>0:
                self.page.grid_slaves(1,0)[0].grid_forget()
                self.page.grid_slaves(1,1)[0].grid_forget()
                self.page.grid_slaves(2,1)[0].grid_forget()
                self.page.grid_slaves(3,1)[0].grid_forget()
                self.page.grid_slaves(4,1)[0].grid_forget()
                slaves01[s-1].grid(sticky='NS',row=1,column=0,rowspan=4,ipadx=50)
                slaves11[s-1].grid(sticky='EW',row=1,column=1)
                slaves12[s-1].grid(sticky='EW',row=2,column=1)
                slaves13[s-1].grid(sticky='EW',row=3,column=1)
                slaves14[s-1].grid(sticky='EW',row=4,column=1)
            else:
                self.page.destroy()
                fourthpage(self.root)  
            s = s-1          
    # def foupage(self):
    #     self.page.destroy()
    #     fourthpage(self.root)  
#显示第四页，统计结果
class fourthpage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()
        url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        data_ranks = {'category': ciku,
                    'phase': '',
                    'right_ranks': ','.join(right_ranks),
                    'word_ranks':  ','.join(word_ranks)}
        res_vocab = requests.post(url,headers=headers,data=data_ranks)
        js_vocab = json.loads(res_vocab.text)
        tk.Label(self.page, text='你的词汇量大约是：'+str(js_vocab['data']['vocab'])).grid()
        tk.Label(self.page, text=js_vocab['data']['comment']).grid()
        tk.Label(self.page, text='在上述'+str(len(words['data']))+'个单词中，有'+str(len(danci))+'个是你认识的，有'+str(right_num)+'个是你掌握的,有'+str(len(wrong_words))+'个是你记错的').grid()
        self.Button = tk.Button(self.page, text=u'退出',command=self.quit) 
        self.Button.grid()
    def quit(self):
        self.page.quit()

firstpage(root)
# 设置窗口标题:
root.title('5分钟，评估你的单词量')
# 主消息循环:（必需组件）
root.mainloop() 
# 注意root = tk.Tk()是在class外的
# 這樣destroy就可以確實的破壞原來的頁面

