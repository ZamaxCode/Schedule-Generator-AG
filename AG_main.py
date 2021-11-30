from xlsx_reader import *
from materias import *
from AG import *

def main():
    path = 'D:\\Escritorio\\Proyecto Seminario de Algoritmia\\Plantilla_Horario.xlsx'
    lista_materias = read_excel(path)
    max_creditos = Horario_Max_Creditos(lista_materias, 'M')
    alelos = len(lista_materias)
    individuos = 40
    tamano_gen = 1 
    generaciones = 1000
    factor_mutacion = 0.01
    ag = AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, max_creditos)
    ag.run()

main()