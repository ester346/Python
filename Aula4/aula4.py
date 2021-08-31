# Tipos de dados no Python

x = 1  # interiro
x = "CBF Cursos"  # string
x = 15.6  # float
x = False  # bool (boleano = True e False. com F e T maiúsculo)
n1 = 5
n2 = 2
x = complex(n1, n2)


# Imprimindo o valor de uma variável

print("O valor: " + str(x))

# Imprimindo o tipo de uma varíavel através da função TYPE

print("O tipo " + str(type(x)))

# Imprimindo um Dado do Tipo Complex (Real e Imaginário)

print(x.real)
print(x.imag)

# Imprimindo  Array

# Coleções no python
# Arrays

x = ["Carro", "Avião", "Navio", 1, 58.3, True]  # List/ Array
x[0] = "Onibus"  # alterando o valor da posição 0.

# o x indica a variável (que é uma lista), e o [0] indica a posição do primeiro elemento da lista.
print("Valor " + x[0])
print("O tipo " + str(type(x)))

# Tupla (a tupla é dirente de um array, porque nela vc n pode alterar um elemente)
x = ("Carro", "Avião", "Navio", 1, 58.3, True)


print("Valor " + x[0])
print("Tipo" + str(type(x)))

# Range (Finalidade criar uma lista de maneira fácil)

x = range(0, 100)  # List (Criou uma list de 0 a 100 posições)
print("Valor " + str(x[0]))
print("Tipo" + str(type(x)))

# Dictonary (Elemento chave e valor)

x = {
    #Dict (Chave -- Valor)
    "Canal": "CFB Cursos",
    "Curso": "Cursos de Python",
    "Nome": "Bruno",
}

print("Valor " + x["Nome"])
print("Tipo" + str(type(x)))

# Set
x = {5, 7, 4, 5, 7, 4, 8}  # set não repete os valores
print("Valor " + str((x)))
print("Tipo" + str(type(x)))

# flozenset

# frozenset tem a finalidade de blockear o set, fazendo que a gente não consiga altera-lo.
x = frozenset({5, 7, 4, 5, 7, 4, 8})
