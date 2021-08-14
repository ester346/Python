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


# 1. Coleções no python
# 1.1 Arrays

x = ["Carro", "Avião", "Navio", 1, 58.3, True]  # List/ Array
x[0] = "Onibus"  # alterando o valor da posição 0.

# Imprimindo  um Dado tipo Array
# o x indica a variável (que é uma lista), e o [0] indica a posição do (primeiro) elemento da lista.
print("Valor " + x[0])
print("O tipo " + str(type(x)))

# 1.2 Tupla (a tupla é dirente de um array, porque nela vc n pode alterar um elemento)

x = ("Carro", "Avião", "Navio", 1, 58.3, True) # Uma lista pode possuir mais de um Tipo de Dado

# Imprimindo uma lista de dados Tipo Tupla 
print("Valor " + x[0])
print("Tipo" + str(type(x)))

# 1.3 Range (Finalidade criar uma lista de maneira fácil)

x = range(0, 100)  # List (Criou uma list de 0 a 100 posições)

# Imprimido uma lista de dados tipo Range 
print("Valor " + str(x[0]))
print("Tipo" + str(type(x)))

# 1.4 Dictonary (Elemento chave e valor)

# Declarando uma Dictonary
x = {
    #Dict (Chave -- Valor)
    "Canal": "CFB Cursos",
    "Curso": "Cursos de Python",
    "Nome": "Bruno",
}

# Imprimindo uma Dictonary 
print("Valor " + x["Nome"])
print("Tipo" + str(type(x)))

# 1.5 Set

x = {5, 7, 4, 5, 7, 4, 8}  # set não repete os valores

#Imprimindo um lista tipo Set 
print("Valor " + str((x)))
print("Tipo" + str(type(x)))

# 1.6 flozenset

# frozenset tem a finalidade de blockear o set, fazendo com q não seja possível altera-lo os valores dos dados.
x = frozenset({5, 7, 4, 5, 7, 4, 8})
