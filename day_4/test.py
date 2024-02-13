num=(1,4,8,16.12,3,78,9,64,32,10)
x=1
i=0
while i<len(num):
    if(num[i]==x):
        print("find",i)
    i+=1
else :
    print("not find")