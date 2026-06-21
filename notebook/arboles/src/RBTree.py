class Node:
    # Constructor para el nodo
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node(color={self.color}, data={self.data})"

class RBTree:
    # Constructor para el árbol rojo-negro
    def __init__(self):
        self.NIL = Node(data=None, color="black")
        self.root = self.NIL

    # ---- Sección: Métodos de Inserción ---- #

    # Método para insertar un nuevo nodo
    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        # Búsqueda del lugar adecuado para la inserción
        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        # Determinación de la posición del nuevo nodo dentro del árbol
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        # Establecer el color inicial del nuevo nodo a rojo
        new_node.color = "red"
        # Llamar al método para corregir la inserción
        self.fix_insert(new_node)

    # ---- Sección: Métodos auxiliares de Inserción ---- #

    # Método para corregir las propiedades después de la inserción
    def fix_insert(self, new_node):
        # Mientras que no se llegue a la raíz y el padre sea rojo
        while new_node != self.root and new_node.parent.color == "red":

            # Si el padre es hijo izquierdo
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                # Caso 1
                if uncle.color == "red":
                    new_node.parent.color = "black"
                    uncle.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    # Caso 2: si el nuevo nodo es el hijo derecho
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    # Caso 3
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.right_rotate(new_node.parent.parent)
            else:
                # Los mismos casos pero con el padre siendo hijo derecho
                uncle = new_node.parent.parent.left
                # Caso 1
                if uncle.color == "red":
                    new_node.parent.color = "black"
                    uncle.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    # Caso 2: si el nuevo nodo es el hijo izquierdo
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    # Caso 3
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.left_rotate(new_node.parent.parent)

        # Aseguramos que la raíz siempre sea negra
        self.root.color = "black"

    # Método para realizar rotación izquierda
    def left_rotate(self, node):
        # Establecer y como el hijo derecho del nodo actual
        y = node.right
        # Trasladar el hijo izquierdo de y al hijo derecho de node
        node.right = y.left
        if y.left != self.NIL:
            # Si el hijo izquierdo de y no es NIL, actualizar su padre
            y.left.parent = node
        # Hacer que el padre de y sea el padre de node
        y.parent = node.parent
        if node.parent is None:
            # Si node es la raíz, hacer a y la nueva raíz
            self.root = y
        elif node == node.parent.left:
            # Si node es hijo izquierdo, actualizar el hijo izquierdo de su
            # padre a y
            node.parent.left = y
        else:
            # Si node es hijo derecho, actualizar el hijo derecho de su
            # padre a y
            node.parent.right = y
        # Colocar node a la izquierda de y
        y.left = node
        # Hacer que el padre de node sea y
        node.parent = y

    # Método para realizar rotación derecha
    def right_rotate(self, node):
        # Establecer x como el hijo izquierdo del nodo actual
        x = node.left
        # Trasladar el hijo derecho de x al hijo izquierdo de node
        node.left = x.right
        if x.right != self.NIL:
            # Si el hijo derecho de x no es NIL, actualizar su padre
            x.right.parent = node
        # Hacer que el padre de x sea el padre de node
        x.parent = node.parent
        if node.parent is None:
            # Si node es la raíz, hacer a x la nueva raíz
            self.root = x
        elif node == node.parent.right:
            # Si node es hijo derecho, actualizar el hijo derecho de su
            # padre a x
            node.parent.right = x
        else:
            # Si node es hijo izquierdo, actualizar el hijo izquierdo de su
            # padre a x
            node.parent.left = x
        # Colocar node a la derecha de x
        x.right = node
        # Hacer que el padre de node sea x
        node.parent = x

    # ---- Sección: Métodos de Busqueda ---- #

    def search(self, key):
        # Referencia al nodo raíz
        current = self.root
        # Bucle mientras no se encuentre el nodo y no se llegue a un nodo NIL
        while current != self.NIL and key != current.data:
            # Si la clave es menor que el dato actual, ir hacia la izquierda
            if key < current.data:
                current = current.left
            # Si la clave es mayor que el dato actual, ir hacia la derecha
            else:
                current = current.right
        # Retornar el nodo encontrado o None si se llegó a un nodo NIL
        return current if current != self.NIL else None

    # ---- Sección: Métodos de Eliminación ---- #

    def delete(self, data):
        # Encontrar el nodo a eliminar
        node_to_delete = self.find_node(self.root, data)
        # Verificar si se encontró el nodo
        if node_to_delete == self.NIL:
            return  # Nodo no encontrado

        # Guardar referencia al nodo original y su color
        original_node = node_to_delete
        original_color = original_node.color
        # Si el hijo izquierdo es NIL, usar el hijo derecho
        if node_to_delete.left == self.NIL:
            temp_node = node_to_delete.right
            self.transplant(node_to_delete, node_to_delete.right)
        # Si el hijo derecho es NIL, usar el hijo izquierdo
        elif node_to_delete.right == self.NIL:
            temp_node = node_to_delete.left
            self.transplant(node_to_delete, node_to_delete.left)
        # Si tiene ambos hijos
        else:
            # Encontrar el sucesor (mínimo en subárbol derecho)
            original_node = self.minimum(node_to_delete.right)
            original_color = original_node.color
            temp_node = original_node.right
            # Si el padre del sucesor es el nodo a eliminar
            if original_node.parent == node_to_delete:
                temp_node.parent = original_node
            else:
                # Reemplazar sucesor por su hijo derecho
                self.transplant(original_node, original_node.right)
                # Preparar para transplantar el sucesor
                original_node.right = node_to_delete.right
                original_node.right.parent = original_node

            # Reemplazar nodo a eliminar por sucesor
            self.transplant(node_to_delete, original_node)
            original_node.left = node_to_delete.left
            original_node.left.parent = original_node
            original_node.color = node_to_delete.color

        # Si el nodo original era negro, corregir propiedades RB
        if original_color == 'black':
            self.fix_delete(temp_node)

    # ---- Sección: Métodos auxiliares de Eliminación ---- #

    def fix_delete(self, node):
        # Continuar hasta que el nodo no sea la raíz y el color del nodo sea negro
        while node != self.root and node.color == 'black':
            # Si el nodo es hijo izquierdo
            if node == node.parent.left:
                sibling = node.parent.right
                # Si el hermano es rojo
                if sibling.color == 'red':
                    # Cambiar colores y realizar rotación izquierda
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.left_rotate(node.parent)
                    sibling = node.parent.right

                # Si ambos hijos del hermano son negros
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    # Si el hijo derecho del hermano es negro
                    if sibling.right.color == 'black':
                        # Cambiar colores y realizar rotación derecha
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.right_rotate(sibling)
                        sibling = node.parent.right

                    # Cambiar colores y realizar rotación izquierda
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.right.color = 'black'
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                # Manejar caso simétrico para el hijo derecho
                sibling = node.parent.left
                # Si el hermano es rojo
                if sibling.color == 'red':
                    # Cambiar colores y realizar rotación derecha
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotate(node.parent)
                    sibling = node.parent.left

                # Si ambos hijos del hermano son negros
                if sibling.right.color == 'black' and sibling.left.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    # Si el hijo izquierdo del hermano es negro
                    if sibling.left.color == 'black':
                        # Cambiar colores y realizar rotación izquierda
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotate(sibling)
                        sibling = node.parent.left

                    # Cambiar colores y realizar rotación derecha
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.left.color = 'black'
                    self.right_rotate(node.parent)
                    node = self.root

        # Establecer el color del nodo a negro
        node.color = 'black'

    def find_node(self, node, data):
        # Caso base: si encontramos un nodo NIL o los datos coinciden
        if node == self.NIL or node.data == data:
            return node
        # Subárbol izquierdo si los datos buscados son menores que los del nodo actual
        if data < node.data:
            return self.find_node(node.left, data)
        else:
            # Subárbol derecho si los datos buscados son mayores o iguales al nodo actual
            return self.find_node(node.right, data)

    def transplant(self, u, v):
        # Si el padre de u es None, entonces v se convierte en la nueva raíz
        if u.parent == None:
            self.root = v
        # U está en el lado izquierdo de su padre
        elif u == u.parent.left:
            u.parent.left = v
        else:
            # U está en el lado derecho de su padre
            u.parent.right = v
        # V hereda el padre de U
        v.parent = u.parent

    def minimum(self, node):
        # Recorrer hacia el nodo más a la izquierda (el mínimo)
        while node.left != self.NIL:
            node = node.left
        return node

