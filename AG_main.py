from xlsx_reader import *
from materias import *
from AG import *

def main(path, turno, preferencia):
    lista_materias_excel = read_excel(path)
    lista_materias = filtrarTurno(turno, lista_materias_excel)

    materias = []

    if preferencia == 1:
        if len(lista_materias) >= 2:
            mejor_profe = Horario_Max_Creditos(lista_materias)
            alelos = len(lista_materias)
            individuos = 20
            tamano_gen = 1 
            generaciones = 1500
            factor_mutacion = 0.05
            ag = AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, mejor_profe)
            materias = ag.run()
        else:
            print('No hay materias sufucientes en la lista para el turno elegido')

    if preferencia == 2:
        if len(lista_materias) >= 2:
            mejor_profe = Horario_Mejor_Profesor(lista_materias)
            alelos = len(lista_materias)
            individuos = 40
            tamano_gen = 1 
            generaciones = 3000
            factor_mutacion = 0.05
            ag = AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, mejor_profe)
            materias = ag.run()
        else:
            print('No hay materias sufucientes en la lista para el turno elegido')
    
    if preferencia == 3:
        if len(lista_materias) >= 2:
            mejor_profe = Horario_Max_Materias(lista_materias)
            alelos = len(lista_materias)
            individuos = 40
            tamano_gen = 1 
            generaciones = 3000
            factor_mutacion = 0.1
            ag = AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, mejor_profe)
            materias = ag.run()
        else:
            print('No hay materias sufucientes en la lista para el turno elegido')

    return materias

def filtrarTurno(turno, lista_materias):
    lista_filtrada = []
    if turno == 'M':
        for materia in lista_materias:
            dh = materia._dias_horas.split('/')
            h = dh[1].split('-')
            if int(h[1]) <= 15:
                lista_filtrada.append(materia)
    elif turno == 'V':
        for materia in lista_materias:
            dh = materia._dias_horas.split('/')
            h = dh[1].split('-')
            if int(h[0]) >= 15:
                lista_filtrada.append(materia)
    else:
        lista_filtrada = lista_materias
    return lista_filtrada


