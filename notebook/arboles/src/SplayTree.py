class Node:
    def __init__(self, data):
        # Constructor de la clase Nodo.
        # 'data' contiene el valor almacenado en el nodo.
        # 'left' apunta al hijo izquierdo del nodo (None si no tiene).
        # 'right' apunta al hijo derecho del nodo (None si no tiene).
        # 'parent' apunta al nodo padre (None si es la raíz).
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    def __init__(self):
        # Constructor de la clase SplayTree.
        # Inicializa un árbol splay sin nodos, por lo tanto 'root' es None.
        self.root = None

    # ---- Sección: Métodos de Inserción ---- #

    def insert(self, data):
        # Insertar un nuevo dato en el árbol splay.
        # El método encuentra la posición correcta del nuevo nodo y luego realiza un 'splay' de este.
        print(f"Insertar: {data}")
        node = Node(data)
        y = None
        x = self.root

        # Buscar dónde insertar el nuevo nodo.
        while x:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y

        # Si el árbol estaba vacío, el nuevo nodo será la raíz.
        if y is None:
            self.root = node
        else:
            # Si el valor es menor, inserta a la izquierda, sino a la derecha.
            if node.data < y.data:
                y.left = node
            else:
                y.right = node

        # Una vez insertado el nodo, es necesario hacer un 'splay' para optimizar futuros accesos.
        self.splay(node)

    # ---- Sección: Métodos auxiliares de Inserción ---- #

    def rotate_left(self, x):
        # Realiza una rotación hacia la izquierda en el nodo x para reestructurar el árbol.
        # Este movimiento promueve el nodo derecho de x (y) a la posición de x,
        # Mientras que x se convierte en el hijo izquierdo de y.
        y = x.right
        x.right = y.left

        if y.left:
            y.left.parent = x

        y.parent = x.parent

        if not x.parent:
            print(f"Rotación izquierda: {x.data} ahora es la nueva raíz.")
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, x):
        # Realiza una rotación hacia la derecha en el nodo x para reestructurar el árbol.
        # Este movimiento promueve el nodo izquierdo de x (y) a la posición de x,
        # Mientras que x se convierte en el hijo derecho de y.
        y = x.left
        x.left = y.right

        if y.right:
            y.right.parent = x

        y.parent = x.parent

        if not x.parent:
            print(f"Rotación derecha: {x.data} ahora es la nueva raíz.")
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # ---- Sección: Métodos auxiliares generales ---- #

    def splay(self, x):
        # Realiza la operación de 'splay' en el nodo x. El objetivo es traer el nodo x a la raíz del árbol,
        # mediante una serie de rotaciones, para optimizar tiempos de acceso futuros a este nodo.
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left:
                    print(f"Splay - rotación a la derecha (Zig): {x.data}")
                    self.rotate_right(x.parent)
                else:
                    print(f"Splay - rotación a la izquierda (Zag): {x.data}")
                    self.rotate_left(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                print(
                    f"Splay - doble rotación a la derecha (Zig-Zig): {x.data}")
                self.rotate_right(x.parent.parent)
                self.rotate_right(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                print(
                    f"Splay - doble rotación a la izquierda (Zag-Zag): {x.data}")
                self.rotate_left(x.parent.parent)
                self.rotate_left(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                print(
                    f"Splay - rotación a la izquierda seguido de rotación a la derecha (Zag-Zig): {x.data}")
                self.rotate_left(x.parent)
                self.rotate_right(x.parent)
            else:
                print(
                    f"Splay - rotación a la derecha seguido de rotación a la izquierda (Zig-Zag): {x.data}")
                self.rotate_right(x.parent)
                self.rotate_left(x.parent)

    # ---- Sección: Métodos de Busqueda ---- #

    def search(self, data):
        # Inicializamos con el nodo raíz y preparamos una variable para recordar el
        # último visitado.
        node = self.root
        lastVisited = None

        # Recorremos los nodos del árbol para buscar el dato solicitado.
        while node:
            # Guardamos el último nodo visitado para poder realizar un "splay" si es
            # necesario.
            lastVisited = node
            # Imprimimos el valor del nodo actual para trazar la búsqueda.
            print(f"Visitando: {node.data}")

            # Decidimos en qué dirección continuar la búsqueda basándonos en el
            # valor buscado.
            if data < node.data:
                # Nos movemos al hijo izquierdo si el dato buscado es menor.
                node = node.left
            elif data > node.data:
                # Nos movemos al hijo derecho si el dato buscado es mayor.
                node = node.right
            else:
                # Si encontramos el nodo con el dato, realizamos la operación de
                # splay.
                print(f"Nodo encontrado: {node.data}. Realizando splay...")
                # Al encontrar el nodo, lo llevamos a la raíz.
                self.splay(node)
                return node  # Retornamos el nodo encontrado.

        # Si hemos terminado el bucle sin retornar un nodo, significa que no se
        # encontró el buscado.
        if lastVisited:
            # Si había nodos en el árbol, realizamos splay en el último visitado
            # para mantener propiedades optimización.
            print(
                f"Nodo no encontrado. Realizando splay en último nodo visitado: {lastVisited.data}")
            self.splay(lastVisited)
        else:
            # En caso de que el árbol esté vacío, informamos al usuario.
            print("El árbol está vacío.")

        # Retornamos None ya que no encontramos el nodo con el dato buscado.
        return None

    # ---- Sección: Métodos de Eliminación ---- #

    def delete(self, data):
        # Primero, buscamos el nodo con el valor a eliminar y realizamos un splay
        # para llevarlo a la raíz.
        node_to_delete = self.search(data)

        if node_to_delete is None:
            print(f"El nodo con el valor {data} no se encuentra en el árbol.")
            return

        # Separamos el árbol en dos subárboles, izquierdo y derecho, excluyendo la
        # raíz (nodo a eliminar).
        left_subtree = node_to_delete.left
        right_subtree = node_to_delete.right

        if left_subtree:
            left_subtree.parent = None
        if right_subtree:
            right_subtree.parent = None

        # Si el subárbol izquierdo es no nulo, buscamos el elemento más grande (el
        # más a la derecha) para hacerlo la nueva raíz.
        if left_subtree:
            self.root = left_subtree
            # Buscamos el elemento más a la derecha del subárbol izquierdo.
            largest_in_left = left_subtree
            while largest_in_left.right:
                largest_in_left = largest_in_left.right
            # Realizamos un splay de este nodo, para que sea la nueva raíz del
            # árbol.
            self.splay(largest_in_left)
            # Conectamos el subárbol derecho con la nueva raíz.
            self.root.right = right_subtree
            if right_subtree:
                right_subtree.parent = self.root
        else:
            # Si no hay subárbol izquierdo, el subárbol derecho se convierte
            # directamente en la nueva raíz.
            self.root = right_subtree

        print(f"El nodo con el valor {data} ha sido eliminado.")
