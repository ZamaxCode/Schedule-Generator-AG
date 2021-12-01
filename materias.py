class Materia:
    def __init__(self, materia, seccion, profesor, dias_horas, creditos, calificacion):
        self._materia = materia
        self._seccion = seccion
        self._profesor = profesor
        self._dias_horas = dias_horas
        self._creditos = creditos
        self._calificacion = calificacion

class Horario_Max_Creditos:
    def __init__(self, materias):
        self._materias = []
        self._materias = materias
    
    def f(self, cromosoma):
        f = 0
        materias_seleccionadas = []
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                if self.is_valid(materias_seleccionadas, self._materias[i]):
                    materias_seleccionadas.append(self._materias[i])
                    f+=self._materias[i]._creditos
                else:
                    if f>0:
                        f-=self._materias[i]._creditos
                        if f<0:
                            f=0
        return f, materias_seleccionadas
                

    def is_valid(self, materias_seleccionadas, materia):
        for ms in materias_seleccionadas:
            if materia._materia == ms._materia:
                return False
            
            dh_ms = ms._dias_horas.split('/')
            d_ms = dh_ms[0].split('-')
            h_ms = dh_ms[1].split('-')

            dh_materia = materia._dias_horas.split('/')
            d_materia = dh_materia[0].split('-')
            h_matetia = dh_materia[1].split('-')
            
            intersection = set(d_ms) & set(d_materia)

            if len(intersection) > 0:
                if h_ms[0] == h_matetia[0] or h_ms[1] == h_matetia[1]:
                    return False
        return True
    
class Horario_Mejor_Profesor:
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
                    f+=self._materias[i]._calificacion
                else:
                    f-=10

        return f, materias_seleccionadas
                

    def is_valid(self, materias_seleccionadas, materia):

        if materia._calificacion < 4:
                return False

        for ms in materias_seleccionadas:
            
            if materia._materia == ms._materia:
                return False
            
            dh_ms = ms._dias_horas.split('/')
            d_ms = dh_ms[0].split('-')
            h_ms = dh_ms[1].split('-')

            dh_materia = materia._dias_horas.split('/')
            d_materia = dh_materia[0].split('-')
            h_matetia = dh_materia[1].split('-')
            
            intersection = set(d_ms) & set(d_materia)

            if len(intersection) > 0:
                if h_ms[0] == h_matetia[0] or h_ms[1] == h_matetia[1]:
                    return False

        return True

class Horario_Max_Materias:
    def __init__(self, materias, turno):
        self._materias = []
        self._materias = materias
        self._turno = turno
    
    def f(self, cromosoma):
        materias_seleccionadas = []
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                if self.is_valid(materias_seleccionadas, self._materias[i]):
                    materias_seleccionadas.append(self._materias[i])
                else:
                    return 0, []

        return len(materias_seleccionadas), materias_seleccionadas
                

    def is_valid(self, materias_seleccionadas, materia):

        for ms in materias_seleccionadas:
            
            if materia._materia == ms._materia:
                return False
            
            dh_ms = ms._dias_horas.split('/')
            d_ms = dh_ms[0].split('-')
            h_ms = dh_ms[1].split('-')

            dh_materia = materia._dias_horas.split('/')
            d_materia = dh_materia[0].split('-')
            h_matetia = dh_materia[1].split('-')
            
            intersection = set(d_ms) & set(d_materia)

            if len(intersection) > 0:
                if h_ms[0] == h_matetia[0] or h_ms[1] == h_matetia[1]:
                    return False

        return True
