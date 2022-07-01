
f=open("abc.txt","w")
lst=["c","python","javascript"]
for lan in lst:
    lan+="\n"
    f.write(lan)