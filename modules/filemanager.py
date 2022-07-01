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