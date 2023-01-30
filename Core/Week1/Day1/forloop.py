#basic
for i in range(151):
    print(i)
#
for i in range(5,1001):
    if i%5==0:
        print(i)
#
for i in range(1,101):
    if i %5==0:
        print("Coding")
    elif i%10==0:
        print("Coding Dojo")
#
sum=0
for i in range(0,500001):
    if i%2==1:
        sum+=i
print(sum)
#
for i in range(2018,0,-4):
    if i>0:
        print(i)
#
lowNum=int(input())
highNum=int(input())
mult=int(input())
for i in range(lowNum,highNum):
    if i % mult==0:
        print(i)