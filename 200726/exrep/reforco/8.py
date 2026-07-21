num1 = int(0)
num2 = int(1)
numsoma = 0
for i in range(29):
    numsoma = num1+num2
    num1 = num2
    num2 = numsoma
    print(numsoma)

