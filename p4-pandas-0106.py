import pandas as pd
import numpy as np
# Samuel Nicola NC 0106
n_filas=5
n_columnas=5
tag_columnas=tuple("ABCDE") # Etiquetas para las columnas de una tupla
print(tag_columnas)
matriz=np.random.randint(1, 6, size=(n_filas, n_columnas))
print("genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
# la variable df es DataFrame
print(matriz)
df = pd.DataFrame(matriz, columns= tag_columnas)
print("--- La tabla o DataFrame --- NC= 0106")
print(df)
print("--- Samuel Nicola NC= 0106---")
