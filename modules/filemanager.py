from ast import arg
from dbm import dumb
import json
RUTA_DATA = 'data/'

def check_file() -> bool:
    try:
        with open (RUTA_DATA, 'r') as f:
            return True
            f.close()
    except:
        return False

# *arg integra los parametros enviados dentro de una tupla, para poder almacenar multiples datos
def Create_file(*args): 
    with open(RUTA_DATA, 'w') as wf:
        json.dump(args[0], wf, indent=4)
        wf.close()

def Read_file():
    with open (RUTA_DATA, 'r') as rf:
        return json.load(rf)

def add_info(llave_pp, categoria, llave_cat, info):
    """
    Ingrese la información que desea guardar
    """
    with open(RUTA_DATA, 'r+') as rwf:
        data_file = json.load(rwf)
        data_file[llave_pp][categoria][llave_cat].append(info)
        rwf.seek(0)
        json.dump(data_file, rwf, indent= 4)
        rwf.close()