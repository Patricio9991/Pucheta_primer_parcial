from packages.modulo_funciones import *
from packages.modulo_menu import *
from leer_escribir_archivos import *
from random import randint



seguir = True
flag_csv = False
flag_tiempos_asignados = False
flag_orden = False

while seguir:

    try:
        match menu():
            case '1':
                nombre_archivo = input("Ingrese nombre del archivo .csv: ")
                data_bikes = leer_procesar_archivo_csv(nombre_archivo)
                flag_csv = True
                break
            case '0':
                break
            case _:
                  print("Primero debe cargar el archivo")
                  pause()
    except FileNotFoundError:
         print("No se encuentra el archivo")
         pause()




while seguir:
        match menu():
            case '2':
                  mostrar_participantes(data_bikes)
            case '3':
                  for_each_lista(lambda a: a.update({"tiempo":randint(50,120)}),data_bikes)
                  flag_tiempos_asignados = True
            case '4':
                if flag_tiempos_asignados:
                    lista_tiempos = mapear_lista(lambda a: a["tiempo"],data_bikes)
                    min_tiempo = reduce_list(lambda ant,sig: ant if ant<sig else sig ,lista_tiempos)

                    primeros_puestos= calcular_ganador_or_empate(data_bikes,min_tiempo)
                    print_ganador_or_empate(primeros_puestos)
                else:
                     print("Aun no se han ingresado los tiempos")
            case '5':
                if flag_tiempos_asignados:
                    opcion = input("Ingrese un tipo de bici: ")

                    tipo_bici_buscado = validar_tipo_bici(opcion)

                    data_filtro_bici = filtrar_lista(lambda a: a["tipo"] == tipo_bici_buscado,data_bikes)

                    nombre_archivo = tipo_bici_buscado + "_file.csv"

                    escribir_archivo_csv(nombre_archivo,data_filtro_bici) 
                else:
                     print("Aun no se han ingresado los tiempos")
            case '6':
                tipos_bici = list(set(mapear_lista(lambda a : a["tipo"],data_bikes)))
                    
                for i in range(len(tipos_bici)):
                    lista_filtrado_por_tipo = filtrar_lista(lambda a : a["tipo"] == tipos_bici[i],data_bikes)
    
                    lista_tiempos = mapear_lista(lambda a: a["tiempo"],lista_filtrado_por_tipo)
    
                    suma_tiempos = reduce_list(lambda ant,act: ant+act,lista_tiempos)
                    promedio = suma_tiempos / len(lista_tiempos)

                    print(f"El promedio de tipo:{tipos_bici[i]}, es {promedio:.2f}")
            case '7':
                if flag_tiempos_asignados:
                    ordenar_competidores_doble(data_bikes)
                    flag_orden = True
                    mostrar_participantes(data_bikes)
                else:
                     print("Aun no se han ingresado los tiempos")
            case '8':
                if flag_tiempos_asignados and  flag_orden:
                    escribir_archivo_json(data_bikes,"orden_tipo_tiempo.json")
                   
                else:
                     print("Debe asignar tiempos y ordenar para continuar")
            case '0':
                  break
                       
        pause()
                  
                     
                  
        





