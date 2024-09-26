print("Jesus Mota 1275")
import datetime
#Zona de clase
class Inventario1275:
    ID_Inventario1275=0
    ID_Productos1275=0
    Cantidad1275=0
    Fecha_Ingreso1275=datetime.date
    Fecha_Vencimiento1275=datetime.date
    Proveedor1275=""
    Notas1275=""
    #zona de funciones
    def mostrar_datos1275(self):
        print("")

    def Listar_Productos1275(self):
        lista1275=["Cappuccino","Espresso","Americano","Mocca","Latte","Doppio","Flat White"]
        for x in lista1275:
            print(x)
        print()
    
    def Tupla_Proveedores1275(self):
        tupla1275=("Procafé","Abascafé","Polvora café","Caffenio","Cafe Boato","Cafetto 22","Cafenix")
        for y in tupla1275:
            print(y)
        print()

    def Diccionario_Productos_Precio1275(self):
        diccionario1275={
            "Cappuccino:": 70,
            "Espresso:": 80,
            "Americano:": 90,
            "Mocca:": 60,
            "Latte:": 68,
            "Doppio:":79,
            "Flat White:":10
        }
        for dick, di in diccionario1275.items():
            print(dick,di)
        print()

    def altas1275(self):
        print("La operación se realizo correctamente para los datos del inventario")
        print()

    def bajas1275(self):
        print("La operación se realizo correctamente para los datos del inventario")
        print()

#zona de objetos
Mota1275=Inventario1275()

#zona de uso de objetos
Mota1275.mostrar_datos1275()
print("~~Lista de Productos~~")
Mota1275.Listar_Productos1275()
print("~~Tupla de Proveedores~~")
Mota1275.Tupla_Proveedores1275()
print("~~Diccionario de Productos y Precios~~")
Mota1275.Diccionario_Productos_Precio1275()
Mota1275.altas1275()
Mota1275.bajas1275()