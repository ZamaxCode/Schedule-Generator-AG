from xlsx_reader import *
from materias import *
from AG import *

def main():
    path = 'C:\\Users\\Dalia\\Schedule-Generator-AG\\Plantilla_Horario.xlsx'
    lista_materias_excel = read_excel(path)
    lista_materias = filtrarTurno('V', lista_materias_excel)
    if len(lista_materias) >= 2:
        mejor_profe = Horario_Max_Creditos(lista_materias)
        alelos = len(lista_materias)
        individuos = 40
        tamano_gen = 1 
        generaciones = 3000
        factor_mutacion = 0.05
        ag = AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, mejor_profe)
        materias = ag.run()
        for m in materias:
            print(m._materia, m._dias_horas, m._calificacion)
    else:
        print('No hay materias sufucientes en la lista para el turno elegido')


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


main()