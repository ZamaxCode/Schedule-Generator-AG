class Materia:
    def __init__(self, materia, seccion, profesor, dias_horas, creditos, calificacion):
        self._materia = materia
        self._seccion = seccion
        self._profesor = profesor
        self._dias_horas = dias_horas
        self._creditos = creditos
        self._calificacion = calificacion

class Horario_Max_Creditos:
    def __init__(self, materias, turno):
        self._materias = []
        self._materias = materias
        self._turno = turno
    
    def f(self, cromosoma):
        f = 0
        materias_seleccionadas = []
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                if self.is_valid(materias_seleccionadas, self._materias[i]):
                    materias_seleccionadas.append(self._materias[i])
                    f+=self._materias[i]._creditos
                else:
                    return 0
        return f
                

    def is_valid(self, materias_seleccionadas, materia):
        for ms in materias_seleccionadas:
            if materia._materia == ms._materia:
                return False
            else:
                dh = ms._dias_horas.split('/')
                d_ms = dh[0].split('-')
                h_ms = dh[1].split('-')

                dh = materia._dias_horas.split('/')
                d_materia = dh[0].split('-')
                h_matetia = dh[1].split('-')
                
                intersection = set(d_ms) & set(d_materia)

                if intersection != 0:
                    if h_ms[0] == h_matetia[0] or h_ms[1] == h_matetia[1]:
                        return False

        return True         
    

                
                


    