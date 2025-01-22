class CarritoDeCompras:
    def __init__(self):
        """Inicializa el carrito vacío"""
        self.articulos = []  # Lista para almacenar los artículos en el carrito
        print("Carrito de compras iniciado.")

    def agregar_articulo(self, articulo):
        """Agrega un artículo al carrito"""
        self.articulos.append(articulo)
        print(f"Artículo '{articulo}' agregado al carrito.")

    def mostrar_contenido(self):
        """Muestra los artículos en el carrito"""
        if self.articulos:
            print("Artículos en el carrito:")
            for articulo in self.articulos:
                print(f"- {articulo}")
        else:
            print("El carrito está vacío.")

    def __del__(self):
        """Simula la finalización de la compra al destruir el objeto"""
        if self.articulos:
            print("Realizando el pago de los artículos en el carrito...")
            # Aquí iría el proceso de pago
            print("Pago realizado con éxito.")
        else:
            print("El carrito está vacío. No hay nada que comprar.")


# Ejemplo de ejecución:

# Crear una instancia del carrito
carrito = CarritoDeCompras()

# Agregar artículos al carrito
carrito.agregar_articulo("Laptop")
carrito.agregar_articulo("Smartphone")
carrito.agregar_articulo("Auriculares")
carrito.agregar_articulo("Smartwatch")
carrito.agregar_articulo("Tablet")


# Mostrar el contenido del carrito
carrito.mostrar_contenido()

# El destructor se ejecutará cuando el objeto 'carrito' se destruya
