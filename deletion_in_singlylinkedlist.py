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


def enter_list_in_linkedlist(head,root,lis):
    for i in lis:
        head,root=insert_linkedlist(i,head,root)
    return head,root


def delete_a_node(head,ele):
    prev=None
    root=head
    while root:
        if root.next!=None:
            if root.next.data==ele:
                root.next=root.next.next
                return head
                break
        if root.data==ele:
            head=head.next
            return head
        root=root.next

        
            
head=None
root=head
lis=[1,2,3,4,5,6,7]
head,root=enter_list_in_linkedlist(head,root,lis)
print("before deleting 7")
print_linkedlist(head)
head=delete_a_node(head,7)
print("after deleting 7")
print_linkedlist(head)
