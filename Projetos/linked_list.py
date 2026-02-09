class LinkedList():
    class Node():
        def __init__(self, element):
            self.element = element
            self.next = None # Não aponta para nada no primeiro momento
    def __init__(self):
        self.length = 0
        self.head = None # Referencia o primeiro node na lista
    
    def is_empty(self):
        return self.length == 0
    

    def add(self, element):
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None: # passa por cada nó até achar o ultimo
                current_node = current_node.next
            current_node.next = node # adiciona um nó a lista
        self.length += 1

    def remove(self, element):
        previous_node = None
        current_node = self.head # starta o atravessamento desde o primeiro node
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next # muda o ponteiro do current_node para o p´roximo node, possibilitando atravessar a linked list até o elemento ser encontrado ou chegar ao fim
        if current_node is None:
            return 
        elif previous_node is not None:
            previous_node.next = current_node.next # Se o elemento a ser removido for encontrado e não é o head, o ponteiro next do node anterior será atualizado para pular o node atual, assim o removendo
        else:
            self.head = current_node.next # caso o elemento a ser removido seja o head, o head vira o proximo node 
        self.length -= 1

my_list = LinkedList()
print(my_list.is_empty())
my_list.add(1)
my_list.add(2)
print(my_list.is_empty())
print(my_list.length)
my_list.remove(1)
print(my_list.length)

