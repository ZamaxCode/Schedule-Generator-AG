from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import AG_main as agm

preferencia = 0
turno = ''
path = ''

def matutino_clicked():
    global turno
    turno = 'M'
    logger.config(state=NORMAL)
    logger.insert(END, '+++++ Turno Matutino Seleccionado +++++\n')
    logger.config(state=DISABLED)

def vespertino_clicked():
    global turno
    turno = 'V'
    logger.config(state=NORMAL)
    logger.insert(END, '+++++ Turno Vespertino Seleccionado +++++\n')
    logger.config(state=DISABLED)

def turno_indistinto_clicked():
    global turno
    turno = 'N'
    logger.config(state=NORMAL)
    logger.insert(END, '+++++ Turno Indistinto Seleccionado +++++\n')
    logger.config(state=DISABLED)

def max_creditos():
    global preferencia
    preferencia = 1
    logger.config(state=NORMAL)
    logger.insert(END, '+++++ Preferencia Por Maximo De Creditos +++++\n')
    logger.config(state=DISABLED)

def mejor_profe():
    global preferencia
    preferencia = 2
    logger.config(state=NORMAL)
    logger.insert(END, '+++++ Preferencia Por Mejores Profesores +++++\n')
    logger.config(state=DISABLED)

def max_materias():
    global preferencia
    preferencia = 3
    logger.config(state=NORMAL)
    logger.insert(END, '+++++ Preferencia Por Maximo De Materias +++++\n')
    logger.config(state=DISABLED)

def select_excel():
    global path
    file = askopenfilename()
    name, extension = os.path.splitext(file)
    if extension == '.xlsx':
        logger.config(state=NORMAL)
        logger.insert(END, 'File: '+name+extension+'\n')
        logger.config(state=DISABLED)
        path = file
    else:
        logger.config(state=NORMAL)
        logger.insert(END, 'Error. Seleccione un archivo de excel (.xlsx)\n')
        logger.config(state=DISABLED)

def start():
    global path
    global turno
    global preferencia

    if preferencia != 0 and turno != '' and path != '':
        materias = agm.main(path, turno, preferencia)
        cont = 1
        logger.config(state=NORMAL)
        logger.insert(END, '\n------------------------\n')
        for m in materias:
            logger.insert(END, 'Materia ' + str(cont) + '\n' +
                                m._materia + '\n' +
                                m._seccion + '\n' +
                                m._profesor + '\n' +
                                m._dias_horas + '\n' +
                                str(m._creditos) + ' creditos' + '\n' +
                                'Rating del profesor: ' + str(m._calificacion) + '\n' +
                                '------------------------\n')
            cont += 1
        logger.config(state=DISABLED)

    else:
        logger.config(state=NORMAL)
        logger.insert(END, 'Error. Faltó un parametro por seleccionar (turno/preferencia/archivo)\n')
        logger.config(state=DISABLED)

window = Tk()

window.geometry("1300x593")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 593,
    width = 1300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

#--------------------------------------------------Turno Buttons----------------------------------------------------------------
img2 = PhotoImage(file = f"img2.png")
matutino_button = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = matutino_clicked, relief = "flat")
matutino_button.place(x = 51, y = 130, width = 260, height = 47)

img3 = PhotoImage(file = f"img3.png")
vespertino_button = Button(image = img3, borderwidth = 0, highlightthickness = 0, command = vespertino_clicked, relief = "flat")
vespertino_button.place(x = 51, y = 189, width = 260, height = 47)

img4 = PhotoImage(file = f"img4.png")
turno_indistinto_button = Button(image = img4, borderwidth = 0, highlightthickness = 0, command = turno_indistinto_clicked, relief = "flat")
turno_indistinto_button.place(x = 51, y = 260, width = 260, height = 47)
#--------------------------------------------------Turno Buttons End------------------------------------------------------------

#--------------------------------------------------Preferencia Buttons----------------------------------------------------------
img5 = PhotoImage(file = f"img5.png")
max_creditos_button = Button(image = img5, borderwidth = 0, highlightthickness = 0, command = max_creditos, relief = "flat")
max_creditos_button.place(x = 403, y = 260, width = 355, height = 47)

img6 = PhotoImage(file = f"img6.png")
mejor_profe_button = Button(image = img6, borderwidth = 0, highlightthickness = 0, command = mejor_profe, relief = "flat")
mejor_profe_button.place(x = 403, y = 333, width = 355, height = 47)

img7 = PhotoImage(file = f"img7.png")
max_materias_button = Button(image = img7, borderwidth = 0, highlightthickness = 0, command = max_materias, relief = "flat")
max_materias_button.place(x = 403, y = 398, width = 355, height = 47)
#--------------------------------------------------Preferencia Buttons End------------------------------------------------------

img0 = PhotoImage(file = f"img0.png")
start_button = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = start, relief = "flat")
start_button.place( x = 279, y = 536, width = 265, height = 47)

img1 = PhotoImage(file = f"img1.png")
excel_button = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = select_excel, relief = "flat")
excel_button.place(x = 277, y = 479, width = 265, height = 45)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    644.5, 296.5,
    image=background_img)

logger = Text(window, bg= '#baeba8')
logger.config(state=DISABLED)
logger.place(
    x = 790, y = 34,
    width = 446,
    height = 473)

window.resizable(False, False)
window.mainloop()
