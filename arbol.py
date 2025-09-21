import sys
import networkx as nx
import matplotlib.pyplot as plt

class Parser:
    def __init__(self, cadena):
        self.cadena = list(cadena.replace(" ", ""))
        self.pos = 0
        self.G = nx.DiGraph()
        self.node_id = 0

    def new_node(self, label):
        self.node_id += 1
        self.G.add_node(self.node_id, label=label)
        return self.node_id

    def peek(self):
        if self.pos < len(self.cadena):
            return self.cadena[self.pos]
        return None

    def consume(self, expected=None):
        ch = self.peek()
        if ch is None:
            return None
        if expected is not None and ch != expected:
            raise ValueError(f"Se esperaba '{expected}' pero se encontró '{ch}'")
        self.pos += 1
        return ch

    # Gramática:
    # E -> E opsuma T
    # E -> T
    # T -> T opmul F
    # F -> F
    # F -> id
    # F -> num
    # F -> pari E pard

    def parse_E(self, parent=None):
        node = self.new_node("E")
        if parent: self.G.add_edge(parent, node)

        left = self.parse_T(node)

        while self.peek() == '+':   # solo + permitido
            op = self.consume()
            op_node = self.new_node(op)
            self.G.add_edge(node, op_node)
            right = self.parse_T(node)

        return node

    def parse_T(self, parent=None):
        node = self.new_node("T")
        if parent: self.G.add_edge(parent, node)

        left = self.parse_F(node)

        while self.peek() == '*':   # solo * permitido
            op = self.consume()
            op_node = self.new_node(op)
            self.G.add_edge(node, op_node)
            right = self.parse_F(node)

        return node

    def parse_F(self, parent=None):
        node = self.new_node("F")
        if parent: self.G.add_edge(parent, node)

        ch = self.peek()
        if ch is None:
            raise ValueError("Cadena inesperada al final")

        if ch.isdigit():  # num
            num = self.consume()
            num_node = self.new_node(num)
            self.G.add_edge(node, num_node)

        elif ch == "(":
            self.consume("(")
            expr_node = self.parse_E(node)
            self.consume(")")

        else:
            raise ValueError(f"Símbolo inesperado: {ch}")

        return node

    def parse(self):
        root = self.parse_E()
        if self.peek() is not None:
            raise ValueError("Cadena no consumida completamente")
        return self.G



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python programa.py gra.txt cadenas.txt")
        sys.exit(1)

    archivo_gramatica = sys.argv[1]  
    archivo_cadenas = sys.argv[2]

    with open(archivo_cadenas, "r") as f:
        cadenas = [line.strip() for line in f.readlines() if line.strip()]

    for cad in cadenas:
        print(f"\nAnalizando cadena: {cad}")
        try:
            parser = Parser(cad)
            G = parser.parse()

            labels = nx.get_node_attributes(G, "label")
            pos = nx.nx_pydot.graphviz_layout(G, prog="dot")  # ordenado jerárquico
            nx.draw(G, pos, labels=labels, with_labels=True,
                    node_size=1500, node_color="lightblue", font_size=10)
            plt.show()
        except Exception as e:
            print("Cadena inválida:", cad)
