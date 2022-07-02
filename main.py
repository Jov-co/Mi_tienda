import modules.filemanager as fm
import modules.dataManager as dm


template_info = {
    'productos':[
        {
            'frutas' : []
        },
        {
            'verduras' : []
        },
        {
            'lacteos' : []
        },
        {
            'licores' : []
        }
    ]
}
info = {}

def listar_categorias():
    print('******* Seleccione una categoria *******')
    for i, item in enumerate(info['productos']):
        print(f'{i+1}: {list(item.keys())[0]}')
    cat = int(input(': ')) - 1
    llave = list(info['productos'][cat].keys())[0]
    return (cat, llave)

if __name__ == '__main__':
    fm.RUTA_DATA += 'inventario.json'
    if fm.check_file():
        info = fm.Read_file()
    else:
        fm.Create_file(template_info)
    print("""
1. Agregar un producto
2. Buscar un producto
3. Eliminar un producto
    """)
    opcion = int(input(': '))
    if opcion == 1:
        filtro = listar_categorias
        codigo = int(input('Ingrese el codigo: '))
        nombre = input('Ingrese el nombre del producto: ')
        cantidad = int(input('Ingrese la cantidad: '))
        producto = {
            'codigo': codigo,
            'nombre' : nombre,
            'cantidad' : cantidad
        }
        fm.add_info('productos', filtro[0], filtro[1], producto)
    elif opcion == 2:
        filtro = listar_categorias
        dm.buscar(info)
    elif opcion == 3:
        filtro = listar_categorias
