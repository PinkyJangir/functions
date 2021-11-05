def shownumber(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i,'even')
        else:
            print(i,'odd')
        i=i+1
num=int(input('enter thenumber'))
shownumber(num)