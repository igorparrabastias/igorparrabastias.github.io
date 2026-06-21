### Introducción:

El algoritmo A* (A estrella) es una de las técnicas de búsqueda más eficientes y populares utilizadas en la búsqueda de caminos y gráficos. Es ampliamente usado en áreas como inteligencia artificial para juegos y planificación de rutas. A* es un algoritmo informado, lo que significa que utiliza conocimientos adicionales (heurísticas) para encontrar de manera eficiente el camino más corto entre un nodo inicial y un nodo objetivo.

### Conceptos Clave de A*:

- **Función de Costo `f(n)`**: `f(n) = g(n) + h(n)`
    - `g(n)`: Costo real del camino desde el nodo inicial hasta el nodo `n`.
    - `h(n)`: Heurística estimada del costo más bajo desde `n` hasta el nodo objetivo.
- **Heurística**: Una función que estima el costo del camino más barato de un nodo a un nodo objetivo. La elección de una buena heurística es clave para el rendimiento de A*.

### Implementación de A*:

Para ilustrar A*, implementaremos un simple ejemplo en un espacio de cuadrícula.

```python
import heapq

class Nodo:
    def __init__(self, nombre, heuristic_value=0):
        self.nombre = nombre
        self.heuristic_value = heuristic_value
        self.adjacencies_list = []
        self.parent = None
        self.g = 0
        self.f = 0

class Edge:
    def __init__(self, peso, start_vertex, target_vertex):
        self.peso = peso
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

def calculate_shortest_path(start_vertex):
    queue = []
    start_vertex.f = start_vertex.g + start_vertex.heuristic_value
    heapq.heappush(queue, (start_vertex.f, start_vertex))

    while len(queue) > 0:
        actual_vertex = heapq.heappop(queue)[1]

        for edge in actual_vertex.adjacencies_list:
            child_vertex = edge.target_vertex
            temp_g = actual_vertex.g + edge.peso

            if temp_g < child_vertex.g:
                child_vertex.parent = actual_vertex
                child_vertex.g = temp_g
                child_vertex.f = temp_g + child_vertex.heuristic_value
                heapq.heappush(queue, (child_vertex.f, child_vertex))

def get_shortest_path(target_vertex):
    print("El camino más corto es: ")
    node = target_vertex
    while node is not None:
        print(f"{node.nombre} - ", end='')
        node = node.parent
```

### Ejercicios:

**Ejercicio 1: Crear un Grafo y Aplicar A***

- **Objetivo**: Crea un grafo simple con nodos y aristas, y aplica el algoritmo A* para encontrar el camino más corto.
- **Solución**:
    
    ```python
    # Crear nodos
    nodo_a = Nodo("A", 10)
    nodo_b = Nodo("B", 8)
    nodo_c = Nodo("C", 5)
    nodo_d = Nodo("D", 7)
    nodo_e = Nodo("E", 3)
    nodo_f = Nodo("F", 6)
    nodo_g = Nodo("G", 0)
    
    # Crear aristas (caminos)
    edge_ab = Edge(4, nodo_a, nodo_b)
    edge_ac = Edge(3, nodo_a, nodo_c)
    edge_be = Edge(5, nodo_b, nodo_e)
    edge_ce = Edge(1, nodo_c, nodo_e)
    edge_bd = Edge(6, nodo_b, nodo_d)
    edge_de = Edge(5, nodo_d, nodo_e)
    
    # Asignar aristas a los nodos
    nodo_a.adjacencies_list.append(edge_ab)
    nodo_a.adjacencies_list.append(edge_ac)
    nodo_b.adjacencies_list.append(edge_be)
    nodo_b.adjacencies_list.append(edge_bd)
    nodo_c.adjacencies_list.append(edge_ce)
    nodo_d.adjacencies_list.append(edge_de)
    
    # Aplicar A*
    calculate_shortest_path(nodo_a)
    get_shortest_path(nodo_e)
    
    ```
    

**Ejercicio 2: Modificar Heurística y Observar Cambios**

- **Objetivo**: Modifica los valores heurísticos de los nodos y observa cómo cambia el camino encontrado por A*.
- **Solución**: Cambia los valores heurísticos de varios nodos y ejecuta el algoritmo A* para ver cómo afecta al camino resultante.

### Conclusión:

El algoritmo A* es una herramienta poderosa para la búsqueda de caminos en grafos, equilibrando eficientemente entre el costo del camino y la heurística. Es ampliamente utilizado en aplicaciones que van desde la planificación de rutas en mapas hasta la inteligencia artificial en videojuegos. La clave de su eficacia reside en elegir una heurística adecuada que guíe la búsqueda hacia el objetivo de manera eficiente.