import openpyxl
import materias as mat

def read_excel(path):
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    lista_materias = []
    i = 2
    while True:
        if(ws.cell(row=i, column=1).value):
            materia = ws.cell(row=i, column=1).value
            seccion = ws.cell(row=i, column=2).value
            profesor = ws.cell(row=i, column=3).value
            dias_horas = ws.cell(row=i, column=4).value
            creditos = ws.cell(row=i, column=5).value
            calificacion = ws.cell(row=i, column=6).value
            m = mat.Materia(materia, seccion, profesor, dias_horas, creditos, calificacion)
            lista_materias.append(m)
            i+=1
        else:
            break
    return lista_materias
