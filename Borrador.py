class OpcionesMenu():
    
    pass
    

#
class OpcionesMenu2():

    def __init__(self, nombre, apellido, edad, telefono, cedula):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.telefono=telefono
        self.cedula=cedula
        
    def objeto_persona():
        nombre = str(input("Introuce el nombre: "))
        apellido = str(input("Introduce tus apellidos: "))
        edad = int(input("Introduce edad: "))
        telefono = int(input("Inrese si telefono: "))
        cedula =int(input("Inrese su cedula: "))
                                                                                                                                                                                                                   
 
    def imprimir_persona(lista):
        for i in lista:
            print("Elementos registrados: {0}".format(i))
      
class opcionesMenu3():
    def __init__(self, nombreAnimal, especie, raza, enfermedad):
        self.nombreAnimal= nombreAnimal
        self.especie=especie
        self.raza=raza
        self.enfermedad=enfermedad

    def IngresarAnimal(self):
        nombreAnimal = input("Ingrese nombre del animal: ")
        especie = input("Ingrese especie del animal: ") 
        raza = input("Ingrese raza del animal: ")
        
        while(True):
            opcionEnfermedad = input("Tiene enfermedades <SI/NO> : ")
            if opcionEnfermedad == 'SI'  :
                enfermedad = input("Ingrese enfermedad que padece: ")
                break   
            elif opcionEnfermedad == 'NO':
                print("Es bueno saber eso")
                enfermedad = 'Sin enfermedad'   
                break
            else:
                print("| Dato ingresado incorrecto")
                print("| Vuelva a intentar") 
                    
            
            
        
        animal = [nombreAnimal, especie, raza, enfermedad]
        return animal

class menu(OpcionesMenu, OpcionesMenu2):
    """
    Una clase que representa el menú principal || Hereda la clase OpcionMenu0, OpcionesMenu, OpcionesMenu2
    Se llaman a las clase respecto a la opciónn que elija el usuario
    ------------------
    Método
    --------------------
    menuPrincipal():
       Obtiene un valor y devuelve la opción correspondiente

    """
    def menuPrincipal():
        while (True):#Ciclo Do-While hasta no finalizar el programa
            opc = str(input("| Ingrese una opción: ")) #Valores colocados de tipo str para un mejor control en las opciones
            if opc == '1':
                
                break

            elif opc == '2':
                
                objetoOpcionMenu2 = OpcionesMenu2
                print(objetoOpcionMenu2.imprimir_persona(OpcionesMenu2.objeto_persona()))
                
            elif opc == '3':
                
                objetoOpcionMenu3 = opcionesMenu3
                print(objetoOpcionMenu3.IngresarAnimal(opcionesMenu3))
                return main()
            elif opc == '4':
                print ("|------------------------------------------|")
                print ("|     Salio con éxito, Vuelva Pronto!!     |")
                print ("|------------------------------------------|")
                break
            else:
                print ("|------------------------------------------|")
                print ("|          ¡¡ Opcion invalida !!           |")
                print ("|------------------------------------------|")

def main():
    """
    Función main para ejecutar el programa principal
    Contiene unicamnete el menú principal que será desplegado
    """
    print ("____________________________________________")
    print ("|  Clínica Veterinaria Salud Animal        |")
    print ("|------------------------------------------|")
    print ("| 1.Registro de usuario                    |")
    print ("| 2.Datos del usuario                      |")
    print ("| 3.Datos de animal                        |")
    print ("| 4.Agendar cita                           |")
    print ("|------------------------------------------|")
    Llamado=menu.menuPrincipal()#Llamado a la funcion menuPrincipal de la clase menu para elegir la opción del menú
    print(Llamado)

if __name__ == '__main__':

    main()#Llamado al menúPrincipal