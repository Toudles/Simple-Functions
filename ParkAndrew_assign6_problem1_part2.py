#determine the max between the 2 with inequality
def maximum(x,y):
    if(x>y):
        return x
    else:
        return y
        
#same as max but for min instead
def minimum(x,y):
    if(x<y):
        return x
    else:
        return y
a=5
b=10
c=15
d=20

#test code
ans1=maximum(a,b)
ans2=maximum(a,c)
ans3=maximum(a,d)
print(ans1,ans2,ans3)

ans4=minimum(d,c)
ans5=minimum(d,b)
ans6=minimum(d,a)
print(ans4,ans5,ans6)

ans7=maximum(maximum(a,b),maximum(c,d))
print("The biggest is:",ans7)
