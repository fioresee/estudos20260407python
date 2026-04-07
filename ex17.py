#Exercício 17 - Calcular a área de um quadrado, um retângulo, um triângulo e um círculo.

#Quadrado
lado_quadrado = float(input("Digite o valor do lado quadrado em cm: "))

area_quadrado = lado_quadrado * lado_quadrado
print(f"A área desse quadrado com lado {lado_quadrado}cm equivale a {area_quadrado:.2f}cm²")

#Retângulo
lado_maior_retangulo = float(input("Digite o valor do lado maior do retângulo em cm: "))
lado_menor_retangulo = float(input("Digite o valor do lado menor do retângulo em cm: "))

area_retangulo = lado_menor_retangulo * lado_maior_retangulo
print(f"A área desse retângulo com lado maior {lado_maior_retangulo}cm e lado menor {lado_menor_retangulo}cm equivale a {area_retangulo:.2f}cm²")

#Triângulo
base_triangulo = float(input("Digite o valor da base do triângulo em cm: "))
altura_triangulo = float(input("Digite o valor da altura do triângulo em cm: "))

area_triangulo = (base_triangulo * altura_triangulo) / 2
print(f"A área desse triângulo com base {base_triangulo}cm e altura {altura_triangulo}cm equivale a {area_triangulo:.2f}cm²")

#Círculo
pi = 3.14
raio_circulo = float(input("Digite o valor do raio do circulo em cm: "))

area_circulo = pi * (raio_circulo * raio_circulo)
print(f"A área desse círculo com raio {raio_circulo}cm equivale a {area_circulo:.2f}cm²")



