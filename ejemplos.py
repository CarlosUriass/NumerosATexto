from numero_a_texto import num_txt

# Ejemplo 1
print(num_txt("123.45", "MXN"))
# Output: "ciento veintitrés pesos con cuarenta y cinco centavos"

# Ejemplo 2
print(num_txt("9876.54", "MXN"))
# Output: "nueve mil ochocientos setenta y seis pesos con cincuenta y cuatro centavos"

# Ejemplo 3
print(num_txt("456.789", "MXN"))
# Output: "cuatrocientos cincuenta y seis pesos con setenta y ocho centavos"

# Ejemplo 4
print(num_txt("9999999.99", "MXN"))
# Output: "nueve millones novecientos noventa y nueve mil novecientos noventa y nueve pesos con noventa y nueve centavos"
