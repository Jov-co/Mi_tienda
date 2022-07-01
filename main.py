from distutils.log import info
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
        info = fm.Read_file
    else:
        fm.Create_file(template_info)
