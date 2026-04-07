#Exercício 16 - Conversão de Temperatura (Celsius -> Fahrenheit)

temp_celsius = float(input("Escreva a temperatura em Graus Celsius (°C): "))

temp_fahrenheit = (temp_celsius * 9 / 5) + 32

print(f"A temperatura de {temp_celsius} °C corresponde a {temp_fahrenheit:.1f} F")

#Exercício 16 - Conversão de Temperatura (Fahrenheit -> Celsius)

temp_fahrenheit2 = float(input("Escreva a temperatura em Graus Fahrenheit (F): "))

temp_celsius2 = (temp_fahrenheit2 - 32) * (5 / 9)

print(f"A temperatura de {temp_fahrenheit2} F corresponde a {temp_celsius2:.1f} °C")