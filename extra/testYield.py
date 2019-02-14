def testYield():
    n=0
    m=1
    while n<5:
        n=n+1
        m=m*2
        yield n,m

for i,j in testYield():
    print(i,j)
