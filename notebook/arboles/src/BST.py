# Clase que representa un nodo individual en el árbol
class Node:
    # Inicializa un nuevo nodo con datos pasados como parámetro
    def __init__(self, data):
        self.left = None  # Nodo izquierdo inicializado en None
        self.right = None  # Nodo derecho inicializado en None
        self.data = data  # Almacena los datos en el nodo

# Clase que representa un Árbol Binario de Búsqueda (BST)
class BST:
    # Inicializa un árbol binario de búsqueda vacío
    def __init__(self):
        self.root = None  # Raíz del árbol inicializada en None

    # -------------- Section: Insertion Methods -------------- #

    # Inserta un elemento nuevo en el árbol
    def insert(self, data):
        # Si la raíz es None, se crea el nodo raíz con la data proporcionada
        if self.root is None:
            self.root = Node(data)
        else:
            # De lo contrario, se llama al método recursivo para insertar en la posición adecuada
            self._insert_recursive(self.root, data)

    # Método auxiliar recursivo para insertar datos en el árbol
    def _insert_recursive(self, current_node, data):
        if data < current_node.data:  # Si la data es menor que la del nodo actual
            if current_node.left is None:  # Si no hay nodo izquierdo, inserta aquí
                current_node.left = Node(data)
            else:
                # En caso contrario, hacer una llamada recursiva hacia la izquierda
                self._insert_recursive(current_node.left, data)
        else:  # Si la data es mayor o igual que la del nodo actual
            if current_node.right is None:  # Si no hay nodo derecho, inserta aquí
                current_node.right = Node(data)
            else:
                # En caso contrario, hacer una llamada recursiva hacia la derecha
                self._insert_recursive(current_node.right, data)

    # -------------- Section: Search Methods -------------- #

    # Función pública para buscar una llave en el árbol
    def search(self, key):
        return self._search_recursive(self.root, key)

    # Función recursiva privada para buscar un nodo
    def _search_recursive(self, current_node, key):
        # Caso base: el valor no se encontró o se llegó a un nodo hoja.
        if current_node is None:
            return False

        # Si el valor actual del nodo es el que buscamos, retorna True.
        if current_node.data == key:
            return True

        # Decide si debe buscar en el subárbol izquierdo o derecho.
        if key < current_node.data:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

    # -------------- Section: Deletion Methods -------------- #

    def delete(self, key):
        # Eliminar un nodo con la llave dada.
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if not node:
            # No se encontró el nodo, regresar None.
            return None

        # Buscar el nodo a eliminar.
        if key != node.data:
            if key < node.data:
                # El nodo a eliminar está en el subárbol izquierdo.
                node.left = self._delete_recursive(node.left, key)
            else:  # key > node.data
                # El nodo a eliminar está en el subárbol derecho.
                node.right = self._delete_recursive(node.right, key)
            return node

        # Si se encontró el nodo, procedemos a eliminarlo.
        return self._delete_node_found(node)

    def _delete_node_found(self, node):
        # Caso con cero o un hijo.
        if not node.left or not node.right:
            # Retornar el nodo hijo si existe, sino None.
            return node.left or node.right

        # Nodo con dos hijos: encontrar y asignar el sucesor inorden.
        successor_value = self._get_min_value(node.right)
        node.data = successor_value
        # Eliminar el sucesor inorden después de reasignarlo.
        node.right = self._delete_recursive(node.right, successor_value)
        return node

    def _get_min_value(self, node):
        # Obtener el valor mínimo del subárbol comenzando por el nodo dado.
        while node.left:
            node = node.left
        return node.data