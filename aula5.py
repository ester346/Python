# Tipos númericos

import random  # importanto  biblioteca random
num_i = 10  # inteiro
num_f = 5.2  # float
num_c = 1j  # complexo

x = int(num_f)

# Operação de casting para string -- str() --
print("Valor: " + str(x) + " - Tipo: " + str((type(x))))

# Transformando um float (decimal) em um inteiro
x = int(num_f)

# Transformando um inteiro para float
x = float(num_i)

# Random (numéros aleatórios)

# 1. Gerando num aleatórios
num_r = random.randrange(0, 59) # random: gera num aleatórios. randrange: gera inicio da seq e fim da seq de num aleatorios.

x = num_r

print("Valor: " + str(num_r) + " - Tipo: " + str((type(num_r))))

num_r = [  # list
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
]

print("Valor 1: " + str(num_r[0]))
print("Valor 2: " + str(num_r[1]))
print("Valor 3: " + str(num_r[2]))
print("Valor 4: " + str(num_r[3]))
print("Valor 5: " + str(num_r[4]))
print("Valor 6: " + str(num_r[5]))
