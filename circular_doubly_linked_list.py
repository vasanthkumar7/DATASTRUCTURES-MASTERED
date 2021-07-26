class Node:
    def __init__(self,data):
        self.data=data
        self.front=None
        self.back=None


def insert_in_doublylinkedlist(head,root,i):
    if head==None:
        head=Node(i)
        head.front=head
        head.back=head
        root=head
    else:
        ne=Node(i)
        ne.front=head
        ne.back=root
        root.front=ne
        root=ne

    return head,root


def traverse_forward(head):
    root=head
    while root:
        print(root.data,"->",end="")
        root=root.front
        if root==head:
            break
    print("")


def insert_list_in_doubly_linkedlist(head,root,l):
    for i in l:
        head,root=insert_in_doublylinkedlist(head,root,i)
    return head,root

head=None
root=head
l=[1,2,3,4,5,6,7,8]
head,root=insert_list_in_doubly_linkedlist(head,root,l)
traverse_forward(head)
        
