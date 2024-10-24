def check2(chislo):
    col=0
    for i in chislo:
        if i =="0" or i=="1":col+=1
        else: col=0
    if col == len(chislo): return True 
    else: return False
def print_chislo(chislo):
    print("Минимальное число в последовательности:")
    for i in chislo:
        print(i)
    print("===================")
check=1024
min_len=''
s=[]
flag1,flag2=False,False
f=open("test.txt","r")
while True:
    buf = f.readline().split()
    if not buf: break
    for i in range(len(buf)-1):
        if flag1 and flag2:
            print_chislo(min_len)
            flag1,flag2=False,False
        if check2(buf[i]) and check2(buf[i+1]):
            ch1=int(buf[i],2)
            ch2=int(buf[i+1],2)
            if ch1<check and ch2<check:
                if ch1<ch2:
                    if len(s)==0:
                        s.append(buf[i])
                    s.append(buf[i+1])
                    min_len=min(s)
                    flag1=True
                    if i == len(buf)-2:
                        print_chislo(min_len)
                else: 
                    s=[]
                    flag2=True
            else:
                s=[]
                flag2=True
        else:
            s=[]
            flag2=True
f.close()