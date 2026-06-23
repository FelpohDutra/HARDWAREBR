x = int(input())
y = int(input())
z = int(input())

if x>y and x>z:
    print(f"{x} eh o maior numero")
elif y>x and y>z:
    print(f"{y} eh o maior numero")
else:
    print(f"{z} eh o maior numero")