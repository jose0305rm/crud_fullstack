from databse import connect_db

def parse_json(data):
    lista_dic = []

    for tupla in data:
        diccionario ={
            "id": tupla[0],
            "nombre": tupla[1],
            "apellido": tupla[2],
            "correo": tupla[3],
            "puesto": tupla[4],
        }

        lista_dic.append(diccionario)

    return lista_dic


def select():
    try:
        connection = connect_db()

        if connection:
            cursor = connection.cursor() #extrae todos la base de datos
            cursor.execute("SELECT * FROM empleados")  # Extrae todos los datos de la tabla registros
            datos = cursor.fetchall() # guarda los datos del query anterior (devuelve una lista de tuplas) 
            # [(1,nombre1,apellido1) , (2,nombre2,apellido2)]

            # cerramos la base de datos
            cursor.close()              

            # Imprimir los datos obtenidos (como prueba en saber si funciona)
            # for dato in datos:
            # print(dato)

            lista = parse_json(datos)
            return lista

    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

print(select())  # Llamada de prueba para verificar que la función funciona correctamente