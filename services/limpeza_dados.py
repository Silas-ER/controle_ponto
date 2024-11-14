import pandas as pd
from services.crud import read_atrasos, read_ausencias

#######################################################################################################################################

def avulsos_por_data(data):
    pass

def avulsos_por_mes(mes):
    pass

def atrasos_por_data(data):
    atrasos = read_atrasos()
    atrasos = atrasos[atrasos['data'] == data]
    
    return atrasos
    
def atrasos_por_mes(mes):
    pass

def ausencias_por_data(data):
    pass

def ausencias_por_mes(mes):
    pass