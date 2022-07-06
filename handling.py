# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
#
# try:
#     res=num1/num2
#     print(f"result{res}")
#
# except Exception as e:
#     num2=int(input("enter another value num2"))
#     print(num1/num2)
# finally:
#     print("db transaction")
#     print("file operation")

# age=int(input("enter age"))
#
# if(age<18):
#     raise Exception("not eligible for taking booster dose")
# else:
#     print("eligible")

phone_num=(input("enter phone number"))
if(len(phone_num)!=10):
    raise Exception("number must be 10")
else:
    print("valid number")





