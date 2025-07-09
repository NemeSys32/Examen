
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'HDD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'HDD', '1T', 'Intel Core i3', 'Integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'HDD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '6GB', 'HDD', '1T', 'AMD Ryzen 5', 'Integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'HDD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'HDD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
    'FS1230HD': ['Acer', 15.6, '8GB', 'SSD', '512GB', 'Intel Core i5', 'Integrada'],
    'XYZ456': ['MSI', 17.3, '32GB', 'SSD', '1T', 'Intel Core i9', 'Nvidia RTX3080'],
    'ABC789': ['Dell', 15.6, '16GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1660Ti'],
    'QWE123': ['Acer', 14, '8GB', 'HDD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    'ZXC456': ['HP', 15.6, '16GB', 'SSD', '1T', 'AMD Ryzen 7', 'Nvidia RTX2060'],   
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    'GF75HD': [749990, 2],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'UWU131HD': [349990, 7],
    'FS1230HD': [249990, 15], 
    'XYZ456': [1299990, 3],
    'ABC789': [899990, 5],
    'QWE123': [399990, 8],
    'ZXC456': [599990, 0],
}

def stock_marca(marca):
    try:
        total = 0
        marca_lower = marca.lower()
        for modelo, detalles in productos.items():
            if detalles[0].lower() == marca_lower:
                if modelo in stock and len(stock[modelo]) > 1:
                    total += stock[modelo][1]
        print(f"El stock total para {marca.capitalize()} es: {total}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def actualizar_precio(modelo, p):
    try:
        if modelo in stock:
            stock[modelo][0] = p
            return True
        return False
    except Exception as e:
        print(f"Error inesperado: {e}")
        return False
    
def busqueda_precio(p_min, p_max):
    try:
        resultados = []
        for modelo, detalles in productos.items():
            if modelo in stock and len(stock[modelo]) > 1:
                precio, cantidad = stock[modelo]
                if p_min <= precio <= p_max and cantidad > 0:
                    resultados.append(f"{detalles[0]}--{modelo}")
        if resultados:
            resultados.sort()
            print("Los modelos en el rango de precios son:")
            for item in resultados:
                print(f" - {item}")
        else:
            print("No hay notebooks en ese rango de precios.")
    except ValueError:
        print(f"Error! Ingrese números enteros positivos.")

def main():
    while True:
        try:
            print("\n*** Tienda Pybooks ***")
            print("1. Stock por marca")
            print("2. Búsqueda por precio")
            print("3. Actualizar precio")
            print("4. Salir")
            opcion = input("\n Ingrese opción: ").strip()

            if opcion == "1":
                marca = input("\n Ingrese marca a consultar: ").strip()
                if not marca:
                    raise ValueError("\n La marca no puede estar vacía")
                marcas_disponibles = {detalles[0].lower() for detalles in productos.values()}
                if marca.lower() not in marcas_disponibles:
                    print("\n Marca no encontrada en el catálogo.")
                    print("\n Marcas disponibles: \n")
                    for m in sorted({detalles[0] for detalles in productos.values()}):
                        print(f" - {m}")
                    continue
                stock_marca(marca)

            elif opcion == "2":
                while True:
                    try:
                        p_min = int(input("Ingrese precio mínimo: ").strip())
                        p_max = int(input("Ingrese precio máximo: ").strip())
                        if p_min < 0 or p_max < 0:
                            raise ValueError("Los precios no pueden ser negativos")
                        if p_min > p_max:
                            raise ValueError("El precio mínimo no puede ser mayor al máximo")
                        busqueda_precio(p_min, p_max)
                        break
                    except ValueError:
                        print(f"\n Error! Ingrese números enteros positivos.")
                    except Exception as e:
                        print(f"\n Error inesperado: {e}")

            elif opcion == "3":
                while True:
                    try:
                        modelo = input("\n Ingrese modelo a actualizar: ").strip().upper()
                        if not modelo:
                            raise ValueError("\n El modelo no puede estar vacío")
                        if modelo not in stock:
                            print("\n El modelo no existe! Modelos disponibles para actualizar:")
                            for m in sorted(stock.keys()):
                                print(f" - {m}")
                            continuar = input("\n ¿Intentar con otro modelo? (s/n): ").strip().lower()
                            if continuar != 's':
                                break
                            else:
                                continue

                        nuevo_precio = int(input("\n Ingrese nuevo precio: ").strip())
                        if nuevo_precio < 0:
                            raise ValueError("\n El precio no puede ser negativo")

                        confirmar = input(f"\n ¿Confirma el nuevo precio ${nuevo_precio}? (s/n): ").strip().lower()
                        if confirmar != 's':
                            print("\n Actualización cancelada.")
                            continuar = input("\n ¿Actualizar otro precio? (s/n): ").strip().lower()
                            if continuar != 's':
                                break
                            else:
                                continue

                        if actualizar_precio(modelo, nuevo_precio):
                            print("\n Precio actualizado!")
                        continuar = input("\n ¿Actualizar otro precio? (s/n): ").strip().lower()
                        if continuar != 's':
                            break
                    except ValueError: 
                        print(f"Error: Ingrese un número entero positivo.")
                    except Exception as e:
                        print(f"Error inesperado: {e}")

            elif opcion == "4":
                print("\n Programa Finalizado.")
                break

            else:
                print("\n Debe seleccionar una opción válida.")

        except Exception as e:
                print(f"\n Error inesperado en el menú: {e}")
if __name__ == "__main__":
    main()