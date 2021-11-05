def fun():
    t = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
    b=[]
    i=0
    while i<len(t):
        if t[i] not in b:
            b.append(t[i])
        i=i+1
    print(b)
fun()