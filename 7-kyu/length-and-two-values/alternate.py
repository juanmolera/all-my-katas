def alternate(n, first_value, second_value):

    lista = []
    flag = True

    for i in range(0,n):

        if flag:

            lista.append(first_value)
            flag = False

        else:

            lista.append(second_value)
            flag = True

    return lista