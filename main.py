
ls = [1,2,3,4,5,6,7,8,9,10]
x = int(input("sheiyvane cifri:"))
y = int(input("sheiyvane indeqsi:"))
ls.insert(y,x)
print(ls)

def dict():
    saxeli = input("write your name:")
    gvari = input("write your surname:")
    age = input("write your age:")
    return saxeli,gvari,age
ilia = dict()
print(f"you are {ilia}")


sax = ""
while len(sax) == 0:
 sax = input("saxeli:")

gv = ""
while len(gv) == 0:
 gv = input("gvari:")

wl = int(input("asaki:"))

an = ""
while len(an) == 0:
 an = input("do you want to be the member of our crew:")
if wl >= 16 and (an == "yes" or an == "of course"):
    print("congratulation,now you are in!")
elif an == "no":
    print("if you dont want to be the member of the crew,go!")
elif wl < 16:
    print("you are under 16,you cant be member of the crew,bye!")




