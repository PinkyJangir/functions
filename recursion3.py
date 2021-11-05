def GCD (p,q):
    if q==p:
        return p
    else:
        return(GCD(q,p%2))
p=int(input("enter the first vlue"))
q=int(input("enter the second value"))
z=GCD(p,q)
print(z)