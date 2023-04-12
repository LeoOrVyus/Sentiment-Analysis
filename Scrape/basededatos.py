# Crear un objeto "cursor"
mycursor = mydb.cursor()

# Crear una base de datos llamada "mydatabase"
mycursor.execute("CREATE DATABASE Analisis_twitter")

with open('C:\\Users\\clase\\OneDrive\\Escritorio\\NAO\\sentiment_scores8M.csv', 'r', encoding='utf-8') as file:
    csv_data = csv.reader(file)
    # Saltar la primera fila si contiene nombres de columna
    next(csv_data)
    # Recorrer las filas del archivo CSV y guardar los datos en una lista
    data = []
    for row in csv_data:
        data.append(row)

        # Obtener los nombres de columna del archivo CSV
    column_names = ['Usuario', 'Texto', 'Puntaje_sentimientos']  # Reemplazar con los nombres correctos
    # Crear la tabla en la base de datos
    mycursor.execute("CREATE TABLE Tweets_Analisis (Usuario VARCHAR(100), Texto VARCHAR(1000), Puntaje_sentimientos FLOAT)")

    import csv
import mysql.connector
