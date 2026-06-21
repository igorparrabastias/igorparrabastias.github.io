# Definición de la clase TreeNode:
# Esta clase representa un nodo de un árbol. Cada nodo contiene datos y una
# lista de sus nodos hijos.
class TreeNode:
    # Método inicializador para un objeto TreeNode.
    # Este método se llama automáticamente al crear un nuevo nodo.
    # @param data: Los datos que va a contener el nodo.
    def __init__(self, data):
        # Almacena los datos pasados como argumento en la propiedad `data`.
        self.data = data
        # Inicializa la propiedad `children` como una lista vacía, para guardar
        # los hijos del nodo.
        self.children = []

# Definición de la clase Tree:
# Esta clase representa un árbol, el cual puede tener varios nodos (TreeNode).
# Un árbol siempre tiene un nodo raíz ('root') desde donde se inicia.
class Tree:
    # Método inicializador para un objeto Tree.
    # Este método se llama automáticamente al crear un nuevo árbol.
    def __init__(self):
        # Inicializa la propiedad `root` como None, indicando que aún no hay un
        # nodo raíz.
        self.root = None
