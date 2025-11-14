class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Verifica se a pilha está vazia."""
        return len(self.items) == 0

    def push(self, item):
        """Adiciona um item ao topo da pilha."""
        self.items.append(item)

    def pop(self):
        """Remove e retorna o item do topo da pilha."""
        if not self.is_empty():
            return self.items.pop()
        else:
            return "A pilha está vazia."

    def peek(self):
        """Retorna o item do topo sem removê-lo."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return "A pilha está vazia."

    def __str__(self):
        """Exibe a pilha como string."""
        return str(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Verifica se a fila está vazia."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Adiciona um item ao final da fila."""
        self.items.append(item)

    def dequeue(self):
        """Remove e retorna o primeiro item da fila."""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "A fila está vazia."

    def front(self):
        """Retorna o primeiro item da fila sem removê-lo."""
        if not self.is_empty():
            return self.items[0]
        else:
            return "A fila está vazia."

    def __str__(self):
        """Exibe a fila como string."""
        return str(self.items)



if __name__ == "__main__":
    print("===== TESTE DA PILHA =====")
    pilha = Stack()

    pilha.push(10)
    pilha.push(20)
    pilha.push(30)
    print("Pilha após inserções:", pilha)

    print("Topo da pilha:", pilha.peek())
    print("Removendo elemento:", pilha.pop())
    print("Pilha após remoção:", pilha)
    print("A pilha está vazia?", pilha.is_empty())

    print("\n===== TESTE DA FILA =====")
    fila = Queue()

    fila.enqueue("A")
    fila.enqueue("B")
    fila.enqueue("C")
    print("Fila após inserções:", fila)

    print("Primeiro da fila:", fila.front())
    print("Removendo elemento:", fila.dequeue())
    print("Fila após remoção:", fila)
    print("A fila está vazia?", fila.is_empty())
