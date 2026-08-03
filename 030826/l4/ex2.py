def celFah(temp):
    return (temp*(9/5))+32

celcius = int(input("Digite a temperatura em Celcius para tranforma-la em Fahrenheit:\n"))
print(f"{celFah(celcius)}°F")