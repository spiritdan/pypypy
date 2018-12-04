for i in range(1,10):
    for j in range(i):
        #包含end=''作为print()BIF的一个参数，会使该函数关闭“在输出中自动包含换行”的默认行为。
        print(str(i)+'*'+str(j+1)+'='+str(i*(j+1)),end=' ')
    print('')
