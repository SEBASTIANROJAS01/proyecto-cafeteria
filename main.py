import os
import globales
import ventas
os.system("cls")

def menu_general():
    while True:
        os.system("cls")
        print("1. Precargar ventas")
        print("2. Crear venta")
        print("3. Reporte de sueldos")
        print("4. Estadisticas")
        print("5. Salir")

        opcion = globales.seleccionar_opcion(5)
        
        input(opcion)

        if opcion == 1:
            print("1. Precargar ventas")
            ventas.prevcargar_ventas()
        elif opcion == 2:
            print("2. Crear venta")
        elif opcion == 3:
            print("3. Reporte de sueldos")
        elif opcion == 4:
            print("4. Estadisticas")
        elif opcion == 5:
            print("5. Salir")
            return

        input()
if __name__ == "__main__":
    menu_general()