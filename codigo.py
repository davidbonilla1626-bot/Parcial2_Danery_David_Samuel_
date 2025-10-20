from prettytable import PrettyTable

# Crear tabla y definir columnas
tabla = PrettyTable(["Nombre", "Edad", "Carrera"])

# Agregar filas
tabla.add_row(["Samuel", 20, "Informática"])
tabla.add_row(["David", 22, "Ingeniería"])
tabla.add_row(["Danery", 21, "Computación"])

# Alinear al centro
tabla.align = "c"

print(tabla)