                                                            # Двусвязный список

# В двусвязном списке каждый узел содержит данные, ссылку на узел, после него, и ссылку на узел, предшествующий ему.
# Преимущества дополнительного указателя означают, 
#   что список можно перемещать в любом направлении при доступе к информации - это означает, что переход от узла 5 к узлу 8 может быть проще, чем обход с начала списка
# 

class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data                                        # data — это значение, которое мы хотим сохранять в узле
        self.next = next                                        # адрес след значения
        self.prev = prev                                        # адрес предыдущего значения
	
class doubly_linked_list(object):                               # класс дввойной связки списка
    def __init__(self):
        self.head = None                                        # первый эл-т в списке
        self.tail = None                                        # последний эл-т в списке
        self.count = 0                                          # эл-ов в списке

    def append_item(self, data):                                # ф-я добавления эл-та в список
        new_item = Node(data, None, None)                       # добавляем эл-т
        if self.head is None:                                   # если первого эл-та в списке нет, то:
            self.head = new_item                                #   первый элм-т равен новому эл-ту
            self.tail = self.head                               #   последний равен первому (прим: [1], список из одного эл-та)
        else:                                                   # иначе:
            new_item.prev = self.tail                           #   адрес предыдущего значения равен последнему эл-ту
            self.tail.next = new_item                           #   адрес след значения последнего эл-та равен новому
            self.tail = new_item                                #   последний эл-т равен новому

        self.count += 1

    def print_foward(self):
        for node in self.iter():
            print(node)

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev
            
    def iter(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val

if __name__ == "__main__":
    items = doubly_linked_list()
    items.append_item(1)
    items.append_item(2)
    items.append_item(3)
    items.append_item(4)
    items.append_item(5)

    items.print_foward()