y = int(input())
x = int(input())
forx = 0
fory = 0
kolvo = 0
napr = 0
while True:  
    if forx == x and fory == y:
        break      
    a = input()
    if a == "стоп":
        break  
    while napr > 3:
        napr -=4      
    if a == "направо":
        kolvo +=1
        napr += 1
    elif a == "налево":
        napr +=3
        kolvo +=1
    elif a == "разворот":
        napr += 2 
        kolvo +=1
        continue
    elif a == "вперёд":
        b = int(input())
        kolvo += 1  
        if napr == 0:         
            forx += b
        elif napr == 2:
            forx -= b
        elif napr ==1:
            fory += b          
        elif napr == 2:
            forx -= b
        elif napr == 3:
            fory -= b
print(kolvo)
if napr == 0:
    print("север")
elif napr == 3:
    print("запад")
elif napr == 2:
    print("юг")
elif napr == 1:
    print("восток")