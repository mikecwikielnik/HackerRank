N,M=map(int,input().split())
for i in range (N):
    if i <=(N//2)-1:
        s=int(1+(2*i))                 # '.|.' pattern
        t=int((M-(s*3))/2)             # '-' pattern
        print('-'*t+'.|.'*s+'-'*t)
    elif i==N//2:
        s=int((M-7)/2)
        print('-'*s+'WELCOME'+'-'*s)   # WELCOME LINE
    else:
        t=int(2*(N-i)-1)               # '.|.' pattern
        s=int((M-(3*t))/2)             # '-' pattern
        print('-'*s+'.|.'*t+'-'*s)