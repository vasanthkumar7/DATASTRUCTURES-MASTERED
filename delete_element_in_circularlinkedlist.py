class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_circularlinkedlist(d,head,root):
    if head==None:
        head=Node(d)
        head.next=head
        root=head
    else:
        n=Node(d)
        n.next=head
        root.next=n
        root=n
    return head,root

def print_circularlinkedlist(head):
    root=head
    while root:
        print(root.data,"->",end="")
        root=root.next
        if root==head:
            break
    print("")

def delete_in_circular_linked_list(head,element):

    root=head.next
    prev=None

    temp=None

    if head.data==element:
        if head.next==head:
            return None
        else:
            temp=True
    

    while root.next:
        if root.next.data==element:
            prev=root
            break
        root=root.next
        if root==head:
            break

    if temp:
        head=prev.next.next

    prev.next=prev.next.next

    

    return head

    
def enter_list_in_circularlinkedlist(head,root,lis):
    for i in lis:
        head,root=insert_circularlinkedlist(i,head,root)
    return head,root

head=None
root=head
lis=[1,2,3,4,5,6,7]
head,root=enter_list_in_circularlinkedlist(head,root,lis)
print_circularlinkedlist(head)
head=delete_in_circular_linked_list(head,1)
print_circularlinkedlist(head)
