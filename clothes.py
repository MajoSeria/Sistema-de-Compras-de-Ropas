from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre  
        self._precio = precio  

    @abstractmethod
    def mostrar_info(self):  
        pass

    @property
    def precio(self):
        return self._precio

class Camisa(Producto):
    def __init__(self, nombre, precio, talla, color):
        super().__init__(nombre, precio)
        self._talla = talla
        self._color = color

    def mostrar_info(self):  
        return f"Camisa - {self._nombre}, Talla: {self._talla}, Color: {self._color}, Precio: ${self._precio}"

class Pantalon(Producto):
    def __init__(self, nombre, precio, talla, color):
        super().__init__(nombre, precio)
        self._talla = talla
        self._color = color

    def mostrar_info(self):  
        return f"Pantalón - {self._nombre}, Talla: {self._talla}, Color: {self._color}, Precio: ${self._precio}"

class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def mostrar_info(self):  
        return f"Zapato - {self._nombre}, Talla: {self._talla}, Precio: ${self._precio}"


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"{producto._nombre} agregado al carrito.")

    def mostrar_resumen(self):
        print("\nResumen de compra:")
        total = 0
        for producto in self.productos:
            print(producto.mostrar_info())
            total += producto.precio
        print(f"Total a pagar: ${total:.2f}")


class Tienda:
    def __init__(self):
        self._inventario = []
        self.carrito = Carrito()

    def agregar_producto_inventario(self, producto):
        self._inventario.append(producto)

    def mostrar_inventario(self):
        print("\nInventario disponible:")
        for index, producto in enumerate(self._inventario, start=1):
            print(f"{index}. {producto.mostrar_info()}")

    def seleccionar_producto(self):
        while True:
            self.mostrar_inventario()
            seleccion = input("Seleccione el número de los productos para agregar al carrito (separados por comas, o 'q' para finalizar): ")
            if seleccion.lower() == 'q':
                break
            indices = seleccion.split(",")
            for idx in indices:
                try:
                    index = int(idx.strip()) - 1  
                    producto = self._inventario[index]
                    self.carrito.agregar_producto(producto)
                except (IndexError, ValueError):
                    print(f"Selección no válida para: {idx.strip()}. Intente nuevamente.")

    def finalizar_compra(self):
        self.carrito.mostrar_resumen()

tienda = Tienda()


camisa = Camisa("Camisa Casual", 20.00, "M", "Azul")
pantalon = Pantalon("Pantalón Jeans", 30.00, "32", "Negro")
zapato = Zapato("Zapato Deportivo", 50.00, 42)

tienda.agregar_producto_inventario(camisa)
tienda.agregar_producto_inventario(pantalon)
tienda.agregar_producto_inventario(zapato)

tienda.seleccionar_producto()

tienda.finalizar_compra()
