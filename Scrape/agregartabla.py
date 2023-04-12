
# Abrir el archivo CSV
with open('C:\\Users\\clase\\OneDrive\\Escritorio\\NAO\\sentiment_scores8M.csv', 'r', encoding='utf-8') as archivo_csv:
    datos = csv.reader(archivo_csv)
    encabezado = next(datos)  # Ignorar la primera fila (encabezado)

    # Conexión a la base de datos
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Grettel33',
        database='Analisis_twitter'
    )

    # Cursor
    cursor = conexion.cursor()

    # Consulta SQL para insertar datos
    consulta = "INSERT INTO Tweets_Analisis (Usuario, Texto, Puntaje_sentimientos) VALUES (%s, %s, %s)"
    

    # Insertar cada fila en la tabla
    for fila in datos:
        cursor.execute(consulta, (fila[0], fila[1], fila[2]))

    # Confirmar cambios y cerrar cursor y conexión
    conexion.commit()
    cursor.close()
    conexion.close()

print("Datos agregados correctamente")