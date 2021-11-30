from xlsx_reader import *
from materias import *
from AG import *

def main():
    path = 'D:\\Escritorio\\Proyecto Seminario de Algoritmia\\Plantilla_Horario.xlsx'
    lista_materias = read_excel(path)
    mejor_profe = Horario_Max_Materias(lista_materias, 'M')
    alelos = len(lista_materias)
    individuos = 40
    tamano_gen = 1 
    generaciones = 3000
    factor_mutacion = 0.1
    ag = AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, mejor_profe)
    materias = ag.run()
    for m in materias:
        print(m._materia, m._dias_horas, m._calificacion)

main()