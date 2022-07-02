import modules.filemanager as fm

def Buscar(data : dict, filtro : tuple, llave_principal, codigop):
    Lista_datos = []
    for item in data[llave_principal]:
        Lista_datos = item.get(filtro[1], -1)
        if Lista_datos != -1:
            break
    for i, producto in enumerate(Lista_datos):
        if codigop in producto['codigo']:
            return i


def Mostrar_producto(data : dict, filtro : tuple, llave_principal):
    codigo = input('Ingrese el codigo del producto a buscar: ')
    i = Buscar(data, filtro, llave_principal, codigo)
    print(f'''
Codigo : {data[llave_principal][filtro[0]][filtro[1]][i]["codigo"]}
Nombre : {data[llave_principal][filtro[0]][filtro[1]][i]["nombre"]}
Cantidad : {data[llave_principal][filtro[0]][filtro[1]][i]["cantidad"]}
    ''')


def Borrar_producto(data : dict, filtro : tuple, llave_principal):
    codigo = input('Ingrese el codigo del producto a borrar: ')
    i = Buscar(data, filtro, llave_principal, codigo)
    print(f'''
Codigo : {data[llave_principal][filtro[0]][filtro[1]][i]["codigo"]}
Nombre : {data[llave_principal][filtro[0]][filtro[1]][i]["nombre"]}
Cantidad : {data[llave_principal][filtro[0]][filtro[1]][i]["cantidad"]}
    ''')
    data[llave_principal][filtro[0]][filtro[1]].pop(i)
    print('Registro eliminado correctamente')
    fm.Create_file(data)


def Modificar_producto(data : dict, filtro : tuple, llave_principal):
    codigo = input('Ingrese el codigo del producto a modificar: ')
    i = Buscar(data, filtro, llave_principal, codigo)
    print(f'''
Codigo : {data[llave_principal][filtro[0]][filtro[1]][i]["codigo"]}
Nombre : {data[llave_principal][filtro[0]][filtro[1]][i]["nombre"]}
Cantidad : {data[llave_principal][filtro[0]][filtro[1]][i]["cantidad"]}
    ''')
    opc = input('''
Desea actualizar el codigo?
presione una tecla y Enter para si
presione solo Enter para no
    ''')
    if opc:
        data[llave_principal][filtro[0]][filtro[1]][i]["codigo"] = input('Ingrese el nuevo codigo: ')
    opc = input('''
Desea actualizar el nombre?
presione una tecla y Enter para si
presione solo Enter para no
    ''')
    if opc:
        data[llave_principal][filtro[0]][filtro[1]][i]["nombre"] = input('Ingrese el nuevo nombre: ')
    opc = input('''
Desea actualizar la cantidad?
presione una tecla y Enter para si
presione solo Enter para no
    ''')
    if opc:    
        data[llave_principal][filtro[0]][filtro[1]][i]["cantidad"] = int(input('Actualice la cantidad: '))

    print('Registro a sido actualizado correctamente')
    fm.Create_file(data)