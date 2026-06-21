# Definición de la clase para un Nodo del Árbol B
class BTreeNode:
    # Inicializador del nodo con opción de especificar si es hoja
    def __init__(self, leaf=False):
        # Determina si el nodo es una hoja
        self.leaf = leaf
        # Lista de llaves en el nodo
        self.keys = []
        # Hijos del nodo
        self.children = []

        print("Nodo BTree inicializado como hoja" if leaf else "Nodo BTree inicializado")


class BTree:
    # Constructor del árbol B que establece grado mínimo t y crea raíz
    def __init__(self, t):
        # La raíz del árbol inicialmente es una hoja hasta que se inserten más
        # valores
        self.root = BTreeNode(True)
        # Grado mínimo del árbol (determina tamaño máximo y mínimo de cada nodo)
        self.t = t

        print("Árbol B inicializado con grado mínimo", t)

    # -------------- Section: Insertion Methods -------------- #

    # Función para insertar una nueva llave en el árbol
    def insert(self, k):
        root = self.root
        # Si la raíz está llena, el árbol crece en altura
        if len(root.keys) == (2*self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            # La antigua raíz ahora es hija de la nueva raíz
            temp.children.insert(0, root)
            # Se divide la antigua raíz ya que estaba llena
            self.split_children(temp, 0)
            # Insertamos la llave en el árbol no lleno
            self.insert_non_full(temp, k)
        else:
            # Insertamos directamente si la raíz no está llena
            self.insert_non_full(root, k)

        print("Llave insertada:", k)

    # Inserta una llave en un nodo que asume no está lleno
    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            # Agrega espacio para la nueva llave
            x.keys.append((None, None))
            # Encuentra la posición para la nueva llave
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            # Inserta la nueva llave en su posición encontrada
            x.keys[i+1] = k

            print("Llave insertada en nodo hoja.")
        else:
            # Si no es una hoja, encuentra el hijo correcto donde insertar la
            # nueva llave
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            # Divide el hijo si está lleno antes de la inserción
            if len(x.children[i].keys) == (2*self.t) - 1:
                self.split_children(x, i)
                if k > x.keys[i]:
                    i += 1
            # Hace llamada recursiva al hijo correcto
            self.insert_non_full(x.children[i], k)

            print("Navegando hacia hijo para continuar inserción.")

    # Divide el hijo del nodo x en la posición i
    def split_children(self, x, i):
        t = self.t
        # Nodo a dividir
        y = x.children[i]
        # Nuevo nodo que contendrá las llaves [t, 2t-1] de y
        z = BTreeNode(y.leaf)
        # Añade el nuevo nodo como hijo
        x.children.insert(i+1, z)
        # Llave mediana se mueve al padre
        x.keys.insert(i, y.keys[t-1])
        # Reparte las llaves a los nodos nuevos
        z.keys = y.keys[t:(2*t)-1]
        y.keys = y.keys[0:(t-1)]
        if not y.leaf:
            # Si no son hojas, repartimos los hijos también
            z.children = y.children[t:(2*t)]
            y.children = y.children[0:t]

        print("Nodo hijo dividido en dos nodos.")
