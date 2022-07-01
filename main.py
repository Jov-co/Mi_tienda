from cgi import print_form
import modules.filemanager as fm

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

if __name__ == '__main__':
    fm.RUTA_DATA += 'inventario.json'
    if fm.check_file():
        info = fm.Read_file()
    else:
        fm.Create_file(template_info)
    print('******* Seleccione una categoria *******')
    for i, item in enumerate(info['productos']):
        print(f'{i+1}: {list(item.keys())[0]}')
    cat = int(input(': ')) - 1
    llave = list(info['productos'][cat].keys())[0]
    print(llave)