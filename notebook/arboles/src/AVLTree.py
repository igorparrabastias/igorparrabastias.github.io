class Node:
    # Inicialización del nodo
    def __init__(self, data):
        self.data = data  # Dato almacenado en el nodo
        self.left = None  # Nodo hijo izquierdo
        self.right = None  # Nodo hijo derecho
        self.height = 1  # Altura del nodo (utilizada en AVL)

class AVLTree:
    # Inicialización del árbol AVL
    def __init__(self):
        self.root = None  # Raíz del árbol

    # -------------- Section: Insertion Methods -------------- #

    # Método para insertar un dato en el árbol
    def insert(self, data):
        if not self.root:  # Si el árbol está vacío
            self.root = Node(data)  # Crear el nodo raíz
        else:  # Si el árbol no está vacío
            self.root = self._insert(self.root, data)  # Insertar recursivamente

    # Método auxiliar para insertar nodos recursivamente
    def _insert(self, node, data):
        if not node:  # Si el nodo es nulo
            return Node(data)  # Retornar un nuevo nodo
        elif data < node.data:  # Si el dato a insertar es menor que el del nodo actual
            node.left = self._insert(node.left, data)  # Insertar en el subárbol izquierdo
        else:  # Si el dato a insertar es mayor o igual que el del nodo actual
            node.right = self._insert(node.right, data)  # Insertar en el subárbol derecho

        # Actualizar la altura del nodo actual
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        # Obtener el factor de balance del nodo actual
        balance = self._get_balance(node)

        # Caso: Desbalance Izquierda-Izquierda
        if balance > 1 and data < node.left.data:
            return self._rotate_right(node)
        # Caso: Desbalance Derecha-Derecha
        if balance < -1 and data > node.right.data:
            return self._rotate_left(node)
        # Caso: Desbalance Izquierda-Derecha
        if balance > 1 and data > node.left.data:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # Caso: Desbalance Derecha-Izquierda
        if balance < -1 and data < node.right.data:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        # Retornar el nodo con factores de equilibrio actualizados
        return node

    # Método para obtener la altura de un nodo
    def _get_height(self, node):
        if not node:  # Si el nodo es nulo
            return 0  # La altura es 0
        return node.height  # Retornar la altura

    # Método para obtener el factor de balance de un nodo
    def _get_balance(self, node):
        if not node:  # Si el nodo es nulo
            return 0  # El factor de balance es 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Método para realizar una rotación a la izquierda
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Actualizar las alturas
        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        # Retornar la nueva raíz después de la rotación
        return y

    # Método para realizar una rotación a la derecha
    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Actualizar las alturas
        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        # Retornar la nueva raíz después de la rotación
        return y

    # -------------- Section: Search Methods -------------- #

    # Método para buscar un valor en el árbol AVL
    def search(self, key):
        return self._search_recursive(self.root, key)

    # Función recursiva privada para realizar la búsqueda
    def _search_recursive(self, current_node, key):
        # Si el nodo actual es None, el valor no se encontró
        if not current_node:
            return False

        # Si el valor actual del nodo es el que buscamos, retorna True
        if current_node.data == key:
            return True

        # Si el valor buscado es menor que el del nodo actual, busca en el subárbol izquierdo
        elif key < current_node.data:
            return self._search_recursive(current_node.left, key)

        # Si el valor buscado es mayor que el del nodo actual, busca en el subárbol derecho
        else:
            return self._search_recursive(current_node.right, key)

    # -------------- Section: Delete Methods -------------- #

    def _get_min_value_node(self, node):
        """
        Obtiene el nodo con el valor mínimo en un subárbol.
        El nodo más a la izquierda del subárbol es el que tiene el valor mínimo.
        """
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    # Método para eliminar un nodo del árbol AVL
    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        # Paso 1: Realizar la eliminación estándar de BST
        if not node:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Nodo con solo un hijo o sin hijos
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Nodo con dos hijos: Obtener el sucesor inorden (el menor en el subárbol derecho)
            temp = self._get_min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)

        # Si el árbol tenía solo un nodo, retornarlo
        if node is None:
            return node

        # Paso 2: Actualizar la altura del nodo actual
        node.height = 1 + max(self._get_height(node.left),
                                self._get_height(node.right))

        # Paso 3: Obtener el factor de equilibrio
        balance = self._get_balance(node)

        # Paso 4: Balancear el árbol
        # Caso Izquierda Izquierda
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        # Caso Izquierda Derecha
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Caso Derecha Derecha
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        # Caso Derecha Izquierda
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node