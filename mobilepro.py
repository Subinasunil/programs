fmobile=open("mobile.txt")
all_mobiles=[]
for line in fmobile:
    mobile=line.rstrip("\n").split(",")
    all_mobiles.append(mobile)

print(all_mobiles)
costly_mobiles=max(all_mobiles,key=lambda mob:int(mob[2]))
print(costly_mobiles)
fg=[mob for mob in all_mobiles if mob[3]=="5g"]
print(fg)