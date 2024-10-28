class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
    
    def __del__(self):
        print(f"Eliminando nodo con valor: {self.valor}")

class Arbol:
    def __init__(self):
        self.raiz = None
    
    def __del__(self):
        self._destruir_recursivo(self.raiz)
        print("Árbol destruido completamente")
    
    def _destruir_recursivo(self, nodo):
        if nodo:
            self._destruir_recursivo(nodo.izquierda)
            self._destruir_recursivo(nodo.derecha)
            nodo.izquierda = None
            nodo.derecha = None
            del nodo
    
    def esta_vacio(self):
        return self.raiz == None
    
    def agregar(self, valor):
        if self.esta_vacio():
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)
    
    def _agregar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.derecha)
    
    def buscar(self, valor):
        if self.esta_vacio():
            return False
        return self._buscar_recursivo(valor, self.raiz)
    
    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor:
            return True
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.izquierda)
        return self._buscar_recursivo(valor, nodo_actual.derecha)
    
    def recorrido_inorden(self):
        if self.esta_vacio():
            return []
        return self._inorden_recursivo(self.raiz, [])
    
    def _inorden_recursivo(self, nodo_actual, elementos):
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.izquierda, elementos)
            elementos.append(nodo_actual.valor)
            self._inorden_recursivo(nodo_actual.derecha, elementos)
        return elementos
    
    def recorrido_preorden(self):
        if self.esta_vacio():
            return []
        return self._preorden_recursivo(self.raiz, [])
    
    def _preorden_recursivo(self, nodo_actual, elementos):
        if nodo_actual:
            elementos.append(nodo_actual.valor)
            self._preorden_recursivo(nodo_actual.izquierda, elementos)
            self._preorden_recursivo(nodo_actual.derecha, elementos)
        return elementos
    
    def recorrido_postorden(self):
        if self.esta_vacio():
            return []
        return self._postorden_recursivo(self.raiz, [])
    
    def _postorden_recursivo(self, nodo_actual, elementos):
        if nodo_actual:
            self._postorden_recursivo(nodo_actual.izquierda, elementos)
            self._postorden_recursivo(nodo_actual.derecha, elementos)
            elementos.append(nodo_actual.valor)
        return elementos

    def mostrar_arbol(self):
        if self.esta_vacio():
            print("El árbol está vacío")
            return
        
        def _obtener_altura(nodo):
            if nodo is None:
                return 0
            return 1 + max(_obtener_altura(nodo.izquierda), _obtener_altura(nodo.derecha))
        
        def _obtener_espacios(altura):
            return 2 ** (altura - 1)
        
        def _imprimir_nivel(nodo, nivel, espacios):
            if nodo is None:
                return
            if nivel == 1:
                print(" " * espacios + str(nodo.valor) + " " * espacios, end="")
            elif nivel > 1:
                _imprimir_nivel(nodo.izquierda, nivel - 1, espacios)
                _imprimir_nivel(nodo.derecha, nivel - 1, espacios)
        
        altura = _obtener_altura(self.raiz)
        espacios_iniciales = _obtener_espacios(altura) - 1
        
        for i in range(1, altura + 1):
            print("\n")
            _imprimir_nivel(self.raiz, i, espacios_iniciales)
            espacios_iniciales //= 2

def mostrar_menu():
    print("\n=== MENÚ DEL ÁRBOL BINARIO ===")
    print("1. Insertar un valor")
    print("2. Buscar un valor")
    print("3. Mostrar recorrido inorden")
    print("4. Mostrar recorrido preorden")
    print("5. Mostrar recorrido postorden")
    print("6. Verificar si el árbol está vacío")
    print("7. Mostrar árbol completo")
    print("8. Salir")
    return input("Seleccione una opción (1-8): ")

def main():
    arbol = Arbol()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            try:
                valor = int(input("Ingrese el valor a insertar: "))
                arbol.agregar(valor)
                print(f"Valor {valor} insertado correctamente.")
                print("\nEstado actual del árbol:")
                arbol.mostrar_arbol()
            except ValueError:
                print("Error: Por favor ingrese un número válido.")
        
        elif opcion == "2":
            try:
                valor = int(input("Ingrese el valor a buscar: "))
                if arbol.buscar(valor):
                    print(f"El valor {valor} se encuentra en el árbol.")
                else:
                    print(f"El valor {valor} no se encuentra en el árbol.")
            except ValueError:
                print("Error: Por favor ingrese un número válido.")
        
        elif opcion == "3":
            if arbol.esta_vacio():
                print("El árbol está vacío.")
            else:
                print("Recorrido Inorden:", arbol.recorrido_inorden())
        
        elif opcion == "4":
            if arbol.esta_vacio():
                print("El árbol está vacío.")
            else:
                print("Recorrido Preorden:", arbol.recorrido_preorden())
        
        elif opcion == "5":
            if arbol.esta_vacio():
                print("El árbol está vacío.")
            else:
                print("Recorrido Postorden:", arbol.recorrido_postorden())
        
        elif opcion == "6":
            if arbol.esta_vacio():
                print("El árbol está vacío.")
            else:
                print("El árbol no está vacío.")
        
        elif opcion == "7":
            print("\nVisualización del árbol:")
            arbol.mostrar_arbol()
        
        elif opcion == "8":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")

if __name__ == "__main__":
    main()