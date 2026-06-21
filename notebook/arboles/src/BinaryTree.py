# Definición de la clase Node que representa cada nodo en el árbol.
class Node:
    def __init__(self, data):
        # Almacena la data (o valor) en el nodo.
        self.data = data
        # Inicializa los nodos hijo izquierdo y derecho como None (vacíos).
        self.left = None
        self.right = None

# Definición de la clase BinaryTree que representa el árbol binario completo.
class BinaryTree:
    def __init__(self):
        # Inicializa la raíz del árbol binario como None (vacía).
        self.root = None

    # Método para insertar un nuevo nodo en el árbol.
    def insert(self, data):
        # Crea un nuevo nodo con la data proporcionada.
        new_node = Node(data)

        # Si el árbol está vacío, establece el nuevo nodo como raíz.
        if not self.root:
            self.root = new_node
            return

        # Utiliza una cola para realizar un recorrido por niveles en el árbol.
        queue = [self.root]

        # Itera sobre los nodos del árbol hasta encontrar un lugar para insertar
        # el nuevo nodo.
        while queue:
            current = queue.pop(0)  # Extrae el primer nodo de la cola.

            # Si el nodo actual no tiene un hijo izquierdo, inserta el nuevo
            # nodo aquí.
            if not current.left:
                current.left = new_node
                return  # Finaliza el método después de insertar el nodo.
            else:
                # Si el nodo actual tiene un hijo izquierdo, lo agrega a la cola
                # para continuar el recorrido.
                queue.append(current.left)

            # Si el nodo actual no tiene un hijo derecho, inserta el nuevo nodo
            # aquí.
            if not current.right:
                current.right = new_node
                return  # Finaliza el método después de insertar el nodo.
            else:
                # Si el nodo actual tiene un hijo derecho, lo agrega a la cola
                # para continuar el recorrido.
                queue.append(current.right)
