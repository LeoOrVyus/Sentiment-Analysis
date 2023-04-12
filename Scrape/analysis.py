import pandas as pd
from collections import Counter

# Cargar datos
df = pd.read_csv('sentiment_scoresTammy.csv')
columna = df['Texto']
lista = columna.tolist()

# Contar frecuencia de cada palabra
palabras = {}
for palabra in lista:
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1

# Encontrar las 5 palabras más comunes
counter_palabras = Counter(palabras)
palabras_comunes = counter_palabras.most_common(5)

# Imprimir las palabras más comunes
print("Las 5 palabras más comunes son:")
for palabra, frecuencia in palabras_comunes:
    print(f"{palabra}: {frecuencia} veces")