l=[]
a=int(input())
for i in range(a):
     b=input()
     l.append(b)
b=set(l)    # set yields only unique values! 
print(len(b))