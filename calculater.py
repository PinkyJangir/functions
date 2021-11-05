def calculater(a,b, symbel):
    if symbel=='+':
        print(a+b)
    elif symbel== '-':
        print(a-b)
    elif symbel=='*':
        print(a*b)
    elif symbel=='/':
        print(a/b)
    elif symbel=='%':
        print(a%b)
    elif symbel=='//':
        print(a//b)
a=int(input('enter the number'))
b=int(input('enter the second numner'))
symbel=input('emter the symbel')
calculater(a,b,symbel)
