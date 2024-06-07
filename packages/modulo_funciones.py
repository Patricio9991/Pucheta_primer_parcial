

def mostrar_un_participante(un_participante):
    """mustra informacion de un participante

    Args:
        un_participante (dict): diccionario que ocntiene la info del participatne
    """

    print(f"{un_participante["id_bike"]:<5}  {un_participante["nombre"]:<10}   {un_participante["tipo"]:<10}   {un_participante["tiempo"]:6}")

def mostrar_participantes(lista_dict)->None:
    """muestra en una tabla la informacion de los participantes

    Args:
        lista_dict (dict): lista de diccionarios de participantes
    """
    print("                                *****LISTA PARTICIPANTES******")
    print("id_bike nombre      tipo        tiempo   ")
    print("------------------------------------------------------------------------------")
    for i in range(len(lista_dict)):
        mostrar_un_participante(lista_dict[i])



def valirdar_lista(lista:list)->bool:
    """Valida que se ingrese una lista (aunque este vacia)

    Args:
        lista (list): parametro donde se ingresa la lista

    Raises:
        ValueError: error en caso de que no sea una lista valida

    """

    if not isinstance(lista,list):
        raise ValueError("No se ingreso una lista")

def validar_string(string):
    if not string.isalpha():
        raise ValueError("No se permiten caracteres especiales ni numeros")
    return string

def mapear_lista(proceso,lista:list)->list:
    """mapea una lista segun un determinado criterio

    Args:
        proceso (funcion): funcion criterio
        lista (list): lista para mapear

    Returns:
        list: lista mapeada segun la funcion proceso
    """
    valirdar_lista(lista)
    lista_retorno = []

    for item in lista:
        lista_retorno.append(proceso(item))

    return lista_retorno

def for_each_lista(proceso,lista:list)->list:
    """Aplica cambios a cada elemento de una lista

    Args:
        proceso (funcion): Una funcion que modifica elementos de una lista
        lista (list): lista valida

    """

    valirdar_lista(lista)

    for i in range(len(lista)):
        proceso(lista[i])

def filtrar_lista(filtradora:bool,list:list)->list: 
    """filtra lista segun criterio

    Args:
        filtradora (bool): devuelve True o False
        list (list): lista a filtrar

    Returns:
        list: lista con appends de los resultados True de la filtradora
    """
    valirdar_lista(list)
    lista_filtrada = []
    for i in range(len(list)):
        if filtradora(list[i]):
            lista_filtrada.append(list[i])

    return lista_filtrada


def reduce_list(funcion,lista)-> any:
    """reduce los elementos de la lista a un solo valor

    Args:
        funcion (function): criterio de reduccion
        lista (list): lista valida

    Returns:
        any: devulve el dato reducido
    """
    valirdar_lista(lista)
    anterior = lista[0]

    for el in lista[1:]:
        anterior = funcion(anterior,el)

    return anterior


def calcular_ganador_or_empate(lista:list,tiempo_minimo:int)->list:
    """calcula el ganador de la carrera o los que empataron

    Args:
        lista (list): lista de participantes
        tiempo_minimo (int): tiempo

    Returns:
        retorna una lista con el ganador o los que empataron
    """
    valirdar_lista(lista)

    ganadores = []

    for i in range(len(lista)):
        if lista[i]["tiempo"] == tiempo_minimo:
            ganadores.append([lista[i]["nombre"],lista[i]["tiempo"]])

    return ganadores

def print_ganador_or_empate(lista_ganador:list)->None:
    """imprime por pantalla al ganador o a los que empataron

    Args:
        lista_ganador (list): lsita de ganador o empatados
    """

    valirdar_lista(lista_ganador)

    if len(lista_ganador) == 1:
        print(f"El ganador es {lista_ganador[0][0]}, tiempo: {lista_ganador[0][1]}")
    else:
        print("EMPATE")
        for i in range(len(lista_ganador)):
            print(f"nombre:{lista_ganador[i][0]} | tiempo: {lista_ganador[i][1]}")

def validar_tipo_bici(input_bici:str)->None:
    """verifica que el tipo de bici ingresado se encuentre entre las opciones validas

    Args:
        input_bici (str): tipo de bici

    """

    while input_bici!='BMX' and input_bici!='PASEO' and input_bici!='PLAYERA' and input_bici!='MTB':
        input_bici = input("Invalido. Reingrese un tipo de bici: ")
    return input_bici

def swap_items(lista,i,j):
    """intercambia posiciones de items en una lista
    Args:
        lista (lista): lista
        i (_type_): item posicion i
        j (_type_): item posicion j
    """
    aux = lista[i]
       
    lista[i] = lista[j] 
    
    lista[j]  = aux


def ordenar_competidores_doble(list):
    """ordena competidores por tipo de bici y dentro del tipo por tiempo ascendente

    Args:
        list (dict): lista valida
    """
    valirdar_lista(list)
    tam = len(list)

    for i in range(tam - 1):
        for j in range(i+1, tam):
            if list[i]["tipo"] == list[j]["tipo"]:
                if list[i]["tiempo"] < list[j]["tiempo"]:
                        swap_items(list,i,j) 
            elif list[i]["tipo"] < list[j]["tipo"]:
                swap_items(list,i,j) 

def pause():
    from os import system
    system('pause')