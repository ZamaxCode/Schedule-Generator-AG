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
            dh = dias_horas.split('/')
            d = dh[0].split('-')
            h = dh[1].split('-')
            print(d,h)
            m = mat.Materias(materia, seccion, profesor, dias_horas, creditos, calificacion)
            lista_materias.append(m)
            i+=1
        else:
            break


#read_excel('D:\\Escritorio\\Plantilla_Horario.xlsx')
list1 = ['L', 'I']
list2 = ['M', 'J']
list3 = ['I', 'V']
list4 = ['V']
list5 = ['L', 'I']
list6 = ['M', 'J']

intersection = set(list1) & set(list5)
#En caso de que la interseccion sea mayor a 0, se revisan las horas comparando la horas de inicio y las horas de fin
print(len(intersection))