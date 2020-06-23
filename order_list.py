#/usr/bin/env python

def order_list(lista):
    print("-"*30)
    print("Lista original: ", lista)
    print("-"*30)

    # Cantidad de indices en la lista
    l = len(lista)-1

    # Recorrido a los elementos de la lista no ordenados
    while l > 0:
        last_pos = 0
        
        for i in range(0, l+1):
            if lista[i] > lista[last_pos]:
                last_pos = i

        # intercambia los valores en las posiciones
        lista[last_pos], lista[l] = lista[l], lista[last_pos]

        # Cambia el tamaño de la lista a ordenar
        l = l-1

    return lista

elements = [100, 9, 5, 3, 8, 6, 7, 34, 0, 90,-3, 90,-6]
print ("Lista ordenada ", order_list(elements))
print("-"*30)