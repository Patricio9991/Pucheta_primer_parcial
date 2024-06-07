import json


def get_path_actual(nombre_archivo:str):
    """Obtiene el path desde donde abrimos el archivo 
    y devuelve la direccion concatenada con el nombre del archivo

    Args:
        nombre_archivo (str): nombre del archivo y extension

    Returns:
        str: direccion del directorio actual con el nombre del archivo incluido
    """

    import os  

    directorio_actual = os.path.dirname(__file__)

    return os.path.join(directorio_actual,nombre_archivo)


def leer_procesar_archivo_json(nombre_archivo:str)->list:
    """Lee un archivo json y lo transforma en una lista de diccionaros

    Args:
        nombre_archivo (str): Nombre del archivo json para leer

    Returns:
        list: lsita de diccionarios extraidos del json
    """
    with open(get_path_actual(nombre_archivo),'r',encoding="utf-8") as archivo:
        
        archivo_json = json.load(archivo)

    return archivo_json

def escribir_archivo_json(archivo_json,nombre_archivo):
    """Crea y escribe un archivo json

    Args:
        archivo_json (list[dict]): lista de origen
        nombre_archivo (str): nombre del archivo que se va a crear
    """
    with open(get_path_actual(nombre_archivo),'w',encoding="utf-8") as archivo:
        json.dump(archivo_json,archivo,indent = 4)


def leer_procesar_archivo_csv(nombre_archivo)->list:

    with open(get_path_actual(nombre_archivo),'r',encoding="utf-8") as archivo:
        encabezado = archivo.readline().strip("\n").split(",")
        
        lista = []
        lineas = archivo.readlines()
        for linea in lineas:
            persona = {}
            linea = linea.strip("\n").split(",")
            id_bike,nombre,tipo,tiempo = linea
            persona["id_bike"] = int(id_bike)
            persona["nombre"] = nombre
            persona["tipo"] = tipo
            persona["tiempo"] = int(tiempo)
       
            lista.append(persona)

        return lista

def escribir_archivo_csv(nombre_archivo:str,lista_de_lectura:list):
    """Convierte una lista a archivo CSV

    Args:
        nombre_archivo (str): Nombre del archivo en .csv
        lista_de_lectura (list): lista de origen
    """
    with open(get_path_actual(nombre_archivo),'w',encoding="utf-8") as archivo:

        keys = list(lista_de_lectura[0].keys())
        print(keys)

        encabezado = ",".join(keys) + "\n" #lo vuelve una cadena de nuevo
        print(encabezado)
        archivo.write(encabezado)

        for item in lista_de_lectura:   #aca iria la lista
            values = list(item.values())
            l = []
            for value in values:
                if isinstance(value,int):
                    l.append(str(value))
                elif isinstance(value,float):
                    l.append(str(value))
                else:
                    l.append(value)

            linea = ",".join(l) + "\n"
            archivo.write(linea)