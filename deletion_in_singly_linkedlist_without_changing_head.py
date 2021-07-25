class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_linkedlist(d,head,root):
    if head==None:
        head=Node(d)
        head.next=None
        root=head
    else:
        n=Node(d)
        n.next=None
        root.next=n
        root=n
    return head,root

def print_linkedlist(head):
    root=head
    
    while root:
        print(root.data,"->",end="")
        root=root.next
    print("")

def delete_an_node_in_linked_list(head,element):
    if head.data==element:
        head=head.next
        return head

    pos=None
    root=head

    while root.next:
        if root.next.data==element:
            pos=root
            break
        root=root.next

    if pos.next.next:
        pos.next=pos.next.next
    else:
        pos.next=None
    return head
        


def enter_list_in_linkedlist(head,root,lis):
    for i in lis:
        head,root=insert_linkedlist(i,head,root)
    return head,root

head=None
root=head
lis=[1,2,3,4,5,6,7]
head,root=enter_list_in_linkedlist(head,root,lis)
print_linkedlist(head)
head=delete_an_node_in_linked_list(head,7)
print_linkedlist(head)
