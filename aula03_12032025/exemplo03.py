import math
raio = float(input("Digite o raio da circunferencia: "))
comprimento = 2 * math.pi * raio
#area = math.pi * math.pow(raio,2)
#area = math.pi **2
area = math.pi * raio * raio
print(f"O comprimento da circunferencia é igual a {round(comprimento,2)}")
print(f"A área da circunferencia é igual a {round(area,2)}")
