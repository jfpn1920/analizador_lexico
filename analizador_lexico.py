import random
ids = []
titulos = []
textos = []
analisis_lexico = []
cantidad_tokens = []
fechas = []
estados = []
observaciones = []
palabras_reservadas = [
    "if", "else", "elif", "for", "while", "print",
    "input", "True", "False", "and", "or", "not",
    "def", "class", "return", "break", "continue"
]
operadores_aritmeticos = ["+", "-", "*", "/", "%"]
operadores_asignacion = ["=", "+=", "-=", "*=", "/="]
operadores_relacionales = ["==", "!=", ">", "<", ">=", "<="]
simbolos = ["(", ")", "{", "}", "[", "]", ":", ",", ";"]
#--------------------------------------#
#--|menu_principal_analizador_lexico|--#
#--------------------------------------#
while True:
    print("menu principal analizador lexico")
    print("1) crear análisis")
    print("2) editar análisis")
    print("3) eliminar análisis")
    print("4) buscar análisis")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_analisis|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_analisis = 1
        else:
            id_analisis = ids[-1] + 1
        titulo = input("título: ")
        texto = input("texto o código: ")
        fecha = input("fecha: ")
        estado = input("estado (analizado o pendiente): ")
        observacion = input("observación: ")
        tokens = texto.split()
        resultado = ""
        for token in tokens:
            if token in palabras_reservadas:
                tipo = "Palabra reservada"
            elif token.isdigit():
                tipo = "Número"
            elif token in operadores_aritmeticos:
                tipo = "Operador aritmético"
            elif token in operadores_asignacion:
                tipo = "Operador de asignación"
            elif token in operadores_relacionales:
                tipo = "Operador relacional"
            elif token in simbolos:
                tipo = "Símbolo"
            elif token.replace("_", "").isalnum():
                tipo = "Identificador"
            else:
                tipo = "Desconocido"
            resultado += token + " -> " + tipo + " "
        ids.append(id_analisis)
        titulos.append(titulo)
        textos.append(texto)
        analisis_lexico.append(resultado)
        cantidad_tokens.append(len(tokens))
        fechas.append(fecha)
        estados.append(estado)
        observaciones.append(observacion)
        print("análisis registrado correctamente.")
        print("id:", id_analisis)
    #---------------------#
    #--|editar_analisis|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar análisis")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {cantidad_tokens[i]} tokens | {estados[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {titulos[posicion]} | {textos[posicion]}")
                titulos[posicion] = input("nuevo título: ")
                textos[posicion] = input("nuevo texto o código: ")
                fechas[posicion] = input("nueva fecha: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                tokens = textos[posicion].split()
                resultado = ""
                for token in tokens:
                    if token in palabras_reservadas:
                        tipo = "Palabra reservada"
                    elif token.isdigit():
                        tipo = "Número"
                    elif token in operadores_aritmeticos:
                        tipo = "Operador aritmético"
                    elif token in operadores_asignacion:
                        tipo = "Operador de asignación"
                    elif token in operadores_relacionales:
                        tipo = "Operador relacional"
                    elif token in simbolos:
                        tipo = "Símbolo"
                    elif token.replace("_", "").isalnum():
                        tipo = "Identificador"
                    else:
                        tipo = "Desconocido"
                    resultado += token + " -> " + tipo + " "
                analisis_lexico[posicion] = resultado
                cantidad_tokens[posicion] = len(tokens)
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_analisis|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar análisis")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {cantidad_tokens[i]} tokens | {estados[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {textos[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    titulos.pop(posicion)
                    textos.pop(posicion)
                    analisis_lexico.pop(posicion)
                    cantidad_tokens.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_analisis|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar análisis")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("título:", titulos[posicion])
                print("texto:", textos[posicion])
                print("resultado del análisis:")
                print(analisis_lexico[posicion])
                print("cantidad de tokens:", cantidad_tokens[posicion])
                print("fecha:", fechas[posicion])
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            analizados = 0
            pendientes = 0
            total_tokens = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {cantidad_tokens[i]} tokens | {estados[i]}")
                total_tokens += cantidad_tokens[i]
                if estados[i].lower() == "analizado":
                    analizados += 1
                elif estados[i].lower() == "pendiente":
                    pendientes += 1
            promedio = total_tokens / len(ids)
            print("estadísticas analizador lexico")
            print("cantidad de análisis:", len(ids))
            print("análisis completados:", analizados)
            print("análisis pendientes:", pendientes)
            print("total de tokens encontrados:", total_tokens)
            print("promedio de tokens por análisis:", round(promedio, 2))
            posicion = random.randint(0, len(ids) - 1)
            print("análisis seleccionado")
            print("título:", titulos[posicion])
            print("texto:", textos[posicion])
            print("resultado:")
            print(analisis_lexico[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el analizador lexico.")
        break
    else:
        print("opción no válida.")