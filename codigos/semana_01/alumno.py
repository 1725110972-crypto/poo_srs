class Alumno:
    def __init__(self, matricula, nombre_completo, carrera, cuatrimestre, grupo, promedio_general, estatus_academico, nivel_ingles, turno, tutor):
        self.matricula=matricula
        self.nombre_completo=nombre_completo
        self.carrera=carrera
        self.cuatrimestre=cuatrimestre
        self.grupo=grupo
        self.promedio_general=promedio_general
        self.estatus_academico=estatus_academico
        self.nivel_ingles=nivel_ingles
        self.turno=turno
        self.tutor=turno

        print(f"Matriclua: {self.matricula}")
        print(f"Nombre Completo del alumno:{self.nombre_completo}")
        print(f"Nombre de la carrere:{self.carrera}")
        print(f"Cuatricula:{self.cuatrimestre}")
        print(f"Grupo:{self.grupo}")
        print(f"Promedio General:{self.promedio_general}")
        print(f"Estatus Académico:{self.estatus_academico}")
        print(f"Nivel de Ingles:{self.nivel_ingles}")
        print(f"Turno:{self.turno}")

    def inscribirse(self):
        print("Incribirse a la escuela")
    def reprobar(self):
        print("Reprobar la materia")
    def pasar(self):
        print("Pasar la materia")
    def exponer(self):
        print("Exponer un proyecto")
    def hacer(self):
        print("Hacer la tarea")

stephanie_yo=Alumno("1725110971", "Stephanie Ramírez Santander", "TIS", "3°", "32", "9.07", "regular", "A1", "Matutino", "Rigoberto Garcia")

stephanie_yo.inscribirse()
stephanie_yo.reprobar()
stephanie_yo.pasar()
stephanie_yo.exponer()
stephanie_yo.hacer()
