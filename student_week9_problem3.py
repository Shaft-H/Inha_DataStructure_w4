class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linkedList(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

class MergeLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addList(self, head2):

        if self.head == None:
            self.head = head2
            temp = self.head
            while temp.next !=None:
                temp = temp.next
            self.tail = temp


        else:

            self_search = self.head
            new_search = head2.head
            temp = None

            if new_search.data < self_search.data:
                self.head = new_search
                while new_search.data < self_search.data:
                    new_search = new_search.next



            while self_search != None:
                if self_search.data < self_search.data:
                    

                self_search_former = self_search
                self_search = self_search.next

            if new_search != None:
                self_search.next = new_search

            


def main():
    # Create two linked lists
    # List 1: 1 -> 3 -> 5
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)

    # List 2: 2 -> 4 -> 6
    head2 = Node(2)
    head2.next = Node(4)
    head2.next.next = Node(6)

    # Print the original lists
    print("List 1: ", end='')
    print_linkedList(head1)
    print("List 2: ", end='')
    print_linkedList(head2)

    # Merge the lists
    merged_list = MergeLinkedList()
    merged_list.addList(head1)
    merged_list.addList(head2)

    # Print the merged list
    print("Merged List: ", end='')
    print_linkedList(merged_list.head)

if __name__ == '__main__':
    main()