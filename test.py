import time
list=[1,2,3,4,5,6,7,8]

a=[str(list[n-1])+'+'+str(list[n]) for n in range(1,len(list))]
print(a)

words='t'
print(words.split())

for i in words.split():
    print('\n'.join([''.join([(i[(x-y) % len(i)]
    if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0
    else ' ')
    for x in range(-30, 30)]) for y in range(12, -12, -1)]))
    time.sleep(1.5)
