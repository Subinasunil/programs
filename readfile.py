f=open("abc.txt")
# for line in f:
#     print(line)
out=[line.rstrip("\n") for line in f]

print(out)